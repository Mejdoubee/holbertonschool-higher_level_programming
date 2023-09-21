// JavaScript script that adds a li element to a list
// when the user clicks on the element with id add_item
document.getElementById("add_item").addEventListener("click", function() {
	let Item = document.createElement("li");
	Item.innerText = "Item";
	document.querySelector(".my_list").appendChild(Item);
});
