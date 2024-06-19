# UData-test-task

# Real Estate Data Collection Project

This project is a script for collecting real estate data from the website [kelm-immobilien.de](https://kelm-immobilien.de). The collected data is stored in a JSON file.

## Description

The script performs the following actions:
1. Iterates through the website pages, collecting links to individual real estate listings.
2. Collects detailed information about each listing, including name, price, description, location, contact information, and images.
3. Saves the collected data into a `data.json` file.

## Usage

1. Clone the repository to your computer.
2. Install the required libraries: `requests`, `beautifulsoup4`, `lxml`.
3. Run the script: `python script.py`.

## Example of JSON file

```json
    "Stilvolle und großzügige Dachgeschosswohnung mit Gestaltungsfreiraum": {
        "url": "https://kelm-immobilien.de/immobilien/wohnung-eigentumswohnung-dachgeschosswohnung-in-arnsberg-kaufen-7953-prvtx/",
        "title": "Stilvolle und großzügige Dachgeschosswohnung mit Gestaltungsfreiraum",
        "status": "",
        "pictures": [
            "https://kelm-immobilien.de/wp-content/uploads/immomakler/openimmo1718794161331/1d002522-9ec4-44a3-86d0-21f3bc533769-100x67.jpg",
            "https://kelm-immobilien.de/wp-content/uploads/immomakler/openimmo1718794161331/c551dbce-0518-4c8b-912e-2bc83fbacc35-100x67.jpg",
            "https://kelm-immobilien.de/wp-content/uploads/immomakler/openimmo1718794161331/096057c0-246e-4313-92b6-8335be10d09d-100x67.jpg",
            "https://kelm-immobilien.de/wp-content/uploads/immomakler/openimmo1718794161331/81da5240-ddf7-406f-a5a5-556084753506-100x67.jpg",
            "https://kelm-immobilien.de/wp-content/uploads/immomakler/openimmo1718794161331/e9bebd91-e6de-4841-ad13-a9ef9654f4f1-100x67.jpg",
            "https://kelm-immobilien.de/wp-content/uploads/immomakler/openimmo1718794161331/22511273-9188-418e-946f-f54fd1631c17-100x67.jpg",
            "https://kelm-immobilien.de/wp-content/uploads/immomakler/openimmo1718794161331/2046981e-9c82-4075-b496-012434e365f4-100x67.jpg",
            "https://kelm-immobilien.de/wp-content/uploads/immomakler/openimmo1718794161331/00e38e81-0004-4fa6-8ae6-0dd6d1190894-100x67.jpg",
            "https://kelm-immobilien.de/wp-content/uploads/immomakler/openimmo1718794161331/c4d8e742-732c-49c3-ad95-7333e75cc22f-100x67.jpg",
            "https://kelm-immobilien.de/wp-content/uploads/immomakler/openimmo1718794161331/f5b9aeb4-f8a9-40c7-9ae6-ae521970602b-100x67.jpg",
            "https://kelm-immobilien.de/wp-content/uploads/immomakler/openimmo1718794161331/e2814a1b-2e63-47e6-82e1-c446a7bc8c70-100x67.jpg",
            "https://kelm-immobilien.de/wp-content/uploads/immomakler/openimmo1718794161331/eade33a1-db17-40d4-ba68-4342af921c6b-100x67.jpg",
            "https://kelm-immobilien.de/wp-content/uploads/immomakler/openimmo1718794161331/d32cdb06-a4f2-4b4c-8040-870fbb510992-100x67.jpg",
            "https://kelm-immobilien.de/wp-content/uploads/immomakler/openimmo1718794161331/23cec9b4-f910-4f19-a935-bcb2f1d6d10a-100x67.jpg",
            "https://kelm-immobilien.de/wp-content/uploads/immomakler/openimmo1718794161331/92081eef-d7e9-46f8-9607-c79bd29f5f9f-100x67.jpg",
            "https://kelm-immobilien.de/wp-content/uploads/immomakler/openimmo1718794161331/0562edaf-afd2-4b47-a8aa-b360f039e844-100x54.jpg"
        ],
        "rent_price": "199.500",
        "description": "Objekt­beschreibung\n\n\nBeschreibung\nDiese stilvolle und großzügige Eigentumswohnung befindet sich in einem Mehrfamilienhaus aus dem Baujahr 1968 und erstreckt sich über ca. 127m² Wohnfläche im Dachgeschoss. \nDie Wohnung wurde kürzlich renoviert und präsentiert sich in einem modernen und ansprechenden Zustand. Die Renovierung umfasste unter anderem die Erneuerung der Böden, die Montage neuer Fenster sowie die Sanitärinstallationen.\nDiese charmante Dachgeschosswohnung kann sofort bezogen oder vermietet werden.\nIn dem Mehrfamilienhaus besteht die Möglichkeit, einen Aufzug nachzurüsten. Die Genehmigung für den Einbau des Aufzugs liegt bereits vor. Diese Maßnahme bietet den Bewohnern des Hauses nicht nur einen bequemeren Zugang zu ihren Wohnungen, sondern erhöht auch den Wohnkomfort.\nAusstattung\nDiese charmante Eigentumswohnung verfügt über insgesamt 5 geräumige Zimmer auf 127 m² und bietet ein praktisches Raumkonzept und vielfältige Nutzungsmöglichkeiten.\nZudem verfügt die Wohnung über eine separate Küche mit angrenzendem Esszimmer sowie ein Badezimmer mit Badewanne.\nEine Besonderheit dieser Dachgeschosswohnung ist der dazugehörige Dachboden, der für weitere Nutzungszwecke zur Verfügung steht und in Sondereigentum befindet.\nAktuell wird das Objekt über eine Zentralheizung aus dem Jahr 2000 beheizt. Der jetzige Eigentümer wird die Gasheizung innerhalb nächsten Jahres verpflichtend erneuern.\nEin PKW-Stellplatz kann optional angemietet werden, um das Auto bequem vor dem Gebäude zu parken.\nDiese Eigentumswohnung eignet sich ideal für Familien, Paare oder Kapitalanleger, die auf der Suche nach einer großzügigen und gut gelegenen Immobilie sind.\nSonstige Informationen\nAlle Angaben in der Beschreibung beruhen auf Auskünften des Eigentümers. Flächen- und Maßangaben sind ca. Werte. Die hier aufgeführten Grundrisse dienen nur der besseren Darstellung. Abweichungen zum Original können möglich sein. Für die Richtigkeit dieser Angaben übernehmen wir keine Haftung. Irrtum und Zwischenverkauf vorbehalten.\nVereinbaren Sie gerne einen Besichtigungstermin mit uns.\nDas Kelm Immobilien-Team aus Neheim steht Ihnen jederzeit gern zur Verfügung!\nAuf Wunsch erarbeiten wir mit Ihnen ein attraktives Finanzierungsangebot. Sprechen Sie uns gern dazu an.",
        "phone_number": "+49 2932 9417117",
        "email": "anfragen@kelm-immobilien.de",
        "country": "DE",
        "location": "59821 Arnsberg, Dachgeschosswohnung"
    }
```

## Questions and Clarifications

I have completed a small part of the task to find out if I am doing it correctly. If I am doing something wrong, please specify what exactly. If the task is being done correctly, please indicate what is missing and what mistakes there are.


[Test Task](<Test Task - Python Developer (Scrapy).pdf>)