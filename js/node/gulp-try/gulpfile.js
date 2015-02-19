var gulp = require('gulp');
var uglify = require('gulp-uglify');

gulp.task('consolelog', function(){
  console.log('Task named default ran');
});


// task dependencies
// Run order: msguglify -> uglify

gulp.task('uglify', ['msguglify'], function(){
  gulp.src('./src/**/*.js')
    .pipe(uglify())
    .pipe(gulp.dest('dst'));
});

gulp.task('msguglify', function(done){
  console.log('Running uglify');
  done();
});

gulp.task('default', ['uglify']);
