import dash
from dash import html, dcc

dash.register_page(__name__, path='/pages/TheEnd')

layout = html.Div([
	html.Br(),
	html.Br(),
	html.H2("Merci pour votre participation !"),
	html.Br(),
	html.Div("Vous pouvez fermer cette fenêtre."),
	html.Br(),
	html.Br(),
	dcc.Link(html.Button("BACK"), href="/pages/home", refresh=True),
])