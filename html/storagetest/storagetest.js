var StorageTest = (function(){
    var k1 = "key1";
    var k2 = "key2";

    function init(){
        window.addEventListener("load", onLoadListener);
    }

    function onLoadListener(){
        if (! window.localStorage) {
            alert("This browser does not support localstorage.");
            return;
        }

        var v1 = window.localStorage.getItem(k1);
        var v2 = window.localStorage.getItem(k2);
        var num1, num2;

        if (v1) {
            num1 = parseInt(v1) + 1;
        } else {
            num1 = 0;
        }
        if (v2) {
            num2 = parseInt(v2) + 2;
        } else {
            num2 = 0;
        }

        alert("num1 : " + num1.toString() + " num2 : " + num2.toString());

        window.localStorage.setItem(k1, num1.toString(), true);
        window.localStorage.setItem(k2, num2.toString(), true);
    }

    return {
        init : init
    };
})();

StorageTest.init();
