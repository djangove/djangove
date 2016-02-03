/* Sass tasks */

var config = require('../config.json');
var routes = require('./routes.json');
var gulpif = require('gulp-if');

// Gulp Dependencies
var gulp = require('gulp');
var browserSync = require('browser-sync');

// Style Dependencies
var sass = require('gulp-sass');
var prefix = require('gulp-autoprefixer');

function sassTask(route){
	'use strict';
    return gulp.src(route.src)
    .pipe(sass({includePaths: ['sass']}))
    .pipe(gulpif(config.browserSync, browserSync.reload({stream:true})))
    .pipe(gulp.dest(route.dest));
}

gulp.task('sass', function() {
    sassTask(routes.sass);
});