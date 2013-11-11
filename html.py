from django.template import Template, Context
from django.conf import settings
settings.configure()

def save(file_name, imdb_movies, filmweb_movies):
    template = open("template.html").read()
    t = Template(template)
    c = Context({"imdb_movies": imdb_movies, "filmweb_movies": filmweb_movies})
    html = t.render(c)
    f = open(file_name, "w")
    f.write(html.encode("utf-8"))
    f.close()
