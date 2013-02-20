var Clock = (function () {
    function init (){
        if(window.addEventListener) { /* W3C準拠ブラウザ用 */
            window.addEventListener("load", draw, false);
            // } else if(window.attachEvent) { /* Internet Explorer用 */
            //     window.attachEvent("onload", init);
        }
    };
    function draw () {
        /* canvas要素のノードオブジェクト */
        var canvas = document.getElementById('clock');
        /* canvas要素の存在チェックとCanvas未対応ブラウザの対処 */
        if ( ! canvas || ! canvas.getContext ) {
            return false;
        }
        /* 2Dコンテキスト */
        var ctx = canvas.getContext('2d');
        /* 四角を描く */
        ctx.strokeStyle = '#ff0000';
        ctx.beginPath();
        ctx.moveTo(20, 20);
        ctx.lineTo(120, 20);
        ctx.lineTo(120, 120);
        ctx.lineTo(20, 120);
        ctx.closePath();
        ctx.stroke();
        ctx.beginPath();
        ctx.arc(70, 70, 60, 0, Math.PI*2, false);
        ctx.strokeStyle = '#00ff00';
        ctx.stroke();
        return null;
    };
    return {
        init : init
    };
})();

Clock.init();
