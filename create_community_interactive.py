from invenio_app.factory import create_app
from invenio_access.permissions import system_identity
from invenio_communities.proxies import current_communities
import slugify  # Optional, um Slugs zu erzeugen (oder selbst bauen)

app = create_app()
app.app_context().push()

def create_community(title, description, curation_policy, website,
                     visibility, record_policy, member_policy, slug, organizations, about_community):
    identity = system_identity
    community_data = {
        "access": {
            "visibility": visibility,
            "record_policy": record_policy,
            "member_policy": member_policy
                },
        "slug": slug,
        "metadata": {
            "title": title,
            "description": description,
            "curation_policy": curation_policy,
            "page": about_community, 
            "website": website,
            "organizations": organizations
            }
        }
    created = current_communities.service.create(identity=identity, data=community_data)
    print(f"Community '{title}' erstellt mit ID: {created['id']}")

# Beispiel Organisation (nur Felder, die erlaubt sind)
organizations = [
    {
        "name": "DHBW Mannheim"
        # "acronym", "identifiers", "links" weglassen, da unbekannt
    }
]

create_community(
    title="DHBW Mannheim",
    description="Forschung an der DHBW Mannheim",
    curation_policy="Standard",
    website="https://www.dhbw-mannheim.de",
    visibility="public",
    record_policy="open",
    member_policy="open",
    slug="dhbw-mannheim",
    organizations=organizations,
    about_community="Information for my community."
)






organizations = [
    {
        "name": "DHBW Stuttgart",
        # "acronym", "identifiers", "links" weglassen, da unbekannt
    }
]

create_community(
    title="DHBW Stuttgart",
    description="DHBW Stuttgart",
    curation_policy="Standard",
    website="https://www.dhbw-stuttgart.de",
    visibility="public",
    record_policy="open",
    member_policy="open",
    slug="dhbw-stuttgart",
    organizations=organizations,
    about_community="Information for my community."
)



organizations = [
    {
        "name": "DHBW Heidenheim",
        # "acronym", "identifiers", "links" weglassen, da unbekannt
    }
]

create_community(
    title="DHBW Heidenheim",
    description="DHBW Heidenheim",
    curation_policy="Standard",
    website="https://www.heidenheim.dhbw.de/startseite",
    visibility="public",
    record_policy="open",
    member_policy="open",
    slug="dhbw-heidenheim",
    organizations=organizations,
    about_community="Information for my community."
)


organizations = [
    {
        "name": "DHBW Lörrach",
        # "acronym", "identifiers", "links" weglassen, da unbekannt
    }
]

create_community(
    title="DHBW Lörrach",
    description="DHBW Lörrach",
    curation_policy="Standard",
    website="https://dhbw-loerrach.de/home",
    visibility="public",
    record_policy="open",
    member_policy="open",
    slug="dhbw-loerrach",
    organizations=organizations,
    about_community="Information for my community."
)



organizations = [
    {
        "name": "DHBW Mosbach",
        # "acronym", "identifiers", "links" weglassen, da unbekannt
    }
]

create_community(
    title="DHBW Mosbach",
    description="DHBW Mosbach",
    curation_policy="Standard",
    website="https://www.mosbach.dhbw.de",
    visibility="public",
    record_policy="open",
    member_policy="open",
    slug="dhbw-mosbach",
    organizations=organizations,
    about_community="Information for my community."
)


organizations = [
    {
        "name": "DHBW Ravensburg",
        # "acronym", "identifiers", "links" weglassen, da unbekannt
    }
]

create_community(
    title="DHBW Ravensburg",
    description="DHBW Ravensburg",
    curation_policy="Standard",
    website="https://www.ravensburg.dhbw.de/startseite",
    visibility="public",
    record_policy="open",
    member_policy="open",
    slug="dhbw-ravensburg",
    organizations=organizations,
    about_community="Information for my community."
)


organizations = [
    {
        "name": "DHBW Villingen-Schwenningen",
        # "acronym", "identifiers", "links" weglassen, da unbekannt
    }
]

create_community(
    title="DHBW Villingen-Schwenningen",
    description="DHBW Villingen-Schwenningen",
    curation_policy="Standard",
    website="https://www.dhbw-vs.de",
    visibility="public",
    record_policy="open",
    member_policy="open",
    slug="dhbw-villingen-schwenningen",
    organizations=organizations,
    about_community="Information for my community."
)


organizations = [
    {
        "name": "DHBW Heilbronn",
        # "acronym", "identifiers", "links" weglassen, da unbekannt
    }
]

create_community(
    title="DHBW Heilbronn",
    description="DHBW Heilbronn",
    curation_policy="Standard",
    website="https://www.heilbronn.dhbw.de",
    visibility="public",
    record_policy="open",
    member_policy="open",
    slug="dhbw-heilbronn",
    organizations=organizations,
    about_community="Information for my community."
)


organizations = [
    {
        "name": "DHBW Karlsruhe",
        # "acronym", "identifiers", "links" weglassen, da unbekannt
    }
]

create_community(
    title="DHBW Karlsruhe",
    description="DHBW Karlsruhe",
    curation_policy="Standard",
    website="https://www.karlsruhe.dhbw.de/startseite.html",
    visibility="public",
    record_policy="open",
    member_policy="open",
    slug="dhbw-Karlsruhe",
    organizations=organizations,
    about_community="Information for my community."
)

