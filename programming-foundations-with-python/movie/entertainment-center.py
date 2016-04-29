# tell code to use contents of media.py file
# best pracitce to keep class in one file and call class in another

import media

# media.Movie called the __init__ function that created a new instance called
# toy_story - toy_story is an instance
toy_story = media.Movie("Toy Story",
                        "A story of a boy and his toys that come to life",
                        "https://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
                        "https://www.youtube.com/watch?v=vwyZH85NQC4")
print(toy_story.storyline)
