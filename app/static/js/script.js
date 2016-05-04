$(window).load(function() {
	console.log("loaded");
	$('#discover').click(function(){
		$("html, body").animate({ scrollTop: $(document).height() - $(window).height() });
	});
	
$('p.undone').on( "click", function() {
	console.log("Started");
	var strng = $(this).text();
	console.log(strng);
	$(this).remove();
	$('#dones').append('<p class="done">' + strng + '</p>' );
	});
	
$('p.done').on( "click", function() {
	console.log("Started");
	var strng = $(this).text();
	console.log(strng);
	$(this).remove();
	$('#todos').append('<p class="undone">' + strng + '</p>' );
	});
	
	
$('#add-button').on('click', function() {
	var todo = $('#todo-field').val();
	$('#todo-field').val('');
	$('#todos').append('<p class="undone">' + todo + '</p>');
	});
	
$('#clear').on('click', function() {
	$("#dones").empty();
	});
	

var cross_todo = function(e) {
	console.log("clicked");
	$.getJSON($SCRIPT_ROOT + '/_cross_todo', {
		a : $(this).attr('name')
	}, function(data) {
	console.log(data);
	console.log("class changed");
	});
return false;
};

$('p#todo').on('click', cross_todo);
});