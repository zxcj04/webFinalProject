var colorShow= 0;
function start(){
    var bookdiv= document.getElementById("divvv");
    var h= screen.clientHeight/ 2;
    bookdiv.setAttribute("style","height: "+ h+ "px;");

    var smallFont= document.getElementById("fontSmall");
    smallFont.addEventListener("click", setSmallFont, false);

    var bigFont= document.getElementById("fontBig");
    bigFont.addEventListener("click", setBigFont, false);
}

$("#menu").click(function(){
    $("#firstmenu").fadeOut("slow", function(){
        $("#secondmenu").slideDown("slow");
    });
});

$("#closebtn").click(function(){
    $(".adjust").removeClass("selected");
    if(colorShow== 1){
        $("#colorPart").hide("fast");
        colorShow= 0;
    }
    $("#firstmenu").slideDown("slow");
    $("#secondmenu").slideUp("slow");
});

$(".adjust").click(function(){
    $(this).toggleClass("selected");
});

$("#changeColor").click(function(){
    if(colorShow== 0){
        $("#colorPart").show("slow");
        colorShow= 1;
    }
    else{
        $("#colorPart").hide("slow");
        colorShow= 0;
    }
});

$("#closeColor").click(function(){
    $("#colorPart").hide("slow");
    colorShow= 0;
    $("#changeColor").removeClass("selected");
});

$("#wholeScreen").click(function(){
    if(colorShow== 1){
        $("#colorPart").hide("fast");
        colorShow= 0;
        $("#changeColor").removeClass("selected");
    }
    $(".elsePart").hide();
    $("#firstmenu").show();
    $("#secondmenu").hide();
    $("#smallScreen").show();
    $("#divvv").toggleClass("whole");
});

$("#smallScreen").click(function(){
    $(this).hide();
    $(".elsePart").show();
    $("#firstmenu").show();
    $("#divvv").removeClass("whole");
    $(".adjust").removeClass("selected");
});

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


$(".eyeType").click(function(){
    var colorStr= $(this).css("color");
    var bgcolorStr= $(this).css("background-color");
    $("#divvv").css("color", colorStr);
    $("#divvv").css("background-color", bgcolorStr);
});
$(".nightType").click(function(){
    var colorStr= $(this).css("color");
    var bgcolorStr= $(this).css("background-color");
    $("#divvv").css("color", colorStr);
    $("#divvv").css("background-color", bgcolorStr);
});
$(".whiteblack").click(function(){
    var colorStr= $(this).css("color");
    var bgcolorStr= $(this).css("background-color");
    $("#divvv").css("color", colorStr);
    $("#divvv").css("background-color", bgcolorStr);
});
$(".whitegreen").click(function(){
    var colorStr= $(this).css("color");
    var bgcolorStr= $(this).css("background-color");
    $("#divvv").css("color", colorStr);
    $("#divvv").css("background-color", bgcolorStr);
});
$(".whiteindigo").click(function(){
    var colorStr= $(this).css("color");
    var bgcolorStr= $(this).css("background-color");
    $("#divvv").css("color", colorStr);
    $("#divvv").css("background-color", bgcolorStr);
});
$(".whiteblue").click(function(){
    var colorStr= $(this).css("color");
    var bgcolorStr= $(this).css("background-color");
    $("#divvv").css("color", colorStr);
    $("#divvv").css("background-color", bgcolorStr);
});
$(".whitepurple").click(function(){
    var colorStr= $(this).css("color");
    var bgcolorStr= $(this).css("background-color");
    $("#divvv").css("color", colorStr);
    $("#divvv").css("background-color", bgcolorStr);
});
$(".whitepink").click(function(){
    var colorStr= $(this).css("color");
    var bgcolorStr= $(this).css("background-color");
    $("#divvv").css("color", colorStr);
    $("#divvv").css("background-color", bgcolorStr);
});
$(".whitered").click(function(){
    var colorStr= $(this).css("color");
    var bgcolorStr= $(this).css("background-color");
    $("#divvv").css("color", colorStr);
    $("#divvv").css("background-color", bgcolorStr);
});
$(".whiteorange").click(function(){
    var colorStr= $(this).css("color");
    var bgcolorStr= $(this).css("background-color");
    $("#divvv").css("color", colorStr);
    $("#divvv").css("background-color", bgcolorStr);
});
$(".blackwhite").click(function(){
    var colorStr= $(this).css("color");
    var bgcolorStr= $(this).css("background-color");
    $("#divvv").css("color", colorStr);
    $("#divvv").css("background-color", bgcolorStr);
});
$(".blackgreen").click(function(){
    var colorStr= $(this).css("color");
    var bgcolorStr= $(this).css("background-color");
    $("#divvv").css("color", colorStr);
    $("#divvv").css("background-color", bgcolorStr);
});
$(".blackindigo").click(function(){
    var colorStr= $(this).css("color");
    var bgcolorStr= $(this).css("background-color");
    $("#divvv").css("color", colorStr);
    $("#divvv").css("background-color", bgcolorStr);
});
$(".blackblue").click(function(){
    var colorStr= $(this).css("color");
    var bgcolorStr= $(this).css("background-color");
    $("#divvv").css("color", colorStr);
    $("#divvv").css("background-color", bgcolorStr);
});
$(".blackpurple").click(function(){
    var colorStr= $(this).css("color");
    var bgcolorStr= $(this).css("background-color");
    $("#divvv").css("color", colorStr);
    $("#divvv").css("background-color", bgcolorStr);
});
$(".blackpink").click(function(){
    var colorStr= $(this).css("color");
    var bgcolorStr= $(this).css("background-color");
    $("#divvv").css("color", colorStr);
    $("#divvv").css("background-color", bgcolorStr);
});
$(".blackred").click(function(){
    var colorStr= $(this).css("color");
    var bgcolorStr= $(this).css("background-color");
    $("#divvv").css("color", colorStr);
    $("#divvv").css("background-color", bgcolorStr);
});
$(".blackorange").click(function(){
    var colorStr= $(this).css("color");
    var bgcolorStr= $(this).css("background-color");
    $("#divvv").css("color", colorStr);
    $("#divvv").css("background-color", bgcolorStr);
});
$(".whitegray").click(function(){
    var colorStr= $(this).css("color");
    var bgcolorStr= $(this).css("background-color");
    $("#divvv").css("color", colorStr);
    $("#divvv").css("background-color", bgcolorStr);
});
$(".greenblack").click(function(){
    var colorStr= $(this).css("color");
    var bgcolorStr= $(this).css("background-color");
    $("#divvv").css("color", colorStr);
    $("#divvv").css("background-color", bgcolorStr);
});
$(".indigoblack").click(function(){
    var colorStr= $(this).css("color");
    var bgcolorStr= $(this).css("background-color");
    $("#divvv").css("color", colorStr);
    $("#divvv").css("background-color", bgcolorStr);
});
$(".blueblack").click(function(){
    var colorStr= $(this).css("color");
    var bgcolorStr= $(this).css("background-color");
    $("#divvv").css("color", colorStr);
    $("#divvv").css("background-color", bgcolorStr);
});
$(".purpleblack").click(function(){
    var colorStr= $(this).css("color");
    var bgcolorStr= $(this).css("background-color");
    $("#divvv").css("color", colorStr);
    $("#divvv").css("background-color", bgcolorStr);
});
$(".pinkblack").click(function(){
    var colorStr= $(this).css("color");
    var bgcolorStr= $(this).css("background-color");
    $("#divvv").css("color", colorStr);
    $("#divvv").css("background-color", bgcolorStr);
});
$(".redblack").click(function(){
    var colorStr= $(this).css("color");
    var bgcolorStr= $(this).css("background-color");
    $("#divvv").css("color", colorStr);
    $("#divvv").css("background-color", bgcolorStr);
});
$(".orangeblack").click(function(){
    var colorStr= $(this).css("color");
    var bgcolorStr= $(this).css("background-color");
    $("#divvv").css("color", colorStr);
    $("#divvv").css("background-color", bgcolorStr);
});
$(".graywhite").click(function(){
    var colorStr= $(this).css("color");
    var bgcolorStr= $(this).css("background-color");
    $("#divvv").css("color", colorStr);
    $("#divvv").css("background-color", bgcolorStr);
});
$(".greenwhite").click(function(){
    var colorStr= $(this).css("color");
    var bgcolorStr= $(this).css("background-color");
    $("#divvv").css("color", colorStr);
    $("#divvv").css("background-color", bgcolorStr);
});
$(".indigowhite").click(function(){
    var colorStr= $(this).css("color");
    var bgcolorStr= $(this).css("background-color");
    $("#divvv").css("color", colorStr);
    $("#divvv").css("background-color", bgcolorStr);
});
$(".bluewhite").click(function(){
    var colorStr= $(this).css("color");
    var bgcolorStr= $(this).css("background-color");
    $("#divvv").css("color", colorStr);
    $("#divvv").css("background-color", bgcolorStr);
});
$(".purplewhite").click(function(){
    var colorStr= $(this).css("color");
    var bgcolorStr= $(this).css("background-color");
    $("#divvv").css("color", colorStr);
    $("#divvv").css("background-color", bgcolorStr);
});
$(".pinkwhite").click(function(){
    var colorStr= $(this).css("color");
    var bgcolorStr= $(this).css("background-color");
    $("#divvv").css("color", colorStr);
    $("#divvv").css("background-color", bgcolorStr);
});
$(".redwhite").click(function(){
    var colorStr= $(this).css("color");
    var bgcolorStr= $(this).css("background-color");
    $("#divvv").css("color", colorStr);
    $("#divvv").css("background-color", bgcolorStr);
});
$(".orangewhite").click(function(){
    var colorStr= $(this).css("color");
    var bgcolorStr= $(this).css("background-color");
    $("#divvv").css("color", colorStr);
    $("#divvv").css("background-color", bgcolorStr);
});
$(".bluegray").click(function(){
    var colorStr= $(this).css("color");
    var bgcolorStr= $(this).css("background-color");
    $("#divvv").css("color", colorStr);
    $("#divvv").css("background-color", bgcolorStr);
});
$(".preetygreen").click(function(){
    var colorStr= $(this).css("color");
    var bgcolorStr= $(this).css("background-color");
    $("#divvv").css("color", colorStr);
    $("#divvv").css("background-color", bgcolorStr);
});
$(".justblue").click(function(){
    var colorStr= $(this).css("color");
    var bgcolorStr= $(this).css("background-color");
    $("#divvv").css("color", colorStr);
    $("#divvv").css("background-color", bgcolorStr);
});
$(".preetyblue").click(function(){
    var colorStr= $(this).css("color");
    var bgcolorStr= $(this).css("background-color");
    $("#divvv").css("color", colorStr);
    $("#divvv").css("background-color", bgcolorStr);
});
$(".preetypurple").click(function(){
    var colorStr= $(this).css("color");
    var bgcolorStr= $(this).css("background-color");
    $("#divvv").css("color", colorStr);
    $("#divvv").css("background-color", bgcolorStr);
});
$(".preetypink").click(function(){
    var colorStr= $(this).css("color");
    var bgcolorStr= $(this).css("background-color");
    $("#divvv").css("color", colorStr);
    $("#divvv").css("background-color", bgcolorStr);
});
$(".preetybrown").click(function(){
    var colorStr= $(this).css("color");
    var bgcolorStr= $(this).css("background-color");
    $("#divvv").css("color", colorStr);
    $("#divvv").css("background-color", bgcolorStr);
});
$(".preetyorange").click(function(){
    var colorStr= $(this).css("color");
    var bgcolorStr= $(this).css("background-color");
    $("#divvv").css("color", colorStr);
    $("#divvv").css("background-color", bgcolorStr);
});
$(".preetydarkblue").click(function(){
    var colorStr= $(this).css("color");
    var bgcolorStr= $(this).css("background-color");
    $("#divvv").css("color", colorStr);
    $("#divvv").css("background-color", bgcolorStr);
});
$(".preetyindigo").click(function(){
    var colorStr= $(this).css("color");
    var bgcolorStr= $(this).css("background-color");
    $("#divvv").css("color", colorStr);
    $("#divvv").css("background-color", bgcolorStr);
});
$(".darkgreenwhite").click(function(){
    var colorStr= $(this).css("color");
    var bgcolorStr= $(this).css("background-color");
    $("#divvv").css("color", colorStr);
    $("#divvv").css("background-color", bgcolorStr);
});
$(".pinkpurple").click(function(){
    var colorStr= $(this).css("color");
    var bgcolorStr= $(this).css("background-color");
    $("#divvv").css("color", colorStr);
    $("#divvv").css("background-color", bgcolorStr);
});
$(".redyellow").click(function(){
    var colorStr= $(this).css("color");
    var bgcolorStr= $(this).css("background-color");
    $("#divvv").css("color", colorStr);
    $("#divvv").css("background-color", bgcolorStr);
});
$(".orangetwoblack").click(function(){
    var colorStr= $(this).css("color");
    var bgcolorStr= $(this).css("background-color");
    $("#divvv").css("color", colorStr);
    $("#divvv").css("background-color", bgcolorStr);
});
$(".webcolor").click(function(){
    var colorStr= $(this).css("color");
    var bgcolorStr= $(this).css("background-color");
    $("#divvv").css("color", colorStr);
    $("#divvv").css("background-color", bgcolorStr);
});
$(".origin").click(function(){
    var colorStr= $(this).css("color");
    var bgcolorStr= $(this).css("background-color");
    $("#divvv").css("color", colorStr);
    $("#divvv").css("background-color", bgcolorStr);
});
$(".yellowindigo").click(function(){
    var colorStr= $(this).css("color");
    var bgcolorStr= $(this).css("background-color");
    $("#divvv").css("color", colorStr);
    $("#divvv").css("background-color", bgcolorStr);
});
$(".coral").click(function(){
    var colorStr= $(this).css("color");
    var bgcolorStr= $(this).css("background-color");
    $("#divvv").css("color", colorStr);
    $("#divvv").css("background-color", bgcolorStr);
});
$(".graygray").click(function(){
    var colorStr= $(this).css("color");
    var bgcolorStr= $(this).css("background-color");
    $("#divvv").css("color", colorStr);
    $("#divvv").css("background-color", bgcolorStr);
});
$(".bone").click(function(){
    var colorStr= $(this).css("color");
    var bgcolorStr= $(this).css("background-color");
    $("#divvv").css("color", colorStr);
    $("#divvv").css("background-color", bgcolorStr);
});
$(".bakery").click(function(){
    var colorStr= $(this).css("color");
    var bgcolorStr= $(this).css("background-color");
    $("#divvv").css("color", colorStr);
    $("#divvv").css("background-color", bgcolorStr);
});