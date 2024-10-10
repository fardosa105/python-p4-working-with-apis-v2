import sys
from lib.open_library_api import Search

def main():
    # Check if the user provided a search term as an argument
    if len(sys.argv) < 2:
        print("Usage: python main.py <book title>")
        sys.exit(1)

    # Join the arguments to handle multi-word titles
    search_term = " ".join(sys.argv[1:])

    # Call the Search class and pass the user input to search
    result = Search().get_user_search_results(search_term)

    # Display the formatted result
    print("Search Result:\n")
    print(result)

# Execute the main function when the script is run
if __name__ == "__main__":
    main()
