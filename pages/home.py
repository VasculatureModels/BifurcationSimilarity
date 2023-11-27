import dash
from dash import html, dcc

dash.register_page(__name__, path='/')

layout = html.Div([
	html.Br(),
	html.Br(),
	html.Div("L'objectif de ce test est d'évaluer les similarités entre des bifurcatsion cérébrales"),
	html.Div("Deux bifurcations seront présentées dans un display 3D, l'une est une originale (acquise depuis une MRA-TOF), l'autre est le fruit d'un modèle synthétique."),
	html.Br(),
	html.Div("La bifurcation affichée en vert est une originale (extraite d'une IRM de patient) la jaune provient d'un modèle synthétique."),
	html.Br(),
	#html.Div("Une barre de défilement positionnée en haut de la page sert à évaluer les similarités."),
	html.Div("Dix boutons sont positionnés en haut de la page et servent à évaluer les similarités."),
	html.Br(),
	#html.Div("Une fois un score sélectionné (1 : très peu de similarités, 10 : bifurcations quasi-identiques),"),
	#html.Div("Vous pouvez valider le score grâce au bouton 'NEXT'."),
	html.Div("La sélection d'un score (1 : très peu de similarités, 10 : bifurcations quasi-identiques), permet de passer à l'affichage suivant."),
	html.Br(),
	html.Br(),
	html.Div("Pour chaque affichage 3D, il est possible de faire pivoter la bifurcation avec le bouton de gauche de la souris. "),
	html.Div("Il est aussi possible de zoomer (avec la molette de la souris) ou encore déplacer (en utilisant la touche 'SHIFT' du clavier)."),
	html.Br(),
	html.Br(),
	dcc.Link(html.Button("NEXT"), href="/pages/subjexp", refresh=True),
])