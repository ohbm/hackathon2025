<section class="projects">
    {% if projects.projectlist.length > 0 %}
        <div id="filter-container">
            {% assign all_tags = "" %}
            {% for project in projects.projectlist %}
                {% for tag in project.categories %}
                    {% assign all_tags = all_tags | append: tag | append: "," %}
                {% endfor %}
            {% endfor %}
            {% assign unique_tags = all_tags | split: "," | uniq %}
            {% for tag in unique_tags -%}
                <button class="filter-button" onclick="toggleTag(this, '{{ tag }}')" id="{{ tag }}">{{ tag }}</button>
            {%- endfor %}
        </div>
        <div id="hackathon-container">
            {% for project in projects.projectlist -%}
                <div class="hackathon-project-card" data-tags="{{ project.categories | join: ' ' }}">
                    <div class="hackathon-img-wrapper">
                        <a href="https://github.com/ohbm/hackathon2025/issues/{{ project.issue }}">
                            <img src="/_img/{{ project.image_path }}" alt="Hackathon">
                        </a>
                    </div>
                    <div class="hackathon-details animated hiding">
                        <h3>{{ project.title }}</h3>
                        <ul>
                            {% for tag in project.categories -%}
                                <li class="tag">{{ tag }}</li>
                            {%- endfor %}
                        </ul>
                        <div class="text-primary reveal-button"><i class="fa-solid fa-magnifying-glass"></i> Project details</div>
                    </div>
                    <div class="hackathon-hidden-details">
                        <div class="button-container">
                            <div class="btn-primary">
                                <a href="https://github.com/ohbm/hackathon2025/issues/{{ project.issue }}" target="_blank">
                                    <i class="fa-brands fa-github"></i> GitHub issue 
                                </a>
                            </div>
                            <div class="btn-primary">
                                <a href="{{ project.link }}" target="_blank">
                                    <i class="fa-solid fa-link"></i> Project URL 
                                </a>
                            </div>
                        </div>
                        <div class="markdown-content">
                            {{ project.summary | markdownify }}
                        </div>
                    </div>
                </div>
            {%- endfor %}
        </div>
    {% else %}
        Be patient, this emptiness will soon be filled with many amazing HackTrack projects.
        <div class="submit-projects-container">
            <a class="submit-projects-button" href="https://ohbm.github.io/hackathon2024/hacktrack/">
                Check last year's projects for inspiration!
            </a>
        </div>
    {% endif %}
</section>

<script>
document.addEventListener('DOMContentLoaded', () => {
    document.querySelectorAll('.reveal-button').forEach((button) => {
        button.addEventListener('click', function () {
            const card = button.closest('.hackathon-project-card');
            const details = card.querySelector('.hackathon-hidden-details');
            if (details) {
                if (details.classList.contains('show')) {
                    details.classList.remove('show');
                    card.classList.remove('fullscreen');
                    button.innerHTML = '<i class="fa-solid fa-magnifying-glass"></i> Project details';
                    document.body.classList.remove('no-scroll'); // Remove no-scroll class
                } else {
                    details.classList.add('show');
                    card.classList.add('fullscreen');
                    button.innerHTML = '<i class="fa-solid fa-xmark"></i> Hide details';
                    document.body.classList.add('no-scroll'); // Add no-scroll class
                }
            }
        });
    });
    document.addEventListener('click', function (event) {
        const fullscreenCard = document.querySelector('.hackathon-project-card.fullscreen');
        if (fullscreenCard && !fullscreenCard.contains(event.target)) {
            fullscreenCard.querySelector('.hackathon-hidden-details').classList.remove('show');
            fullscreenCard.classList.remove('fullscreen');
            fullscreenCard.querySelector('.reveal-button').innerHTML = '<i class="fa-solid fa-magnifying-glass"></i> Project details';
            document.body.classList.remove('no-scroll'); // Remove no-scroll class
        }
    });
});
// Keep only one tag active at a time, the tags in the projects are also highlighted
function toggleTag(button, tag) {
    const tags = document.querySelectorAll('.filter-button');
    const projects = document.querySelectorAll('.hackathon-project-card');
    tags.forEach((t) => {
        if (t === button) {
            t.classList.toggle('active');
        } else {
            t.classList.remove('active');
        }
    });
    const activeTag = document.querySelector('.filter-button.active');
    if (activeTag) {
        // If a tag is active, filter projects
        const activeTagName = activeTag.id;
        projects.forEach((project) => {
            if (project.getAttribute('data-tags').includes(activeTagName)) {
                project.classList.remove('hide');
            } else {
                project.classList.add('hide');
            }
        });
    } else {
        // If no tag is active, show all projects
        projects.forEach((project) => project.classList.remove('hide'));
    };
}
</script>
