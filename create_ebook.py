import argparse
import requests
from bs4 import BeautifulSoup
from ebooklib import epub

def create_ebook(url, book_title):
    try:
        # Fetch the content from the URL
        response = requests.get(url)
        response.raise_for_status()  # Raise an error for bad HTTP status
        soup = BeautifulSoup(response.content, 'html.parser')
        
        # Create an EPUB book
        book = epub.EpubBook()
        book.set_title(book_title)
        
        # Create and add a chapter
        chapter = epub.EpubHtml(title='Chapter 1', file_name='chap_01.xhtml')
        chapter.content = soup.prettify()
        book.add_item(chapter)
        
        # Set spine and navigation
        book.spine = ['nav', chapter]
        epub.write_epub(f'{book_title}.epub', book, {})
        print(f"eBook '{book_title}.epub' created successfully!")
    except requests.exceptions.RequestException as e:
        print(f"Error fetching URL: {e}")
    except Exception as e:
        print(f"Error creating eBook: {e}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Create an eBook from a webpage.")
    parser.add_argument('url', type=str, help='The URL of the webpage')
    parser.add_argument('title', type=str, help='The title of the eBook')
    
    args = parser.parse_args()
    create_ebook(args.url, args.title)
