from lxml.html import parse
from itertools import izip
from django.template import Template, Context
from django.conf import settings
settings.configure()

class Movie:

    def __init__(self, pos, title, image = "", rating = ""):
        self.pos = pos
        self.title = title
        self.image = image
        self.rating = rating

def group(l, n = 2):
    return izip(*[iter(l)]*n)

def filmweb():
    movies = []
    page = parse("http://www.filmweb.pl/rankings/film/world")
    html_movies = page.xpath(".//td[@class='fInfo']")

    for idx, td in enumerate(html_movies):
        title = td.find(".//img").get("title")
        image = td.find(".//img").get("src")
        rating = td.find("..//td[@class='averageRate']").text_content().strip()
        movie = Movie(idx + 1, title.encode("utf-8"), image, rating)
        movies.append(movie)

    return movies

def imdb():
    movies = []
    page = parse("http://www.imdb.com/chart/top")
    html_movies = page.xpath(".//table//td[@class='posterColumn' or @class='titleColumn' or @class='ratingColumn']")

    for idx, (x, y, z, yr) in enumerate(group(html_movies, 4)):
        title  = y.find('a').text_content()
        image  = x.find('.//img').get('src'),
        rating = z.find('.//strong').text_content()
        movie = Movie(idx + 1, title.encode("utf-8"), image[0], rating)
        movies.append(movie)

    return movies


def save(file_name, imdb_movies, filmweb_movies):
    template = open("template.html").read()
    t = Template(template)
    c = Context({"imdb_movies": imdb_movies, "filmweb_movies": filmweb_movies})
    html = t.render(c)
    f = open(file_name, "w")
    f.write(html.encode("utf-8"))
    f.close()


if __name__ == "__main__":
    save("index.html", imdb(), filmweb())

