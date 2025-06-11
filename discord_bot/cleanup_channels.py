"""
TESTING ONLY - Channel Cleanup Script

⚠️  WARNING: THIS SCRIPT IS FOR TESTING PURPOSES ONLY ⚠️

This script cleans up project channels from the Discord server so you can 
test whether the bot creates them correctly. It is NOT meant for production use.

What it does:
- Deletes ALL channels in "Projects" and "Projects-text" categories
- Leaves all roles untouched (preserves user assignments)
- Used to reset the server state for testing bot functionality

Usage: python cleanup_channels.py
"""

import discord
import logging
from dotenv import load_dotenv
import os
import asyncio

# Initialize logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger('discord')

class ProjectsClient(discord.Client):
    """
    TESTING CLEANUP CLIENT
    
    This client connects to Discord and removes all project channels
    for testing purposes. It does NOT delete roles or affect user assignments.
    """
    def __init__(self, guild_id: int, *args, **kwargs):
        intents = discord.Intents.default()
        super().__init__(intents=intents, *args, **kwargs)
        self._guild_id = guild_id

    async def on_ready(self):
        logger.info(f'Logged in as {self.user} (ID: {self.user.id})')
        logger.info('------')
        guild = self.get_guild(self._guild_id)
        if guild:
            await self.delete_non_entrance_channels(guild)
        logger.info('Cleanup completed. Shutting down...')
        # Small delay to ensure all operations complete
        await asyncio.sleep(1)
        await self.close()

    async def delete_non_entrance_channels(self, guild: discord.Guild):
        deleted_count = 0
        
        # ONLY Delete project channels from Projects and Projects-text categories
        projects_category = discord.utils.get(guild.categories, name="Projects")
        projects_text_category = discord.utils.get(guild.categories, name="Projects-text")
        
        categories_to_clean = [projects_category, projects_text_category]
        
        logger.info("CHANNELS ONLY: Deleting channels in 'Projects' and 'Projects-text' categories")
        
        for category in categories_to_clean:
            if category:
                logger.info(f'Cleaning category: {category.name}')
                # Make a copy of the channels list to avoid modification during iteration
                channels_to_delete = list(category.channels)
                for channel in channels_to_delete:
                    try:
                        logger.info(f'Deleting channel: {channel.name} (ID: {channel.id}) from category {category.name}')
                        await channel.delete()
                        deleted_count += 1
                    except discord.errors.NotFound:
                        logger.warning(f'Channel {channel.name} already deleted')
                    except Exception as e:
                        logger.error(f'Failed to delete channel {channel.name}: {e}')
        
        logger.info(f'CLEANUP COMPLETED: {deleted_count} channels deleted.')

if __name__ == '__main__':
    load_dotenv('../.env')
    guild_id = int(os.getenv('DISCORD_GUILD_ID', ''))
    token = os.getenv('DISCORD_TOKEN', '')

    client = ProjectsClient(guild_id)
    client.run(token) 