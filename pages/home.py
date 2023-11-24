import dash
from dash import html, dcc

#dash.register_page(__name__, path='/')
dash.register_page(__name__, path='/pages/home')

layout = html.Div([
	#html.H1('Test subjectif de mesure de similarités entre bifurcations'),
	html.Br(),
	html.Br(),
	html.Div("L'objectif de ce test est d'évaluer les similarités entre des bifurcatsion cérébrales"),
	html.Div("Deux bifurcations seront présentées dans un display 3D, "),
	html.Div("l'une est une originale (acquise depuis une MRA-TOF)"),
	html.Div("l'autre est le fruit d'un modèle synthétique."),
	html.Br(),
	html.Div("Une barre de défilement positionnée en haut de la page sert à évaluer les similarités."),
	html.Br(),
	html.Br(),
	#html.A(html.Button('NEXT', id='submit-val', n_clicks=0),href='/pages/app', refresh=True),
	dcc.Link(html.Button("NEXT"), href="/app_slider", refresh=True),
])