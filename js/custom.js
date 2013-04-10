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