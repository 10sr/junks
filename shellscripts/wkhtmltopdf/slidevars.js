function getVars() {
    var vars = {};
    var queries = document.location.search.substring(1).split('&');
    for (var q in queries) {
        var z = queries[q].split('=', 2);
        vars[z[0]] = decodeURIComponent(z[1]);
    }
    vars["__all"] = document.location.search.substring(1);

    return vars;
}

function setHeader() {
    var vars = getVars();

    var elems = document.getElementsByClassName("section");
    for (var j = 0; j<elems.length; j++) {
        elems[j].textContent = vars["section"];
    }
}

function setVars() {
    var vars = getVars();

    var names = [
        'frompage',
        'topage',
        'page',
        'webpage',
        'section',
        'subsection',
        'subsubsection',
        'title',
        'doctitle'
    ];

    for (var e in names) {
        var elems = document.getElementsByClassName(names[e]);
        for (var j = 0; j<elems.length; j++) {
            elems[j].textContent = vars[names[e]];
        }
    }
}
