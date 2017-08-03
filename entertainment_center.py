import media
import fresh_tomatoes

wind_talkers = media.Movie("Windtalkers",
                          "Native Americans'crucial roles in the WWII",
                          "https://images-na.ssl-images-amazon.com/images/M/MV5BYWU3NmIzMmQtZjE2Mi00NDlkLWI2NDMtZWZmYjUxZWRiZDZiL2ltYWdlXkEyXkFqcGdeQXVyMTQxNzMzNDI@._V1_UY268_CR1,0,182,268_AL_.jpg",
                           "https://www.youtube.com/watch?v=KOmH0_F8_XI")
matchstick_men = media.Movie("Matchstick Men",
                             "A comedy starred by Nicolas Cage",
                             "https://i.ytimg.com/vi/WgsmEhnIy7I/hqdefault.jpg?sqp=-oaymwEXCNACELwBSFryq4qpAwkIARUAAIhCGAE=&rs=AOn4CLC0IJpty4mfQ3-571CgMKmcyco4hw",
                             "https://www.youtube.com/watch?v=WgsmEhnIy7I")
army_of_one = media.Movie("Army of One",
                          "A new movie starred by Nicolas Cage",
                          "https://i.ytimg.com/vi/RYsPEl-xOv0/hqdefault.jpg?sqp=-oaymwEXCNACELwBSFryq4qpAwkIARUAAIhCGAE=&rs=AOn4CLD1zrmyhvzX4Y3f9eDZxBNjqGc86Q",
                          "https://www.youtube.com/watch?v=RYsPEl-xOv0")
inconceivable = media.Movie("Inconceivable",
                            "A 2017 movie starred by Nicolas Cage",
                            "https://i.ytimg.com/vi/MaU2hf4iGew/hqdefault.jpg?sqp=-oaymwEXCNACELwBSFryq4qpAwkIARUAAIhCGAE=&rs=AOn4CLBL3y1BOIE0arfek3HQhefzBq_Sgw",
                            "https://www.youtube.com/watch?v=MaU2hf4iGew")

movies = [wind_talkers,matchstick_men,army_of_one,inconceivable]
fresh_tomatoes.open_movies_page(movies)
