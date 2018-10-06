# Classe de filmes para criacao das instancias
import media

# Modulo que recebe a lista de filmes e retorna um site que os exibe
import fresh_tomatoes

# Instanciamento dos filmes a serem exbidos.
# Os roteiros foram copiados da Wikipedia e resumidos para melhor visualizacao
inception = media.Movie("Inception",
                        "Dominick 'Dom' Cobb and Arthur"
                        " are 'extractors', who perform corporate...",
                        "https://i.ytimg.com/vi_webp/bRywrZaOFEg/movieposter.webp",  # noqa
                        "https://youtu.be/8hP9D6kZseM")

the_dark_knight = media.Movie("The Dark Knight",
                              "A gang of criminals rob a Gotham City mob bank,"
                              "murdering each other for a higher share...",
                              "https://i.ytimg.com/vi_webp/e-OEZeUAMmA/movieposter.webp",  # noqa
                              "https://youtu.be/_PZpmTj1Q8Q",
                              )

dead_poets_society = media.Movie("Dead Poets Society",
                                 "In the autumn of 1959, shy"
                                 "Todd Anderson begins his senior"
                                 "year of high school at Welton Academy...",
                                 "https://i.ytimg.com/vi_webp/4PRwJEMTnKE/movieposter.webp",  # noqa
                                 "https://youtu.be/4lj185DaZ_o",
                                 )

# Criacao da variavel que junta os filmes em uma lista
movies = [inception, the_dark_knight, dead_poets_society]

# Funcao para criar e abrir o site com os filmes
fresh_tomatoes.open_movies_page(movies)
