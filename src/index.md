---
layout: default.md
title: OHBM Hackathon 2025
---

<div class="bg-image" style="background: url('_img/background_imgs/brisbane_1.jpg') no-repeat center center/cover;"></div>

<!-- Added floating credits for background photo -->
<div class="photo-credits">
  Background photo by
  <a href="https://flic.kr/p/puMyXa" target="_blank" rel="noopener">Andrew S.</a>
  distributed under a
  <a href="https://creativecommons.org/licenses/by-sa/2.0/" target="_blank" rel="noopener"><i class="fab fa-creative-commons"></i><i class="fa-brands fa-creative-commons-by"></i><i class="fa-brands fa-creative-commons-sa"></i></a>
  CC BY-SA 2.0 license.
</div>

<section class="content">
  {% block content %}
  ## Welcome to the OHBM Hackathon 2025!

  <div class="cta-buttons">
    <a href="#" class="btn-primary" onclick="showPopup()">Registration ended on June 14th, 2025</a>
  </div>

  Join us in vibrant Brisbane for an unforgettable experience of innovation, collaboration, and learning.
  Together, let's shape the future of neuroimaging and open science!

  What is new this year? For the first time, this year's BrainHack will feature the [NeuroDesk](https://www.neurodesk.org/) Workshop  & the [Neuroimaging Statistics Workshop (check the program here!)](https://sites.google.com/view/nsw2025).
  **The NeuroDesk Workshop** will introduce participants to NeuroDesk, an open-source flexible and scalable data analysis environment for reproducible neuroimaging.
  **The Neuroimaging Statistics Workshop** will showcase emerging brain image processing & analysis techniques through expert lectures, as well as networking opportunities for students and researchers.

  To ensure your participation in either or both workshops, *please select the appropriate option during registration*.
  
  The OHBM Hackathon will take place from June 21-23, 2025, at the Precinct (check the [venue](venue)).
  Registration has ended as of June 14th, 2025.
  We look forward to welcoming all registered participants in Brisbane!

  {% endblock %}
</section>

<section class="content">

{% block content %}

## Who supports the OHBM Hackathon?

The OHBM Hackathon is organized by the Open Science Special Interest Group (SIG) with the support of the Organization for Human Brain Mapping (OHBM) and our generous [sponsors](#sponsors).

  <section id="sponsorsindex">
    <div class="sponsor-logos">
      {% for sponsor in sponsors.sponsorlist -%}
        <a href="{{ sponsor.url }}" target="_blank" rel="noopener noreferrer">
          <img src="/_img/{{ sponsor.logo }}" alt="{{ sponsor.name }} logo" title="{{ sponsor.name }}">
        </a>
        {{sponsor.name}} 
      {% endfor -%}
    </div>
  </section>

## What is OHBM?

OHBM is the Organization for Human Brain Mapping.
A society of scientists dedicated to mapping the brain using all neuroimaging technologies.

## What is Brainhack?

An event where people get together to learn about open science and to collaborate on projects they are interested in—it can be on anything!

The OHBM Brainhack is a chance for anyone interested in brains to work collaboratively on common projects and learn about new ideas and tools in open science.

Brainhacks are not the typical academic conference.
Here, attendees can actively take part in the program and learn from each other—sounds like something you would like? You can become a part of the event as a volunteer by filling out the form linked above.
Many Brainhack projects might involve coding, but it is not a requirement, and you can contribute in most cases even without coding skills.

We look for neuroimagers of all modalities from all over the world at different career stages, and from all racial and gender backgrounds who are interested in working together to build an open science community.
If you're new to the Brainhack community, please join us! If you belong to any minority groups, we want to reiterate that we want you here and are excited to have you join us!


{% endblock %}
</section>

