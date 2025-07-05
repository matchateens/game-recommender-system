import os
import django

# Set environment variable untuk settings.py
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')

# Inisialisasi Django sebelum mengimpor model apa pun
django.setup()

import csv
from games.models import Game

def load_data():
    with open('games_with_images.csv', newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            Game.objects.create(
                name=row['Name'],
                rating=row['Rating'],
                genres=row['Genres'],
                platforms=row['Platforms'],
                esrb=row['ESRB'],
                image_url=row.get('Image_URL', '')  # pastikan field ini ada di model Game
            )

if __name__ == '__main__':
    load_data()
