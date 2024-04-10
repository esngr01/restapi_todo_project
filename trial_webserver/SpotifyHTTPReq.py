import requests

#Search Term definieren

search_term = input('Wunschkünstler eingeben: ')

#API Definierung

artist_url = f'https://api.spotify.com/v1/search?type=artist&q={search_term}'
token = 'BQClbc8a6yxr2w07L0tCI-De0GTqB7_KyI7fSLDTz9pW6LwajXykHsEflpr5f4R7TjaAQENfbuI1QhEYcvS2cJ88hIoOymkxQDjmgs3OsAad4Tvygq8'
headers = {
    'Authorization': f'Bearer {token}'
}

#Request absenden

response = requests.get(artist_url, headers=headers)

#Check auf Status Code 200
if response.status_code == 200:
    
    data = response.json()
    
    if data['artists']['items']:
        artist = data['artists']['items'][0]
        artist_name = artist['name']
        artist_id = artist['id']
        print(f'Künstler: {artist_name}')
        print(f'Künstler-ID: {artist_id}')

#Alben Abfragen
        album_url = f'https://api.spotify.com/v1/artists/[{artist_id}]/albums'

        album_response = requests.get(album_url, headers=headers)
        
        album_data = album_response.json()
            
        if album_data['albums']['items']:
                album = album_data['albums']['items'][0]
                album_name = album['name']
                album_id = album['id']
                
                print(f'Alben von {artist_name}: ')
                for album in album_data:
                    print(f"Album: {album_name}")
            