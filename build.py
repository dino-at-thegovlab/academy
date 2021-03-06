import staticjinja
import os
import json
import yaml

# We define constants for the deployment.
cwd = os.getcwd()
searchpath  = os.path.join(cwd, "templates")
outputpath  = os.path.join(cwd, "site")

# We load the data we want to use in the templates.
#PEOPLE = json.load(open('data/cards.json'))
PEOPLE    = yaml.load(open('data/people.yaml'))
WORKSHOPS = yaml.load(open('data/workshops.yaml'))
CLINICS   = yaml.load(open('data/clinics.yaml'))

def loadAcademyData():
	return { 'people': PEOPLE,
					 'workshops': WORKSHOPS,
					 'clinics': CLINICS,
					 'resources': None }

# We define some filters we want to use in the templates.
def containsTag(x, y):
	if x['tags'] is None:
		return None
	return x if y in x['tags'] else None

filters = {
	'byName':   lambda x: [p for p in PEOPLE if p.name == x],
	'containsTag': containsTag,
}


site = staticjinja.make_site(
	searchpath=searchpath,
	outpath=outputpath,
	staticpaths=['static', '../data'],
	filters=filters,
	contexts=[(r'.*.html', loadAcademyData),]
	)
site.render(use_reloader=True)