# This program allows users to shorten and customize URLs

import pyshorteners  # for shortening URLs
import requests  # for making HTTP requests


def shorten_url(url):
    shortener = pyshorteners.Shortener()
    return shortener.tinyurl.short(url)


def customize_url(url, custom_alias):
    # TinyURL API endpoint for creating a custom alias
    api_url = "http://tinyurl.com/api-create.php"
    params = {"url": url, "alias": custom_alias}
    response = requests.get(api_url, params=params)
    if response.status_code == 200:
        return response.text
    else:
        return None


def main():
    url = input("Enter the URL to shorten: ")
    choice = input("Do you want to customize the URL? (yes/no): ").strip().lower()
    if choice == "yes":
        custom_alias = input("Enter the custom alias: ")
        short_url = customize_url(url, custom_alias)
    else:
        short_url = shorten_url(url)
    print("Shortened URL:", short_url)


if __name__ == "__main__":
    main()
