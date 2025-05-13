#!/usr/bin/env node

const fs = require('fs');
const axios = require('axios');
const yaml = require('js-yaml');
const path = require('path');
require('dotenv').config();

async function fetchGhIssues() {
    const GH_AUTH = process.env.GH_AUTH;
    const REPO = 'ohbm/hackathon2025';
    const ISSUE_LABEL_PROJECT = ':rocket: HackTrack Project';
    const ISSUE_LABEL_TUTORIAL = '🎓 TrainTrack Tutorial';
    const ISSUE_READY_LABEL = ':mag: Review: Good to go ✅';
    const ISSUE_FILTER = `per_page=100`;
    const URL = `https://api.github.com/repos/${REPO}/issues?${ISSUE_FILTER}`;

    // Load the YAML template
    const hacktrackIssueForm = yaml.load(fs.readFileSync('.github/ISSUE_TEMPLATE/brainhack-hacktrack-project.yml', 'utf8'));
    const traintrackIssueForm = yaml.load(fs.readFileSync('.github/ISSUE_TEMPLATE/brainhack-traintrack-project.yml', 'utf8'));
    const hacktrackFields = hacktrackIssueForm.body.filter(f => f.type !== 'markdown');
    const traintrackFields = traintrackIssueForm.body.filter(f => f.type !== 'markdown');
    const fields = hacktrackFields.concat(traintrackFields);

    try {
        // Fetch issues from GitHub
        const res = await axios.get(URL, {
            headers: {
                Authorization: `token ${GH_AUTH}`
            }
        });

        const issues = res.data;
        const projectsList = [];
        const tutorialsList = [];

        for (const issue of issues) {
            if (!issue.labels.some(label => label.name === ISSUE_READY_LABEL)) continue;
            if (issue.state !== 'open') continue;

            try {
                const body = issue.body;
                const lines = body.replace(/\r\n/g, '\n').split('\n').map(line => line.trim());

                const fieldOrdering = fields.map(field => {
                    const fieldLabel = field.attributes.label;
                    const fieldStart = lines.findIndex(line => line.startsWith(`### ${fieldLabel}`));
                    return { field, fieldStart };
                }).filter(f => f.fieldStart !== -1);

                fieldOrdering.sort((a, b) => a.fieldStart - b.fieldStart);

                const issueInfo = {};
                const fieldBounds = fieldOrdering.map((field, idx) => ({
                    current: field,
                    next: fieldOrdering[idx + 1] || null
                }));

                for (const { current, next } of fieldBounds) {
                    const fieldId = current.field.id;
                    const start = current.fieldStart;
                    const end = next ? next.fieldStart : lines.length;

                    let fieldValue = lines.slice(start + 1, end).join('\n').replace(/<!--.*?-->/gs, '').trim();

                    if (fieldValue === '_No response_') fieldValue = null;

                    if (current.field.type === 'checkboxes') {
                        const options = current.field.attributes.options.map(opt => opt.label.trim());
                        const selectedOptions = fieldValue ? fieldValue.split('\n')
                            .filter(line => line.startsWith('- [X] ') || line.startsWith('- [x] '))
                            .map(line => line.slice(6).trim())
                            .filter(option => options.includes(option)) : [];
                        fieldValue = selectedOptions;
                    }

                    issueInfo[fieldId] = fieldValue;
                }

                if (issueInfo.hub && issueInfo.otherhub && issueInfo.otherhub.includes(issueInfo.hub)) {
                    issueInfo.otherhub = issueInfo.otherhub.filter(hub => hub !== issueInfo.hub);
                }

                issueInfo.title = issue.title;
                issueInfo.link = issue.html_url;
                issueInfo.details = issue.body;
                issueInfo.issue = issue.number;
                issueInfo.leads = issueInfo.leads || [];
                issueInfo.shortname = issueInfo.shortname || issue.title.toLowerCase().replace(/\s+/g, '_');

                if (issue.labels.some(label => label.name === ISSUE_LABEL_PROJECT)) {
                    projectsList.push(issueInfo);
                } else if (issue.labels.some(label => label.name === ISSUE_LABEL_TUTORIAL)) {
                    tutorialsList.push(issueInfo);
                }

                // Check if image file exists, if not, download it
                const imageDir = path.join(__dirname, '../src/_img');
                // not every image will be a png, download as is
                const imageFile = issueInfo['website-image']; // this is a full URL
                if (imageFile) {
                    const imageExt = imageFile.split('.').pop();
                    const imageName = issueInfo.chatchannel + '.' + imageExt;
                    // if not a valid image extension, skip
                    if (!['png', 'jpg', 'jpeg', 'gif', 'svg'].includes(imageExt)) {
                        console.log(`Image extension not supported: ${imageName}`);
                        continue;
                    }
                    const imagePath = path.join(imageDir, imageName);
                    if (!fs.existsSync(imagePath)) {
                        const imageRes = await axios.get(imageFile, { responseType: 'stream' });
                        imageRes.data.pipe(fs.createWriteStream(imagePath));
                        console.log(`Image downloaded: ${imageName}`);
                    }
                    issueInfo['image_path'] = imageName;
                }

                const labels = issue.labels.map(label => label.name);
                // keep labels that start with ':label:' or 🌐, remove that from the resulting labels
                filteredLabels = labels.filter(label => label.startsWith(':label: ') || label.startsWith('🌐 ') || label.startsWith(':computer: '))
                issueInfo.categories = filteredLabels.map(label => label.replace(':label: ', '').replace('🌐 ', '').replace(':computer: ', ''));

            } catch (err) {
                console.error(`Error processing issue ${issue.number}:`, err.message);
            }
        }

        // Save issues list to YAML files
        const projectsYamlContent = { projectlist: projectsList };
        fs.writeFileSync('./src/_data/projects.yaml', yaml.dump(projectsYamlContent));
        console.log('Projects saved to ./src/_data/projects.yaml');

        const tutorialsYamlContent = { tutoriallist: tutorialsList };
        fs.writeFileSync('./src/_data/tutorials.yaml', yaml.dump(tutorialsYamlContent));
        console.log('Tutorials saved to ./src/_data/tutorials.yaml');
    } catch (err) {
        console.error('Error fetching issues:', err.message);
    }
}

fetchGhIssues();