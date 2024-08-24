import PyPDF2
from collections import defaultdict
import re

with open('stopwords.txt', 'r') as f:
    lines = f.readlines()
lines = [line.strip() for line in lines]
stopwords = set(lines)


def extract_words_from_pdf(pdf_path):
    # Create a PDF reader object
    pdf_reader = PyPDF2.PdfReader(open(pdf_path, "rb"))

    # Initialize a defaultdict to store the words and their page numbers
    word_index = defaultdict(set)

    # Loop through each page
    for page_num in range(len(pdf_reader.pages)):
        page = pdf_reader.pages[page_num]
        text = page.extract_text()

        # if 'starship automation' in text.lower():
        #     print(text)
        #     print(page)
        words = re.findall(r'\b\w+\b', text)
        # words = re.findall(r'\b\w+\b', text.lower())

        # Add the page number to the set for each word
        for word in words:
            if word.lower() not in stopwords:
                if not bool(re.search(r'\d', word)):
                    if word != word.lower():
                        word_index[word].add(page_num + 1)  # Page numbers are 1-indexed

    # Convert the sets to sorted lists for easier reading
    word_index = {word: sorted(pages) for word, pages in word_index.items()}

    return word_index


def save_index_to_file(word_index, output_file):
    with open(output_file, 'w', encoding='utf-8') as f:
        for word, pages in sorted(word_index.items()):
            f.write(f'{word}: {", ".join(map(str, pages))}\n')


# Example usage
pdf_path = 'w:\\traveller\\mongoose latest\\Companion Update 2024.pdf'
output_file = 'companion-2024.txt'
word_index = extract_words_from_pdf(pdf_path)
save_index_to_file(word_index, output_file)
pdf_path = 'w:\\traveller\\Arcturus Station.pdf'
output_file = 'Arcturus Station.txt'
word_index = extract_words_from_pdf(pdf_path)
save_index_to_file(word_index, output_file)
