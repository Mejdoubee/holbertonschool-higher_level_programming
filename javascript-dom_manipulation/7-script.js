fetch('https://swapi-api.hbtn.io/api/films/?format=json')
  .then(response => response.json())
  .then(data => {
    const movieList = document.getElementById("list_movies");
    data.results.forEach(movie => {
      let listItem = document.createElement('li');
      listItem.innerText = movie.title;
      movieList.appendChild(listItem)
    });
  })
  .catch(console.error);
