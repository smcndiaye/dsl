from django.shortcuts import render,render_to_response
from django.core.files.storage import FileSystemStorage
from django.views.decorators.csrf import csrf_exempt
import numpy as np
import matplotlib.image as mpimg
from skimage.transform import  resize
import os
import tensorflow as tf
from django.http import HttpResponse,JsonResponse
import json
settings_dir = os.path.dirname(__file__)
PROJECT_ROOT = os.path.abspath(os.path.dirname(settings_dir))

#md = '/Users/mac/Documents/dragdrop/imclass/trnedmodel'
IMG_SIZE = 80
#LR = 1e-3
#EPOCHS = 100
#MODEL_NAME = 'Flowers-{}-{}-{}-epochs.model'.format(LR, 'alexnet',EPOCHS)
#model = alexnet(IMG_SIZE,IMG_SIZE, LR)
model =  tf.keras.models.load_model('64x2-CNN.model')
model._make_predict_function()
imdir  = 'medialoaded/'#'/Users/mac/Documents/personnal_web/mysite/medialoaded/'
@csrf_exempt

def simple_upload(request):
    if request.method == 'POST' and request.FILES['myfile']:
        myfile = request.FILES['myfile']
        #myfile = cv2.imread(myfile,cv2.IMREAD_GRAYSCALE)
        #myfile   = cv2.resize(myfile,(IMG_SIZE,IMG_SIZE))
        fs = FileSystemStorage(location="medialoaded")
        filename = fs.save(myfile.name, myfile)
        #img = cv2.imread(myfile.name,cv2.IMREAD_GRAYSCALE)
        #imres   = cv2.resize(img,(IMG_SIZE,IMG_SIZE))
        #imdir+'/'+ filename
        uploaded_file_url = fs.url(filename)
        img = im_data = mpimg.imread(imdir+'/'+ filename)
        image_resized = resize(im_data, (80,80,1),
                       anti_aliasing=True)
        im   = np.array(image_resized)#.reshape(IMG_SIZE, IMG_SIZE)
        im = im.reshape(-1,IMG_SIZE,IMG_SIZE,1)


        results = model.predict([im])[0]
        print(results)
        context = [round(results[0]*100),round(results[1]*100),round(results[2]*100),round(results[3]*100),round(results[4]*100)]
        return render(request, 'rpd/home.html',{'results': context})
    return render(request, 'rpd/home.html')


