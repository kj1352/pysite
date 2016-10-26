import fresh_movie
import media

avatar = media.Movie("Avatar", "A marine on an alien planet", "https://upload.wikimedia.org/wikipedia/en/b/b0/Avatar-Teaser-Poster.jpg", "https://www.youtube.com/watch?v=5PSNL1qE6VY")

deadpool = media.Movie("Deadpool", "American Superhero comedy film", "https://upload.wikimedia.org/wikipedia/en/4/46/Deadpool_poster.jpg", "https://www.youtube.com/watch?v=Xithigfg7dA")

inception = media.Movie("Inception", "A science fiction heist thriller film", "https://upload.wikimedia.org/wikipedia/en/2/2e/Inception_%282010%29_theatrical_poster.jpg", "https://www.youtube.com/watch?v=YoHD9XEInc0")

inferno = media.Movie("Inferno", "An american mystery thriller film", "https://upload.wikimedia.org/wikipedia/en/6/66/Inferno_%282016_film%29.png", "https://www.youtube.com/watch?v=RH2BD49sEZI")

interstellar = media.Movie("Interstellar", "A british american science fiction movie", "https://upload.wikimedia.org/wikipedia/en/b/bc/Interstellar_film_poster.jpg", "https://www.youtube.com/watch?v=Lm8p5rlrSkY" )

martian = media.Movie("Martian", "A survival story of an astronut", "https://upload.wikimedia.org/wikipedia/en/c/cd/The_Martian_film_poster.jpg", "https://www.youtube.com/watch?v=ej3ioOneTy8")

the_da_vinci_code = media.Movie("The Da Vinci Code", "A mystery thriller film", "https://upload.wikimedia.org/wikipedia/en/e/e9/The_da_vinci_code_final.jpg", "https://www.youtube.com/watch?v=QfvmkH59-zA")

the_pursuit_of_happyness = media.Movie("The Pursuit of Happyness", "A biographical drama film based on entrepreneur", "https://upload.wikimedia.org/wikipedia/en/8/81/Poster-pursuithappyness.jpg", "https://www.youtube.com/watch?v=89Kq8SDyvfg")

toy_story = media.Movie("Toy Story 4", "A Story of a boy and his toys that come to life", "https://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg", "https://www.youtube.com/watch?v=Bj4gS1JQzjk" )

movies = [avatar, deadpool, inception, inferno, interstellar, martian, the_da_vinci_code, the_pursuit_of_happyness, toy_story]
fresh_movie.open_movies_page(movies)

