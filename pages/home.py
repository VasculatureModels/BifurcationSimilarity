import dash
from dash import html, dcc

dash.register_page(__name__, path='/')

""" 
layout = html.Div([
	dcc.Markdown(['''

	---
	
	## &nbsp;&nbsp;Ce test a pour objectif d'évaluer les similarités entre des bifurcations cérébrales.

	&nbsp;&nbsp;Deux portions d'arbres vasculaires seront présentées dans un affichage 3D, l'une est une originale (acquise depuis une MRA-TOF), l'autre est le fruit d'un modèle synthétique.

	&nbsp;&nbsp;La portion affichée en jaune est une originale (extraite d'une IRM de patient), la verte provient du modèle synthétique.

	&nbsp;&nbsp;Il y aura nécessairement des différences dans la tortuosité des branches, ce qui importe c'est surtout leur présence, pas leur forme.

	## &nbsp;&nbsp;Protocole :
	&nbsp;&nbsp;Dix boutons sont positionnés en haut de la page et servent à évaluer les similarités.

	&nbsp;&nbsp;La sélection d'un score (1 : très peu de similarités, 10 : bifurcations quasi-identiques), permet de passer à l'affichage suivant.  
	&nbsp;&nbsp;Un score de 1 signifie : "entre 0% et 10% de similarités", un score de 2 : "entre 10 et 20% de similarités", etc.

	&nbsp;&nbsp;Ce score est une mesure du pourcentage de fiabilité du modèle, i.e. il quantifie le nombre de branches présentes.

	&nbsp;&nbsp;Il y a sept tests différents, composés chacun de 150 portions d'arbres vasculaires, chaque test dure approximativement 20 à 25 minutes.

	## &nbsp;&nbsp;Commandes : 
	+ &emsp;Pour chaque affichage 3D, il est possible de faire pivoter la bifurcation avec le bouton de gauche de la souris. 
	+ &emsp;Il est aussi possible de zoomer (avec la molette de la souris)
	+ &emsp;ou encore déplacer (en utilisant la touche 'SHIFT' du clavier).

	&nbsp;NOTES :  
	&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 1) Les 5 premières images servent d'ancrage, i.e. elles montrent l'amplitude des distortions sur l'échelle de similarités \[1,10\].  
	&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 2) Parfois, la partie "modèle" (verte) peut être manquante, mais un score est requis (noter "1").  
	
'''],),
html.Br(),
dcc.Link(html.Button("EXPERIMENT #1"), href="/pages/subjexp1", refresh=True),
html.Br(),
html.Br(),
dcc.Link(html.Button("EXPERIMENT #2"), href="/pages/subjexp2", refresh=True),
html.Br(),
html.Br(),
dcc.Link(html.Button("EXPERIMENT #3"), href="/pages/subjexp3", refresh=True),
html.Br(),
html.Br(),
dcc.Link(html.Button("EXPERIMENT #4"), href="/pages/subjexp4", refresh=True),
html.Br(),
html.Br(),
dcc.Link(html.Button("EXPERIMENT #5"), href="/pages/subjexp5", refresh=True),
html.Br(),
html.Br(),
dcc.Link(html.Button("EXPERIMENT #6"), href="/pages/subjexp6", refresh=True),
html.Br(),
html.Br(),
dcc.Link(html.Button("EXPERIMENT #7"), href="/pages/subjexp7", refresh=True),
])
""" 


layout = html.Div([
	dcc.Markdown(['''

	---

	## &nbsp;&nbsp;The goal of this subjective experiment is to assess the similarities between cerebral bifurcations.

	&nbsp;&nbsp;Two portions (3D crops) of vascular trees will be shown within a 3D display, one is an original bifurcaion (acquired from an MRA-TOF), the other has been generated via a synthetic model.

	&nbsp;&nbsp;The yellow vascular tree is the original (from a patient MRI), the green one is generated from the synthetic modeled.

	&nbsp;&nbsp;There will necessarily be some differences in the geometrical layout (different tortuosity between the branches), but what actually matters is mostly the branches presence, not quite their shape.

	## &nbsp;&nbsp;Protocol description:

	&nbsp;&nbsp;The observers shall use the ten push buttons, placed at the very top of the page, to assess the similarities.

	&nbsp;&nbsp;When selecting a similarity score (1 : very few simialrities, 10 : almost identical vascular trees), the protocol moves on to the next display.  
	&nbsp;&nbsp;A score of 1 means : "between 0% and 10% similarities", a score of 2 : "between 10 and 20% similarities", etc.

	&nbsp;&nbsp;This score can be seen as a measure of the reliability percentage of the synthetic model, i.e. we quantify the number of modeled branches.

	&nbsp;&nbsp;There are seven distinct experiments, each one being composed of 150 portions of vascular trees, for each test, the duration is about 20 to 25 minutes.

	## &nbsp;&nbsp;Controls :
	+ For each 3D display, the user can rotate the bifurcation using the left mouse button. 
	+ It is also possible to zoom (in/out) (using the scroll wheel).
	+ The display can also be shifted (by holding the 'SHIFT' key, whie dragging the image).
	
	
	NOTES :  
	&nbsp;&nbsp;&nbsp;&nbsp; 1) The first 5 images are used for anchoring, i.e. their purpose is to give the user an idea of the distortions within the \[1,10\] similmarity range.  
	&nbsp;&nbsp;&nbsp;&nbsp; 2) It can happen that the model portion is missing, a score is required anyway (allocate a "1").  

'''],),
html.Br(),
dcc.Link(html.Button("EXPERIMENT #1"), href="/pages/subjexp1", refresh=True),
html.Br(),
html.Br(),
dcc.Link(html.Button("EXPERIMENT #2"), href="/pages/subjexp2", refresh=True),
html.Br(),
html.Br(),
dcc.Link(html.Button("EXPERIMENT #3"), href="/pages/subjexp3", refresh=True),
html.Br(),
html.Br(),
dcc.Link(html.Button("EXPERIMENT #4"), href="/pages/subjexp4", refresh=True),
html.Br(),
html.Br(),
dcc.Link(html.Button("EXPERIMENT #5"), href="/pages/subjexp5", refresh=True),
html.Br(),
html.Br(),
dcc.Link(html.Button("EXPERIMENT #6"), href="/pages/subjexp6", refresh=True),
html.Br(),
html.Br(),
dcc.Link(html.Button("EXPERIMENT #7"), href="/pages/subjexp7", refresh=True),
])

