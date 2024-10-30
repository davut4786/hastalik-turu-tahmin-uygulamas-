import pickle
import urllib.request
import anvil.server
import pandas as pd

# Google Drive'dan modeli indirme
def load_model_from_drive():
    url = "https://drive.google.com/uc?id=1V26NN9pxPHbpIrfpQN271T36PPaIYqkU"  # Güncellenmiş URL
    model_path = "/tmp/hastalikturu_model.pkl"  # Geçici dosya yolu
    urllib.request.urlretrieve(url, model_path)  # Model dosyasını indir
    with open(model_path, 'rb') as file:
        model = pickle.load(file)  # Modeli yükle
    return model

# Modeli yükleme
model = load_model_from_drive()  # Bir kez indirip bellekte tut

@anvil.server.callable
def model_tahmin(features):
    # Özellikleri DataFrame'e çevirme
    columns = ['tur', 'sistem', 'cBasebC', 'cBaseEcfc', 'HCO3Pc', 'p50c', 
               'cHCO3Pst', 'cNa', 'FHHb', 'sO2', 'GRAN', 'LYM', 'MON_A', 
               'HCT', 'MCH', 'MCHC', 'abdominal_agri', 'genel_durum', 
               'idar_problemi', 'inkordinasyon', 'ishal', 'istahsizlik', 
               'kanama', 'kusma', 'oksuruk']
    
    input_data = pd.DataFrame([features], columns=columns)  # Özellikleri DataFrame'e çevir

    # Kategorik değişkenleri sayısal hale getirme (one-hot encoding)
    input_data = pd.get_dummies(input_data, drop_first=True)

    # Tahmin yapma
    prediction = model.predict(input_data)

    return prediction[0]  # Tekil bir sonuç döndür
