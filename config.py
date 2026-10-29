import os

# Google Places API Key (aus Umweltvariable oder direkt eintragen)
API_KEY = os.getenv("GOOGLE_PLACES_API_KEY", "DEIN_API_KEY_HIER")

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
