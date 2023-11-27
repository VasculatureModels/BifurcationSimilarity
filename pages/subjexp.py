import dash
from dash.dependencies import Input, Output
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

Anchoring = lines[0:3]

# Randomize Playlist :
Random_PL = lines[3:NbImages]
random.shuffle(Random_PL)

FinalPlaylist = lines.copy()
FinalPlaylist[0:3] = Anchoring
FinalPlaylist[3:NbImages] = Random_PL

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
	#cameraPosition=[1, 0, 0],
	#cameraViewUp=[0, 0, -1],
	#cameraParallelProjection=False,

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
			#dash_vtk.Volume(state=vtkVol),
		]
	)

views = []
for i in range(NbImages):
	views.append(build_vtk_representation(vtkVol, FinalPlaylist[i][:-1], _id="bar"),)


Scores = []

layout = html.Div(
	style={"width": "100%", "height": "600px"},
	children=[
		#dcc.Slider(1, 10, 1,
		#		value=0,
		#		id='my-slider'
		#),
		#html.Div(id='slider-output-container'),
		#html.Label('Dropdown'),
		#dcc.Dropdown(['1', '2', '3', '4', '5', '6', '7', '8', '9', '10'], '1'),
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
		#dcc.Input(id='input-on-submit', type='text'),
		#html.A(html.Button('NEXT', id='submit-val', n_clicks=0)),
		html.Br(),
		html.Div(id="output"),
		html.Br(),
		dash_vtk.View(id="vtk-view"),
	],
)


@callback(
	Output("vtk-view", "children"),
	#Output('slider-output-container', 'children'),
	#Output("vtk-view", "triggerRender"),
	#Output('my-slider', 'value'),
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
	#Input('submit-val', 'n_clicks'),
	#State('my-slider', 'value'),
	#State('input-on-submit', 'value'),
	prevent_initial_call=False

)
def update_vtk_view(btn1, btn2, btn3, btn4, btn5, btn6, btn7, btn8, btn9, btn10):
	#msg = "Select a score in [1,10]"
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

	#print(Scores)
	#print("{} {} {} {}\n".format(idx, volname, Val, Scores))
	
	if len(Scores) == NbImages:
		now = datetime.now()
		current_time = now.strftime("%H:%M:%S")
		today = date.today()
		if os.path.exists('./outputs/') == False:
			os.makedirs("outputs/")
			os.chmod("outputs/", 0o755)

		with open(r'./outputs/output_' + str(today) + '_' + current_time + '.txt', 'w') as fp:
			for item in Scores:
				#fp.write("volname: %s\tScore:  %s\n" % {volname,item})
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
		#return flask.redirect('/pages/TheEnd')
		return dcc.Location(pathname="/pages/TheEnd", id="backhome")
	else:
		return views[idx], 'Image "{}", Score "{}"'.format(volname, Val)

