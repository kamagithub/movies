import json

def save(file_name, dict = {}):
    json_movies = json.dumps(movies)
    f = open("movies.html", "w").write(json_movies)
