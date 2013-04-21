// $.get("test.txt", null, function(data, textStatus){
//     console.log(data);
// }, "text");

$(function(){
    // initialize field
    function initField(){
        ;
    };

    $("#fileInfo").click(function(){
        // http://thinkit.co.jp/story/2013/02/06/3953
        var fileData = $("#myFile").get(0).files[0];
        var txt = "name: " + fileData.name + "<br />";
        txt += "size: " + fileData.size + "<br />";
        txt += "type: " + fileData.type + "<br />";
        console.log(txt);
        $("#result").html(txt);
    });
});
// $(function () {
//     $("#data").load("test.txt");
// }
// );
