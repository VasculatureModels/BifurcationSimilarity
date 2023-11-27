import dash
from dash.dependencies import Input, Output
from dash.exceptions import PreventUpdate
from dash import Dash, dcc, html, Input, Output, State, callback, ctx
import numpy as np
import os, sys
import webbrowser
import itk
import vtk
from dash_vtk.utils import to_volume_state
import dash_vtk
import flask
import random
from datetime import datetime, date


try:
	# VTK 9+
	from vtkmodules.vtkImagingCore import vtkRTAnalyticSource
except ImportError:
	# VTK =< 8
	from vtk.vtkImagingCore import vtkRTAnalyticSource


dash.register_page(__name__, path='/pages/subjexp')



lines = []
# Read image playlist :
with open(r"playlist.txt", 'r') as fp:
	lines = fp.readlines()

NbImages = len(lines)

NbAnchors = 5
Anchoring = lines[0:NbAnchors]

# Randomize Playlist :
Random_PL = lines[NbAnchors:NbImages]
random.shuffle(Random_PL)

FinalPlaylist = lines.copy()
FinalPlaylist[0:NbAnchors] = Anchoring
FinalPlaylist[NbAnchors:NbImages] = Random_PL

#FinalPlaylist = lines

# Load vtk image (3D) :
volname = FinalPlaylist[0][:-1]

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
			dash_vtk.ImageData(
				dimensions=[64, 64, 128],
				spacing=[1, 1, 1],
				origin=[0, 0, 0],
				children=dash_vtk.PointData(
					dash_vtk.Volume(state=vtkVol)
				),
			),
		]
	)

views = []
for i in range(NbImages):
	views.append(build_vtk_representation(vtkVol, FinalPlaylist[i][:-1], _id="foo"),)


Scores = []

layout = html.Div(
	style={"width": "100%", "height": "600px"},
	children=[
		html.A(html.Button(' 1 ', id='val1', n_clicks=0,   style={'font-size': '24px', 'width': '80px', 'margin-bottom': '20px', 'margin-right': '15px', 'height':'42px'})),
		html.A(html.Button(' 2 ', id='val2', n_clicks=0,   style={'font-size': '24px', 'width': '80px', 'margin-bottom': '20px', 'margin-right': '15px', 'height':'42px'})),
		html.A(html.Button(' 3 ', id='val3', n_clicks=0,   style={'font-size': '24px', 'width': '80px', 'margin-bottom': '20px', 'margin-right': '15px', 'height':'42px'})),
		html.A(html.Button(' 4 ', id='val4', n_clicks=0,   style={'font-size': '24px', 'width': '80px', 'margin-bottom': '20px', 'margin-right': '15px', 'height':'42px'})),
		html.A(html.Button(' 5 ', id='val5', n_clicks=0,   style={'font-size': '24px', 'width': '80px', 'margin-bottom': '20px', 'margin-right': '15px', 'height':'42px'})),
		html.A(html.Button(' 6 ', id='val6', n_clicks=0,   style={'font-size': '24px', 'width': '80px', 'margin-bottom': '20px', 'margin-right': '15px', 'height':'42px'})),
		html.A(html.Button(' 7 ', id='val7', n_clicks=0,   style={'font-size': '24px', 'width': '80px', 'margin-bottom': '20px', 'margin-right': '15px', 'height':'42px'})),
		html.A(html.Button(' 8 ', id='val8', n_clicks=0,   style={'font-size': '24px', 'width': '80px', 'margin-bottom': '20px', 'margin-right': '15px', 'height':'42px'})),
		html.A(html.Button(' 9 ', id='val9', n_clicks=0,   style={'font-size': '24px', 'width': '80px', 'margin-bottom': '20px', 'margin-right': '15px', 'height':'42px'})),
		html.A(html.Button(' 10 ', id='val10', n_clicks=0, style={'font-size': '24px', 'width': '80px', 'margin-bottom': '20px', 'margin-right': '15px', 'height':'42px'})),
		html.Br(),
		html.Br(),
		html.Div(id="output"),
		html.Br(),
		dash_vtk.View(id="vtk-view"),
	],
)


@callback(
	Output("vtk-view", "children"),
	Input('val1', 'n_clicks'),
	Input('val2', 'n_clicks'),
	Input('val3', 'n_clicks'),
	Input('val4', 'n_clicks'),
	Input('val5', 'n_clicks'),
	Input('val6', 'n_clicks'),
	Input('val7', 'n_clicks'),
	Input('val8', 'n_clicks'),
	Input('val9', 'n_clicks'),
	Input('val10', 'n_clicks'),
	prevent_initial_call=False

)
def update_vtk_view(btn1, btn2, btn3, btn4, btn5, btn6, btn7, btn8, btn9, btn10):
	#if (btn1 is None) and (btn2 is None) and (btn3 is None) and (btn4 is None) and (btn5 is None) and (btn6 is None) and (btn7 is None) and (btn8 is None) and (btn9 is None) and (btn10 is None):
	#	return dash.no_update
	#else:
	Done = 0
	idx = 0
	volname = ''
	Val = 0
	if "val1" == ctx.triggered_id:
		Val = 1
		idx = len(Scores)
		volname = FinalPlaylist[idx][:-1]
		Scores.append((volname, '1'))

	elif "val2" == ctx.triggered_id:
		Val = 2
		idx = len(Scores)
		volname = FinalPlaylist[idx][:-1]
		Scores.append((volname, '2'))

	elif "val3" == ctx.triggered_id:
		Val = 3
		idx = len(Scores)
		volname = FinalPlaylist[idx][:-1]
		Scores.append((volname, '3'))

	elif "val4" == ctx.triggered_id:
		Val = 4
		idx = len(Scores)
		volname = FinalPlaylist[idx][:-1]
		Scores.append((volname, '4'))

	elif "val5" == ctx.triggered_id:
		Val = 5
		idx = len(Scores)
		volname = FinalPlaylist[idx][:-1]
		Scores.append((volname, '5'))

	elif "val6" == ctx.triggered_id:
		Val = 6
		idx = len(Scores)
		volname = FinalPlaylist[idx][:-1]
		Scores.append((volname, '6'))

	elif "val7" == ctx.triggered_id:
		Val = 7
		idx = len(Scores)
		volname = FinalPlaylist[idx][:-1]
		Scores.append((volname, '7'))

	elif "val8" == ctx.triggered_id:
		Val = 8
		idx = len(Scores)
		volname = FinalPlaylist[idx][:-1]
		Scores.append((volname, '8'))

	elif "val9" == ctx.triggered_id:
		Val = 9
		idx = len(Scores)
		volname = FinalPlaylist[idx][:-1]
		Scores.append((volname, '9'))

	elif "val10" == ctx.triggered_id:
		Val = 10
		idx = len(Scores)
		volname = FinalPlaylist[idx][:-1]
		Scores.append((volname, '10'))

	print("{} {} {} {}\n".format(idx, volname, Val, Scores))

	if len(Scores) == NbImages:
		now = datetime.now()
		current_time = now.strftime("%H:%M:%S")
		today = date.today()
		if os.path.exists('./outputs/') == False:
			os.makedirs("outputs/")
			os.chmod("outputs/", 0o755)

		with open(r'./outputs/output_' + str(today) + '_' + current_time + '.txt', 'w') as fp:
			for item in Scores:
				fp.write('volname: {}; Score: {}\n'.format(item[0], item[1]))
		print('Done')
		Done = 1
		idx = 0
		volname = ''
		Val = 0
		#Scores = []
		#dcc.Location(pathname="/pages/TheEnd", id="backhome")
		#sys.exit()

	if Done == 1:
		idx = 0
		volname = ''
		Val = 0
		#Scores = []
		return dcc.Location(pathname="/pages/TheEnd", id="backhome")
	else:
		#if idx == 0:
		#	Scores.append(('start',0))
		return views[idx]

