import skimage.io
import io
import base64

def img_from_b64(b64str):
    imdata=base64.b64decode(b64str)
    im=skimage.io.imread(io.BytesIO(imdata))

def b64_from_img(img,format_str='png'):
    bio=io.BytesIO()
    # use 'pil' plugin because it supports writing image files to memory
    skimage.io.imsave(bio,img,plugin='pil',format_str=format_str)
    b64str=base64.b64encode(bio.getvalue()).decode()
