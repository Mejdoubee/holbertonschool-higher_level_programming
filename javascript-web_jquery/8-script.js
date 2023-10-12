const url = 'https://swapi-api.hbtn.io/api/films/?format=json';
$.get(url, function(data) {
	let i = 0;
	const movies = data.results;
	for(;i < movies.length; i++) {
		$('#list_movies').append('<li>' + movies[i].title + '</li>');
	}
});