function start(){
    var bookdiv= document.getElementById("divvv");
    var h= screen.clientHeight/ 2;
    bookdiv.setAttribute("style","height: "+ h+ "px;");

    var smallFont= document.getElementById("fontSmall");
    smallFont.addEventListener("click", setSmallFont, false);

    var bigFont= document.getElementById("fontBig");
    bigFont.addEventListener("click", setBigFont, false);
}

function setSmallFont(){
    var bookdiv= document.getElementById("divvv");
    var s= getComputedStyle(bookdiv).getPropertyValue("font-size");
    s= s.substring(0, s.length- 2);
    s= parseInt(s);
    if(s>= 8) s-= 2;
    bookdiv.setAttribute("style","font-size: "+ s+ "px;");
}

function setBigFont(){
    var bookdiv= document.getElementById("divvv");
    var s= getComputedStyle(bookdiv).getPropertyValue("font-size");
    s= s.substring(0, s.length- 2);
    s= parseInt(s);
    if(s<= 50) s+= 2;
    bookdiv.setAttribute("style","font-size: "+ s+ "px;");
}

window.addEventListener("load", start, false);