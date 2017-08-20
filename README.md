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
```
Toy Story
```


### 2. fresh_tomatoes.py
This file is provided by Udacity.
[Click Here](https://github.com/udacity/ud036_StarterCode) for original file.
I have made changes in it.

### 3. movie_trailer.py
In this the data is been extracted with help of the API provided by [The Movie DB](https://developers.themoviedb.org/3/) 
