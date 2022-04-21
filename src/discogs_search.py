import urllib.parse
import requests
import json
from src.items import no_input_item, no_results_item, generate_search_items

BASE_SEARCH_URL = 'https://api.discogs.com/database/search'

def strip_list(elements):
    return [element for element in elements if len(element.strip()) > 0]

class DiscogsSearch():
    def __init__(self, params, token):
        self.show_thumbnails = None
        self.query = ' '.join(params)
        self.api_token = token

    def has_query(self):
        return len(self.query) > 0

    def execute(self, num):
        payload = {'q': self.query, 'type': 'release', 'token': self.api_token}
        response = requests.get(BASE_SEARCH_URL, params=payload)
        results = []
        data = response.json()
        for i in range(num):
            results.append({
                'id': data['results'][i]['id'],
                'title': data['results'][i]['title'],
                'label': data['results'][i]['label'][0],
                'genre': ' '.join(data['results'][i]['genre']),
                'country': data['results'][i]['country'],
                'url': 'https://discogs.com/release/' + str(data['results'][i]['id']),
                'thumb': data["results"][i]['thumb']
            })
        return results
