# Roffl

Roffl ist eine Problem-Lösungs-Website, die ähnlich wie Reddit aus Posts von Usern besteht. Die Website ist rein für Projektideen und andere Ziele (z. B. das Trainieren auf einen Marathon) sowie natürlich deren Umsetzung gedacht. Hierbei posten die Ersteller des Projekts täglich, wöchentlich, etc. ihren Projektfortschritt, in einem einfachen und schnellen, aber informierenden Format (steckbriefähnlich), so dass man die Entwicklung des Projektes über die Zeit nachvollziehen kann. Durch bestimmte Features hebt sich Roffl von reinen Diskussionsforen wie Reddit ab. Roffl sorgt damit auch dafür, dass Ersteller zielgerichteter und produktiver sind, da sie von ihren Verfolgern motiviert werden (Social Motivation).

## Was Roffl auszeichnet

Folgende Features machen Roffl speziell für das „Posten" von Projektideen geeignet:

1. **Festes Post-Format** — jeder Post folgt der gleichen Struktur (Steckbrief). Niedriger Postaufwand für den Ersteller, einfach zu verfolgen für die Community.
2. **Timeline pro Projekt** — alle Posts eines Projekts chronologisch dargestellt, sodass die Entwicklung visuell nachvollziehbar wird.
3. **Lösungs-Sektionen** — zu jedem genannten Problem in einem Post können Mitlesende konkrete Lösungsvorschläge / Hilfestellungen anbieten.
4. **Bots** — automatisierte Verfolger, die Projekte mitverfolgen und Hilfestellungen geben können (z. B. Recherche-Vorschläge, Erinnerungen, Quellen).
5. **Projekt-Rating** — automatisch berechnetes Rating aus Faktoren wie Fortschrittsgeschwindigkeit, Risiken und Community-Einschätzung des Schwierigkeitsgrades.
6. **Project-Blueprint** — Clone-Funktion ähnlich wie auf GitHub: andere können ein Projekt forken, um eine eigene Variante, Beta-Tests oder Weiterentwicklungen zu starten.
7. **Project-Challenges** — realistische, durch Community oder Bots gestellte Herausforderungen, die das Projekt schneller pushen.
8. **Cooperation-Funktion** — Hilfe anbieten und Mitstreiter für neue gemeinsame Projekte finden.

## Tech-Stack

- **Backend:** Python 3.12, Flask, Flask-SQLAlchemy, Flask-Migrate (Alembic)
- **Datenbank:** SQLite (Datei `instance/database.db`)
- **Auth:** Cookie-basierte Sessions, signiert mit `app.secret_key` (aus `.env` über `python-dotenv`)
- **Passwörter:** Werkzeug `generate_password_hash` / `check_password_hash`
- **Frontend:** Server-rendered Jinja2-Templates, Vanilla JavaScript (`static/js/main.js`), Custom-CSS mit Design-Tokens (`static/style/main.css`)
- **Live-Updates:** Server-Sent Events (SSE) über `/stream`
- **Deployment (Raspberry Pi):** Gunicorn mit Gevent-Workern hinter Nginx, als systemd-Dienst registriert

## Datenmodell (`models.py`)

| Modell    | Felder                                                                        | Beziehungen                                          |
|-----------|-------------------------------------------------------------------------------|------------------------------------------------------|
| `User`    | `id` (UUID), `username`, `email`, `password_hash`                             | hat viele `entries`, hat viele `projects`            |
| `Project` | `id`, `name`, `description`, `owner_id`                                       | gehört zu `User`, hat viele `posts` (`Entry`)        |
| `Entry`   | `id`, `title`, `text`, `created_at`, `owner_id`, `project_id` (nullable)      | gehört zu `User` & optional zu `Project`, hat `images` |
| `Image`   | `id`, `data` (`LargeBinary`), `entry_id`                                      | gehört zu `Entry`                                    |

Bilder werden als Binärdaten direkt in der DB gespeichert (nicht auf dem Dateisystem) und über die Route `/image/<id>` ausgeliefert.

## Routen (`app.py`)

| Methode    | Pfad                  | Zweck                                                                  |
|------------|-----------------------|------------------------------------------------------------------------|
| GET        | `/`                   | Mainpage-Feed (10 neueste Posts)                                       |
| GET / POST | `/signup`             | Registrierung, loggt direkt ein                                        |
| GET / POST | `/login`              | Login                                                                  |
| GET        | `/logout`             | Session löschen                                                        |
| GET / POST | `/create_post`        | Neuen Post zu einem Projekt anlegen (Auth nötig)                       |
| GET / POST | `/create_projects`    | Neues Projekt anlegen (Auth nötig)                                     |
| GET        | `/statistics`         | Eigene Projekte mit zugehörigen Posts und Übersichts-Stats             |
| GET        | `/image/<id>`         | Liefert ein Bild aus der DB                                            |
| GET        | `/stream`             | SSE-Endpoint, streamt neue Posts als JSON                              |

## CLI-Befehle

- `flask reset-db` — droppt und re-erstellt alle Tabellen (nur Entwicklung).
- `flask dummy` — legt einen Test-User „Yan" an (Passwort aus `DUMMY` in `.env`).

## Frontend-Struktur

- `base.html` — globales Layout mit Top-Panel (Logo, Seitentitel, User-Dropdown).
- `index.html` — Mainpage-Feed.
- `create.html` / `projects.html` — Formulare für Post bzw. Projekt.
- `statistics.html` — Eigene Projekte als Karten-Grid mit Stat-Kacheln (Projekte / Posts / Bilder) und kompakter Post-Liste pro Projekt.
- `login.html` / `signup.html` / `logout.html` — Auth-Seiten.
- `static/js/main.js` — User-Dropdown-Toggle und SSE-Client.
- `static/style/main.css` — zentrales Stylesheet, Design-Tokens via CSS-Variablen (`--brand-gradient`, `--bg-card`, …).


## Für die Entwicklung

```bash
python3.12 -m venv venv
source venv/bin/activate
pip install -r requirements.txt

# .env mit SKEY (Flask-Secret) und optional DUMMY (Dummy-User-Passwort) anlegen
flask db upgrade
flask run
```

Das Entwicklungsprotokoll (chronologisch) liegt in [`log.md`](log.md).
