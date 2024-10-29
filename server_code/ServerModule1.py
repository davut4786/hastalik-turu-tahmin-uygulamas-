import anvil.server

import anvil.server
import joblib
import pandas as pd

# Modeli yükleme
model = joblib.load('/content/drive/MyDrive/hastalikturu_model.pkl')

@anvil.server.callable
def model_tahmin(features):
    # Özellikleri DataFrame'e çevirme
    columns = ['tur', 'sistem', 'cBasebC', 'cBaseEcfc', 'HCO3Pc', 'p50c', 'cHCO3Pst', 'cNa', 'FHHb', 'sO2', 'GRAN', 'LYM', 'MON_A', 'HCT', 'MCH', 'MCHC', 'abdominal_agri', 'genel_durum', 'idar_problemi', 'inkordinasyon', 'ishal', 'istahsizlik', 'kanama', 'kusma', 'oksuruk']
    input_data = pd.DataFrame([features], columns=columns)

    # Kategorik değişkenleri sayısal hale getirme (one-hot encoding)
    input_data = pd.get_dummies(input_data, drop_first=True)

    # Tahmin yapma
    prediction = model.predict(input_data)

    return prediction[0]  # Tekil bir sonuç döndür
