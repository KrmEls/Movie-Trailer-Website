import media
import fresh_tomatoes


# instants of class Movies, need 4 arguments:
# 		title, storyline, poster image url, trailer url

batman_begins = media.Movies("Batman Begins",
"Part I of Dark Knight triology by Cristopher Nolan",
"https://m.media-amazon.com/images/M/MV5BZmUwNGU2ZmItMmRiNC00MjhlLTg5YWUtODMyNzkxODYzMmZlXkEyXkFqcGdeQXVyNTIzOTk5ODM@._V1_SY1000_SX750_AL_.jpg",  # noqa
"https://www.youtube.com/watch?v=neY2xVmOfUM")

the_dark_knight = media.Movies("The Dark Knight",
"Part II of Dark Knight triology by Cristopher Nolan",
"https://m.media-amazon.com/images/M/MV5BMTMxNTMwODM0NF5BMl5BanBnXkFtZTcwODAyMTk2Mw@@._V1_SY1000_CR0,0,675,1000_AL_.jpg",  # noqa
"https://www.youtube.com/watch?v=LDG9bisJEaI")

the_dark_knight_rises = media.Movies("The Dark Knight Rises",
"Part III of the triology",
"https://m.media-amazon.com/images/M/MV5BMTk4ODQzNDY3Ml5BMl5BanBnXkFtZTcwODA0NTM4Nw@@._V1_.jpg",  # noqa
"https://www.youtube.com/watch?v=g8evyE9TuYk")

# list of the created instants

movies = [batman_begins, the_dark_knight, the_dark_knight_rises]

# call open_movies_page function from fresh_tomatoes module.

fresh_tomatoes.open_movies_page(movies)
