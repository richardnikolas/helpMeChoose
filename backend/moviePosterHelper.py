import requests  

headers = {
    "accept": "application/json",
    "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiIyMzNjMTY2NDI1NDFiMGExZWNjMDIyNTIzYjY1MjJlOSIsInN1YiI6IjY2M2Y3MDNiYmUyMjk0ZDgwNjQ3ZGFkZiIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.xt0DAoBnne0yg_0KTsFOhJokVphLionVGLLXWC4HpjE"
}

# themoviedb
apiKey = "YOUR_TMDB_DEV_API_KEY"

def getMoviePoster(movieName):
    # themoviedb API to get details and poster
    movieDetailsUrl = f"https://api.themoviedb.org/3/search/movie?api_key={apiKey}&query={movieName}"

    movieDetails = requests.get(movieDetailsUrl).json()

    if len(movieDetails["results"]) > 0:
        movieId = movieDetails["results"][0]["id"]

        url = f"https://api.themoviedb.org/3/movie/{movieId}/images?api_key={apiKey}&language=en-US&include_image_language=en,pt,null"

        moviePosters = requests.get(url).json()

        filePath = moviePosters["posters"][0]["file_path"]

        if len(filePath) == 0 or filePath is None:
            return None
        else:
            posterUrl = f"https://image.tmdb.org/t/p/original{filePath}"
            return posterUrl
