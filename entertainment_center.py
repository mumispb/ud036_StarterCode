import media
import fresh_tomatoes

inception = media.Movie("Inception",
                        "Dominick 'Dom' Cobb and Arthur are 'extractors', who perform corporate espionage using...",
                        "https://i.ytimg.com/vi_webp/bRywrZaOFEg/movieposter.webp",
                        "https://youtu.be/8hP9D6kZseM")

the_dark_knight = media.Movie("The Dark Knight",
                                "A gang of criminals rob a Gotham City mob bank, murdering each other for a higher share...",
                                "https://i.ytimg.com/vi_webp/e-OEZeUAMmA/movieposter.webp",
                                "https://youtu.be/_PZpmTj1Q8Q",
)

dead_poets_society = media.Movie("Dead Poets Society",
                                "In the autumn of 1959, shy Todd Anderson begins his senior year of high school at Welton Academy...",
                                "https://i.ytimg.com/vi_webp/4PRwJEMTnKE/movieposter.webp",
                                "https://youtu.be/4lj185DaZ_o",
)

movies = [inception, the_dark_knight, dead_poets_society]

fresh_tomatoes.open_movies_page(movies)