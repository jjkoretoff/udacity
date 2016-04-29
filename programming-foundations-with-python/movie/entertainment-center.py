# tell code to use contents of media.py file
# best pracitce to keep class in one file and call class in another
# must save front-end script in the same folder
import fresh_tomatoes
import media

# media.Movie called the __init__ function that created a new instance called
# toy_story - toy_story is an instance
toy_story = media.Movie("Toy Story",
                        "A story of a boy and his toys that come to life",
                        "https://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
                        "https://www.youtube.com/watch?v=vwyZH85NQC4")
#print(toy_story.storyline)
avatar = media.Movie("Avatar",
                     "A marine on an alien planet",
                     "http://upload.wikimedia.org/wikipedia/id/b/b0/Avatar-Teaser-Poster.jpg",
                     "https://www.youtube.com/watch?v=5PSNL1qE6VY")
#print(avatar.storyline)
#avatar.show_trailer()
the_great_gatsby = media.Movie("The Great Gatsby",
                               "An ageless story of love and deceit",
                               "https://upload.wikimedia.org/wikipedia/en/2/26/TheGreatGatsby2012Poster.jpg",
                               "https://www.youtube.com/watch?v=rARN6agiW7o")
#print(the_great_gatsby.storyline)
#the_great_gatsby.show_trailer()
school_of_rock = media.Movie("School of Rock",
                             "Using rock music to learn",
                             "http://upload.wikimedia.org/wikipedia/en/1/11/School_of_Rock_Poster.jpg",
                             "https://www.youtube.com/watch?v=3PsUJFEBC74")

ratatouille = media.Movie("Ratatouille",
                         "A rat is a chef in Paris",
                         "http://upload.wikimedia.org/wikipedia/en/5/50/RatatouillePoster.jpg",
                         "https://www.youtube.com/watch?v=c3sBBRxDAqk")

hunger_games = media.Movie("Hunger Games",
                           "A really real reality show",
                           "http://upload.wikimedia.org/wikipedia/en/4/42/HungerGamesPoster.jpg",
                           "https://www.youtube.com/watch?v=PbA63a7H0bo")

movies = [toy_story, avatar, the_great_gatsby, school_of_rock, ratatouille, hunger_games]
fresh_tomatoes.open_movies_page(movies)


