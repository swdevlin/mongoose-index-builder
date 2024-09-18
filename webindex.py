def add_entry(topic, indented=False):
	lines = []
	lines.append('<tr>')
	if indented:
		lines.append(f'<td class="entry-name indented">{topic["topic"]}</td>')
	else:
		lines.append(f'<td class="entry-name">{topic["topic"]}</td>')
	lines.append('<td class="book-pages">')

	books = []
	for book, entries in sorted(topic['entries'].items()):
		pages = ', '.join(str(entry['page']) for entry in entries)
		books.append(f'{book}: {pages}')
	lines.append(', '.join(books))
	lines.append('</td>')
	lines.append('</tr>')

	for child_key in sorted(topic['children'].keys()):
		child = topic['children'][child_key]
		lines.extend(add_entry(child, True))

	return lines


def generate_web_index(topics, output_file):
	with open(output_file, 'wt', encoding='utf-8') as f:
		f.write("""
			<!DOCTYPE html>
			<html lang="en">
			<head>
				<meta charset="UTF-8">
				<meta name="viewport" content="width=device-width, initial-scale=1.0">
				<link rel="preconnect" href="https://fonts.googleapis.com">
				<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
				<link href="https://fonts.googleapis.com/css2?family=Orbitron:wght@600&family=Roboto:ital,wght@0,400&display=swap" rel="stylesheet">
				<title>Traveller Index</title>
				<style>
					body {
						font-family: "Roboto", sans-serif;
						font-weight: 400;
						background-color: black;
						color: white;
						font-size: 10pt;
					}
					h1, h2 {
						color: #e10600; /* Traveller red */
						font-family: "Orbitron", sans-serif;
            font-optical-sizing: auto;
            font-weight: 600;
            font-style: normal;
					}
					h3 {
						color: white;
					}
					a {
						text-decoration: none;
						color: #e10600;
					}
					a:hover {
						text-decoration: underline;
					}
					.toc {
						margin-bottom: 20px;
					}
					.toc a {
						display: block;
						margin-bottom: 5px;
					}
					.group {
						margin-bottom: 30px;
					}
					.entry {
						margin-left: 20px;
					}
					.indented {
					  padding-left: 12px;
					}
					.book-pages {
						font-size: 0.9em;
						color: #aaa;
					}
				</style>
			</head>
			<body>
				<h1>Mongoose Traveller 2<sup>nd</sup> Edition Grand Index</h1>
				<div class="toc">
				<h2>Table of Contents</h2>
		""")

		groups = set(topic['type'] for topic in topics)
		for group in sorted(groups):
			f.write(f'<a href="#{group}">{group}</a>\n')

		f.write('</div>')

		# Write each group and its entries in table format
		last_type = None
		for topic in topics:
			if topic['type'] != last_type:
				if last_type:
					f.write('<table>\n')
				f.write(f'<h2 id="{topic["type"]}">{topic["type"]}</h2>\n')
				f.write('<table>\n')
				last_type = topic['type']

			lines = add_entry(topic)
			f.write('\n'.join(lines))

		f.write("""
				</body>
				</html>
				""")