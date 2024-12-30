<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <link rel="stylesheet" href="/bundle.css">
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.6.0/css/all.min.css">
  <title>{{ title }}</title>
</head>
<body>
  <!-- Include header -->
  {% include 'header.md' %}

  <main>
  <section class="markdown-body">
    {{ content }}
  </section>
  </main>

  <!-- Include footer -->
  {% include 'footer.md' %}
</body>
</html>