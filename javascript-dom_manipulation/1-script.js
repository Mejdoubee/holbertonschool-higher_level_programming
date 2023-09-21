// JavaScript script that updates the text color of the header element
// to red (#FF0000) when the user clicks on the tag with id red_header
document.getElementById("red_header").addEventListener("click", function() {
	document.querySelector("header").style.color = "#FF0000";
});
