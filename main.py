import requests
import pandas as pd
import time
import os
from config import API_KEY, TARGET_CITIES, SEGMENTS

PLACES_API_URL = "https://places.googleapis.com/v1/places:searchText"

def fetch_places(text_query, page_token=None):
    headers = {
        "Content-Type": "application/json",
        "X-Goog-Api-Key": API_KEY,
        "X-Goog-FieldMask": (
            "places.id,places.displayName,places.formattedAddress,"
            "places.nationalPhoneNumber,places.websiteUri,places.rating,"
            "places.userRatingCount,nextPageToken"
        )
    }
    
    payload = {
        "textQuery": text_query,
        "languageCode": "fr",
        "pageSize": 20
    }
    
    if page_token:
        payload["pageToken"] = page_token

    try:
        response = requests.post(PLACES_API_URL, json=payload, headers=headers)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f" Fehler bei Anfrage '{text_query}': {e}")
        return {}

def run_lead_extraction():
    all_leads = []
    seen_place_ids = set()

    print("\n==========================================")
    print(" STARTE EXTRAKTION FÜR DIE ROMANDIE")
    print("==========================================\n")

    for city in TARGET_CITIES:
        for segment_name, queries in SEGMENTS.items():
            for query_term in queries:
                full_query = f"{query_term} in {city}, Switzerland"
                print(f"[{segment_name}] Suche: '{full_query}'...")

                next_token = None
                page_count = 0

                while True:
                    data = fetch_places(full_query, page_token=next_token)
                    places = data.get("places", [])

                    for p in places:
                        place_id = p.get("id")
                        if place_id in seen_place_ids:
                            continue
                        
                        seen_place_ids.add(place_id)

                        lead = {
                            "Region": "Romandie",
                            "Segment": segment_name,
                            "Stadt": city,
                            "Suchbegriff": query_term,
                            "Firmenname": p.get("displayName", {}).get("text", ""),
                            "Adresse": p.get("formattedAddress", ""),
                            "Telefon": p.get("nationalPhoneNumber", ""),
                            "Website": p.get("websiteUri", ""),
                            "Bewertung": p.get("rating", ""),
                            "Anzahl Bewertungen": p.get("userRatingCount", ""),
                            "Google Place ID": place_id
                        }
                        all_leads.append(lead)

                    next_token = data.get("nextPageToken")
                    page_count += 1

                    if not next_token or page_count >= 3:
                        break

                    time.sleep(2)

    if all_leads:
        df = pd.DataFrame(all_leads)
        
        os.makedirs("output", exist_ok=True)
        output_file = "output/culligan_leads_romandie.xlsx"
        df.to_excel(output_file, index=False, engine="openpyxl")
        
        print(f"\n ERFOLG: {len(df)} einzigartige Leads für die Romandie extrahiert.")
        print(f"Gespeichert unter: {output_file}")
    else:
        print("\n Keine Leads gefunden.")

if __name__ == "__main__":
    if not API_KEY or API_KEY == "AIzaSy...":
        print(" Fehler: Bitte zuerst den GOOGLE_PLACES_API_KEY in config.py hinterlegen.")
    else:
        run_lead_extraction()
