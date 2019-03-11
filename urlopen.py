#!/usr/bin/env python3
import sys
from urllib.request import urlopen

def fetch_words(url):
    """Fetches a list of words from a URL.
    
    Args:
        url: The URL of a UTF-8 text document.

    Returns:
        A list of strings containing the words from the document.
    """
    with urlopen(url) as story:
        story_words = []
        for line in story:
            line_words = line.decode('utf-8').split()
            for word in line_words:
                story_words.append(word)
        print(list(story_words))
        #return story_words


def main():
    # sys.argv[0] is the script name
    url = sys.argv[1] # first argument when running the script must be an url http://sixty-north.com/c/t.txt, http://web.textfiles.com/humor/maple.txt
    fetch_words(url)

if __name__ == "__main__":
    main()
