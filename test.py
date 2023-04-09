import requests
from urllib.parse import urlencode

def search(query: str):
    encoded_query = urlencode({"q": query})
    url = f"https://customsearch.googleapis.com/customsearch/v1?{encoded_query}&cx=YOUR_CX&num=5&key=YOUR_API_KEY&alt=json"
    response = requests.get(url)

    if response.status_code == 200:
        results = response.json()
        return results
    else:
        raise Exception(f"Error: {response.status_code} - {response.text}")

if __name__ == "__main__":
    query = "pros and cons of golang vs rust"
    search_results = search(query)

    # Do something with search_results, e.g., print the first result's title and snippet
    first_result = search_results["items"][0]
    print(f"Title: {first_result['title']}\nSnippet: {first_result['snippet']}")
