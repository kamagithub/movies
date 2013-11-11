import downloaders.imdb as imdb
import downloaders.filmweb as filmweb
import html

if __name__ == "__main__":
    imdb_movies = imdb.top()
    filmweb_movies = filmweb.top()
    file_name = "index.html"
    html.save(file_name, imdb_movies, filmweb_movies)
