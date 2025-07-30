import requests
from tqdm import tqdm #анімація завантаження

url = 'https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/photos'
params = {'sol': 1000, 'camera': 'fhaz', 'api_key': 'DEMO_KEY'}

response = requests.get(url, params=params)
data = response.json()

photo_urls = [photo['img_src'] for photo in data['photos']]

for i, url in enumerate(tqdm(photo_urls[:3], desc="📸 Скачивание фото"), start=1):
    img_data = requests.get(url).content
    with open(f'mars_photo{i}.jpg', 'wb') as f:
        f.write(img_data)

print("✅ Фотографії успішно збережено!")