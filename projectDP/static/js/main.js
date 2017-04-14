$(document).ready(function(){
	console.log("main.js loaded!")
	$( function() {
		$("#sortable1").sortable();
		$("#sortable1").disableSelection();
	} );

	$( function() {
		$( "#sortable1, #sortable2" ).sortable({
			connectWith: ".connectedSortable"
		}).disableSelection();
	} );

	$('#update_list').on('click', function(event){
		event.preventDefault();
		console.log("clicked 'Update List Order' button!");
		var wip = $("#sortable1").sortable("toArray");
		var future = $("#sortable2").sortable("toArray");
		console.log("wip:",wip);
		console.log("future:",future);
		kwargs = {
			"wip": wip,
			"future": future,
			"csrfmiddlewaretoken": $('input[name="csrfmiddlewaretoken"]').val(),
		}
	
		$.ajax({
			url: "",
			data: kwargs,
			type: "POST",
			success: function(response){
				console.log("AJAX success!");
			},
			error: function(){
				console.log("Error in AJAX")
			}
		}) //end ajax
	

	}); //end update_list button

}); //end doc