from urllib import request
from media import Movie
import fresh_tomatoes
import yaml


def get_data():
    # To get popular movie data and return a list of Movie instance
    url = 'https://api.themoviedb.org/3/movie/popular?api_key=1f4817acb34ea3063d54e2f4c641c5cb&language=en-US&page=1'
    response = request.urlopen(url)
    # opening the url and getting the data
    response_read = str(response.read())

    # Removing unwanted characters from response_read
    response_read = response_read.replace('b\'', '')
    response_read = response_read.replace('\'', '')
    response_read = response_read.replace('\\\\\"', '')
    response_read = response_read.replace('\\', '')

    # Converting String to Python Dictionary
    movie_dict = yaml.load(response_read)['results']

    # list to store Movie instances
    movies = []
    for movie in movie_dict:
        if(movie['original_language'] == 'en'):
            trailer = get_trailer_link(movie['id'])
            if(trailer is None):
                # if trailer does not exist do not include the movie
                continue
            storyline = movie["overview"]
            title = movie['title']
            poster = get_poster_link(movie['poster_path'])
            # Movie Instance and adding them to movie list
            movies.append(
                Movie(title, storyline, poster, trailer)
            )
    return movies  # returing the list of Movie instance


def get_trailer_link(movie_id):
    # To get movie_id and return the youtube link
    url = 'https://api.themoviedb.org/3/movie/{id}/videos?api_key=1f4817acb34ea3063d54e2f4c641c5cb&language=en-US'
    url = url.format(id=movie_id)

    response = request.urlopen(url)

    response_read = str(response.read())

    # Removing unwanted characters from response_read
    response_read = response_read.replace('b\'', '')
    response_read = response_read.replace('\'', '')
    response_read = response_read.replace('\\\\\"', '')
    response_read = response_read.replace('\\', '')

    trailer_dict = yaml.load(response_read)
    if(trailer_dict['results'] != []):
        trailer = trailer_dict['results'][0]['key']
        return ('https://www.youtube.com/watch?v=' + trailer)

    # return None if movie trailer does not exist
    return None


def get_poster_link(file_name):
    # To return the full path of the poster
    return ('https://image.tmdb.org/t/p/w780' + file_name)


# getting data by call the function get_data()
movie_data = get_data()
fresh_tomatoes.open_movies_page(movie_data)
# fresh_tomatoes.open_movies_page() will create the html file for the movies
