import wget
import os
import zipfile

link = 'https://github.com/AI4Bharat/Indic-TTS/releases/download/v1-checkpoints-release/'

models = ['as', 'brx', 'en+hi', 'gu', 'kn', 'ml', 'mni', 'mr', 'or', 'pa', 'raj', 'ta']

# models = ['bn']

for model in models:
    wget.download(link+model+'.zip', out='models/v1/')
    with zipfile.ZipFile('models/v1/'+model+'.zip', 'r') as zip_ref:
        zip_ref.extractall('models/v1/')

    os.remove('models/v1/'+model+'.zip')



