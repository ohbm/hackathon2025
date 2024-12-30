const yaml = require("js-yaml");
const markdownIt = require("markdown-it");

module.exports = async function (eleventyConfig) {
	const { EleventyHtmlBasePlugin } = await import("@11ty/eleventy");

	eleventyConfig.addPlugin(EleventyHtmlBasePlugin);

	// Copy CSS to production
	eleventyConfig.addPassthroughCopy("src/css");
	eleventyConfig.addWatchTarget("src/css");
	// Copy images to production
	eleventyConfig.addPassthroughCopy("src/_img");
	eleventyConfig.addWatchTarget("src/_img");
	// Yaml support
	eleventyConfig.addDataExtension("yaml", contents => yaml.load(contents));
	
	// Add markdownify filter
	eleventyConfig.addFilter("markdownify", (content) => {
		const md = new markdownIt();
		return md.render(content);
	});

	return {
		dir: {
			input: "src",
			output: "_site"
		},
		pathPrefix: "/hackathon2025/",
	};
};


