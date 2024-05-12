from flask import Flask, request, jsonify
from flask_cors import CORS
from geminiMoviesService import getMovieListFromGemini

app = Flask(__name__)
CORS(app)

@app.route("/get-movies")
def getMovies():
    prompt = request.args.get("prompt")

    if prompt:        
        return jsonify(getMovieListFromGemini(prompt)), 200
    else:
        defaultQuestion = "Liste os últimos 5 melhores filmes do ano."
        return jsonify(getMovieListFromGemini(defaultQuestion)), 200

@app.route("/")
def home():
    return "Nothing to see here."

if __name__ == "__main__":
    app.run(host="127.0.0.1",port="8000",debug=True)