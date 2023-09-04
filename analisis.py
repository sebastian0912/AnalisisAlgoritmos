import requests
from requests_oauthlib import OAuth1

# Tus credenciales de OAuth 1.0a
# Define tus claves y tokens
CONSUMER_KEY = 'l4vXQt0zsZ34igqLMmKrMJsIN'
CONSUMER_SECRET = 'hAipT7p9IZe8V031DeLj7Tv2E9uXv8ha5b1QHci94c6gwTTgK5'
ACCESS_TOKEN = '1637491843561582592-i9v1176wU6Sb2Rpdotun0MZFszvdac'
ACCESS_TOKEN_SECRET = 'Ib4fVDH64bItiVP1ekxtZx3DuSnuERiFnnK4IeGGrmeI8'

# Configuración de OAuth
auth = OAuth1(CONSUMER_KEY, CONSUMER_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

# URL de la API para obtener tweets (esto es solo un ejemplo, ya que estamos usando el endpoint para crear tweets)
url = 'https://api.twitter.com/2/tweets'

# Parámetros para la solicitud (esto es solo un ejemplo, deberías especificar los parámetros relevantes)
params = {
    'status': 'Hola, mundo!'  # Texto del tweet a crear
}

# Hacer la solicitud POST
response = requests.post(url, auth=auth, params=params)

# Verificar la respuesta
if response.status_code == 201:
    print('Tweet creado con éxito!')
    print(response.json())
else:
    print(f'Error: {response.status_code}')
    print(response.text)
