$(document).ready(function(){
	console.log("main.js loaded!")
	$( function() {
		$("#sortable").sortable();
		$("#sortable").disableSelection();
	} );

	$('#update_list').on('click', function(event){
		event.preventDefault();
		console.log("clicked 'Update List Order' button!");
		var sorted = $("#sortable").sortable("toArray");
		console.log(sorted);

	});

}); //end doc