const url = 'https://hellosalut.stefanbohacek.dev/?lang=fr'
$.get(url, function(data) {
	const inner = data.hello;
	$('#hello').text(inner);
});