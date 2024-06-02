# To-Do-Listen Verwaltung in einer WebApp (Bereitstellung über Raspberry Pi)

## Überblick

Die ToDo-Listen-Verwaltung Web-App ermöglicht es Benutzern, To-Do-Listen und -Einträge zu erstellen, zu aktualisieren, zu löschen und abzurufen. Diese Web-App stellt eine RESTful API zur Verfügung, die mithilfe von Flask implementiert wurde.

## Hauptfunktionen

- **List Management**
  - Erstellen neuer To-Do-Listen
  - Abrufen aller To-Do-Einträge einer bestimmten Liste
  - Löschen einer To-Do-Liste

- **Entry Management**
  - Hinzufügen neuer Einträge zu einer Liste
  - Aktualisieren vorhandener Einträge
  - Löschen vorhandener Einträge

## Ausrollen der Web-App mit Docker

Um die Web-App auf einem Raspberry Pi bereitzustellen, wird Docker verwendet. Folgen Sie diesen Schritten um die Web-App auszurollen:

### Vorbereitungen

1. **Installieren von Docker auf dem Raspberry Pi**

   Zunächst müssen Sie Docker auf Ihrem Raspberry Pi installieren. Verbinden Sie ihren Pi dazu mit einem Internetfähigen Netzwerk. Führen Sie dazu über Bash die folgenden Befehle aus:

   curl -sSL <https://get.docker.com> | sh
   sudo usermod -aG docker pi

   (Bitte entfernen Sie die <> an der URL bevor Sie den Befehl verwenden)

2. **Installieren von Docker Compose**

    Installieren Sie Docker Compose, um den bereitgestellten Container zu orchestrieren. Führen Sie dazu über Bash die folgenden Befehle aus:

    sudo apt-get install -y python3-pip
    sudo pip3 install docker-compose

3. **Bereitstellung der Web-App**

    - Kopieren Sie alle Dateien des Repositories, einschließlich der docker-compose.yml, auf die Micro-SD-Karte.
    - Setzen Sie die Micro-SD-Karte in den Raspberry Pi ein und starten Sie ihn. Wechseln Sie über den Befehl cd in das Verzeichnis, das die docker-compose.yml Datei enthält, und führen Sie, um die Web-App im Hintergrund zu starten, den folgenden Befehl aus:

    sudo docker-compose up -d

### Zugriff auf die Web-App

    Die Web-App ist jetzt bereit und kann über den Swagger-Editor aufgerufen und getestet werden. Öffnen Sie den Swagger-Editor unter 'editor.swagger.io' in Ihrem Browser und kopieren Sie den Inhalt der Specification_ToDo.yaml in den Editor. Die API-Spezifikation wird geladen und Sie können die Endpunkte der Listenverwaltung testen.
