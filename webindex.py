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
					.traveller-red {
						color: #e10600; /* Traveller red */
					}
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
					.flex-container {
						display: flex;
						flex-direction: row;
					}
					dt {
						color: #e10600; /* Traveller red */
						font-family: "Orbitron", sans-serif;
						font-optical-sizing: auto;
						font-weight: 400;
						font-style: normal;
					}
					dd {
						margin-left: 12px;
						margin-bottom: 8px;
					}
					.left-column {
						margin-right: 18px;
					}
					.w50 {
						width: 50%;
					}
				</style>
			</head>
			<body>
				<h1>Mongoose Traveller 2<sup>nd</sup> Edition Grand Index</h1>
				<h2>Books</h2>
				<p>The following books are included in the index:</p>
				<div style="display: flex; justify-content: space-between;">
					<div style="width: 45%;">
						<table style="width: 100%;">
							<tr><td>Adventure Class Ships</td><td>ACS</td></tr>
							<tr><td>Aliens of Charted Space 1-3</td><td>AoCS1-3</td></tr>
							<tr><td>Behind the Claw</td><td>BtC</td></tr>
							<tr><td>Central Supply Catalogue</td><td>CSC</td></tr>
							<tr><td>Core Rulebook</td><td>CRB</td></tr>
							<tr><td>Death Station</td><td>DS</td></tr>
							<tr><td>Deepnight Endeavour</td><td>DE</td></tr>
							<tr><td>Drinax Companion</td><td>DC</td></tr>
							<tr><td>Friends in Dry Places</td><td>FiDP</td></tr>
							<tr><td>Gods of Marduk</td><td>GoM</td></tr>
							<tr><td>High and Dry</td><td>HaD</td></tr>
							<tr><td>High Guard</td><td>HG</td></tr>
							<tr><td>Journal of the Travellers’ Aid Society 1-14</td><td>JTAS1-14</td></tr>
							<tr><td>Liberty Port</td><td>LP</td></tr>
							<tr><td>Lions of Thebus</td><td>LoT</td></tr>
							<tr><td>Marooned on Marduk</td><td>MoM</td></tr>
						</table>
					</div>
					<div style="width: 45%;">
						<table style="width: 100%;">
							<tr><td>Robot Handbook</td><td>RH</td></tr>
							<tr><td>Shadows of Sindal</td><td>SoS</td></tr>
							<tr><td>Ships of the Reach</td><td>SotR</td></tr>
							<tr><td>Small Craft Catalog</td><td>SCC</td></tr>
							<tr><td>Solomani Adventure 1 – Mysteries on Arcturus Station</td><td>MoAS</td></tr>
							<tr><td>Revolution on Acrid</td><td>RoA</td></tr>
							<tr><td>Skandersvik</td><td>Sk</td></tr>
							<tr><td>Stranded</td><td>St</td></tr>
							<tr><td>Sword Worlds</td><td>SW</td></tr>
							<tr><td>The Calixcuel Incident</td><td>TCI</td></tr>
							<tr><td>The Cordon Conflict</td><td>TCC</td></tr>
							<tr><td>The Pirates of Drinax</td><td>TPoD</td></tr>
							<tr><td>The Trojan Reach</td><td>TRR</td></tr>
							<tr><td>Traveller Companion</td><td>TC</td></tr>
							<tr><td>Update 2022 FAQ</td><td>U2FAQ</td></tr>
							<tr><td>Vehicle Handbook</td><td>VH</td></tr>
						</table>
					</div>
				</div>
				<h2>Categories</h2>
				<p>Entries in the Grand Index are group by categories. The categories are:</p>
				<div class="flex-container">
					<div class="left-column w50">
						<dl>
							<dt><a href="#Adventures">Adventures</a></dt>
							<dd>This category includes all pre-written adventures, including campaigns such as Pirates of Drinax.</dd>
						
							<dt><a href="#Ancients">Ancients</a></dt>
							<dd>This category includes entries pertaining to the ancients, including a list of systems reported to have ancient sites.</dd>
						
							<dt><a href="#Aslan">Aslan</a></dt>
							<dd>This category includes entries pertaining to the Aslan. This includes references to the Hierate as well as The Glorious Empire.</dd>
						
							<dt><a href="#Bestiary">Bestiary</a></dt>
							<dd>Includes all animal entries.</dd>
						
							<dt><a href="#Bwap">Bwap</a></dt>
							<dd>This category includes entries pertaining to the Bwaps.</dd>
						
							<dt><a href="#Careers">Careers</a></dt>
							<dd>This category lists the various careers and pre-careers available to characters during the Traveller creation process.</dd>
						
							<dt><a href="#CentralSupply">Central Supply</a></dt>
							<dd>This category includes all non-weapon and non-armour equipment that players can acquire.</dd>
						
							<dt><a href="#Darrian">Darrian</a></dt>
							<dd>This category includes entries pertaining to the Darrians.</dd>
						
							<dt><a href="#Dolphin">Dolphin</a></dt>
							<dd>This category includes entries pertaining to the Dolphins.</dd>
						
							<dt><a href="#Drone">Drone</a></dt>
							<dd>This category lists sample drones. Rules for creating drones are contained in the Robots section.</dd>
						
							<dt><a href="#Droyne">Droyne</a></dt>
							<dd>This category includes entries pertaining to the Droyne.</dd>
						
							<dt><a href="#Encounter">Encounter</a></dt>
							<dd>This category includes random encounters or scenario-specific encounters from the Journal of the Travellers' Aid Society (JTAS).</dd>
						
							<dt><a href="#Geonee">Geonee</a></dt>
							<dd>This category includes entries pertaining to the Geonee.</dd>
						
							<dt><a href="#HighGuard">High Guard</a></dt>
							<dd>This category includes entries for shipbuilding rules, equipment, and other starship-related topics.</dd>
						
							<dt><a href="#KKree">K’Kree</a></dt>
							<dd>This category includes entries pertaining to the K’Kree.</dd>
						
							<dt><a href="#Orca">Orca</a></dt>
							<dd>This category includes entries pertaining to the Orcas.</dd>
						
							<dt><a href="#NPCs">NPCs</a></dt>
							<dd>This category includes skill and characteristic blocks for generic non-player characters (NPCs).</dd>
						
							<dt><a href="#Patron">Patron</a></dt>
							<dd>Entries in this category detail potential patrons from the JTAS, who may offer missions, employment, or other opportunities to Traveller characters.</dd>
						
							<dt><a href="#PersonalProtection">Personal Protection</a></dt>
							<dd>This category covers all types of protective gear and armour.</dd>						
						</dl>
					</div>
					<div class="w50">
						<dl>				
							<dt><a href="#Polity">Polity</a></dt>
							<dd>This category includes political entities and governing bodies that are not given a full write-up.</dd>
						
							<dt><a href="#Psionics">Psionics</a></dt>
							<dd>This category includes entries related to psionics, including powers, training, institutions.</dd>
						
							<dt><a href="#Robotics">Robotics</a></dt>
							<dd>This category covers robot construction and rules.</dd>
						
							<dt><a href="#Robots">Robots</a></dt>
							<dd>This category lists the published robots.</dd>
						
							<dt><a href="#Rules">Rules</a></dt>
							<dd>This category includes entries that affect gameplay, typically involving skill checks, dice modifiers (DMs), or specific rules for various situations.</dd>
						
							<dt><a href="#Setting">Setting</a></dt>
							<dd>This category includes entries that provide flavour or background information.</dd>
						
							<dt><a href="#Ships">Ships</a></dt>
							<dd>This category includes ship types with full description and stat blocks; ship mentions are not included. Rules for ship construction are found in the High Guard category.</dd>
						
							<dt><a href="#Skill">Skill</a></dt>
							<dd>This category covers character skills.</dd>
						
							<dt><a href="#SmallCraft">Small Craft</a></dt>
							<dd>This category includes space craft under 100 tons with full description and stat blocks; entries that simply mention the craft are not included. Rules for small craft construction are found in the High Guard category.</dd>
						
							<dt><a href="#Solomani">Solomani</a></dt>
							<dd>This category includes entries pertaining to the Solomani.</dd>
						
							<dt><a href="#Sophont">Sophont</a></dt>
							<dd>This category lists the sophonts that are not one of the major six.</dd>
						
							<dt><a href="#SwordWorldsConfederacy">Sword Worlds Confederacy</a></dt>
							<dd>This category includes entries about the Sword Worlds Confederacy.</dd>
						
							<dt><a href="#System">System</a></dt>
							<dd>This category includes entries discussing a star system.</dd>
						
							<dt><a href="#Vargr">Vargr</a></dt>
							<dd>This category includes entries pertaining to the Vargr.</dd>
						
							<dt><a href="#VehicleWorkshop">Vehicle Workshop</a></dt>
							<dd>This category covers vehicle construction and rules.</dd>
						
							<dt><a href="#Vehicles">Vehicles</a></dt>
							<dd>This category includes vehicles with full description and stat blocks; vehicle mentions are not included. Rules for vehicle construction are covered in Vehicle Workshop.</dd>
						
							<dt><a href="#Weapon">Weapon</a></dt>
							<dd>This category includes descriptions of personal weapons and their modifications, as well as ammo and weapon traits.</dd>
						
							<dt><a href="#Zhodani">Zhodani</a></dt>
							<dd>This category includes entries pertaining to the Zhodani.</dd>
						</dl>
					</div>
				</div> 
		""")

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
					<footer>
						<p>
							This work is produced in accordance to Mongoose Publishing's <a
							href="https://cdn.shopify.com/s/files/1/0609/6139/0839/files/Traveller_Fair_Use_Policy_2024.pdf?v=1725357857">Fair
							Use Policy</a>.
						</p>
						<p>
							The Traveller game in all forms is owned by Mongoose Publishing. Copyright 1977 - 2024 Mongoose Publishing.
							Traveller is a registered trademark of Mongoose Publishing. Mongoose Publishing permits web sites and fanzines
							for this game, provided it contains this notice, that Mongoose Publishing is notified, and subject to a
							withdrawal of permission on 90 days notice. The contents of this site are for personal, non-commercial use
							only. Any use of Mongoose Publishing’s copyrighted material or trademarks anywhere on this web site and its
							files should not be viewed as a challenge to those copyrights or trademarks. In addition, any
							program/articles/file on this site cannot be republished or distributed without the consent of the author
							who contributed it.
						</p>
					</footer>
				</body>
			</html>
				""")