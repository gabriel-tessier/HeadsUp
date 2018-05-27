const path = require('path');
const merge = require('webpack-merge');
const common = require('./webpack.common.js');

module.exports = function(config) {
	var plugins = [];

	return merge(common(config), {
		plugins: plugins
	});
};
