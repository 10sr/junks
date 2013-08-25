var Source = (function () {
    function init (){
        window.onload = start;
    };

    function start () {
        var xhr = new XMLHttpRequest();
        xhr.open("GET", "http://bing.com", true);
        xhr.onreadystatechange = function(){
            alert(xhr.responseText);
            // alert(xhr.status.toString() + "\n" + xhr.responseText);
            // if (xhr.readyState === 4 && xhr.status === 200){
            // }
        };
        xhr.send(null);
    };

    return {
        init : init
    };
})();

Source.init();
