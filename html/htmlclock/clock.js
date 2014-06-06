var Clock = (function () {
    // -------> x
    // |
    // |
    // \/ y

    const pi = Math.PI;

    function init (){
        window.onload = start;
    };

    function start () {
        var canvas = document.getElementById('clock');
        if ( ! canvas || ! canvas.getContext ) {
            return false;
        };
        setInterval(function () { draw(canvas); }, 1000);
        return null;
    };

    function draw (canvas) {
        var width = parseInt(canvas.width);
        var height = parseInt(canvas.height);

        var ctx = canvas.getContext('2d');

        ctx.clearRect(0, 0, width, height);

        var mr = Math.min(width, height) / 2.0;
        var x0 = width / 2.0;
        var y0 = height / 2.0;

        now = new Date();
        var s = now.getSeconds();
        var m = now.getMinutes();
        var h = now.getHours();
        var srad = 2 * pi * s / 60.0;
        var mrad = 2 * pi * m / 60.0 + 2 * pi * s / 60.0 / 60.0;
        var hrad = 2 * pi * h / 12.0 + 2 * pi * m / 12.0 / 60.0;

        // ctx.strokeStyle = '#00ff00';

        // background
        ctx.fillStyle = "#aaaaaa";
        ctx.beginPath();
        ctx.arc(x0, y0, mr * 0.9, 0, pi * 2, false);
        ctx.fill();

        // plot dots
        ctx.fillStyle = "#ffffff";
        for (var i = 0; i < 12; i++){
            var r;              // r of dots
            if (i % 3 == 0) {
                r = mr * 0.03;
            } else {
                r = mr * 0.02;
            }
            ctx.beginPath();
            ctx.arc(x0 + mr * 0.8 * Math.sin(pi / 6.0 * i),
                    y0 - mr * 0.8 * Math.cos(pi / 6.0 * i),
                    r, 0, pi * 2, false);
            ctx.fill();
        }

        // arrow
        ctx.beginPath();
        ctx.arc(x0 + mr * 0.3 * Math.sin(hrad), y0 - mr * 0.3 * Math.cos(hrad),
                mr * 0.1, 0, pi * 2, false);
        ctx.fill();

        ctx.beginPath();
        ctx.arc(x0 + mr * 0.6 * Math.sin(mrad), y0 - mr * 0.6 * Math.cos(mrad),
                mr * 0.1, 0, pi * 2, false);
        ctx.fill();

        ctx.beginPath();
        ctx.arc(x0 + mr * 0.9 * Math.sin(srad), y0 - mr * 0.9 * Math.cos(srad),
                mr * 0.1, 0, pi * 2, false);
        ctx.fill();
        return null;
    };

    return {
        init : init
    };
})();

Clock.init();
