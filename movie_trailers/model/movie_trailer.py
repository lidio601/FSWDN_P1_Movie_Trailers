__author__ = 'fabiocigliano'

import re

class MovieTrailer:
	"""
	Movie Trailer class specification:
	your favorite movies, including
		movie title,
		box art URL (or poster URL)
		and a YouTube link to the movie trailer.
	"""

	title = ""
	poster_image_url = ""
	trailer_youtube_url = ""

	def __init__(self, titolo, thumb, trailer):
		self.title       = titolo
		self.poster_image_url   = thumb
		self.trailer_youtube_url = trailer

	def valid(self):
		"""
		Check if the data contained in this object
		correctly represent a MovieTrailer
		@return BOOL
		"""
		try:
			assert self.title
			assert self._valid_url(self.poster_image_url)
			assert self._valid_url(self.trailer_youtube_url)
		except AssertionError:
			return False
		else:
			return True

	def _valid_url(self, url):
		"""
		Method to check the validity of an url
		@param url: url to check
		@return BOOL
		"""

		# print url
		if not url:
			return False
		if not isinstance(url, basestring):
			return False
		# @see http://stackoverflow.com/questions/7160737/python-how-to-validate-a-url-in-python-malformed-or-not
		regex = re.compile(
	        r'^(?:http|ftp)s?://' # http:// or https://
	        r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?)|' #domain...
	        r'localhost|' #localhost...
	        r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})' # ...or ip
	        r'(?::\d+)?' # optional port
	        r'(?:/?|[/?]\S+)$', re.IGNORECASE)
		return regex.match(url)

	def __str__(self):
		return "MovieTrailer(%s, thumb=%s, trailer=%s)" % (self.title, self._valid_url(self.poster_image_url), self._valid_url(self.trailer_youtube_url))

	@staticmethod
	def test():
		"""
		Testing functionalities of the main class methods
		"""

		movie = MovieTrailer()

		# test the internal-use method _valid_url()
		assert not movie._valid_url(None)
		assert not movie._valid_url(15)
		assert not movie._valid_url('')
		assert not movie._valid_url('httpo')
		assert not movie._valid_url('http://www')
		assert     movie._valid_url('http://www.youtube.com/abcdef')

		# test the toString() method
		print movie


if __name__ == "__main__":
	MovieTrailer.test()
