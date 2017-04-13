$(document).ready(function(){
	console.log("main.js loaded!")
	$( function() {
		$( "#sortable" ).sortable();
		$( "#sortable" ).disableSelection();
	} );

}); //end doc