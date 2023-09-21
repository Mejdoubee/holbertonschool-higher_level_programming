// JavaScript script that fetches from https://hellosalut.stefanbohacek.dev/?lang=fr 
// and displays the value of hello from that fetch in the HTML element with id hello.
document.addEventListener('DOMContentLoaded', function() {
	fetch('https://hellosalut.stefanbohacek.dev/?lang=fr')
	  .then(response => response.json())
	  .then(data => {
	  	document.getElementById('hello').innerText = data.hello;
	  })
	  .catch(console.error);
});
