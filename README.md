# Hackathon 2025

Welcome to the OSSIG OHBM Hackathon 2025 website!
This website is built using [Eleventy](https://www.11ty.dev/), a static site generator based on JavaScript.

## Local Development

To serve the website locally, follow these steps:

1. Clone the repository:
```bash
    git clone https://github.com/ohbm/hackathon2025.git
```
2. Navigate to the project directory:
```bash
cd hackathon2025
```
3. Install the dependencies:
```bash
npm install
```

This will install all the necessary dependencies to serve the website locally.
Eleventy requires `Node.js` 18 or higher to run.
This will also bundle the `npm` package manager, which is used to install the dependencies.

To serve the website locally, run the following command:
```bash
npx @11ty/eleventy --serve
```

This will start a local server at `http://localhost:8080/` (or another port of your choice) where you can view the website.

## Structure

The website is structured as follows:

- `src/`: Contains the source files for the website.
  - `_includes/`: Contains the reusable components for the website.
  - `_data/`: Contains the data files for the website.	
    - `projects.yaml`: the HackTrack projects.
    - `tutorial.yaml`: the TrainTrack tutorials.
    - `team.yaml`: the team.
    - `_img/`: Contains the images for the website.
    - `css/`: Contains the styles for the website.
  - `conduct.md`: The OHBM Code of Conduct.
  - `contact.md`: The contact information for the event.
  - `css-bundle.njk`: A CSS bundle for the website.
  - `hacktrack.md`: The HackTrack page.
  - `index.md`: The home page.
  - `schedule.md`: The schedule for the event.
  - `team.md`: The team page.
  - `traintrack.md`: The TrainTrack page.
  - `venue.md`: The venue page.
- `.eleventy.js`: The Eleventy configuration file.
- `package.json`: The npm configuration file.
- `package-lock.json`: The npm lock file.
- `README.md`: The README file.