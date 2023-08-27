import requests

def getAllCourses():
    url = 'https://search.ezcampus.org/searchIndex/search'
    body = {"search_term": "ture","page": 1,"results_per_page": 14,"term_id": 1}
    requests.post(url,)