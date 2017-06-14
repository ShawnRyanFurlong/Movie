import webbrowser

class Movie():
    ''' This class holds documentation on  three movies. These three mmovies contin information such as the title, storyline, poster image, and clip.'''
    def __init__(self, movie_title, movie_storyline, poster_image, trailer_youtube):
        '''This def is taking 4 arguments'''
        self.title = movie_title
        ''' provides title ofmovie'''
        self.storyline = movie_storyline
        '''provides storyline of movie'''
        self.poster_image_url = poster_image
        '''provides poster image of movie.'''
        self.trailer_youtube_url = trailer_youtube
        '''provides a youtube video for selected movie'''
    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
