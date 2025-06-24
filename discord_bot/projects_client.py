import asyncio
import yaml
import discord
from discord.ext import commands
import logging
import os
from dotenv import load_dotenv

# Load environment variables from the .env file (in parent directory)
load_dotenv('../.env')

# Retrieve the environment variables from the .env file
discord_token = os.getenv('DISCORD_TOKEN')
guild_id = int(os.getenv('DISCORD_GUILD_ID'))
roles_channel_id = int(os.getenv('DISCORD_ROLES_CHANNEL'))

# Use the 'discord' logger for all logging
logger = logging.getLogger('discord')
logger.setLevel(logging.INFO)

# Define the emoji list for project roles
EMOJI_PROJECT_ROLES = list(
    "🐁🐂🐄🐇🐈🐉🐊🐋🐌"
    "🐍🐎🐏🐐🐑🐒🐓🐕🦛"
    "🦚🐘🐙🐚🐛🦢🐝🐞🦕"
    "🦖🐡🐢🐦🐧🦜🐩🐪🐬"
    "🐿🕊🦜🦂🦃🦆🦇🦈🦒"
    "🦉🦋🦎🦔🦦🦩🍀🌸🌻"
)

# Define the template for project role messages
ROLES_PROJECT_MESSAGE = "{emoji} [{title}]({link}): [@{key}](https://discordapp.com/channels/{guild}/{channel})"

# Define the instructions message for reacting to get project roles
ROLES_MESSAGE = """
> Please react to this message with the appropriate emoji for the project.
> 
> The emoji reaction will allow you to receive notifications from the project via the tag `@proj-<project name>`.
"""

# Define the acknowledgement message for role assignments
ROLES_MESSAGE_ACK = """
The emojis were assigned to the projects *at random*, if you'd like to change your project's emoji, please contact the <@&{staff_role}>.
"""

# Define the Project class to manage project roles and channels
class Project:
    def __init__(self, client, data, emoji):
        self.client = client
        self.guild = client._guild
        self.key = data['chatchannel'].lower()
        self.title = data['title']
        # Updated to use the link field from YAML (fallback to GitHub issue if not present)
        self.link = data.get('link', f"https://github.com/ohbm/hackathon2025/issues/{data.get('issue', '')}")
        self.emoji = emoji
        self.voice = None
        self.text = None
        self.role = None

    async def setup(self):
        # Create the project role, channels, and set permissions
        await self.ensure_role()
        await self.ensure_channels()
        await self.ensure_channel_permissions()
        return self

    async def ensure_role(self):
        if self.role is not None:
            return
        # Check if the role already exists
        self.role = discord.utils.get(self.guild.roles, name=f'proj-{self.key}')
        if self.role:
            logger.info(f"Role already exists: {self.role.name}")
        else:
            # Create the role if it does not exist
            self.role = await self.guild.create_role(name=f'proj-{self.key}', mentionable=True)
            logger.info(f"Created role: {self.role.name}")

    async def ensure_channels(self):
        # Check if the voice and text channels already exist in the Projects category
        self.voice = discord.utils.get(self.client.voice_category.voice_channels, name=self.key)
        self.text = discord.utils.get(self.client.text_category.text_channels, name=self.key)

        if self.voice is None and self.text is None:
            # Create the voice channel in the Projects category
            self.voice = await self.guild.create_voice_channel(name=self.key, category=self.client.voice_category)
            logger.info(f"Created voice channel: {self.voice.name} (ID: {self.voice.id})")

            # Create the text channel in the Projects-text category
            self.text = await self.guild.create_text_channel(name=self.key, category=self.client.text_category)
            logger.info(f"Created text channel: {self.text.name} (ID: {self.text.id})")
        else:
            logger.info(f"Channels for project {self.title} already exist.")

    async def ensure_channel_permissions(self):
        # Ensure that both channels exist
        if self.voice is None or self.text is None:
            logger.info(f"Voice or text channel for project {self.title} is not set.")
            return

        # Define permissions for the channels
        overwrites = {
            self.guild.default_role: discord.PermissionOverwrite(view_channel=False),
            self.client.cached_roles['muted']: discord.PermissionOverwrite(view_channel=False),
            self.client.cached_roles['staff']: discord.PermissionOverwrite(view_channel=True),
            self.role: discord.PermissionOverwrite(view_channel=True),
        }
        # Apply the permissions to the voice and text channels
        await self.voice.edit(overwrites=overwrites)
        await self.text.edit(overwrites=overwrites)
        logger.info(f"Permissions set for voice and text channels of project: {self.title}")

# Define the main bot class
class ProjectsClient(commands.Bot):
    def __init__(self, guild_id, roles_channel_id, *args, **kwargs):
        # Define intents to specify which events the bot should listen to
        intents = discord.Intents.default()
        intents.members = True
        intents.presences = True
        super().__init__(command_prefix='!', intents=intents, *args, **kwargs)
        self._guild_id = guild_id
        self._roles_channel_id = roles_channel_id
        self._guild = None
        self.voice_channels = {}
        self.text_channels = {}
        self.projects_roles = {}
        self.projects = {}
        self.roles_channel = None
        self.voice_category = None
        self.text_category = None
        self.cached_roles = {}
        self.projects_emoji = {}
        self._role_messages_ids = []

    async def on_ready(self):
        # Log that the bot is ready and connected
        logger.info(f'Logged in as {self.user} (ID: {self.user.id})')
        logger.info('Connected to the following guilds:')
        for guild in self.guilds:
            logger.info(f'- {guild.name} (ID: {guild.id})')

        # Cache the guild and roles channel
        self._guild = self.get_guild(self._guild_id)
        self.roles_channel = self.get_channel(self._roles_channel_id)

        if not self._guild or not self.roles_channel:
            logger.error("Guild or roles channel not found.")
            return

        # Ensure categories exist for project channels
        self.voice_category = discord.utils.get(self._guild.categories, name="Projects")
        self.text_category = discord.utils.get(self._guild.categories, name="Projects-text")

        if not self.voice_category:
            self.voice_category = await self._guild.create_category("Projects")
        if not self.text_category:
            self.text_category = await self._guild.create_category("Projects-text")

        # Cache project roles
        for role in self._guild.roles:
            if role.name.startswith("proj-"):
                self.projects_roles[role.name] = role

        # Cache specific roles
        self.cached_roles = {
            'muted': discord.utils.get(self._guild.roles, name='muted'),
            'staff': discord.utils.get(self._guild.roles, name='Event Staff')
        }

        if not self.cached_roles['staff']:
            logger.error("Staff role not found.")
            return

        # Load existing projects from Discord first
        await self.load_existing_projects()
        
        # Ensure all projects (will only create new ones)
        await self.ensure_projects()
        
        # Load existing role messages to handle reactions
        await self.load_existing_role_messages()
        
        # Only setup initial roles message if no projects exist yet
        if not self.projects:
            await self.ensure_roles_message()

        # Indicate that the bot is now running and listening for events
        logger.info("Bot setup complete. Now listening for events...")

    async def load_existing_projects(self):
        """Load existing projects from Discord channels and roles to avoid recreating them"""
        logger.info("Loading existing projects from Discord...")
        
        # Find existing project roles and channels
        for role in self._guild.roles:
            if role.name.startswith("proj-"):
                project_key = role.name[5:]  # Remove 'proj-' prefix
                
                # Find corresponding channels
                voice_channel = discord.utils.get(self.voice_category.voice_channels, name=project_key)
                text_channel = discord.utils.get(self.text_category.text_channels, name=project_key)
                
                if voice_channel and text_channel:
                    # Create a minimal project object for existing projects
                    self.projects_roles[role.name] = role
                    self.voice_channels[project_key] = voice_channel
                    self.text_channels[project_key] = text_channel
                    
                    # Add to projects dict to mark as existing
                    self.projects[project_key] = {
                        'key': project_key,
                        'role': role,
                        'voice': voice_channel,
                        'text': text_channel,
                        'existing': True
                    }
                    logger.info(f"Found existing project: {project_key}")

    async def load_existing_role_messages(self):
        """Load existing role messages from the roles channel"""
        logger.info("Loading existing role messages...")
        self._role_messages_ids = []
        
        async for message in self.roles_channel.history(limit=50):
            # Check if message has embeds and is from this bot
            if (message.author.id == self.user.id and 
                message.embeds and 
                ('Projects' in message.embeds[-1].title or 'New Projects' in message.embeds[-1].title)):
                
                self._role_messages_ids.append(message.id)
                
                # Extract emoji-project mappings from reactions
                for reaction in message.reactions:
                    emoji_str = str(reaction.emoji)
                    if emoji_str in EMOJI_PROJECT_ROLES:
                        # Find which project this emoji belongs to by checking message content
                        embed_description = message.embeds[-1].description
                        if embed_description and emoji_str in embed_description:
                            # Parse the message to find project key
                            lines = embed_description.split('\n')
                            for line in lines:
                                if emoji_str in line and '[@' in line:
                                    # Extract project key from the line
                                    try:
                                        start = line.find('[@') + 2
                                        end = line.find(']', start)
                                        project_key = line[start:end]
                                        
                                        if project_key in self.projects:
                                            # Map emoji to existing project
                                            if isinstance(self.projects[project_key], dict):
                                                self.projects[project_key]['emoji'] = emoji_str
                                            self.projects_emoji[emoji_str] = self.projects[project_key]
                                            logger.info(f"Mapped existing emoji {emoji_str} to project {project_key}")
                                    except:
                                        continue
        
        logger.info(f"Found {len(self._role_messages_ids)} existing role messages")

    async def post_new_projects_message(self, new_projects):
        """Post a message with only new projects for emoji reactions"""
        logger.info(f"Posting message for {len(new_projects)} new projects")
        
        if not new_projects:
            return
            
        # Create description with only new projects
        description = ""
        project_emojis = []
        
        for key, project in new_projects.items():
            description += ROLES_PROJECT_MESSAGE.format(
                emoji=project.emoji, title=project.title, link=project.link,
                key=key, guild=self._guild.id, channel=project.text.id)
            description += "\n"
            project_emojis.append(project.emoji)
        
        # Create embed for new projects
        embed = discord.Embed(
            title='Projects',
            description=description,
            color=0x00ff00,
        )
        
        # Send the message
        message = await self.roles_channel.send(
            content=ROLES_MESSAGE,
            embed=embed
        )
        
        # Add emoji reactions for new projects
        for emoji in project_emojis:
            await message.add_reaction(emoji)
            
        # Store message ID for reaction handling
        self._role_messages_ids.append(message.id)
        
        logger.info(f"Posted new projects message with {len(project_emojis)} emojis")

    async def ensure_projects(self):
        # Load project data from YAML file (updated to use website's YAML file)
        with open('../src/_data/projects.yaml', 'r', encoding='utf-8') as f:
            data = yaml.safe_load(f)
            projects_data = data['projectlist']

        # Track new projects for separate messaging
        new_projects = {}
        
        # Find the highest existing emoji index to continue from there
        existing_emoji_count = len(self.projects)

        for i, data in enumerate(projects_data):
            key = data['chatchannel'].lower()
            # Skip already existing projects
            if key in self.projects:
                continue

            # Assign an emoji to each NEW project, continuing from where we left off
            emoji_index = existing_emoji_count + len(new_projects)
            emoji = EMOJI_PROJECT_ROLES[emoji_index % len(EMOJI_PROJECT_ROLES)]
            project = Project(self, data, emoji)
            await project.setup()
            if project.voice is None or project.text is None:
                logger.error(f"Failed to create channels for project: {project.title}")
                continue
            self.voice_channels[project.key] = project.voice
            self.text_channels[project.key] = project.text
            self.projects_roles[f'proj-{project.key}'] = project.role
            self.projects_emoji[emoji] = project
            self.projects[project.key] = project
            new_projects[project.key] = project
            
        # Post messages only for new projects
        if new_projects:
            await self.post_new_projects_message(new_projects)

    async def ensure_roles_message(self):
        logger.info("Ensuring roles messages")
        self._role_messages = []
        async for message in self.roles_channel.history(limit=10, oldest_first=True):
            if len(message.embeds) < 1:
                continue
            if message.embeds[-1].title != 'Projects':
                continue
            self._role_messages.append(message)
        self._role_messages_ids = [m.id for m in self._role_messages]

        ack_message = ROLES_MESSAGE_ACK.format(
            staff_role=str(self.cached_roles['staff'].id))

        ack_embed = discord.Embed(
            description=ack_message,
            color=0xff0000,
        )

        PROJECTS_PER_MESSAGE = 10
        EMBED_DESCRIPTION_LIMIT = 4096
        EMBEDS_CHAR_SUM = 6000

        description = ""
        project_emojis = []
        projects_in_message = 0
        messages_sent = 0

        for pi, (key, project) in enumerate(self.projects.items()):
            description += ROLES_PROJECT_MESSAGE.format(
                emoji=project.emoji, title=project.title, link=project.link,
                key=key, guild=self._guild.id, channel=project.text.id)
            description += "\n"

            project_emojis.append(project.emoji)
            projects_in_message += 1

            description_limit = EMBED_DESCRIPTION_LIMIT
            if messages_sent == 0:
                sum_limit = EMBEDS_CHAR_SUM - len(str(ack_embed.description))
                description_limit = min(description_limit, sum_limit)

            if (len(description) >= description_limit
                    or projects_in_message >= PROJECTS_PER_MESSAGE
                    or pi == len(self.projects) - 1):

                embeds = []
                content = None
                if messages_sent == 0:
                    embeds.append(ack_embed)
                    content = ROLES_MESSAGE

                embed = discord.Embed(
                    title='Projects',
                    description=description,
                    color=0x00ff00,
                )
                embeds.append(embed)

                if messages_sent >= len(self._role_messages):
                    message = await self.roles_channel.send(
                        content=content,
                        embeds=embeds
                    )
                    self._role_messages_ids.append(message.id)
                else:
                    message = self._role_messages[messages_sent]
                    await message.edit(
                        content=content,
                        embeds=embeds
                    )

                for pe in project_emojis:
                    await message.add_reaction(pe)

                # Reset for next message
                description = ""
                project_emojis = []
                projects_in_message = 0

                messages_sent += 1

    async def reaction_role(self, payload, add):
        # Handle adding or removing roles based on reactions
        if (payload.message_id not in self._role_messages_ids
                or str(payload.emoji) not in self.projects_emoji
                or payload.user_id == self.user.id):
            return

        project = self.projects_emoji[str(payload.emoji)]
        user = await self.roles_channel.guild.fetch_member(payload.user_id)
        
        # Handle both Project objects and dict representations
        if hasattr(project, 'role'):
            role = project.role
        elif isinstance(project, dict):
            role = project['role']
        else:
            logger.error(f"Invalid project object for emoji {payload.emoji}")
            return
            
        # Debug: Check current user roles before operation
        user_roles_before = [r.name for r in user.roles]
        logger.info(f"User {user.display_name} roles before: {user_roles_before}")
        logger.info(f"Attempting to {'add' if add else 'remove'} role: {role.name}")
        logger.info(f"Bot permissions: {self.roles_channel.guild.me.guild_permissions.manage_roles}")
        logger.info(f"Bot role position: {self.roles_channel.guild.me.top_role.position}")
        logger.info(f"Target role position: {role.position}")
            
        try:
            if add:
                await user.add_roles(role)
                logger.info(f"API call completed for adding role {role.name} to user {user.display_name}")
            else:
                await user.remove_roles(role)
                logger.info(f"API call completed for removing role {role.name} from user {user.display_name}")
                
            # Debug: Check user roles after operation by getting fresh member data
            try:
                # Get fresh member data from the guild
                fresh_user = await self.roles_channel.guild.fetch_member(user.id)
                user_roles_after = [r.name for r in fresh_user.roles]
                logger.info(f"User {user.display_name} roles after: {user_roles_after}")
                
                # Verify if the operation actually worked
                if add and role.name in user_roles_after:
                    logger.info(f"✅ SUCCESS: Role {role.name} was actually added to {user.display_name}")
                elif add and role.name not in user_roles_after:
                    logger.error(f"❌ FAILED: Role {role.name} was NOT added to {user.display_name} despite no exception")
                elif not add and role.name not in user_roles_after:
                    logger.info(f"✅ SUCCESS: Role {role.name} was actually removed from {user.display_name}")
                elif not add and role.name in user_roles_after:
                    logger.error(f"❌ FAILED: Role {role.name} was NOT removed from {user.display_name} despite no exception")
            except Exception as fetch_error:
                logger.warning(f"Could not verify role assignment: {fetch_error}")
                
        except discord.errors.Forbidden as e:
            logger.error(f"❌ Permission denied: Cannot {'add' if add else 'remove'} role {role.name} for user {user.display_name}. Error: {e}")
        except discord.errors.HTTPException as e:
            logger.error(f"❌ HTTP error: Cannot {'add' if add else 'remove'} role {role.name} for user {user.display_name}. Error: {e}")
        except Exception as e:
            logger.error(f"❌ Unexpected error: Cannot {'add' if add else 'remove'} role {role.name} for user {user.display_name}. Error: {e}")
            logger.error(f"Error type: {type(e).__name__}")
            logger.error(f"Error details: {str(e)}")

    async def on_raw_reaction_add(self, payload):
        # Handle event when a reaction is added
        await self.reaction_role(payload, True)

    async def on_raw_reaction_remove(self, payload):
        # Handle event when a reaction is removed
        await self.reaction_role(payload, False)

if __name__ == '__main__':
    # Initialize and run the bot
    client = ProjectsClient(guild_id, roles_channel_id)
    client.run(discord_token) 