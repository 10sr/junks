var OnHC = (function(){
    function init(){
        window.onload = start;
        window.onhashchange = onhash;
        // or
        // window.addEventListener("hashchange", onhash, false);
    };

    function start(){
        onhash();
    };

    function onhash(){
        var h = window.content.location.hash;
        if (h) {
            alert(h);
        }
    }

    return {
        init : init
    };
})();

OnHC.init();
