import media
import fresh_tomatoes

#Instantiate movies with titles, links to posters, and links to trailers.
wind_talkers = media.Movie(
                            "Windtalkers",
                            ('https://images-na.ssl-images-amazon.com/ima'
                             'ges/M/MV5BYWU3NmIzMmQtZjE2Mi00NDlkLWI2NDMtZW'
                             'ZmYjUxZWRiZDZiL2ltYWdlXkEyXkFqcGdeQXVyMTQxNzM'
                             'zNDI@._V1_UY268_CR1,0,182,268_AL_.jpg'),
                            "https://www.youtube.com/watch?v=KOmH0_F8_XI")

matchstick_men = media.Movie(
                              "Matchstick Men",
                              ('https://images-na.ssl-images-amazon.com/image'
                               's/M/MV5BMjA3NjMyNjIyMF5BMl5BanBnXkFtZTYwOTgzM'
                               'DI3._V1_UX182_CR0,0,182,268_AL_.jpg'),
                              "https://www.youtube.com/watch?v=WgsmEhnIy7I")

army_of_one = media.Movie(
                            "Army of One",
                            ('https://images-na.ssl-images-amazon.com/image'
                             's/M/MV5BZWY4NzQwNWUtYzVkYS00YjIwLWJkYmEtYmU4Mm'
                             'E5ZjJmMjEzXkEyXkFqcGdeQXVyNTU2NDMyOTM@._V1_UY26'
                             '8_CR4,0,182,268_AL_.jpg'),
                            "https://www.youtube.com/watch?v=RYsPEl-xOv0")

inconceivable = media.Movie(
                             "Inconceivable",
                               ('https://images-na.ssl-images-amazon.com/image'
                                's/M/MV5BNWM0ODdkNTYtNjAwNS00OTE1LTlhMWMtOGE5OT'
                                'hjM2MzMzAwXkEyXkFqcGdeQXVyMjM4NTM5NDY@._V1_UX18'
                                '2_CR0,0,182,268_AL_.jpg'),
                             "https://www.youtube.com/watch?v=MaU2hf4iGew")

#Construct an array to hold all instances of movies.
movies = [
            wind_talkers, 
            matchstick_men,
            army_of_one, 
            inconceivable
         ]

#Open the result in a browser.
fresh_tomatoes.open_movies_page(movies)
