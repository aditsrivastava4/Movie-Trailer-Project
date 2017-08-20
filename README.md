# Movie Trailer Project

This project is to create a webpage to show movie title, poster & trailer.The webpage is create by python.

## Modules
* media.py
* fresh_tomatoes.py
* movie_trailer.py

### 1. media.py
> class Movie(title,storyline,poster_image_url,trailer_youtube_url)
> 
> class **Movie** will store the data of a moive which are
> its Title, Storyline, Poster Image link & Trailer Link
> which will create a instance of that movie.
> 
> Parameters
> 
> **title**: Title of the Movie(string type)
> 
> **storyline**:  Storyline of the Movie(string type)
> 
> **poster_image_url**: Poster Image link of the Movie(string type)
> 
> **trailer_youtube_url**: Trailer Link of the Movie(string type)

#### Example
```
from media import Movie
toystory = Movie('Toy Story','movie stroyline','movie poster link','movie youtube trailer link')
print(toystory.title)
```
This will create a instance of a movie.

### 2. fresh_tomatoes.py
This file is provided by Udacity.
[Click Here](https://github.com/udacity/ud036_StarterCode) for original file.
It creates the html file of the webpage.
I have made some changes in its HTML and CSS.

### 3. movie_trailer.py
In this the movie data is being provided by the API [The Movie DB](https://developers.themoviedb.org/3/).
> get_data(): It will get the movie data and ```return``` the list of movie instances.
> 
> get_trailer_link(movie_id): It will take the movie_id and ```return``` the youtube trailer link.
> Parameters
> movie_id: Movie ID provided by the API(string type)
> 
> get_poster_link(file_name): Will take the file name and ```return``` file link/path.
> Parameters
> file_name: Poster file name provided by the API(string type)
> 

## To Run
To run this project execute the movie_trailer.py file
<br>**or**<br>
To run on python shell
```
>>> import movie_trailer
```
