$.get("test.txt", null, function(data, textStatus){
    console.log(data);
}, "text");
$(function(){
    $("#fileInfo").click(function(){
        console.log($("#myFile"));
        $("#myFile").each(function(){
            var fileData = this.files[0]; // how to get file object?
            var txt = "name: "+fileData.name+"<br />";
            txt += "size: "+fileData.size+"<br />";
            txt += "type: "+fileData.type+"<br />";
            console.log(txt);
            // $("#result").innerHTML = txt;
        });
    });
});
// $(function () {
//     $("#data").load("test.txt");
// }
// );
