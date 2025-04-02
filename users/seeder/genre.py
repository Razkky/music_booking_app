#!/usr/bin/env python3

from users.models import Genre

genres = [
  "Rock",
  "Pop",
  "Jazz",
  "Classical",
  "Hip Hop",
  "Reggae",
  "Blues",
  "Electronic",
  "Country",
  "Indie",
  "Folk",
  "R&B",
  "Soul",
  "Punk",
  "Metal",
  "Techno",
  "EDM",
  "Alternative"
]

def seed_genre():
    for genre in genres:
        Genre.objects.get_or_create(name=genre)

def main():
    seed_genre()
