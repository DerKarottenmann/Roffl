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

## 16. April 2026

- Recherche zu Polling, SSE und WebSockets für Live-Updates auf der Mainpage; Entscheidung für SSE.
- Wechsel von synchronem Gunicorn-Worker zu Gevent-Worker (`-w 4 -k gevent --worker-connections 1000`), `gevent` in `requirements.txt` ergänzt.
- systemd-Service `flaskapp.service` entsprechend angepasst.
- Nginx: `client_max_body_size 10M` in `sites-enabled/flaskapp` gesetzt (Fehler 413 bei Bild-Uploads behoben).
- `.env` auf dem Raspi erstellt, `SECRET_KEY` via `secrets.token_hex(16)` generiert.
- Datenbank auf dem Raspi initialisiert (`flask db upgrade`).

## 17. April 2026

- `app.secret_key` auf `os.getenv("SKEY")` umgestellt (Sessions bleiben nach Restart gültig).
- `python-dotenv` integriert.

## 18. April 2026

- SSE-Endpoint `/stream` in `app.py` implementiert: Generator-Funktion mit `yield`, `Response(..., mimetype="text/event-stream")`, Entries als JSON via `json.dumps()`.
- `with app.app_context():` hinzugefügt, damit DB-Zugriffe außerhalb der Request-Phase funktionieren.
- Client-seitig `EventSource('/stream')` in `static/js/main.js` mit `onmessage`-Handler eingebaut.
- Nginx-Buffering-Problem gelöst: `proxy_buffering off;` und `proxy_cache off;` ergänzt (Status 499 behoben).
- SSE funktioniert stabil: Daten kommen alle 5 Sekunden in der Browser-Konsole an.

## 4. Mai 2026

- Bugfix Login-Session nach Signup: In `app.py` wird nach erfolgreicher Registrierung direkt eine Session gesetzt (`session["user_id"]`, `session["username"]`, `session["logged_in"]`) und per `redirect(url_for('Mainpage'))` zur Hauptseite weitergeleitet (statt der bisherigen Klartext-Antwort).
- Neuer Flask-CLI-Befehl `flask reset-db` ergänzt: führt `db.drop_all()` und `db.create_all()` aus, um die Datenbank im Entwicklungsbetrieb schnell zurückzusetzen.
- Version in `static/js/main.js` von `0.1.1` auf `0.1.2` erhöht.

## 6.Mai

- Statistics Grundlagen gebaut

## 7. Mai 2026

- Kleinere CSS-/Layout-Iterationen an Statistics und Stylesheet.

## 9. Mai 2026

- Statistics-Skeleton ausgebaut: neue Route-Grundlage in `app.py`, Anzeige in `index.html` angepasst.
- Größere CSS-Überarbeitung in `static/style/main.css` (~165 Zeilen): Design-Tokens via CSS-Variablen, Karten-Layout, Hover-/Shadow-System für Feed-Items.
- Erste Anpassungen am SSE-Client in `static/js/main.js`.

## 11. Mai 2026

- **`Project`-Modell eingeführt (`models.py`):** neues Modell mit `name`, `description`, `owner_id`; `Entry` bekommt FK `project_id` (nullable); `User`–`Project`–`Entry`-Relationen über Backrefs.
- Neue Route `/create_projects` (`app.py`) + neues Template `templates/projects.html` zum Anlegen von Projekten.
- `create.html` zeigt Projekt-Auswahl beim Erstellen eines Posts.
- Login-Template (`login.html`) erweitert; CSS-Feintuning.

## 17. Mai 2026

- Flask-CLI-Befehl `flask dummy` ergänzt: legt einen Test-User „Yan" mit Passwort aus `.env` (`DUMMY`) an — beschleunigt das lokale Testen.

## 27. Mai 2026

- Struktur-Cleanup: ungenutztes Template `templates/description.html` entfernt; kleinere Konsolidierungen in `base.html`, `index.html`, `logout.html`, `statistics.html` und `app.py`.

## 30. Mai 2026

- `pr_backup`: breiter Zwischenstand vor weiteren Refactorings (Top-Leiste, Create-Form, Index-Feed, Statistics).
- **Projekte im Post-Formular auswählbar gemacht:** `<select name="project_id">` mit allen eigenen Projekten als Optionen (`create.html`), Server liest die Auswahl in `create_post`. ⚠️ Der gewählte `project_id` wurde aber zunächst nicht am `Entry` gespeichert (Bug) — gefixt am 9. Juni.

## 31. Mai 2026

- Statistics-Seite zeigt eigene Projekte (Skeleton): `<details>`-Akkordeon pro Projekt mit Name + Description (`statistics.html`), Route filtert nach `owner_id`.

## 9. Juni 2026

- **Bug-Fix in `create_post` (`app.py`):** beim Speichern eines neuen `Entry` wurde `project_id` ignoriert (Code las fälschlich `session.get("project")` statt aus dem Formular). Jetzt korrekt: `project = request.form.get('project_id') or None` → Posts sind tatsächlich mit ihrem Projekt verknüpft, Empty-String wird zu `NULL` (FK-sauber).
- **Statistics-Seite komplett umgebaut:**
  - Route erweitert um `total_posts` und `total_images` (server-seitige Aggregation).
  - Dashboard-Zeile mit 3 Stat-Kacheln (Projekte / Posts / Bilder).
  - `<details>`-Akkordeon entfernt; stattdessen 2-spaltiges Karten-Grid (`auto-fill, minmax(320px, 1fr)`).
  - Pro Karte: Titel + 2-zeilig geclampte Description, runde Post-Count-Badge im Brand-Gradient, kompakte Post-Liste (Titel + Datum, einzeilig, Ellipsis).
  - Empty-States für „keine Projekte" und „Projekt ohne Posts".
  - Container-Breite von 680 px auf 1080 px erhöht.
- CSS: Standard-`line-clamp` neben `-webkit-line-clamp` ergänzt (Vendor-Prefix-Warnung).
- README deutlich erweitert: Tech-Stack, Datenmodell-Tabelle, Routen-Übersicht, CLI-Befehle, Frontend-Struktur, Sicherheits-Notes. „Was Roffl auszeichnet" mit den 8 Differenzierungs-Features (festes Post-Format, Timeline, Lösungs-Sektionen, Bots, Auto-Rating, Project-Blueprint, Challenges, Cooperation).
- `todo.md` angelegt mit priorisierter Roadmap.
