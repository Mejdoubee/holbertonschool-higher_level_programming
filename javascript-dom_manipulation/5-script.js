// JavaScript script that updates the text of the header element to New Header!!!
// when the user clicks on the element with id update_header
document.getElementById("update_header").addEventListener("click", function() {
	document.querySelector("header").innerText = "New Header!!!";
});
