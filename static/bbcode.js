
var bbcode_timeout=null;

function get_bbcode()
{
	var bbcode = $("#bbcode_textarea").val();		
	$.ajax({
				type: "POST",
				url:'/getbbcode',
				data:bbcode,
				dataType:"text",
				success:function(html){			
					$("#bbcode").html(html);						
				}
			});
}

$(function(){
	
	$("#bbcode_textarea").keydown(function(){			
		clearTimeout(bbcode_timeout);		
		bbcode_timeout = setTimeout(get_bbcode, 20);
	});
	
	get_bbcode();	
});