var gulp = require('gulp');
var sass = require('gulp-sass');
var connect = require('gulp-connect');


// SASS Task
gulp.task('styles', function() {
    gulp.src('sass/**/*.scss')
        .pipe(sass().on('error', sass.logError))
        .pipe(gulp.dest('templates/static/styles/'));
});

// Watch task for SASS
gulp.task('watch', function() {
    gulp.watch('sass/**/*.scss',['styles']);
})

// Server Task - Livereload not really working
gulp.task('webserver', function() {
  connect.server({
    livereload: true
  });
});

// Default task to run the above tasks
gulp.task('default', ['webserver', 'watch']);