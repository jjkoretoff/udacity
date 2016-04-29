# designing a class for movies
# inside class - title, storyline, poster_image, youtube_trailer
# execute - show_trailer

import webbrowser

# google stle guide suggests uppercase for class, Movie
# https://google.github.io/styleguide/pyguide.html
class Movie():
    def __init__(self, movie_title, movie_storyline, poster_image, trailer_youtube):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
