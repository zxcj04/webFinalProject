$( "label" ).focusin(function() {
    $( this ).find( "i" ).animate({"opacity":"0"}, 200);
  });
  
$( "label" ).focusout(function() {
    $( this ).find( "i" ).animate({"opacity":"1"}, 200);
});

$("button").click(function(){
    $(this).toggleClass("afterSub");
    $(this).css("transition", "all 0.5s");
    $(this).css("width", "70px");
    $(this).css("height", "70px");
    $(this).text("✔");
    $(this).css("left", "40%");
    $(this).css("position", "absolute");
    $(this).css("top", "-20px");
    $(this).css("border-radius", "50%");
    $(this).css("background-color", "whitesmoke");
    $(this).css("color", "#A67F78");
    $(this).css("border", "3px #A67F78 solid").delay(3000);
    //set time out
    //$(this)submit();
});

$("img").hover(function(){
    $("#tt").hide();
}, function(){
    $("#tt").show();
});

$(".inputButton").click(function(){
    $("#divvv").fadeOut("slow", function(){
        $("#regdiv").fadeIn();
    });
});

$(".closebtn").click(function(){
    $("#regdiv").fadeOut("slow", function(){
        $("#divvv").fadeIn();
    });
});
