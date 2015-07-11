$(document).ready(function () {
    $(".btn").click(function() {  
        return false; 
    });
    
    
});

var $form = $('form');

$(".btn").click(function() {  
    $.ajax({
        type: "POST",  
        url: "messageme",  
        data: $form.serialize(),
//        cache: false, 
//        dataType: 'json',
//        contentType: "application/json; charset=utf-8",
//        error:  function(error) { 
//          console.log(error);
//       }
        success: function(results) {
            $("p.msg").text(results);
            $(".msg").show();
            
            if (results === "Message sent!"){
                $('#myform')[0].reset();
            }
            console.log(results);
            console.log('finished');	
            // alert('success');   
        }  
        });  
        return false;  
}); 

function displayMessage(results){
    
}

/*TODO
 * 
 * $( "p" ).append( document.createTextNode( "Hello" ) );
 * 
function multiply(x,y) {
     return (x * y);
}
console.log(multiply(2,2));
*/
/*
//var dataString = 'company='+ enq_company + '&name='+ enq_name + '&email=' + enq_email + '&phone=' + enq_phone + '&first_choice='+ enq_first_choice + '&course_date='+ enq_course_date + '&comments='+ enq_comments + '&second_choice='+ enq_second_choice + '&other='+ enq_other;  
     // alert (dataString);return false;  
		  $.ajax({
		    type: "POST",  
		    url: "messageme",  
	//	    data: dataString,  
		    success: function(results) { 
		    console.log(results);
			//  console.log('finished');	
		   // alert('success');   
		    }  
		  });  
		  return false;  

*/
/*
var request = $.ajax({
  url: "/messageme",
  method: "POST",
  data: datastring,
  dataType: "html"
});
 
request.done(function( msg ) {
  $( "#log" ).html( msg );
});
 
request.fail(function( jqXHR, textStatus ) {
  alert( "Request failed: " + textStatus );
});
*/

/*
TODO delete or reuse in the future
$(".contact-details").hide();
$("#contact-btn").click(function() { 
	$(".contact-details").slideToggle();
	return false;
}); 

$(function() {
    $(".ch-image")
        .mouseover(function() { 
            $('img#mainimg').attr("src", "img/moa_pic2.jpg");
        })
        .mouseout(function() {
        	$('img#mainimg').attr("src", "img/GoryoAvatar.jpg");
            
        });
});
*/