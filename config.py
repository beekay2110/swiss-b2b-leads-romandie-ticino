import os

# Google Places API Key
API_KEY = "AIzaSyCm6_DfNZZW1hctQHZf2V3WNpls2TpaIjQ"

# Relevanteste Städte & Hauptorte der Romandie (VD, GE, VS, NE, FR, JU, BE-FR)
TARGET_CITIES = [
    "Genève", "Lausanne", "Nyon", "Morges", "Vevey", "Montreux",
    "Yverdon-les-Bains", "Neuchâtel", "Fribourg", "Sion", "Sierre",
    "Martigny", "Delémont", "Porrentruy", "Bienne"
]

# Zielgruppen-Suchbegriffe auf Französisch (Büros, Praxen, Kanzleien, KMU)
TARGET_QUERIES = [
    "Cabinet médical",
    "Etude d'avocats",
    "Fiduciaire",
    "Agence immobilière",
    "Entreprise de construction",
    "Bureau d'architecte",
    "Siège social",
    "Centre dentaire",
    "Clinique privée",
    "Espace de coworking"
]
