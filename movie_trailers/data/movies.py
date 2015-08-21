__author__ = 'fabiocigliano'

from movie_trailers.model.movie_trailer import MovieTrailer

movie_list = list()

"""
List my favourite movie list
"""

movie_list.append(MovieTrailer("Inside Out", "http://ia.media-imdb.com/images/M/MV5BOTgxMDQwMDk0OF5BMl5BanBnXkFtZTgwNjU5OTg2NDE@._V1_SX214_AL_.jpg", "https://www.youtube.com/watch?v=pI1PY1dxdYs"))
movie_list.append(MovieTrailer("Unbreakable", "http://ia.media-imdb.com/images/M/MV5BMTQ5MzkyMjk2Nl5BMl5BanBnXkFtZTYwOTAxOTE3._V1_SX214_AL_.jpg", "https://www.youtube.com/watch?v=R_f1uCWKZQs"))
movie_list.append(MovieTrailer("Hot Shots", "http://ia.media-imdb.com/images/M/MV5BMTQ4Mjg2NjY4NV5BMl5BanBnXkFtZTcwMjgwMDU1MQ@@._V1_SY317_CR3,0,214,317_AL_.jpg", "https://www.youtube.com/watch?v=ih78dz2XyLc"))
movie_list.append(MovieTrailer("Home", "http://ia.media-imdb.com/images/M/MV5BMTU0MzU4ODI3Ml5BMl5BanBnXkFtZTgwMzQzODk5NDE@._V1_SX214_AL_.jpg", "https://www.youtube.com/watch?v=MyqZf8LiWvM"))

if __name__ == "__main__":
	print movie_list
