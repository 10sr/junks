var gulp = require('gulp');
var jasmine = require('gulp-jasmine');
var karma = require('gulp-karma');

gulp.task('default', function(){
  return gulp.src(['spec/*.js']).
    //pipe(jasmine());
    pipe(karma({
      action: 'run'
    }));
})
