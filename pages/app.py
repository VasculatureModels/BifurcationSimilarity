import dash_vtk
import dash
from dash.dependencies import Input, Output
from dash import Dash, dcc, html, Input, Output, State, callback
import numpy as np
import sys
import webbrowser
import itk
import vtk
from dash_vtk.utils import to_volume_state
import flask

try:
	# VTK 9+
	from vtkmodules.vtkImagingCore import vtkRTAnalyticSource
except ImportError:
	# VTK =< 8
	from vtk.vtkImagingCore import vtkRTAnalyticSource


dash.register_page(__name__, path='/pages/app')


lines = []
# Read image playlist :
with open(r"playlist.txt", 'r') as fp:
	lines = fp.readlines()

NbImages = len(lines)

# Load vtk image (3D) :
volname = lines[0][:-1]

def loadVol(volname):
	itkImage = itk.imread(volname)
	vtkImage = itk.vtk_image_from_image(itkImage)
	vtkVol = to_volume_state(vtkImage)
	return(vtkVol)

vtkVol = loadVol(volname)



def build_vtk_representation(vtkVol, volname, _id):
	vtkVol = loadVol(volname)
	return dash_vtk.VolumeRepresentation(
		id=_id,
		children=[
			dash_vtk.VolumeController(),
			dash_vtk.Volume(state=vtkVol),
		]
	)

views = []
for i in range(NbImages):
	views.append(build_vtk_representation(vtkVol, lines[i][:-1], _id="bar"),)


#app = dash.Dash(__name__)
#server = app.server

Scores = []

layout = html.Div(
	style={"width": "100%", "height": "600px"},
	children=[
		dcc.Slider(1, 10, 1,
				value=0,
				id='my-slider'
		),
		html.Div(id='slider-output-container'),
		html.Br(),
		#dcc.Input(id='input-on-submit', type='text'),
		html.A(html.Button('NEXT', id='submit-val', n_clicks=0),href='/pages/app'),
		html.Br(),
		html.Div(id="output"),
		html.Br(),
		dash_vtk.View(id="vtk-view"),
	],
)


@callback(
	Output("vtk-view", "children"),
	#Output("vtk-view", "triggerRender"),
	Output('slider-output-container', 'children'),
	Input('my-slider', 'value'),
	Input('submit-val', 'n_clicks'),
	#State('input-on-submit', 'value'),
	#prevent_initial_call=True
)
def update_vtk_view(value, n_clicks):
	if value is None :
		return dash.no_update
	#if not n_clicks:
	#	return dash.no_update  

	idx = len(Scores)
	Done = 0

	#if n_clicks == 1:
	#	Scores = []

	#volname = lines[len(Scores)][:-1]

	#if idx > 0:
	volname = lines[len(Scores)][:-1]
	print("\nprocessing image : " + volname + "\tScore = " +str(value))
	#Scores.append(value)

	if len(Scores) == NbImages:
		with open(r'output.txt', 'w') as fp:
			for item in Scores:
				#fp.write("volname: %s\tScore:  %s\n" % {volname,item})
				fp.write('volname: {}; Score: {}\n'.format(item[0], item[1]))
		print('Done')
		Done=1
		sys.exit()

	Scores.append((volname, value))

	#else:
	#	volname = lines[len(Scores)][:-1]
	#	#Scores.append(0)
	#	Scores.append((volname, value))


	#print("{} {} {} {}\n".format(idx,volname, value, Scores))


	if Done == 1:
		#Scores = []
		return flask.redirect('/')
	else:
		return views[idx], 'Image "{}", Score "{}"'.format(volname, value)


