var DMD = (function(){
    function init(){
        // window.onload = onLoadHandler;
        // window.onhashchange = onHashChangeHandler;
        // or
        window.addEventListener("load", onLoadHandler, false);
        window.addEventListener("hashchange", onHashChangeHandler, false);
    };

    function onLoadHandler(){
        onHashChangeHandler();
    };

    function onHashChangeHandler(){
        var h = window.content.location.hash;
        // alert(h);
        if (h) {
            loadContent(h.substr(1));
        } else {
            clearContent();
        }
    }

    function loadContent(name){
        getContent(name + ".md", function(xhr){
            // content available when xhr.status === 0 ...??
            // alert(xhr.status);
            // alert(xhr.responseText);
            var div = window.document.getElementById("dmd-content");
            div.innerHTML = marked(xhr.responseText);
        });
    }

    function clearContent(){
        var div = window.document.getElementById("dmd-content");
        div.innerHTML = "";
    }

    function dirName(str){
        return str.replace(/[^/]*$/, "");
    }

    function getContent(name, callback){
        var xhr = new XMLHttpRequest();
        xhr.open("GET", name, true);
        xhr.onreadystatechange = function(){
            if (xhr.readyState === 4) {
                callback(xhr);
            }
        };
        xhr.overrideMimeType('text/plain; charset=UTF-8');
        xhr.send(null);
    }

    return {
        init : init
    };
})();

DMD.init();
