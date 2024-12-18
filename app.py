
import os
import pandas as pd
import numpy as np
import tensorflow as tf
from flask import Flask, request, render_template, send_from_directory
from tensorflow.keras.preprocessing import image
from keras.models import load_model

app = Flask(__name__)

Plants = ['Corn_(maize)___Cercospora_leaf_spot Gray_leaf_spot', 'Corn_(maize)___Common_rust_', 'Corn_(maize)___healthy', 'Corn_(maize)___Northern_Leaf_Blight', 'Potato___Early_blight', 'Potato___healthy', 'Potato___Late_blight', 'Tomato___Bacterial_spot', 'Tomato___healthy', 'Tomato___Late_blight', 'Tomato___Tomato_Yellow_Leaf_Curl_Virus']

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/upload/<filename>")
def send_image(filename):
    return send_from_directory("images",filename)

@app.route("/upload",methods=["POST","GET"])
def upload():
    if request.method=='POST':
        print("hdgkj")
        m = int(request.form["alg"])
        acc = pd.read_csv("C:\\Users\\HEMA SAI VENKAT\\Desktop\\project IV\\TK55671\\CODE\\Accuracy.csv")

        myfile = request.files['file']
        fn = myfile.filename
        mypath = os.path.join("images/", fn)
        myfile.save(mypath)

        print("{} is the file name", fn)
        print("Accept incoming file:", fn)
        print("Save it to:", mypath)

        if m == 1:
            print("bv1")
            new_model = load_model(r'models/SVC.h5')
            test_image = image.load_img(mypath, target_size=(128, 128))
            test_image = image.img_to_array(test_image)
            a = acc.iloc[m - 1, 1]

        elif m == 2:
            print("bv2")
            new_model = load_model(r'models/ANN.h5')
            test_image = image.load_img(mypath, target_size=(128, 128))
            test_image = image.img_to_array(test_image)
            a = acc.iloc[m - 1, 1]

        elif m == 3:
            print("bv2")
            new_model = load_model(r'models/CNN.h5')
            test_image = image.load_img(mypath, target_size=(128, 128))
            test_image = image.img_to_array(test_image)
            a = acc.iloc[m - 1, 1]

        else:
            print("bv3")
            new_model = load_model(r'models/ResNet50.h5')
            test_image = image.load_img(mypath, target_size=(128, 128))
            test_image = image.img_to_array(test_image)
            a = acc.iloc[m - 1, 1]
    
        test_image = np.expand_dims(test_image, axis=0)
        result = new_model.predict(test_image)
        preds = Plants[np.argmax(result)]
        
        if preds == "Corn_(maize)___Cercospora_leaf_spot Gray_leaf_spot":
            msg="Foliar fungicides can be used to manage gray leaf spot outbreaks"
            
        elif preds =="Corn_(maize)___Common_rust_":
            msg = "Use resistant varieties like DHM 103, Ganga Safed - 2 and avoid sowing of suceptable varieties like DHM 105"
            
        elif preds =="Corn_(maize)___healthy":
            msg = "Plant is Good no treatment required"
            
        elif preds == "Corn_(maize)___Northern_Leaf_Blight":
            msg = "Integration of early sowing, seed treatment and foliar spray with Tilt 25 EC (propiconazole) was the best combination in controlling maydis leaf blight and increasing maize yield"
            
        
        elif preds == "Potato___Early_blight":
            msg = "Mancozeb and chlorothalonil are perhaps the most frequently used protectant fungicides for early blight management"
        
        elif preds =="Potato___healthy":
            msg = "Plant is Good no treatment required"
       
        elif preds == "Potato___Late_blight":
            msg = "Effectively managed with prophylactic spray of mancozeb at 0.25% followed by cymoxanil+mancozeb or dimethomorph+mancozeb at 0.3% at the onset of disease and one more spray of mancozeb at 0.25% seven days"
        
        elif preds == "Tomato___Bacterial_spot":
            msg = "When possible, is the best way to avoid bacterial spot on tomato. Avoiding sprinkler irrigation and cull piles near greenhouse or field operations, and rotating with a nonhost crop also helps control the disease"
        
        elif preds =="Tomato___healthy":
            msg = "Plant is Good no treatment required"
        
        elif preds == "Tomato___Late_blight":
            msg = "Ungicides that contain maneb, mancozeb, chlorothanolil, or fixed copper can help protect plants from late tomato blight"
        
        else:
            msg = "Homemade Epsom salt mixture. Combine two tablespoons of Epsom salt with a gallon of water and spray the mixture on the plant"

        return render_template("template.html", text=preds,msg=msg ,image_name=fn,a=round(a*100,3))
    return render_template("upload.html")

if __name__ == '__main__':
    app.run(debug=True)


