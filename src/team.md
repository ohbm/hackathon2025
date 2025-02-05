---
layout: default.md
title: Team
---
<!-- Added floating credits for background photo -->
<div class="photo-credits">
  Background photo by
  <a href="https://flic.kr/p/fbNRhR" target="_blank" rel="noopener">Andrew S.</a>
  distributed under a
  <a href="https://creativecommons.org/licenses/by-sa/2.0/" target="_blank" rel="noopener"><i class="fab fa-creative-commons"></i><i class="fa-brands fa-creative-commons-by"></i><i class="fa-brands fa-creative-commons-sa"></i></a>
  CC BY-SA 2.0 license.
</div>

<!-- set background image -->
<style>
  body {
    background: url('../_img/background_imgs/brisbane_6.jpg') no-repeat center center/cover;
  }
</style>


<section class="content">

# Meet our amazing team!

## Hackathon organizers

{% include "team.liquid", members: team.members %}

## The OSSIG

{% include "team.liquid", members: team.ossig %}

</section>
