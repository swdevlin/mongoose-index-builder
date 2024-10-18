from jinja2 import Environment, FileSystemLoader


def compute_references(topic):
	books = []
	for book, entries in sorted(topic['entries'].items()):
		pages = ', '.join(str(entry['page']) for entry in entries)
		books.append(f'{book}: {pages}')
	topic['references'] = ', '.join(books)


def generate_web_index(topics, books, source_topics, output_file):
	env = Environment(loader=FileSystemLoader('templates'), trim_blocks=True, lstrip_blocks=True)
	template = env.get_template('web-index.html')

	keys = sorted(topics.keys())

	for topic in source_topics:
		compute_references(topic)
		for child in sorted(topic['children'].keys()):
			compute_references(topic['children'][child])

	rendered_html = template.render(
		books=books,
		topics=topics,
		keys=keys,
		half_categories=len(keys) // 2,
		source_topics=source_topics,
	)

	with open(output_file, 'w', encoding='utf-8') as f:
		f.write(rendered_html)
