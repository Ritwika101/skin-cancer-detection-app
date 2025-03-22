from flask import Flask
from flask import request
from flask import render_template
import os
import sys
from PIL import Image
import numpy as np
#from scipy.misc import imsave, imread, imresize
#from keras.preprocessing import image
from keras.models import load_model

dic = {0:'Benign', 1:'Malignant'}

app = Flask(__name__)

model = load_model('./model/model.h5')
UPLOAD_FOLDER = "./static"



@app.route("/", methods=["GET", "POST"])
def get_output():
    if request.method == "POST":
        image_file=request.files["image"]
        if image_file:
            image_location=os.path.join(
                UPLOAD_FOLDER,
                image_file.filename
            )
            image_file.save(image_location)
            d = predict_label(image_location)
            return render_template("index.html",prediction=d, image_loc=image_location)
        
    return render_template("index.html",prediction=0, image_loc=None)

def predict_label(image_path):
    try:
        arr = Image.open(image_path,mode='r')
        arr = arr.resize((224,224))
        #arr = arr/255.0
        arr = np.reshape(arr,(1,224,224,3))
        r = model.predict(arr)
        print("The result is")
        print(r)
        result = np.argmax(r, axis=1)
        if result==0:
            return "The skin lesion is benign. It is not harmful. However if it's degrading your health, then consult with a doctor soon."
        elif result==1:
            return "The skin lesion is malignant. It is cancerous and can spread over. Consult with a nearby doctor at the earliest."
        else:
            return "Invalid file"
    except:
        print("ERROR IN PREDICT")
    
if __name__=="__main__":
    app.run(port=12000,deubg=True)

