class Movie():
    """Classe que representa filmes

    Atributos:
        title: uma string do titulo do filme
        storyline: uma string do roteiro do filme
        poster_image_url: uma string com a url para a imagem do poster
        trailer_youtube_url: string com a url do youtube para o trailer
    """

    def __init__(self, movie_title, movie_storyline, poster_image,
                 trailer_youtube):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube
