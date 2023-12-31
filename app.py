import dash
from dash import Dash, html, dcc

app = Dash(__name__, use_pages=True, server=True)

server = app.server

app.layout = html.Div([
    html.H1("Evaluation of Bifurcation similarity"),
    #html.Div([
    #    html.Div(
    #        dcc.Link(f"{page['name']} - {page['path']}", href=page["relative_path"])
    #    ) for page in dash.page_registry.values()
    #]),
    dash.page_container
])

if __name__ == '__main__':
    app.run_server(debug=True, port=8050, host="127.0.0.1")