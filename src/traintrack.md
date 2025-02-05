---
layout: default.md
title: TrainTrack
---
<!-- Added floating credits for background photo -->
<div class="photo-credits">
  Background photo by
  <a href="https://flic.kr/p/oLztbu" target="_blank" rel="noopener">Andrew S.</a>
  distributed under a
  <a href="https://creativecommons.org/licenses/by-sa/2.0/" target="_blank" rel="noopener"><i class="fab fa-creative-commons"></i><i class="fa-brands fa-creative-commons-by"></i><i class="fa-brands fa-creative-commons-sa"></i></a>
  license.
</div>

<!-- set background image -->
<style>
  body {
    background: url('../_img/background_imgs/brisbane_4.jpg') no-repeat center center/cover;
  }
</style>

<section class="content">

{% block content %}

# Sessions

The TrainTrack is the official learning side of a Brainhack event, where people can learn together in hands-on or didactic sessions.
For hacking projects check the [HackTrack page](/hacktrack).

### What sessions? Any kind! From data management to data visualization!

<div class="submit-projects-container">
  <a class="submit-projects-button" href="https://github.com/ohbm/hackathon2025/issues/new?assignees=bhvieira&labels=TrainTrack+Tutorial&projects=&template=brainhack-traintrack-project.yml&title=%3CMy+Project+Name%3E">
    Submit a tutorial
  </a>
</div>

---

{% include "traintrack-tutorials.md" %}

{% endblock %}

</section>