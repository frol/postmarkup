
var bbcode_timeout=null;

$(function(){
		
	
	function get_bbcode()
	{
		var bbcode = $("#bbcode_textarea").val();		
		$.post('/getbbcode', {'bbcode':bbcode}, function(html){			
			$("#bbcode").html(html);						
		});
		
	}
	
	
	$("#bbcode_textarea").keydown(function(){
				
		clearTimeout(bbcode_timeout);
		//get_bbcode()	
		bbcode_timeout = setTimeout(get_bbcode, 20);

	});
	

	get_bbcode();
	
});