/* Watch tasks */

// Gulp Dependencies
var gulp = require('gulp');

gulp.task('watch', function() {
  gulp.watch(['./src/sass/**/*.sass', './src/sass/**/*.scss'], ['sass']);
});