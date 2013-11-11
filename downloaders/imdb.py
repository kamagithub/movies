from lxml.html import parse
from utils import *
from movie import *

def top():
    page = parse("http://www.imdb.com/chart/top")
    imdb_movies = page.xpath(".//table//td[@class='posterColumn' or @class='titleColumn' or @class='ratingColumn']")

    movies = []
    for idx, (x, y, z, yr) in enumerate(group(imdb_movies, 4)):
        title  = y.find('a').text_content()
        image  = x.find('.//img').get('src'),
        rating = z.find('.//strong').text_content()
        movie = Movie(idx + 1, title.encode("utf-8"), image[0], rating)
        movies.append(movie)

    return movies
