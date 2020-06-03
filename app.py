import dash
from dash.dependencies import Input, Output, State, ClientsideFunction
import dash_html_components as html
import dash_core_components as dcc
import skimage.io
import base64
import io

app=dash.Dash(__name__)

app.layout=html.Div(id='main',
    children=[
        dcc.Upload(
        id='uploader',
        children=html.Button('Load Image'),
        multiple=False),
        html.Div(id='dummy')
    ]
)

@app.callback(
Output('dummy','children'),
[Input('uploader','contents')])
def print_uploader_contents(uploader_contents):
    if uploader_contents is None:
        return dash.no_update
    imdata=base64.b64decode(uploader_contents.split(",")[-1])
    im=skimage.io.imread(io.BytesIO(imdata))
    # process the image here...
    # write the image
    bio=io.BytesIO()
    print('im.dtype',im.dtype)
    # use 'pil' plugin because it supports writing image files to memory
    skimage.io.imsave(bio,im,plugin='pil',format_str='png')
    with open('/tmp/img.png','wb') as fd:
        fd.write(bio.getvalue())

if __name__ == "__main__":
    app.run_server(debug=True)
