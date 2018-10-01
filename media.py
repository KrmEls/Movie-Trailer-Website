import webbrowser


class Movies():

    ''' contains all arguments of the movies'''
    def __init__(self, movie_title, movie_storyline, movie_poster, trailer_url):  # noqa
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = movie_poster
        self.trailer_youtube_url = trailer_url
