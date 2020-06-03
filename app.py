import dash
from dash.dependencies import Input, Output, State, ClientsideFunction
import dash_html_components as html
import dash_core_components as dcc
import skimage.io
import base64
import io
import io_utils

app=dash.Dash(__name__)

app.layout=html.Div(
    id='main',
    children=[
        dcc.Upload(
        id='uploader',
        children=html.Button('Load Image'),
        multiple=False),
        html.A(
        id='downloader',
        download='image.png',
        children=[html.Button('Save Image')]),
		dcc.Slider(
			id='rotation-slider',
			min=0,
			max=360,
			step=0.5,
			value=0,
		),
        dcc.Store(id='input-image',data={}),
        dcc.Store(id='output-image',data={})

    ]
)

@app.callback(
Output('input-image','data'),
[Input('uploader','contents')])
def store_uploader_contents(uploader_contents):
    if uploader_contents is None:
        return dash.no_update
    return {'img':uploader_contents}

@app.callback(
Output('output-image','data'),
[Input('input-image','data'),
 Input('rotation-slider','value')])
    imdata=uploader_contents.split(",")[-1]
    im=io_utils.img_from_b64(imdata)
    # process the image here...
    # write the image
	imb64=io_utils.b64_from_img(im)
	return {'img':imb64}

if __name__ == "__main__":
    app.run_server(debug=True)
