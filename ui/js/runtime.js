var oldValue='';
function updateCount(){
  var count=140;
  count-=$("#message").val().length;
  count-=$("#name").val().length;
  $("#alert").html("You have "+count+" characters remaining");
  if(count<0){
    $("input[type=submit]").attr('disabled','disabled');
  }
  else if($("#name").val().length>0&&!$("#name").val().startsWith('@')){
    $("input[type=submit]").attr('disabled','disabled');
    $("#alert").html("Include the @ in front of the username!");

  }
  else{
    $("input[type=submit]").removeAttr('disabled');

  }

}

$('#message').keyup(updateCount);
$('#message').keydown(updateCount);
$('#name').keyup(updateCount);
$('#name').keydown(updateCount);




//document.getElementById('message').onkeyup = test();


// $("#alert").html($("#message").value);
// $("#alert").html("lick");
