import requests

def getAllCourses():
    url = 'https://search.ezcampus.org/searchIndex/search'
    # Need to think of a way to go through every single search possibility

def findCourses(search_term: str, term_id: int, results_per_page: int=2**31-1, page: int=1):
    url = 'https://search.ezcampus.org/searchIndex/search'
    body = {"search_term": search_term,"page": page,"results_per_page": results_per_page,"term_id": term_id}
    return requests.post(url,body).json()

def listSchools():
    url = 'https://search.ezcampus.org/searchIndex/school'
    return requests.get(url).json()

def main():
    print(listSchools())

if __name__ == '__main__':
    main()