import argparse
import os

import pandas as pd
from docx import Document
from docx.enum.text import WD_TAB_ALIGNMENT, WD_TAB_LEADER
from docx.shared import Pt, Inches, Cm

LEFT_ALIGNMENT = 0


def add_type_paragraph(document, type_name):
    document.add_page_break()
    paragraph = document.add_paragraph()
    run = paragraph.add_run(type_name)
    run.bold = True
    run.font.size = Pt(12)
    paragraph.alignment = LEFT_ALIGNMENT
    return paragraph


def add_page_text(paragraph, topic):
    paragraph.add_run('\t')

    books = sorted(topic['entries'].keys())
    for i, book in enumerate(books):
        pages = topic['entries'][book]
        p = ','.join(str(page['page']) for page in pages)
        entry_text = paragraph.add_run(f"{book} {p}")
        entry_text.font.size = Pt(8)
        if i < len(books) - 1:
            comma = paragraph.add_run(", ")
            comma.font.size = Pt(8)
    paragraph.alignment = LEFT_ALIGNMENT


def add_index_line(document, topic):
    paragraph = document.add_paragraph()

    subject = topic['topic']
    subject_text = paragraph.add_run(subject)
    subject_text.font.size = Pt(10)

    if len(topic['entries']) > 0:
        paragraph.paragraph_format.tab_stops.add_tab_stop(
            Cm(8.5), WD_TAB_ALIGNMENT.RIGHT, WD_TAB_LEADER.DOTS
        )
        add_page_text(paragraph, topic)

    for child_key in sorted(topic['children'].keys()):
        child = topic['children'][child_key]
        paragraph = document.add_paragraph()

        subject = child['topic']
        subject_text = paragraph.add_run(subject)
        subject_text.font.size = Pt(10)

        paragraph.paragraph_format.tab_stops.add_tab_stop(
            Cm(8.5), WD_TAB_ALIGNMENT.RIGHT, WD_TAB_LEADER.DOTS
        )
        paragraph.paragraph_format.left_indent = Cm(0.5)

        add_page_text(paragraph, child)


def create_traveller_index(topics, filename):
    document = Document()
    section = document.sections[-1]
    section.top_margin = Inches(0.5)
    section.bottom_margin = Inches(0.5)
    section.left_margin = Inches(0.5)
    section.right_margin = Inches(0.5)

    last_type = None
    for index, topic in enumerate(topics):
        if topic['type'] != last_type:
            add_type_paragraph(document, topic['type'])
            last_type = topic['type']

        add_index_line(document, topic)

    document.save(filename)


def add_topic(key, row, topics):
    if not key in topics:
        topics[key] = {
            'children': {},
            'entries': {},
            'topic': row['Topic'],
            'type': row['Type'],
        }
    book = row['Document']
    entry = topics[key]['entries']
    if not book in entry:
        entry[book] = []
    entry[book].append({
        "page": row['Page'],
        "primary": row['Primary'] != 'No',
    })


def parse_topics(source, topics):
    df = pd.read_csv(source, delimiter='\t')
    df = df.replace({pd.NA: None, pd.NaT: None, float('nan'): None})
    for index, row in df.iterrows():
        subject = row['Topic']
        group = row.get('Group', None)
        if group:
            group_key = (row['Type'], group)
            if group_key not in topics:
                topics[group_key] = {
                    'children': {},
                    'topic': group,
                    'type': row['Type'],
                    'entries': {},
                }
        else:
            group_key = None

        key = (row['Type'], subject)
        if group_key:
            add_topic(key, row, topics[group_key]['children'])
            if row['Type'] == 'Setting':
                add_topic(key, row, topics)
        else:
            add_topic(key, row, topics)


def main():
    parser = argparse.ArgumentParser(description="Mongoose Traveller Index Generator")
    parser.add_argument('-f', '--file', nargs='+', help='File to process', required=False, default=[])
    parser.add_argument('-d', '--dir', nargs='+', help='Directory to process', required=False, default=[])
    parser.add_argument('-o', '--output', help='Output Word document', required=True)

    args = parser.parse_args()

    topics = {}
    for file in args.file:
        parse_topics(file, topics)

    for directory in args.dir:
        for root, _, filenames in os.walk(directory):
            for filename in filenames:
                if filename.endswith('.tsv'):
                    full_path = os.path.join(root, filename)
                    parse_topics(full_path, topics)

    sorted_topics = []
    for key in sorted(topics.keys()):
        sorted_topics.append(topics[key])
    create_traveller_index(sorted_topics, args.output)


if __name__ == "__main__":
    main()