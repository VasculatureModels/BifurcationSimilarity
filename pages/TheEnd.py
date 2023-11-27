import dash
from dash import html, dcc

dash.register_page(__name__, path='/pages/TheEnd')

layout = html.Div([
	html.Br(),
	html.Br(),
	html.H1("Merci pour votre participation !"),
	html.Br(),
	html.Br(),
	#dcc.Link(html.Button("NEXT"), href="/pages/subjexp", refresh=True),
])