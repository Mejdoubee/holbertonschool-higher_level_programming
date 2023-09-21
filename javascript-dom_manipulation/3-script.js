// JavaScript script that toggles the class of
// the header element when the user clicks on the tag id toggle_header
document.getElementById("toggle_header").addEventListener("click", function() {
	let element = document.querySelector("header");
	element.classList.toggle("red");
	element.classList.toggle("green")
});
