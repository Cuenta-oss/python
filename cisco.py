import requests
import matplotlib.pyplot as plt
import matplotlib.image as img
from pprint import pprint

url = 'https://pokeapi.co/api/v2/pokemon/pikachu'
res = requests.get(url)

imagen = img.imread(res.json()['sprites']['front_default'])

plt.title(res.json()['name'])
implot = plt.imshow(imagen)
plt.show()