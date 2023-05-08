import requests

response = requests.get("https://en.wikipedia.org/w/api.php?action=query&format=json&list=random&rnnamespace=0&rnlimit=1")

title = response.json()["query"]["random"][0]["title"]

url = "https://en.wikipedia.org/wiki/" + title.replace(" ", "_")

if __name__ == "__main__":
    print(url)
