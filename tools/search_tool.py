import os
import requests
from dotenv import load_dotenv

load_dotenv()

# Note: You'll need a search API key (like Serper.dev or Google Custom Search) 
# to make this fully functional.
SEARCH_API_KEY = os.getenv("SEARCH_API_KEY")

class TravelSearchTool:
    def __init__(self):
        self.base_url = "https://google.serper.dev/search"

    def fetch_safety_data(self, country):
        """
        Fetches the latest unstructured news and alerts for a specific country.
        """
        if not SEARCH_API_KEY:
            return "Error: SEARCH_API_KEY not found in .env"

        payload = {
            "q": f"latest travel safety alerts and government advisories for {country}",
            "gl": "us",
            "hl": "en"
        }
        headers = {
            'X-API-KEY': SEARCH_API_KEY,
            'Content-Type': 'application/json'
        }

        try:
            response = requests.post(self.base_url, headers=headers, json=payload)
            results = response.json()
            
            # Simplified extraction of snippets (unstructured data)
            snippets = [item.get('snippet', '') for item in results.get('organic', [])]
            return " ".join(snippets)
        except Exception as e:
            return f"Agentic Recovery Trigger: Search failed due to {str(e)}. Attempting backup protocol..."

# Mock execution for the demo
if __name__ == "__main__":
    tool = TravelSearchTool()
    print(tool.fetch_safety_data("Japan"))
