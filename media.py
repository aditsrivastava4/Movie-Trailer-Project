"""
class Movie(title,storyline,poster_image_url,trailer_youtube_url)

class Movie will store the data of a moive which are
its Title, Storyline, Poster Image link & Trailer Link
which will create a instance of that movie.

Parameters

title:                  str
                        Title of the Movie

storyline:              str
                        Storyline of the Movie

poster_image_url:       str
                        Poster Image link of the Movie

trailer_youtube_url:    str
                        Trailer Link of the Movie

"""


class Movie():
    def __init__(
            self,
            title,
            storyline,
            poster_image_url,
            trailer_youtube_url):

        # Initializing the values
        self.title = title
        self.storyline = storyline
        self.poster_image_url = poster_image_url
        self.trailer_youtube_url = trailer_youtube_url
