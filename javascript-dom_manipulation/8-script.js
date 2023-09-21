document.addEventListener('DOMContentLoaded', function() {
	fetch('https://hellosalut.stefanbohacek.dev/?lang=fr')
	  .then(response => response.json())
	  .then(data => {
	  	document.getElementById('hello').innerText = data.hello;
	  })
	  .catch(console.error);
});
