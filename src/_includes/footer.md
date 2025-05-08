<footer>
  <section id="sponsors">
    <h2>Our Proud Sponsors</h2>
    <p>We are immensely grateful for the generous contributions of our sponsors. Their support makes our event possible and helps our community to achieve greater heights. Our most sincere thanks goes to:</p>
    <div class="sponsor-logos">
      {% for sponsor in sponsors.sponsorlist -%}
        <a href="{{ sponsor.url }}" target="_blank" rel="noopener noreferrer">
          <img src="/_img/{{ sponsor.logo }}" alt="{{ sponsor.name }} logo" title="{{ sponsor.name }}">
        </a>
        {{sponsor.name}} 
      {% endfor -%}
    </div>
  </section>
  <section id="contact">
      <div class="container">
          <div class="row">
              <div class="col-lg-8 col-lg-offset-2 text-center" style="margin-bottom: 20px;">
                  <h2 class="section-heading">Let's Get In Touch!</h2>
                  <hr class="primary">
                  <p>Have questions or need assistance? We're here to help!</p>
                  <p>Feel free to reach out to us using any of the following methods:</p>
              </div>
              <div class="col-lg-6 col-lg-offset-3 text-center">
                  {% for method in contact.methods -%}
                  <span class="d-inline-block">
                      <a href="{{ method.url }}">
                          <i class="{{ method.icon }} fa-4x wow bounceIn" data-wow-delay="{{ method.delay }}" aria-label="{{ method.label }}" title="{{ method.label }}"></i>
                      </a>
                  </span>
                  {%- endfor %}
              </div>
          </div>
      </div>
  </section>
  <section id="conduct">
    <p><a href="/conduct/">Code of Conduct</a></p>
  </section>
</footer>
