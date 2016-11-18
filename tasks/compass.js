'use strict';

module.exports = {
	options: {
		relativeAssets: true,
		debugInfo: false,
		cacheDir: '<%= pkg.app.tmp %>/sass-cache'
	},
	dev: {
		options: {
			importPath: '<%= pkg.app.lib %>/bower_components',
			javascriptsDir: '<%= pkg.app.assets %>/headsup/scripts',
			sassDir: '<%= pkg.app.assets %>/headsup/styles/base',
			cssDir: '<%= pkg.app.assets %>/headsup/styles/base',
			imagesDir: 'app/static/images',
			noLineComments: true,
			watch: false
		}
	},
	admindev: {
		options: {
			importPath: '<%= pkg.app.lib %>/bower_components',
			javascriptsDir: '<%= pkg.app.assets %>/admin/scripts',
			sassDir: '<%= pkg.app.assets %>/admin/styles/base',
			cssDir: '<%= pkg.app.assets %>/admin/styles/base',
			imagesDir: 'app/static/images',
			noLineComments: true,
			watch: false
		}
	},
	dist: {
		options: {
			importPath: '<%= pkg.app.lib %>/bower_components',
			javascriptsDir: '<%= pkg.app.assets %>/headsup/scripts',
			sassDir: '<%= pkg.app.assets %>/headsup/styles/base',
			cssDir: '<%= pkg.app.assets %>/headsup/styles/base',
			imagesDir: 'app/static/images',
			noLineComments: true,
			watch: false
		}
	}
}
