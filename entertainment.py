import media
import fresh_tomatoes

dark_knight_rises = media.Movie("Dark  Knight Rises",
                        "The last story in the Batman trilogy.",
                        "http://vignette2.wikia.nocookie.net/batman/images/9/91/TheDarkKnightRises_Poster.jpg/revision/latest?cb=20111211002330",
                        "https://www.youtube.com/watch?v=GokKUqLcvD8")

#print(dark_knight_rises.storyline)
#dark_knight_rises.show_trailer()

batman_begins = media.Movie("Batman Begins",
                    "First Batman in newest trilogy",
                    "http://vignette4.wikia.nocookie.net/batman/images/1/1e/Batman_Begins_poster6.jpg/revision/latest?cb=20111218145155",
                    "https://www.youtube.com/watch?v=vak9ZLfhGnQ")
#print(batman_begins.storyline)
#batman_begins.show_trailer()

dark_knight = media.Movie("Dark Knight",
                            "Batman Trilogy",
                            "http://host.trivialbeing.org/up/tdk-apr28-new-poster-posterexclusivoomelete6.jpg",
                            "https://www.youtube.com/watch?v=EXeTwQWrcwY")

#print(dark_knight.storyline)

movies = [batman_begins, dark_knight, dark_knight_rises]
fresh_tomatoes.open_movies_page(movies)
