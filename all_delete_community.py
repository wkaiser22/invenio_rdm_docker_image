from invenio_app.factory import create_app
from invenio_access.permissions import system_identity
from invenio_communities.proxies import current_communities

def main():
    app = create_app()
    app.app_context().push()

    identity = system_identity

    # Alle Communities abrufen (paginieren falls viele)
    search_result = current_communities.service.search(identity=identity)

    total = 0
    for result in search_result.hits:
        community_id = result["id"]
        slug = result["slug"]
        try:
            current_communities.service.delete(identity=identity, id_=community_id)
            print(f"Community '{slug}' gelöscht.")
            total += 1
        except Exception as e:
            print(f"Fehler beim Löschen von '{slug}': {str(e)}")

    print(f"Insgesamt gelöscht: {total} Communities")

if __name__ == "__main__":
    main()
