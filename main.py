from html_handler.html_handler import HtmlHandler
from html_handler.ns import FOLLOWERS, FOLLOWING

def main():
    handler = HtmlHandler()
    followers = handler.extract("test_data/connections/followers_and_following/followers_1.html", FOLLOWERS)

if __name__ == "__main__":
    main()