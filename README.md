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

Contributions are welcome! If you'd like to contribute to indexing more books, feel free to fork this repository, add 
the new data, and submit a pull request.

### Building Source Files

For any of the main sophonts, ships, weapons, robots, and vehicles should be included in both the main category and the
category for the sophont. 

Rules for creating Travellers for sophonts are nested under the Travellers group.

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

The Traveller game in all forms is owned by Mongoose Publishing. Copyright 1977 - 2024 Mongoose Publishing.
Traveller is a registered trademark of Mongoose Publishing. Mongoose Publishing permits web sites and fanzines
for this game, provided it contains this notice, that Mongoose Publishing is notified, and subject to a
withdrawal of permission on 90 days notice. The contents of this site are for personal, non-commercial use
only. Any use of Mongoose Publishing’s copyrighted material or trademarks anywhere on this web site and its
files should not be viewed as a challenge to those copyrights or trademarks. In addition, any
program/articles/file on this site cannot be republished or distributed without the consent of the author
who contributed it.