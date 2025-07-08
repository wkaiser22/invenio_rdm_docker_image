from invenio_app.factory import create_app
from invenio_access.permissions import system_identity
from invenio_communities.proxies import current_communities
from pathlib import Path
import json

# Anwendung starten
app = create_app()
app.app_context().push()

OUTPUT_FILE = "communities.json"

def save_community_info(info):
    data = []
    output_path = Path(OUTPUT_FILE)
    if output_path.exists():
        with open(output_path, "r") as f:
            data = json.load(f)
    data.append(info)
    with open(output_path, "w") as f:
        json.dump(data, f, indent=2)

def upload_logo(community_id, logo_path):
    try:
        with open(logo_path, "rb") as file_stream:
            current_communities.service.update_logo(
                identity=system_identity,
                id_=community_id,
                stream=file_stream,
                content_length=None
            )
            print(f"Logo hochgeladen: {logo_path}")
    except Exception as e:
        print(f"Fehler beim Logo-Upload ({logo_path}): {e}")

def create_community(entry):
    identity = system_identity
    community_data = {
        "access": {
            "visibility": entry["visibility"],
            "record_policy": entry["record_policy"],
            "member_policy": entry["member_policy"]
        },
        "slug": entry["slug"],
        "metadata": {
            "title": entry["title"],
            "description": entry["description"],
            "curation_policy": entry["curation_policy"],
            "page": "Beschreibung folgt.",
            "website": entry["website"],
            "organizations": [{"name": entry["title"]}]
        }
    }

    created = current_communities.service.create(identity=identity, data=community_data)
    community_id = created["id"]
    print(f"Community '{entry['title']}' erstellt mit ID: {community_id}")

    if entry.get("logo_path") and Path(entry["logo_path"]).exists():
        upload_logo(community_id, entry["logo_path"])
    else:
        print(f"Kein gültiger Logo-Pfad: {entry.get('logo_path')}")
    save_community_info({
        "title": entry["title"],
        "id": community_id,
        "slug": entry["slug"],
        "logo_path": entry.get("logo_path", "")
    })

# Liste der Communities mit Logo-Pfaden
communities = [
    {
        "title": "DHBW Mannheim",
        "description": "Forschung an der DHBW Mannheim",
        "curation_policy": "Standard",
        "website": "https://www.dhbw-mannheim.de",
        "visibility": "public",
        "record_policy": "open",
        "member_policy": "open",
        "slug": "dhbw-mannheim",
        "logo_path": "/opt/invenio/src/static/images/logo-fdm-dhbw.png"
    },
    {
        "title": "DHBW Stuttgart",
        "description": "DHBW Stuttgart",
        "curation_policy": "Standard",
        "website": "https://www.dhbw-stuttgart.de",
        "visibility": "public",
        "record_policy": "open",
        "member_policy": "open",
        "slug": "dhbw-stuttgart",
        "logo_path": "/opt/invenio/src/static/images/logo-fdm-dhbw.png"
    },
    {
        "title": "DHBW Heidenheim",
        "description": "DHBW Heidenheim",
        "curation_policy": "Standard",
        "website": "https://www.heidenheim.dhbw.de/startseite",
        "visibility": "public",
        "record_policy": "open",
        "member_policy": "open",
        "slug": "dhbw-heidenheim",
        "logo_path": "/opt/invenio/src/static/images/logo-fdm-dhbw.png"
    },
    {
        "title": "DHBW Lörrach",
        "description": "DHBW Lörrach",
        "curation_policy": "Standard",
        "website": "https://dhbw-loerrach.de/home",
        "visibility": "public",
        "record_policy": "open",
        "member_policy": "open",
        "slug": "dhbw-loerrach",
        "logo_path": "/opt/invenio/src/static/images/logo-fdm-dhbw.png"
    },
    {
        "title": "DHBW Mosbach",
        "description": "DHBW Mosbach",
        "curation_policy": "Standard",
        "website": "https://www.mosbach.dhbw.de",
        "visibility": "public",
        "record_policy": "open",
        "member_policy": "open",
        "slug": "dhbw-mosbach",
        "logo_path": "/opt/invenio/src/static/images/logo-fdm-dhbw.png"
    },
    {
        "title": "DHBW Ravensburg",
        "description": "DHBW Ravensburg",
        "curation_policy": "Standard",
        "website": "https://www.ravensburg.dhbw.de/startseite",
        "visibility": "public",
        "record_policy": "open",
        "member_policy": "open",
        "slug": "dhbw-ravensburg",
        "logo_path": "/opt/invenio/src/static/images/logo-fdm-dhbw.png"
    },
    {
        "title": "DHBW Villingen-Schwenningen",
        "description": "DHBW Villingen-Schwenningen",
        "curation_policy": "Standard",
        "website": "https://www.dhbw-vs.de",
        "visibility": "public",
        "record_policy": "open",
        "member_policy": "open",
        "slug": "dhbw-villingen-schwenningen",
        "logo_path": "/opt/invenio/src/static/images/logo-fdm-dhbw.png"
    },
    {
        "title": "DHBW Heilbronn",
        "description": "DHBW Heilbronn",
        "curation_policy": "Standard",
        "website": "https://www.heilbronn.dhbw.de",
        "visibility": "public",
        "record_policy": "open",
        "member_policy": "open",
        "slug": "dhbw-heilbronn",
        "logo_path": "/opt/invenio/src/static/images/logo-fdm-dhbw.png"
    },
    {
        "title": "DHBW Karlsruhe",
        "description": "DHBW Karlsruhe",
        "curation_policy": "Standard",
        "website": "https://www.karlsruhe.dhbw.de/startseite.html",
        "visibility": "public",
        "record_policy": "open",
        "member_policy": "open",
        "slug": "dhbw-karlsruhe",
        "logo_path": "/opt/invenio/src/static/images/logo-fdm-dhbw.png"
    }
]

# Ausführen für alle Communities
for community in communities:
    create_community(community)
