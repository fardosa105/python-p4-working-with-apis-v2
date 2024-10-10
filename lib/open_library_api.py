import requests
import json
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

class Search:
    def get_user_search_results(self, search_term):
        logging.info(f"Searching for: {search_term}")
        try:
            search_term_formatted = search_term.replace(" ", "+")
            fields = ["title", "author_name"]
            fields_formatted = ",".join(fields)
            limit = 5

            URL = f"https://openlibrary.org/search.json?title={search_term_formatted}&fields={fields_formatted}&limit={limit}"

            logging.info(f"Requesting URL: {URL}")
            response = requests.get(URL)
            response.raise_for_status()

            data = response.json()

            if not data['docs']:
                logging.warning("No results found.")
                return "No results found."

            results = []
            for book in data['docs']:
                title = book.get('title', 'No title')
                author = ', '.join(book.get('author_name', ['Unknown author']))
                results.append(f"Title: {title}\nAuthor: {author}")

            return "\n\n".join(results)
        except requests.exceptions.RequestException as e:
            logging.error(f"HTTP request failed: {e}")
            return f"An error occurred: {e}"
        except (KeyError, IndexError):
            logging.error("Unexpected response format.")
            return "Unexpected response format from the API."
