// $.get("test.txt", null, function(data, textStatus){
//     console.log(data);
// }, "text");
$(function(){
    $("#fileInfo").click(function(){
        console.log($("#myFile").get(0).files[0].name);
        var fileData = $("#myFile").get(0).files[0];
        var txt = "name: "+fileData.name+"<br />";
        txt += "size: "+fileData.size+"<br />";
        txt += "type: "+fileData.type+"<br />";
        console.log(txt);
        $("#result").html(txt);
    });
});
// $(function () {
//     $("#data").load("test.txt");
// }
// );
