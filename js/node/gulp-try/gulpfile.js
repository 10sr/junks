var gulp = require('gulp');
var uglify = require('gulp-uglify');

gulp.task('uglify', function(){
  gulp.src('./src/**/*.js')
    .pipe(uglify())
    .pipe(gulp.dest('dst'));
});

gulp.task('consolelog', function(){
  console.log('Task named default ran');
});

gulp.task('default', ['consolelog', 'uglify']);
