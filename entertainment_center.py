import media
import fresh_tomatoes

# Instantiate movies with titles, links to posters, and links to trailers.
maldives = media.Movie(
                            "Anxiety Treatment: Maldives Dhiffushi Island Time Lapse",
                            "https://i.ytimg.com/vi/U50o92vADOg/hqdefault.jpg?sqp=-oaymwEXCNACELwBSFryq4qpAwkIARUAAIhCGAE=&rs=AOn4CLCGInbF_gv9AgWKrYY867ZWbtc_Aw",
                            "https://www.youtube.com/watch?v=U50o92vADOg"
                        )

thailand = media.Movie(
                            "Life Rhythm In Southeast Asia",
                            "https://i.ytimg.com/vi/jZStK7nfYYo/hqdefault.jpg?sqp=-oaymwEXCNACELwBSFryq4qpAwkIARUAAIhCGAE=&rs=AOn4CLAbUiooSjew67RdeBproi-iCslsUw",
                            "https://www.youtube.com/watch?v=jZStK7nfYYo"
                        )

saipan = media.Movie(
                           "Meditation: Saipan In 4K",
                           "https://i.ytimg.com/vi/FOr7NvXxQQs/hqdefault.jpg?sqp=-oaymwEXCNACELwBSFryq4qpAwkIARUAAIhCGAE=&rs=AOn4CLDD3sASab0XevNtdbOBhmlOzLQrkw",
                           "https://www.youtube.com/watch?v=FOr7NvXxQQs&t=2s"
                    )

everest = media.Movie(
                           "Flying through clouds above Mount Everest",
                           "https://i.ytimg.com/vi/P3sr9xLQpWQ/hqdefault.jpg?sqp=-oaymwEXCNACELwBSFryq4qpAwkIARUAAIhCGAE=&rs=AOn4CLB4ApPYNz208YnqmcFWrWPbXXvR2w",
                           "https://www.youtube.com/watch?v=P3sr9xLQpWQ"
                    )

# Construct an array to hold all instances of movies.
movies = [
            maldives,
            thailand,
            saipan,
            everest,
         ]

# Open the result in a browser.
fresh_tomatoes.open_movies_page(movies)
