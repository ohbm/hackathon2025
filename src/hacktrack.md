---
layout: default.md
title: HackTrack
---
<div class="photo-credits">
  Background photo by
  <a href="https://flic.kr/p/p2RasG" target="_blank" rel="noopener">Andrew S.</a>
  distributed under a
  <a href="https://creativecommons.org/licenses/by-sa/2.0/" target="_blank" rel="noopener"><i class="fab fa-creative-commons"></i><i class="fa-brands fa-creative-commons-by"></i><i class="fa-brands fa-creative-commons-sa"></i></a>
  CC BY-SA 2.0 license.
</div>

<!-- set background image -->
<style>
  body {
    background: url('../_img/background_imgs/brisbane_3.jpg') no-repeat center center/cover;
  }
</style>

<section class="content">

{% block content %}

# Projects

The HackTrack is the hacking component of a Brainhack event, where people can work together on projects.
For tutorials and learning sessions check the [TrainTrack page](/traintrack).

## What projects? Any kind! From exploding brains to resource gathering and data sharing!

<div class="submit-projects-container">
  <a class="submit-projects-button" href="https://github.com/ohbm/hackathon2025/issues/new?assignees=bhvieira&labels=Hackathon+Project&projects=&template=brainhack-hacktrack-project.yml&title=%3CMy+Project+Name%3E">
    Submit a project
  </a>
</div>

---

{% include "hackathon-projects.md" %}

{% endblock %}

</section>