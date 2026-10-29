import os

API_KEY = "AIzaSy..."  # Deinen API Key hier einfügen

TARGET_CITIES = [
    "Genève", "Lausanne", "Nyon", "Morges", "Vevey", "Montreux",
    "Yverdon-les-Bains", "Neuchâtel", "Fribourg", "Sion", "Sierre",
    "Martigny", "Delémont", "Porrentruy", "Bienne"
]

SEGMENTS = {
    "Medical": [
        "Centre médical",
        "Cabinet médical",
        "Médecin généraliste",
        "Pédiatre",
        "Cabinet dentaire",
        "Centre de physiothérapie",
        "Chiropraticien",
        "Ostéopathe",
        "Clinique privée",
        "Pharmacie",
        "Maison de retraite"
    ],

    "Professional_Services": [
        "Fiduciaire",
        "Etude d'avocats",
        "Etude de notaire",
        "Régie immobilière",
        "Bureau d'architecte",
        "Bureau d'ingénieurs",
        "Agence d'assurances",
        "Services informatiques",
        "Société de logiciels",
        "Conseil en gestion",
        "Agence de communication"
    ],

    "Construction": [
        "Entreprise de construction",
        "Entreprise générale de bâtiment",
        "Entreprise de maçonnerie",
        "Génie civil",
        "Entreprise de peinture",
        "Entreprise de plâtrerie",
        "Electricien",
        "Installateur sanitaire",
        "Chauffagiste",
        "Menuiserie",
        "Construction métallique"
    ],

    "Beauty_Wellness": [
        "Salon de coiffure",
        "Institut de beauté",
        "Spa",
        "Onglerie"
    ],

    "Fitness": [
        "Centre de fitness",
        "Salle de sport",
        "Crossfit"
    ],

    "Hospitality": [
        "Hôtel",
        "Hôtel d'affaires",
        "Restaurant"
    ],

    "Industry": [
        "Constructeur de machines",
        "Site de production",
        "Entreprise industrielle",
        "Entreprise de logistique"
    ]
}
