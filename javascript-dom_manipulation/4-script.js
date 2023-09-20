document.getElementById("add_item").addEventListener("click", function() {
	let Item = document.createElement("li");
	Item.innerText = "Item";
	document.querySelector(".my_list").appendChild(Item);
});
