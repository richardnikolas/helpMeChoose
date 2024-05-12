import google.generativeai as genai
import json

from moviePosterHelper import getMoviePoster

genai.configure(api_key="AIzaSyC0yhExP-VrhZFj6bRVTpe_5i3P7hfA2FA")

# Set up the model
generation_config = {
  "temperature": 0.9,
  "top_p": 0.7,
  "top_k": 0,
  "max_output_tokens": 8192,
  "response_mime_type": "application/json",
}

safety_settings = [
  {
    "category": "HARM_CATEGORY_HARASSMENT",
    "threshold": "BLOCK_NONE"
  },
  {
    "category": "HARM_CATEGORY_HATE_SPEECH",
    "threshold": "BLOCK_NONE"
  },
  {
    "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
    "threshold": "BLOCK_NONE"
  },
  {
    "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
    "threshold": "BLOCK_NONE"
  },
]

def getMovieListFromGemini(userPropmt):
    system_instruction = "Responda com um array de no máximo 10 items e use este formato de resposta para cada filme: {'title': 'Titulo do filme','releaseYear': 'Ano de lançamento do filme.','rating': 'A nota do filme de acordo com o IMBD ou o Google','director': 'Diretor ou diretora daquele filme','synopsis': 'Uma sinopse curta do filme traduzida para o Português do Brasil','posterUrl': ''}"

    model = genai.GenerativeModel(model_name="gemini-1.5-pro-latest",
                                generation_config=generation_config,
                                system_instruction=system_instruction,
                                safety_settings=safety_settings)

    response = model.generate_content(userPropmt)

    jsonResponse = json.loads(response.text)
  
    for movie in jsonResponse:
      posterUrl = getMoviePoster(movie["title"])
      movie["posterUrl"] = posterUrl

    return jsonResponse
