import argparse
import os

from books import books
from topic_parser import parse_topics
from topics import topics
from webindex import generate_web_index
from worddoc import create_traveller_index


def main():
    parser = argparse.ArgumentParser(description="Mongoose Traveller Index Generator")
    parser.add_argument('-d', '--dir', nargs='+', help='Directory to process', required=False, default=[])
    parser.add_argument('-w', '--word', help='Output Word document')
    parser.add_argument('--html', help='HTML document')

    args = parser.parse_args()

    source_topics = {}

    for category in books:
        for book in books[category]:
            parse_topics(book, source_topics)

        sorted_topics = []
        for key in sorted(source_topics.keys()):
            sorted_topics.append(source_topics[key])

        if args.word:
            create_traveller_index(sorted_topics, args.word)

        if args.html:
            generate_web_index(topics, books, sorted_topics, args.html)

if __name__ == "__main__":
    main()
