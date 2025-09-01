import pandas as pd

GROUP_CORRECTIONS = {
	'Armour': 'Personal Protection',
	'Augment': 'Augmentations',
	'Augments': 'Augmentations',
	'Augmentation': 'Augmentations',
	'Characteristic': 'Characteristics',
	#  don't nest corps
	'Corporation': '',
	'Corporations': '',
	'Drone': 'Drones',
	'Robot': 'Robots',
	'Ship': 'Ships',
	'Vehicle': 'Vehicles',
}

# Bulk correct entries with the incorrect type
TYPE_CORRECTIONS = {
	# fix pluralization
	'Adventure': 'Adventures',
	'Career': 'Careers',
	'Robot': 'Robots',
	'System': 'Systems',
	'Ship': 'Ships',
	'Skill': 'Skills',
	'small craft': 'Small Craft',
	'Small craft': 'Small Craft',
	'Sophont': 'Sophonts',
	'System': 'Systems',
	'Vehicle': 'Vehicles',
	'Weapons': 'Weapon',

	# Adjust mapping
	'Drone': 'Robots',
	'Drones': 'Robots',
	'Armour': 'Personal Protection',
	"K'Kree": "K'kree",

	# Not sure a list helps people, so moving them to setting
	'Corporation': 'Setting',
	'Megacorporation': 'Setting',
	'Megacorporations': 'Setting',
	'Person': 'Setting',

	# Don't want these pulled out, but might someday, so....
	'Sectors': 'Setting',
	'Sector': 'Setting',
	'Subsectors': 'Setting',
	'Subsector': 'Setting',
	'NPC': 'Setting',
	'NPCs': 'Setting',
}


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


def parse_topics(book, topics):
	url = f"https://docs.google.com/spreadsheets/d/{book['id']}/gviz/tq?tqx=out:csv&sheet=0"
	print(f"Parsing {book['title']} from {url}")
	df = pd.read_csv(url)
	# df = pd.read_csv(source, delimiter='\t')
	df = df.replace({pd.NA: None, pd.NaT: None, float('nan'): None})
	for index, row in df.iterrows():
		# adjust Mongoose's proper use of ’
		row['Type'] = row['Type'].replace('’', "'")
		row['Topic'] = row['Topic'].replace('’', "'")
		row['Document'] = book['abbreviation']

		for key in TYPE_CORRECTIONS:
			if row['Type'] == key:
				row['Type'] = TYPE_CORRECTIONS[key]

		for key in GROUP_CORRECTIONS:
			if row.get('Group', None) == key:
				row['Group'] = GROUP_CORRECTIONS[key]

		subject = row['Topic']
		group = row.get('Group', None)
		if group:
			# adjust Mongoose's proper use of ’
			group = group.replace('’', "'")

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
