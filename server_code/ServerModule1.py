import anvil.server
import pickle
import urllib.request

# GitHub’dan modeli indirme işlevi
def load_model_from_github():
    url = "https://raw.githubusercontent.com/davut4786/HastalikTuru/main/hastalikturu_model.pkl"  # GitHub URL'niz
    model_path = "/tmp/hastalikturu_model.pkl"  # Geçici dosya yolu
    urllib.request.urlretrieve(url, model_path)  # Modeli indir
    with open(model_path, 'rb') as file:
        model = pickle.load(file)  # Modeli yükle
    return model

# Modeli yükleme
model = load_model_from_github()  # Modeli bellekte tut

@anvil.server.callable
def model_tahmin(features):
    # Kategorik değişkenleri sayısal hale getirme (one-hot encoding) burada kaldırılıyor
    # Özellikleri doğrudan kullanıyoruz
    # Özellikler, modelin beklediği formatta olmalı
    # features bir liste olmalı
    # Tahmin yapma
    prediction = model.predict([features])

    return prediction[0]  # Tekil bir sonuç döndür
