// $.get("test.txt", null, function(data, textStatus){
//     console.log(data);
// }, "text");
$(function(){
    $("#fileInfo").click(function(){
        $("#myFile").each(function(){
            var fileData = this.files[0];
            var txt = "name: "+fileData.name+"<br />";
            txt += "size: "+fileData.size+"<br />";
            txt += "type: "+fileData.type+"<br />";
            console.log(txt);
            $("#result").html(txt);
        });
    });
});
// $(function () {
//     $("#data").load("test.txt");
// }
// );
