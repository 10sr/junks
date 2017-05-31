$(function(){
  var jsDataContainer = $("#jsDataContainer");
  var videoUrl = jsDataContainer.attr("videoUrl");

  console.log(videoUrl);

  var player = $("#player");

  var videoSource = $("<source />", {
    src: videoUrl
  }).appendTo(player);

});
