/* gulpfile.js */

var config = require('./config.json');

// Gulp Dependencies
var gulp = require('gulp');
var requireDir = require('require-dir');
var browserSync = require('browser-sync');
var rename = require('gulp-rename');

requireDir('./gulp-tasks', {recurse:true});

/* Browser Sync task */

gulp.task('browser-sync', function() {
  browserSync({server: {baseDir: './dist'}});
});

gulp.task('default', ['sass', 'watch', 'browser-sync']);
