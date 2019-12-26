$( "label" ).focusin(function() {
    $( this ).find( "i" ).animate({"opacity":"0"}, 200);
  });
  
$( "label" ).focusout(function() {
    $( this ).find( "i" ).animate({"opacity":"1"}, 200);
});
  