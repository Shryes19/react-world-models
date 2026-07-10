import requests


class WikipediaTool:
    def search(self, query: str) -> str:
        url = "https://en.wikipedia.org/w/api.php"

        params = {
    "action": "query",
    "list": "search",
    "srsearch": query,
    "format": "json",
}

        headers = {
    "User-Agent": "ReActResearchBot/1.0 (shryes107@gmail.com)"
}

        response = requests.get(
    url,
    params=params,
    headers=headers,
    timeout=10
)
        print(response.status_code)
        print(response.text[:500])
        data = response.json()

        results = data["query"]["search"]

        if not results:
            return "No Wikipedia page found."

        title = results[0]["title"]

        params = {
    "action": "query",
    "prop": "extracts",
    "exintro": True,
    "explaintext": True,
    "titles": title,
    "format": "json",
}

        response = requests.get(
        url,
        params=params,
        headers=headers,
        timeout=10
)

        data = response.json()

        page = next(iter(data["query"]["pages"].values()))

        return page.get("extract", "No summary found.").split("\n")[0]