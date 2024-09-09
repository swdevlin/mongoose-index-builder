# Mongoose Traveller 2nd Edition Grand Index

This repository contains the **Mongoose Traveller 2nd Edition Grand Index**, an attempt to index all Mongoose Traveller 2nd Edition books.

## Table of Contents

- [About the Project](#about-the-project)
- [Repository Structure](#repository-structure)
- [Access the Index](#access-the-index)
- [Contributing](#contributing)
- [License](#license)

## About the Project

The index is generated from tab separated value (TSV) files. The columns in the TSV files are:

- `Document` The abbreviation for the book
- `Topic` The entry in the index
- `Page` Page number for the topic
- `Type` The category for the entry. The column should have been called Category.
- `Primary` If the entry is not the primary entry, a `No` is entered in the column. Non-primary entries will be marked, eventually.
- `Group` If the entry belongs nested under another topic, place the topic name in this column.

The `word-index.py` script generates the .docx file. It takes the following parameters
- `--file` The file to parse. Multiple files can be specified
- `--dir` Parse all files in the specified directory and all subdirectories. Multiple directories can be specified.
- `--output` The name of the Word document to create.

## Repository Structure

- `static/grandindex.html`: The main HTML file that contains the index and links to PDF and DOCX downloads.
- `final/`: Directory that contains the MS Word and PDF versions of the index.
- `sources/`: Directory that contains the tab separated value (TSV) files used to generate the index.

## Access the Index

You can access the **Grand Index** directly at [https://radiofreewaba.net/traveller/grandindex.html](https://radiofreewaba.net/traveller/grandindex.html), where the latest PDF and DOCX versions are available for download.

## Contributing

Contributions are welcome! If you'd like to contribute to indexing more books, feel free to fork this repository, add the new data, and submit a pull request.

### Steps to Contribute:

1. Fork the repository.
2. Create a new branch (`git checkout -b new-index`).
3. Add your changes (index new books, fix bugs, etc.).
4. Commit your changes (`git commit -m 'Added new book to index'`).
5. Push to the branch (`git push origin new-index`).
6. Open a pull request.

## License

This project is licensed under the [MIT License](LICENSE).

---

**Traveller** is a registered trademark of Far Future Enterprises. This project is non-commercial and for personal use only.
