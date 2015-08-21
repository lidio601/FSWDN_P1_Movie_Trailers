
__author__ = 'fabiocigliano'

from movie_trailers.webserver.server import open_movies_page
from movie_trailers.data.movies import movie_list

if __name__ == "__main__":
	open_movies_page(movie_list)
