# Roffl – Entwicklungsprotokoll

## 19. März 2026

- Grundlagen HTML, CSS und Flask erarbeitet; erste Tests mit Routen und Templates durchgeführt.

## 20.–21. März 2026

- Feste obere Leiste (`.top_panel`) und Logo hinzugefügt.
- Basis-Styling in `static/style/main.css` eingerichtet (Hintergrund, Farben, Leistenhöhe).

## 22. März 2026

- `base.html` als globales Layout eingerichtet; Inhalts-Templates erstellt.
- Create-Button (`+`) in die Top-Leiste integriert.

## 23. März 2026

- Sign-up-Formular angelegt; Datenbankmodelle (`User`, `Entry`) und Alembic-Migrationen vorbereitet.

## 24. März 2026

- Header-Aktionen in `.top_actions` gruppiert: Logo links, Aktionen rechts.
- `base.html` strukturell angepasst: Aktionsgruppe mit `.create_button` und `.prlink`.
- `static/style/main.css` erweitert:
  - `.top_panel`: Padding/Höhe optimiert, `box-sizing` gesetzt.
  - `.top_actions`: Flex-Container mit `gap` und Ausrichtung.
  - `.create_button`: rundes Icon-Design (40×40 px), Hover-Effekte und Schatten.
  - `.top_panel .prlink`: weißer Link mit Umrandung und Hover-Hintergrund.
  - `.content`: `margin-top` auf 80 px erhöht, um Überlappung mit der Top-Leiste zu vermeiden.
  - Media Query für kleine Bildschirme (Größen/Padding).

## 28.–29. März 2026

- Login-System implementiert (noch ohne Sessions).
- CSS für die Login-Seite gestaltet.
- `url_for` kennengelernt und in Templates eingebaut.

## 31. März 2026

- XSS-Schutz durch Jinja2-Autoescaping; SQL-Injection-Schutz durch SQLAlchemy-ORM.
- Cookie-basiertes Session-System implementiert: Flask speichert `session["user_id"]`, `session["username"]` und `session["logged_in"]` (signiert via `app.secret_key`).
- Routen `/login`, `/logout` und `/signup` vollständig funktionsfähig.

## 1. April 2026

- Route `/create` (POST) funktioniert: Formular für Projektideen wird verarbeitet und als `Entry`-Objekt in der Datenbank gespeichert.
- Validierung: Textfeld muss mindestens 25 Zeichen enthalten; bei Verstoß wird eine `flash`-Meldung ausgegeben und zur `/create`-Seite zurückgeleitet.
- CSS für die Login-Seite verbessert.

## 2. April 2026

- Bild-Upload implementiert: mehrere Bilder gleichzeitig hochladbar via `request.files.getlist('images')`.
- Bilder werden als `LargeBinary` im `Image`-Modell (Feld `data`) gespeichert und über `db.session.flush()` dem zugehörigen `Entry` zugeordnet.
- Alembic-Migration `b10b07e4560c` erstellt die Tabellen `users`, `entries` und `images`.
- Route `/image/<int:image_id>` liefert gespeicherte Bilder aus (`get_image`).

## 3. April 2026

- Klickbares Home-Icon implementiert (verlinkt zur Route `/` / `Mainpage`).
- Projektideen werden auf der Hauptseite (`index.html`) über `Entry.query.order_by(Entry.created_at.desc()).limit(10)` geladen und angezeigt.

## 4. April 2026

- Seitenanzeige in der Top-Leiste ergänzt.
- Einarbeitung in JavaScript begonnen.
- Projektweiterplanung.

## 5. April 2026

- Weitere JS-Einarbeitung.
- Dropdown-Menü für den eingeloggten Benutzer in `static/js/main.js` implementiert: Der `#user_dropdown`-Button toggelt `#dropdown_menu` über `classList.toggle("show")`; ein Klick außerhalb des Menüs schließt es wieder.

## 7. April 2026

- Website auf lokalem Raspberry Pi gehostet.
- Nginx und Uvicorn eingerichtet und konfiguriert.
- App als systemd-Dienst registriert → dauerhaft online.

## 12. April 2026

- Bugfix am Create-Button.
- WebSockets recherchiert (Einarbeitung).
