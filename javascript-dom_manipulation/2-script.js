// JavaScript script that adds the class red to the header element
// when the user clicks on the tag with id red_header
document.getElementById("red_header").addEventListener("click", function() {
    document.querySelector("header").classList.add("red");
});
