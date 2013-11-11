from lxml.html import parse
from movie import *

URL = "http://www.filmweb.pl/rankings/film/world"

def top():
    movies = []
    page = parse(URL)
    html_movies = page.xpath(".//td[@class='fInfo']")

    for idx, td in enumerate(html_movies):
        title = td.find(".//img").get("title")
        image = td.find(".//img").get("src")
        rating = td.find("..//td[@class='averageRate']").text_content().strip()
        movie = Movie(idx + 1, title.encode("utf-8"), image, rating)
        movies.append(movie)

    return movies

