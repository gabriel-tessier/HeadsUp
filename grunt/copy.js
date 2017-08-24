'use strict';

module.exports = {
	frontend: {
		files: [
			{
				expand: true,
				cwd: '<%= pkg.app.bower_components %>/bootstrap-sass/assets/fonts/bootstrap',
				src: ['**'],
				dest: '<%= pkg.app.assets %>/headsup/fonts/bootstrap'
			},
			{
				expand: true,
				cwd: '<%= pkg.app.templates %>/main/staging',
				src: ['base.html', 'home.html'],
				dest: '<%= pkg.app.templates %>/main/layout'
			}
		]
	},
	backend: {
		files: [
			{
				expand: true,
				cwd: '<%= pkg.app.bower_components %>/bootstrap-sass/assets/fonts/bootstrap',
				src: ['**'],
				dest: '<%= pkg.app.assets %>/admin/fonts/bootstrap'
			},
			{
				expand: true,
				cwd: '<%= pkg.app.templates %>/admin/staging',
				src: ['base.html'],
				dest: '<%= pkg.app.templates %>/admin/layout'
			}
		]
	}
}
