from distutils.command.upload import upload

import cv2
import numpy as np
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from django.shortcuts import render
from keras.applications import vgg16
from keras.models import load_model
import base64


from PIL import Image , ImageTk 
from tensorflow.keras.optimizers import Adam

#from keras.optimizers import Adam
from keras.applications.imagenet_utils import decode_predictions
from keras.preprocessing.image import img_to_array, load_img
from tensorflow.python.keras.backend import set_session
global up
up=""
def nutrition_table(request):
    return render(request,'nutritions.html')
def home(request):
    return render(request,'home.html')
# def home(request):
#         return render(request,'home.html')
def nutritions(request):
    if request.method == 'POST' and request.FILES['upload']:
        upload = request.FILES['upload']
        up=upload
        fn = up
        print("uploaded:",up)
        
    
        fss = FileSystemStorage()
        file = fss.save(upload.name, upload)
        print("save ", file)
        file_url = fss.url(file)
        print("url:",file_url)
       
        imgpath = up
        
        fn = up
        IMAGE_SIZE = 64
        LEARN_RATE = 1.0e-4
        CH=3
        print(fn)
        if fn!="":
        
       
            # model = load_model('C:/Users/admin/Downloads/YT_Django_TensorFlow_Image_Classification_Basic-main/YT_Django_TensorFlow_Image_Classification_Basic-main/YT_Django_TensorFlow_Image_Classification_Basic-main/model/fruit_model.h5')
            # model = load_model('C:\\Users\\ASUS\\Desktop\\fruit image classification\\fruit detection django\\fruit detection django\\model\\fruit_model.h5')
            # model = load_model('C:\\Users\\ASUS\\Desktop\\fruit image classification\\fruit detection django\\fruit detection django\\model\\notrition.h5')
            # C:\Users\ASUS\Desktop\fruit image classification\fruit detection django\fruit detection django\model\.h5
            # model = load_model('C:\\Users\\ASUS\\Desktop\\fruit image classification\\fruit detection django\\fruit detection django\\model\\fresh_fruit.h5')
            model = load_model('C:\\Users\\ASUS\\Desktop\\fruit image classification\\fruit detection django_final\\model\\fruit_model.h5')
            

            img = Image.open(fn)
            g1= Image.open(fn).convert('L')
            g1.save('greyscale_chameleon.jpeg')
            #
            
            img = Image.open(fn)
            img = img.resize((IMAGE_SIZE,IMAGE_SIZE))
            img = np.array(img)
        
            img = img.reshape(1,IMAGE_SIZE,IMAGE_SIZE,3)
        
            img = img.astype('float32')
            img = img / 255.0
            print('img shape:',img)
            prediction = model.predict(img)
            print(np.argmax(prediction))
            fruit=np.argmax(prediction)
            print(fruit)
        

            if fruit == 0:
                Cd="Fresh  apple"
            elif fruit == 1:
                Cd = 'Fresh lemon'
            elif fruit == 2:
                Cd = 'Fresh Lulo'
            elif fruit == 3:    
                Cd = 'Fresh mango'
            elif fruit == 4:
                Cd = 'fresh Orange'
            elif fruit == 5:
                Cd = 'Fresh Strawberry'
            elif fruit == 6:
                Cd = 'Fresh Tamarillo'
            elif fruit == 7:
                Cd = 'Fresh Tomato'
            elif fruit == 8:
                Cd = 'Rotten apple'
            elif fruit == 9:
                Cd = 'Rotten Lemon'
            elif fruit == 10:
                Cd = 'Rotten apple'
            elif fruit == 11:
                Cd = 'Rotten Mango'
            elif fruit == 12:
                Cd = 'rotten Orange'
            elif fruit == 13:
                Cd = 'Rotten Strawberry'
            elif fruit == 14:
                Cd = 'Rotten Tamarillo'
            elif fruit == 15:
                Cd = 'Rotten apple'
            elif fruit == 16 :
                Cd = 'fresh banana'
            A=Cd
            print(A)          
            return render(request, "index1.html", {"predictions": A,'file_url': file_url})  
            
        
        return render(request, "index1.html")
    
    else:
    
        return render(request, "index1.html")     
        #return render(request, 'index.html', {'file_url': file_url})
    #return render(request, 'index.html') 



        # return render(request,'nutritions.html')
        
def index(request):
    if request.method == 'POST' and request.FILES['upload']:
        upload = request.FILES['upload']
        up=upload
        fn = up
        print("uploaded:",up)
        
    
        fss = FileSystemStorage()
        file = fss.save(upload.name, upload)
        print("save ", file)
        file_url = fss.url(file)
        print("url:",file_url)
        #binary_image = base64.b64encode(upload.read())
        #gray= Image.open(up)
        #img1 = gray.resize((IMAGE_SIZE,IMAGE_SIZE)).convert('L')
        
        #gray = cv2.cvtColor(up, cv2.COLOR_BGR2GRAY)
       
        imgpath = up
        
        fn = up
        IMAGE_SIZE = 100
        LEARN_RATE = 1.0e-4
        CH=3
        print(fn)
        if fn!="":
        
       
            # model = load_model('C:/Users/admin/Downloads/YT_Django_TensorFlow_Image_Classification_Basic-main/YT_Django_TensorFlow_Image_Classification_Basic-main/YT_Django_TensorFlow_Image_Classification_Basic-main/model/fruit_model.h5')
            # model = load_model('C:\\Users\\ASUS\\Desktop\\fruit image classification\\fruit detection django\\fruit detection django\\model\\fruit_model.h5')
            # model = load_model('C:\\Users\\ASUS\\Desktop\\fruit image classification\\fruit detection django\\fruit detection django\\model\\cnn_model.h5')
            model = load_model('C:\\Users\\ASUS\\Desktop\\fruit image classification\\fruit detection django_final\\model\cnn_model.h5')
            img = Image.open(fn)
            g1= Image.open(fn).convert('L')
            g1.save('greyscale_chameleon.jpeg')
            #
            
            img = Image.open(fn)
            img = img.resize((IMAGE_SIZE,IMAGE_SIZE))
            img = np.array(img)
        
            img = img.reshape(1,IMAGE_SIZE,IMAGE_SIZE,3)
        
            img = img.astype('float32')
            img = img / 255.0
            print('img shape:',img)
            prediction = model.predict(img)
            print(np.argmax(prediction))
            fruit=np.argmax(prediction)
            print(fruit)
            
            if fruit == 0:
                Cd="Apple Braeburn \n Total Fat 0.2g  \n Cholesterol 0mg \n Sodium 1.1mg \n Tot. Carb. 14.9g"
            elif fruit == 1:
                Cd = 'Apple Crimson Snow \n Total Fat 0.4g  \n Cholesterol 0mg \n Sodium 1.0mg \n Tot. Carb. 11.9g'
            elif fruit == 2:
                Cd = 'Apple Braeburn \n Total Fat 0.2g  \n Cholesterol 0mg \n Sodium 1.1mg \n Tot. Carb. 14.9g'
            elif fruit == 3:    
                Cd = 'Apple Braeburn \n Total Fat 0.2g  \n Cholesterol 0mg \n Sodium 1.1mg \n Tot. Carb. 14.9g'
            elif fruit == 4:
                Cd = 'Apple Braeburn \n Total Fat 0.2g  \n Cholesterol 0mg \n Sodium 1.1mg \n Tot. Carb. 14.9g'
            elif fruit == 5:
                Cd = 'Apple Braeburn \n Total Fat 0.2g  \n Cholesterol 0mg \n Sodium 1.1mg \n Tot. Carb. 14.9g'
            elif fruit == 6:
                Cd = 'Apple Braeburn \n Total Fat 0.2g  \n Cholesterol 0mg \n Sodium 1.1mg \n Tot. Carb. 14.9g'
            elif fruit == 7:
                Cd = 'Apple Braeburn \n Total Fat 0.2g  \n Cholesterol 0mg \n Sodium 1.1mg \n Tot. Carb. 14.9g'
            elif fruit == 8:
                Cd = 'Apple Braeburn \n Total Fat 0.2g  \n Cholesterol 0mg \n Sodium 1.1mg \n Tot. Carb. 14.9g'
            elif fruit == 9:
                Cd = 'Apple Braeburn \n Total Fat 0.2g  \n Cholesterol 0mg \n Sodium 1.1mg \n Tot. Carb. 14.9g'
            elif fruit == 10:
                Cd = 'Apple Braeburn \n Total Fat 0.2g  \n Cholesterol 0mg \n Sodium 1.1mg \n Tot. Carb. 14.9g'
            elif fruit == 11:
                Cd = 'Apple Braeburn \n Total Fat 0.2g  \n Cholesterol 0mg \n Sodium 1.1mg \n Tot. Carb. 14.9g'
            elif fruit == 12:
                Cd = 'Apple Braeburn \n Total Fat 0.2g  \n Cholesterol 0mg \n Sodium 1.1mg \n Tot. Carb. 14.9g'
            elif fruit == 13:
                Cd = 'Apricot \n Total Fat 0.4 g \n Cholesterol 0 mg \n Sodium 1 mg \n Total Carbohydrate 11 g'
            elif fruit == 14:
                Cd = 'Avocado  \n Total Fat 15 g \n Cholesterol 0 mg \n Sodium 7 mg \n Total Carbohydrate 9 g'
            elif fruit == 15:
                Cd = 'Avocado ripe \n Total Fat 15 g \n Cholesterol 0 mg \n Sodium 7 mg \n Total Carbohydrate 9 g'
            elif fruit == 16:
                Cd = 'Banana \n Total Fat 0.3 g \n Cholesterol 0 mg \n Sodium 1 mg \n Total Carbohydrate 23 g'
            elif fruit == 17:
                Cd = 'Banana \n Total Fat 0.3 g \n Cholesterol 0 mg \n Sodium 1 mg \n Total Carbohydrate 23 g'
            elif fruit == 18:
                Cd = 'Banana Red \n Fat: 0.3 grams \n Calories: 90 calories \n Sodium 1 mg \n Carbs: 21 grams'
            elif fruit == 19:
                Cd = 'Beet Root \n Calories: 43 \n Water: 88%  \n Protein: \n  1.6 grams.\n Carbs: 9.6 grams.\n Sugar: 6.8 grams.\n Fiber: 2.8 grams.\n Fat: 0.2 grams.'
            elif fruit == 20:
                Cd = 'Blue Berry \n  Calories: 42.\n Protein: 1 gram. \n  Fat: Less than 1 gram.\n Carbohydrates: 11 grams. \n Fiber: 2 grams. \n Sugar: 7 grams'
            elif fruit == 21:
                Cd = 'Cactus fruit \n Total Fat 0.5 g \n Cholesterol 0 mg \n Sodium 5 mg \n Total Carbohydrate 10 g'
            elif fruit == 22:
                Cd = 'Cantaloupe \n Total Fat 0.2 g \n Cholesterol 0 mg \n Sodium 16 mg \n Total Carbohydrate 8 g'
            elif fruit == 23:
                Cd = 'Cantaloupe \n Total Fat 0.2 g \n Cholesterol 0 mg \n Sodium 16 mg \n Total Carbohydrate 8 g'
            elif fruit == 24:
                Cd = 'Carambula \n Total Fat 0.3 g \n Cholesterol 0 mg \n Sodium 2 mg \n Total Carbohydrate 7 g'
            elif fruit == 25:
                Cd = 'Cauliflower \n 25 calories. \n 0 grams of fat. \n 5 grams of carbohydrates.\n 2 grams of dietary fiber. \n 2 grams of sugar. \n 2 grams of protein. \n 30 milligrams of sodium.'
            elif fruit == 26:
                Cd = "Cherry Calories: 97. \n Protein: 2 grams. \n Carbs: 25 grams. \n Fiber: 3 grams.\n Vitamin C: 18%  of the. Daily Value (DV) \n Potassium: 10% of the DV. \n Copper: 5% of the DV. \n Manganese: 5% of the DV."
            elif fruit == 27:
                Cd = "Cherry  Red \n Calories:97. \n Protein: 2 grams. \n Carbs: 25 grams. \n Fiber: 3 grams.\n Vitamin C: 18%  of the. Daily Value (DV) \n Potassium: 10% of the DV. \n Copper: 5% of the DV. \n Manganese: 5% of the DV."
            elif fruit == 28:
                Cd = "Cherry Calories: 97. \n Protein: 2 grams. \n Carbs: 25 grams. \n Fiber: 3 grams.\n Vitamin C: 18%  of the. Daily Value (DV) \n Potassium: 10% of the DV. \n Copper: 5% of the DV. \n Manganese: 5% of the DV."
            elif fruit == 29:
                Cd = "Cherry Calories: 97. \n Protein: 2 grams. \n Carbs: 25 grams. \n Fiber: 3 grams.\n Vitamin C: 18%  of the. Daily Value (DV) \n Potassium: 10% of the DV. \n Copper: 5% of the DV. \n Manganese: 5% of the DV."
            elif fruit == 30:
                Cd = "Cherry Calories: 97. \n Protein: 2 grams. \n Carbs: 25 grams. \n Fiber: 3 grams.\n Vitamin C: 18%  of the. Daily Value (DV) \n Potassium: 10% of the DV. \n Copper: 5% of the DV. \n Manganese: 5% of the DV."
            elif fruit == 31:
                Cd = "Cherry Calories: 97. \n Protein: 2 grams. \n Carbs: 25 grams. \n Fiber: 3 grams.\n Vitamin C: 18%  of the. Daily Value (DV) \n Potassium: 10% of the DV. \n Copper: 5% of the DV. \n Manganese: 5% of the DV."
            elif fruit == 32:
                Cd = 'Chestnut \n Calories: 77. \n Protein: 1 gram. \n Fat: 1 gram.\n Carbohydrates: 17 grams. \n Fiber: 3 grams. \n Sugar: 0 grams. \n Cholesterol: 0 milligrams. \n Sodium: 1 milligram'
            elif fruit == 33:
                Cd = 'clementine \n  Calories: 35 \n Protein: 1 gram \n Fat: 0 grams \n Carbs: 9 grams \n Fiber: 1 gram'
            elif fruit == 34:
                Cd = 'cocos \n Protein	3 grams	 \n Carbs	15 grams \n Fiber	9 grams	 \n Fat	33 grams'
            elif fruit == 35:
                Cd = 'Corn \n Calories: 90. \n  Protein: 3 grams (g) \n  Fat: 1 g.\n  Carbohydrates: 19 g.'
            elif fruit == 36:
                Cd = 'Corn \n Calories: 90.\n  Protein: 3 grams (g) \n  Fat: 1 g. \n Carbohydrates: 19 g.'
            elif fruit == 37:
                Cd = 'Cucumber Calories: 30 \n  Total fat: 0 grams. \n Carbs: 6 grams. \n Protein: 3 grams. \n Fiber: 2 grams.'
            elif fruit == 38:
                Cd = 'Cucumber Calories: 30 \n  Total fat: 0 grams. \n Carbs: 6 grams. \n Protein: 3 grams. \n Fiber: 2 grams.'
            elif fruit == 39:
                Cd = 'Dates calories: 20. \n total fat: 0.03 grams (g) \n total carbohydrates: 5.33 g. \n dietary fiber: 0.6 g. \n sugar: 4.5 g. \n protein: 0.17 g.'
            elif fruit == 40:
                Cd = 'Eggplant \n Calories: 20. \n Carbs: 5 grams. \n Fiber: 3 grams. \nProtein: 1 gram.'
            elif fruit == 41:
                Cd = 'Fig \n Calories: 37. Fat: 0 grams. \n Cholesterol: 0 milligrams. \n Sodium: 1 milligram. \n Carbohydrates: 10 grams.\n Fiber: 1 gram. \n Sugar: 8 grams. \n Protein: 0 grams.'
            elif fruit == 42:
                Cd = 'Ginger root \n 4.8 calories  \n 1.07 grams (g) of carbohydrate \n .12 g of dietary fiber \n .11 g of protein \n .05 g fat \n .1 g of sugar'
            elif fruit == 43:
                Cd = 'Granadilla \n 55.2g total carbs, \n 30.6g net carbs \n 1.7g fat \n 5.2g protein \n 229 calories. \n Net Carbs. 30.6 g'
            elif fruit == 44:
                Cd = 'Grape Blue \n 104 kilocalories. \n 1.09 g of protein. \n 0.24 g of fat. \n 27.33 g of carbohydrate \n 23.37 g is sugars.'
            elif fruit == 45:
                Cd = 'Grape Pink \n 104 kilocalories. \n 1.09 g of protein. \n 0.24 g of fat. \n 27.33 g of carbohydrate \n 23.37 g is sugars. '
            elif fruit == 46:
                Cd = 'Grape White \n 104 kilocalories. \n 1.09 g of protein. \n 0.24 g of fat. \n 27.33 g of carbohydrate \n 23.37 g is sugars.'
            elif fruit == 47:
                Cd = 'Grape White 2 \n 104 kilocalories. \n 1.09 g of protein. \n 0.24 g of fat. \n 27.33 g of carbohydrate \n 23.37 g is sugars.'
            elif fruit == 48:
                Cd = 'Grape White 3 \n 104 kilocalories. \n 1.09 g of protein. \n 0.24 g of fat. \n 27.33 g of carbohydrate \n 23.37 g is sugars.'
            elif fruit == 49:
                Cd = 'Grape White 4 \n 104 kilocalories. \n 1.09 g of protein. \n 0.24 g of fat. \n 27.33 g of carbohydrate \n 23.37 g is sugars.'
            elif fruit == 50:
                Cd = 'Grapefruit Pink \n 104 kilocalories. \n 1.09 g of protein. \n 0.24 g of fat. \n 27.33 g of carbohydrate \n 23.37 g is sugars.'
            elif fruit == 51:
                Cd = 'Grapefruit White \n 104 kilocalories. \n 1.09 g of protein. \n 0.24 g of fat. \n 27.33 g of carbohydrate \n 23.37 g is sugars.'
            elif fruit == 52:
                Cd = 'Guava \n Calories: 37. \n Fat: 1 gram. \n Sodium: 1 milligram. \n Carbohydrates: 8 grams. \n Fiber: 3 grams. \n Protein:1 gram.'
            elif fruit == 53:
                Cd = 'Hazelnut \n Calories: 178 \n Fat: 17g \n Sodium: 0mg \n Carbohydrates: 4.7g \n Fiber: 2.8g  \n Sugars: 1.2g \n Protein: 4.2g'
            elif fruit == 54:
                Cd = 'Huckleberry \n Sodium 10 mg \n Total Carbohydrate 9 g \n Protein 0.4 g \n Vitamin A,\n 1% Vitamin C \n Calcium 1%'
            elif fruit == 55:
                Cd = 'Kaki \n Calories: 118 \n Protein: 1 gram \n Fat: 0 grams \n Carbohydrates: 31 grams \n Fiber: 6 grams \n Sugars: 21 grams'
            elif fruit == 56:
                Cd = 'Kiwi \n Energy (calories) \n Carbohydrates (g) 10.1 \n 6.2 g of sugar'
            elif fruit == 57:
                Cd = 'Kohlrabi \n Calories: 36 \n Protein: 2 grams \n Fat: 0 grams \n Carbohydrates: 8 grams \n Fiber: 5 grams \n Sugar: 4 grams'
            elif fruit == 58:
                Cd = 'Kumquats \n Calories: 71 \n Carbs: 16 grams \n Protein: 2 grams \n Fat: 1 gram \n Fiber: 6.5 grams '
            elif fruit == 59:
                Cd = 'Lemon \n 16.8 calories (kcal) \n carbohydrates: 5.41 g \n 1.45 g sugars \n calcium 15.1 milligrams (mg) \n iron: 0.35 mg \n magnesium: 4.6 mg'
            elif fruit == 60:
                Cd = 'Lemon Meyer \n 16.8 calories (kcal) \n carbohydrates: 5.41 g \n 1.45 g sugars \n calcium 15.1 milligrams (mg) \n iron: 0.35 mg \n magnesium: 4.6 mg'
            elif fruit == 61:
                Cd = 'Limes \n 16.8 calories (kcal) \n carbohydrates: 5.41 g \n 1.45 g sugars \n calcium 15.1 milligrams (mg) \n iron: 0.35 mg \n magnesium: 4.6 mg'
            elif fruit == 62:
                Cd = 'Lychee \n Calories: 66 \n Protein: 0.8 grams \n Carbs: 16.5 grams \n Sugar: 15.2 grams \n Fiber: 1.3 grams \n Fat: 0.4 grams'
            elif fruit == 63:
                Cd = 'Mandarine \n calories: 46.6. \n carbohydrate: 11.7 g. \n total sugars: 9.33 g '
            elif fruit == 64:
                Cd = 'Mango \n Calories: 99 \n Protein: 1.4 grams \n Carbs: 24.7 grams \n Fat: 0.6 grams \n Fiber: 2.6 grams \n Sugar: 22.5 grams '
            elif fruit == 65:
                Cd = 'Mango Red \n Calories: 99 \n Protein: 1.4 grams \n Carbs: 24.7 grams \n Fat: 0.6 grams \n Fiber: 2.6 grams \n Sugar: 22.5 grams '
            elif fruit == 66:
                Cd = 'Mangostan \n Calories: 99 \n Protein: 1.4 grams \n Carbs: 24.7 grams \n Fat: 0.6 grams \n Fiber: 2.6 grams \n Sugar: 22.5 grams '
            elif fruit == 67:
                Cd = 'Maracuja \n 63 mg of potassium \n 5 mg of magnesium \n 5.4 mg of vitamin C \n 2 mg of calcium \n 0.29 mg of iron \n 1.9 g of fiber'
            elif fruit == 68:
                Cd = 'Melon Piel de Sapo \n Monounsaturated 0 g \n Trans 0 g \n Protein 0 g \n Sodium 17 mg \n Potassium 310 mg.'
            elif fruit == 69:
                Cd = 'Grape Black \n 104 kilocalories. \n 1.09 g of protein. \n 0.24 g of fat. \n 27.33 g of carbohydrate \n 23.37 g is sugars'
            elif fruit == 70:
                Cd = 'Nectarine \n Calories: 62 \n Fat: 0.5g \n Sodium: 0mg \n Carbohydrates: 15g \n Fiber: 2.4g \n Sugars: 11g \n Protein: 1.5g'
            elif fruit == 71:
                Cd = 'Nectarine Flat \n Calories: 62 \n Fat: 0.5g \n Sodium: 0mg \n Carbohydrates: 15g \n Fiber: 2.4g \n Sugars: 11g \n Protein: 1.5g'
            elif fruit == 72:
                Cd = 'Nut Forest \n Calories: 62 \n Fat: 0.5g \n Sodium: 0mg \n Carbohydrates: 15g \n Fiber: 2.4g \n Sugars: 11g \n Protein: 1.5g'
            elif fruit == 73:
                Cd = 'Nut Pecan \n Calories: 62 \n Fat: 0.5g \n Sodium: 0mg \n Carbohydrates: 15g \n Fiber: 2.4g \n Sugars: 11g \n Protein: 1.5g'
            elif fruit == 74:
                Cd = 'Onion Red \n 64 calories \n 14.9 grams (g) of carbohydrate \n 0.16 g of fat \n 0 g of cholesterol \n 2.72 g of fiber \n 6.78 g of sugar \n 1.76 g of protein.'
            elif fruit == 75:
                Cd = 'Onion Red Peeled \n 64 calories \n 14.9 grams (g) of carbohydrate \n 0.16 g of fat \n 0 g of cholesterol \n 2.72 g of fiber \n 6.78 g of sugar \n 1.76 g of protein.'
            elif fruit == 76:
                Cd = 'Onion White \n 64 calories \n 14.9 grams (g) of carbohydrate \n 0.16 g of fat \n 0 g of cholesterol \n 2.72 g of fiber \n 6.78 g of sugar \n 1.76 g of protein.'
            elif fruit == 77:
                Cd = 'Orange \n Calories: 73 \n Fat: 0.2g \n Sodium: 13mg \n Carbohydrates: 16.5g \n Fiber: 2.8g \n Sugars: 12g \n Protein: 1.3g'
            elif fruit == 78:
                Cd = 'Papaya \n Calories: 60 \n Protein: 1.2 grams \n Fat: 0 grams \n Carbs: 13 grams \n Fiber: 3 grams'
            elif fruit == 79:
                Cd = 'Passion Fruit \n 63 mg of potassium \n 5 mg of magnesium \n 5.4 mg of vitamin C \n 2 mg of calcium \n 0.29 mg of iron \n 1.9 g of fiber'
            elif fruit == 80:
                Cd = 'Peach \n Calories: 58 \n Protein: 1 gram \n Fat: less than 1 gram \n Carbs: 14 grams \n Fiber: 2 grams'
            elif fruit == 81:
                Cd = 'Peach 2 \n Calories: 58 \n Protein: 1 gram \n Fat: less than 1 gram \n Carbs: 14 grams \n Fiber: 2 grams'
            elif fruit == 82:
                Cd = 'Peach Flat \n Calories: 58 \n Protein: 1 gram \n Fat: less than 1 gram \n Carbs: 14 grams \n Fiber: 2 grams'
            elif fruit == 83:
                Cd = 'Pear \n Calories 57 \n Carbohydrates 15 grams \n Total Fat 0.1 gram \n Protein 0.4 gram \nDietary Fiber 3.1 gram'
            elif fruit == 84:
                Cd = 'Pear 2 \n Calories 57 \n Carbohydrates 15 grams \n Total Fat 0.1 gram \n Protein 0.4 gram \nDietary Fiber 3.1 gram'
            elif fruit == 85:
                Cd = 'Pear Abate \n Calories 57 \n Carbohydrates 15 grams \n Total Fat 0.1 gram \n Protein 0.4 gram \nDietary Fiber 3.1 gram'
            elif fruit == 86:
                Cd = 'Pear Forelle \n Calories 57 \n Carbohydrates 15 grams \n Total Fat 0.1 gram \n Protein 0.4 gram \nDietary Fiber 3.1 gram'
            elif fruit == 87:
                Cd = 'Pear Kaiser \n Calories 57 \n Carbohydrates 15 grams \n Total Fat 0.1 gram \n Protein 0.4 gram \nDietary Fiber 3.1 gram'
            elif fruit == 88:
                Cd = 'Pear Monster \n Calories 57 \n Carbohydrates 15 grams \n Total Fat 0.1 gram \n Protein 0.4 gram \nDietary Fiber 3.1 gram'
            elif fruit == 89:
                Cd = 'Pear Red \n Calories 57 \n Carbohydrates 15 grams \n Total Fat 0.1 gram \n Protein 0.4 gram \nDietary Fiber 3.1 gram'
            elif fruit == 90:
                Cd = 'Pear Stone \n Calories 57 \n Carbohydrates 15 grams \n Total Fat 0.1 gram \n Protein 0.4 gram \nDietary Fiber 3.1 gram'
            elif fruit == 91:
                Cd = 'Pear Williams \n Calories 57 \n Carbohydrates 15 grams \n Total Fat 0.1 gram \n Protein 0.4 gram \nDietary Fiber 3.1 gram'
            elif fruit == 92:
                Cd = 'Pepino \n Energy 22 Kcal \n Carbohydrates, 5 g \n Protein, 0.6 g \n Total Fat 0.1 g'
            elif fruit == 93:
                Cd = 'Pepper Green \n Calories: 30 \n Protein: 1.3 grams \n Carbs: 7 grams \n Fiber: 2.6 grams'
            elif fruit == 94:
                Cd = 'Pepper Orange \n Vitamin C 146.7mg'
            elif fruit == 95:
                Cd = 'Pepper Red \n Calories: 30 \n Protein: 1 gram \n Fat: 0.5gm \n Carbohydrates: 7 grams \n Fiber: 2.5 grams \n Sugar: 3.5 grams.'
            elif fruit == 96:
                Cd = 'Pepper Yellow \n Calories: 37.\n Protein: 1 g.\n Fat: 0 g. \n Saturated: 0 g \n Monounsaturated: 0 g'
            elif fruit == 97:
                Cd = 'Physalis \n Calories: 66 \n Protein: 1 gram \n Carbohydrates: 15 grams \n Fiber: 15 grams \n Calcium: 41 mg \n Iron: 0.5 mg \n Sodium: 1.5 mg \n Vitamin C: 41 '
            elif fruit == 98:
                Cd = 'Physalis with Husk \n Calories: 66 \n Protein: 1 gram \n Carbohydrates: 15 grams \n Fiber: 15 grams \n Calcium: 41 mg \n Iron: 0.5 mg \n Sodium: 1.5 mg \n Vitamin C: 41 '
            elif fruit == 99:
                Cd = 'Pineapple \n Calories: 82 grams \n Protein: 0.89 grams \n Fat: 0.20 grams \n Carbohydrates: 22 grams \n Fiber: 2.3 grams'
            elif fruit == 100:
                Cd = 'Pineapple Mini \n Calories: 82 grams \n Protein: 0.89 grams \n Fat: 0.20 grams \n Carbohydrates: 22 grams \n Fiber: 2.3 grams'
            elif fruit == 101:
                Cd = 'Pitahaya Red \n Calories: 102 \n Fat: 0 grams \n Protein: 2 grams \n Carbohydrates: 22 grams \n Fiber: 5 grams \n Sugars: 13 grams'
            elif fruit == 102:
                Cd = 'Plum \n Fiber 0.9 g \n Protein 0.46 g \n Iron 0.11 mg \n Potassium 103.62 mg \n Magnesium 4.62 mg'
            elif fruit == 103:
                Cd = 'Plum 2 \n Fiber 0.9 g \n Protein 0.46 g \n Iron 0.11 mg \n Potassium 103.62 mg \n Magnesium 4.62 mg'
            elif fruit == 104:
                Cd = 'Plum 3 \n Fiber 0.9 g \n Protein 0.46 g \n Iron 0.11 mg \n Potassium 103.62 mg \n Magnesium 4.62 mg'
            elif fruit == 105:
                Cd = 'Pomegranate \n Calories: 64 \n Protein: 1 gram \n Fat: 1 gram \n Carbohydrates: 14 grams \n Fiber: 3 grams \n Sugar: 11 grams'
            elif fruit == 106:
                Cd = 'Pomelo Sweetie \n Calories: 231 \n Fat: 0.2g \n Sodium: 6.1mg \n Carbohydrates: 59g \n Fiber: 6.1g \n Protein: 4.6g \n Vitamin C: 116mg'
            elif fruit == 107:
                Cd = 'Potato Red \n Total Fat 0.5g.\n Saturated Fat 0.1g.\n Cholesterol 0mg.\n Sodium 36mg.\n Potassium 1630mg.\n Total Carbohydrates 59g.\n Dietary Fiber 5.4g \n Sugars 4.3g'
            elif fruit == 108:
                Cd = 'Potato Red Washed \n Total Fat 0.5g.\n Saturated Fat 0.1g.\n Cholesterol 0mg.\n Sodium 36mg.\n Potassium 1630mg.\n Total Carbohydrates 59g.\n Dietary Fiber 5.4g \n Sugars 4.3g'
            elif fruit == 109:
                Cd = 'Potato Sweet \n Total Fat 0.5g.\n Saturated Fat 0.1g.\n Cholesterol 0mg.\n Sodium 36mg.\n Potassium 1630mg.\n Total Carbohydrates 59g.\n Dietary Fiber 5.4g \n Sugars 4.3g'
            elif fruit == 110:
                Cd = 'Potato White \n Total Fat 0.5g.\n Saturated Fat 0.1g.\n Cholesterol 0mg.\n Sodium 36mg.\n Potassium 1630mg.\n Total Carbohydrates 59g.\n Dietary Fiber 5.4g \n Sugars 4.3g' 
            elif fruit == 111:
                Cd = 'Quince \n Energy 57 Kcal \n Carbohydrates 13.81 g \n  Protein 0.40 g \n Total Fat 0.10 g '
            elif fruit == 112:
                Cd = 'Rambutan '
            elif fruit == 113:
                Cd = 'Raspberry \n Total Fat 0.5g.\n Saturated Fat 0.1g.\n Cholesterol 0mg.\n Sodium 36mg.\n Potassium 1630mg.\n Total Carbohydrates 59g.\n Dietary Fiber 5.4g \n Sugars 4.3g'
            elif fruit == 114:
                Cd = 'Redcurrant \n Total Fat 0.5g.\n Saturated Fat 0.1g.\n Cholesterol 0mg.\n Sodium 36mg.\n Potassium 1630mg.\n Total Carbohydrates 59g.\n Dietary Fiber 5.4g \n Sugars 4.3g'
            elif fruit == 115:
                Cd = 'Salak \n Total Fat 0.5g.\n Saturated Fat 0.1g.\n Cholesterol 0mg.\n Sodium 36mg.\n Potassium 1630mg.\n Total Carbohydrates 59g.\n Dietary Fiber 5.4g \n Sugars 4.3g'
            elif fruit == 116:
                Cd = 'Strawberry \n Calories: 32 \n Protein: 0.7 grams \n Carbs: 7.7 grams \n Sugar: 4.9 grams \n Fiber: 2 grams \n Fat: 0.3 grams'
            elif fruit == 117:
                Cd = 'Strawberry Wedge \n Calories: 32 \n Protein: 0.7 grams \n Carbs: 7.7 grams \n Sugar: 4.9 grams \n Fiber: 2 grams \n Fat: 0.3 grams'
            elif fruit == 118:
                Cd = 'Tamarillo \n carbohydrates  2 grams \n protein 3.3 grams \n dietary fibre 4 micrograms'
            elif fruit == 119:
                Cd = 'Tangelo \n Calories: 47 \n Fat: 0g \n Sodium: 0mg \n Carbohydrates: 11.6g \n Fiber: 2.1g \n Sugars: 9.5g \n Protein: 1.1g \n Vitamin C: 52.6mg'
            elif fruit == 120:
                Cd = 'Tomato 1 \n Calories: 16 \n Fat: 0.2g \n Sodium: 5mg \n Carbohydrates: 3.5g \n Fiber: 1.1g \n Sugars: 2.4g \n Protein: 0.8g'
            elif fruit == 121:
                Cd = 'Tomato 2 \n Calories: 16 \n Fat: 0.2g \n Sodium: 5mg \n Carbohydrates: 3.5g \n Fiber: 1.1g \n Sugars: 2.4g \n Protein: 0.8g '
            elif fruit == 122:
                Cd = 'Tomato 3 \n Calories: 16 \n Fat: 0.2g \n Sodium: 5mg \n Carbohydrates: 3.5g \n Fiber: 1.1g \n Sugars: 2.4g \n Protein: 0.8g'
            elif fruit == 123:
                Cd = 'Tomato 4 \n Calories: 16 \n Fat: 0.2g \n Sodium: 5mg \n Carbohydrates: 3.5g \n Fiber: 1.1g \n Sugars: 2.4g \n Protein: 0.8g'
            elif fruit == 124:
                Cd = 'Tomato Cherry Red \n Calories: 16 \n Fat: 0.2g \n Sodium: 5mg \n Carbohydrates: 3.5g \n Fiber: 1.1g \n Sugars: 2.4g \n Protein: 0.8g'
            elif fruit == 125:
                Cd = 'Tomato Heart \n Calories: 16 \n Fat: 0.2g \n Sodium: 5mg \n Carbohydrates: 3.5g \n Fiber: 1.1g \n Sugars: 2.4g \n Protein: 0.8g'
            elif fruit == 126:
                Cd = 'Tomato Maroon \n Calories: 16 \n Fat: 0.2g \n Sodium: 5mg \n Carbohydrates: 3.5g \n Fiber: 1.1g \n Sugars: 2.4g \n Protein: 0.8g'
            elif fruit == 127:
                Cd = 'Tomato not Ripened \n Calories: 16 \n Fat: 0.2g \n Sodium: 5mg \n Carbohydrates: 3.5g \n Fiber: 1.1g \n Sugars: 2.4g \n Protein: 0.8g'
            elif fruit == 128:
                Cd = 'Tomato Yellow \n Calories: 16 \n Fat: 0.2g \n Sodium: 5mg \n Carbohydrates: 3.5g \n Fiber: 1.1g \n Sugars: 2.4g \n Protein: 0.8g'
            elif fruit == 129:
                Cd = 'Walnut \n Energy: 200 calories \n Carbohydrate 3.89 grams (g) \n Sugar: 1 g \n Fiber: 2 g \n Protein: 5 g \n Fat: 20 g \n Calcium: 20 milligrams (mg)'
            elif fruit == 130:
                Cd = 'Watermelon \n Calories: 46 \n Fat: 0.2g ·\n Sodium: 1.5mg \n Carbohydrates: 11.5g \n Fiber: 0.6g \n Sugars: 9.4g \n Protein: 0.9g'


            # elif fruit == 1:
            #     Cd="Carambula \n Total Fat 0.3 g \n Cholesterol 0 mg \n Sodium 2 mg \n Total Carbohydrate 7 g "
            # elif fruit == 2:
            #     Cd=" Cherry \n Total Fat 0.3 g \n Cholesterol 0 mg \n Sodium 3 mg \n Total Carbohydrate 12 g "
            # elif fruit == 3:
            #     Cd=" Grape White \n Total Fat0.08g \n Cholesterol0mg \n Sodium1mg \n Total Carbohydrate9.05g"
            # elif fruit == 4:
            #     Cd=" Grapefruit Pink \n Total Fat 0.1 g \n Cholesterol 0 mg \n Sodium 0 mg \n Total Carbohydrate 11 g"
            # elif fruit == 5:
            #     Cd=" Guava \n Total Fat 1 g \n Cholesterol 0 mg \n Sodium 2 mg \n Total Carbohydrate 14 g"
            # elif fruit == 6:
            #     Cd=" Kiwi \n Total Fat 0.5 g \n Cholesterol 0 mg \n Sodium 3 mg \n Total Carbohydrate 15 g"
            # elif fruit == 7:
            #     Cd=" Kumquats \n Total Fat 0.9 g \n Cholesterol 0 mg \n Sodium 10 mg \n Total Carbohydrate 16 g"
            # elif fruit == 8:
            #     Cd=" Lemon \n Total Fat 0.3 g \n Cholesterol 0 mg \n Sodium 2 mg \n Total Carbohydrate 9 g"
            # elif fruit == 9:
            #     Cd="Tomato \n Total Fat 0.2 g \n Cholesterol 0 mg \n Sodium 5 mg \n Total Carbohydrate 3.9 g "
            # elif fruit == 10:
            #     Cd="Apple Golden \n Total Fat	0.2 g \n Protein: 0.3 grams \n Sodium	3 mg \n Total Carbohydrate	17.4 g "
            # elif fruit == 11:
            #     Cd="  Apricot \n Total Fat 0.4 g \n Cholesterol 0 mg \n Sodium 1 mg \n Total Carbohydrate 11 g"
            # elif fruit == 12:
            #     Cd=" Avocado  \n Total Fat 15 g \n Cholesterol 0 mg \n Sodium 7 mg \n Total Carbohydrate 9 g"
            # elif fruit == 13:
            #     Cd=" Avocado ripe \n Fat: 14.7g \n Calories: 160 \n Sodium: 7mg \n Carbohydrates: 8.5g"
            # elif fruit == 14:
            #     Cd=" Banana \n Total Fat 0.3 g \n Cholesterol 0 mg \n Sodium 1 mg \n Total Carbohydrate 23 g"
            # elif fruit == 15:
            #      Cd=" Banana Red \n Fat: 0.3 grams \n Calories: 90 calories \n Sodium 1 mg \n Carbs: 21 grams"
            # elif fruit == 16:
            #      Cd=" Cactus fruit \n Total Fat 0.5 g \n Cholesterol 0 mg \n Sodium 5 mg \n Total Carbohydrate 10 g"
            # elif fruit == 17:
            #      Cd=" Cantaloupe \n Total Fat 0.2 g \n Cholesterol 0 mg \n Sodium 16 mg \n Total Carbohydrate 8 g"
       
            A=Cd
            print(A)          
            return render(request, "index.html", {"predictions": A,'file_url': file_url})  
            
        
        return render(request, "index.html")
    
    else:
    
        return render(request, "index.html")     
        #return render(request, 'index.html', {'file_url': file_url})
    #return render(request, 'index.html') 
    
'''
def detect(request):
    if request.method == "POST":
        imgpath = up
        fn = up
        print(fn)
        IMAGE_SIZE = 100
        LEARN_RATE = 1.0e-4
        CH=3
        print(fn)
        if fn!="":
            model = load_model('C:/Users/admin/Downloads/YT_Django_TensorFlow_Image_Classification_Basic-main/YT_Django_TensorFlow_Image_Classification_Basic-main/model/fruit_model.h5')
            img = Image.open(fn)
            img = img.resize((IMAGE_SIZE,IMAGE_SIZE))
            img = np.array(img)
        
            img = img.reshape(1,IMAGE_SIZE,IMAGE_SIZE,3)
        
            img = img.astype('float32')
            img = img / 255.0
            print('img shape:',img)
            prediction = model.predict(img)
            print(np.argmax(prediction))
            brain=np.argmax(prediction)
            print(brain)
            if brain == 0:
                Cd="Normal_Brain"
            elif brain == 1:
                Cd="Brain_Tumor_Glioma Level"
            elif brain ==2:
                Cd="Brain_Tumor_Meningioma Level"
            elif brain ==3:
                Cd="Brain_Tumor_Pitutorial"
            A=Cd
          
            return render(request, "preprocess.html", {"predictions": A})  

  
def preprocess(request):
    return render(request, "preprocess.html")
         
        imgpath = up
        
        fn = up
        IMAGE_SIZE = 100
        LEARN_RATE = 1.0e-4
        CH=3
        print(fn)
        if fn!="":
        
       
            model = load_model('C:/Users/admin/Downloads/YT_Django_TensorFlow_Image_Classification_Basic-main/YT_Django_TensorFlow_Image_Classification_Basic-main/model/brain_model.h5')
            img = Image.open(fn)
            img = img.resize((IMAGE_SIZE,IMAGE_SIZE))
            img = np.array(img)
        
            img = img.reshape(1,IMAGE_SIZE,IMAGE_SIZE,3)
        
            img = img.astype('float32')
            img = img / 255.0
            print('img shape:',img)
            prediction = model.predict(img)
            print(np.argmax(prediction))
            brain=np.argmax(prediction)
            print(brain)
            if brain == 0:
                Cd="Normal_Brain"
            elif brain == 1:
                Cd="Brain_Tumor_Glioma Level"
            elif brain ==2:
                Cd="Brain_Tumor_Meningioma Level"
            elif brain ==3:
                Cd="Brain_Tumor_Pitutorial"
            A=Cd
          
            return render(request, "preprocess.html", {"predictions": A})  

  
    if request.method == "POST":
        #
        # Django image API
        #
        file = request.FILES["imageFile"]
        print(file)
        fs=FileSystemStorage()
        file_name = fs.save(file.name, file)
        file_url = fs.path(file_name)
        ff=fs.url(file_name)
        
        imgpath = file
        fn = file
        IMAGE_SIZE = 100
        LEARN_RATE = 1.0e-4
        CH=3
        print(fn)
        if fn!="":
        
       
            model = load_model('C:/Users/admin/Downloads/YT_Django_TensorFlow_Image_Classification_Basic-main/YT_Django_TensorFlow_Image_Classification_Basic-main/model/brain_model.h5')
            img = Image.open(fn)
            img = img.resize((IMAGE_SIZE,IMAGE_SIZE))
            img = np.array(img)
        
            img = img.reshape(1,IMAGE_SIZE,IMAGE_SIZE,3)
        
            img = img.astype('float32')
            img = img / 255.0
            print('img shape:',img)
            prediction = model.predict(img)
            print(np.argmax(prediction))
            brain=np.argmax(prediction)
            print(brain)
            if brain == 0:
                Cd="Normal_Brain"
            elif brain == 1:
                Cd="Brain_Tumor_Glioma Level"
            elif brain ==2:
                Cd="Brain_Tumor_Meningioma Level"
            elif brain ==3:
                Cd="Brain_Tumor_Pitutorial"
            A=Cd
          
            #return render(request, "index.html", {"predictions": A})  
            
        return render(request, 'main/upload.html', {'file_url': file_url})
    else:
        return render(request, "index.html")
         

        #
        # https://www.tensorflow.org/api_docs/python/tf/keras/preprocessing/image/load_img
        #
def upload(request):
    if request.method == 'POST' and request.FILES['upload']:
        upload = request.FILES['upload']
        fss = FileSystemStorage()
        file = fss.save(upload.name, upload)
        file_url = fss.url(file)
        return render(request, 'upload.html', {'file_url': file_url})
    return render(request, 'upload.html')        
               '''