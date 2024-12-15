# -*- coding: utf-8 -*-
"""
Created on Tue Oct 22 11:42:23 2024

@author: ASUS
"""
import rasterio
import matplotlib.pyplot as plt
import os
from collections import defaultdict

directory = 'misirVerileri'

# Çekim setlerine göre bantları depolamak için bir sözlük oluşturuyoruz
bands_by_set = defaultdict(lambda: {
    "green": None,
    "red": None,
    "nir": None,
    "red-edge": None,
    "rgb": None
})

# Dosyaları döngü ile tara ve her çekim seti için ilgili bantlara ata
for filename in os.listdir(directory):
    # Çekim setini dosya adının ilk kısmından çıkar
    parts = filename.split('_')
    if len(parts) < 3:
        continue  # Dosya adı beklenen formata uymuyorsa atla
    
    capture_set = f"{parts[0]}_{parts[1]}_{parts[2]}"  # Örneğin: "DJI_202410051655_16"

    if 'MS_G' in filename:
        with rasterio.open(os.path.join(directory, filename)) as src:
            bands_by_set[capture_set]["green"] = src.read(1)
    elif 'MS_R' in filename:
        with rasterio.open(os.path.join(directory, filename)) as src:
            bands_by_set[capture_set]["red"] = src.read(1)
    elif 'MS_NIR' in filename:
        with rasterio.open(os.path.join(directory, filename)) as src:
            bands_by_set[capture_set]["nir"] = src.read(1)
    elif 'MS_RE' in filename:
        with rasterio.open(os.path.join(directory, filename)) as src:
            bands_by_set[capture_set]["red-edge"] = src.read(1)
    elif 'D.JPG' in filename:
        bands_by_set[capture_set]["rgb"] = plt.imread(os.path.join(directory, filename))

# Her çekim seti için bantları görselleştir
for capture_set, bands in bands_by_set.items():
    for band, data in bands.items():
        if data is not None:
            plt.figure()
            plt.title(f"{capture_set} - {band.capitalize()} Band")
            plt.imshow(data, cmap='gray' if band != 'rgb' else None)
            plt.axis('off')
            plt.show()

    
                       
                       


