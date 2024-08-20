from PIL import Image
from io import BytesIO
import requests


def get_photo(url):
    response = requests.get(url)
    image = Image.open(BytesIO(response.content))
    image.save("very_secret.png")


URL = input("Enter the URL: ")
get_photo(URL)
