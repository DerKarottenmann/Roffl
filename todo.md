# Roffl – TODO / Roadmap

Priorisierte Vorschläge für die Weiterentwicklung. Strukturiert in drei Phasen: Foundation (muss kommen, bevor die 8 Differenzierungs-Features Sinn ergeben), Differenzierer (die im README beschriebenen 8 Features) und Polish.

---

## Phase 1 – Foundation

Ohne diese Schritte hat Roffl kein soziales Fundament. Die 8 Features bauen alle darauf auf.

- [ ] **Öffentliche Projekt-Detailseite** (`/project/<id>`)
  - Zeigt Projekt-Steckbrief + alle Posts chronologisch (= erste Form von Feature 2 „Timeline").
  - Für jeden sichtbar (auch ausgeloggt? Entscheidung treffen).
  - Posts im Mainpage-Feed müssen auf die Projekt-Seite verlinken.
- [ ] **Öffentliches User-Profil** (`/user/<username>`)
  - Liste der Projekte eines Users; Einstiegspunkt zum späteren Folgen.
- [ ] **Posts im Feed mit Projekt-Kontext**
  - Aktuell zeigt `index.html` nur Titel + Text + Username. Projekt-Name als klickbares Label ergänzen (`entry.project.name`).
- [ ] **Edit / Delete für eigene Posts und Projekte**
  - Aktuell ist alles unveränderlich — schon ein Tippfehler ist permanent.
  - Routen `/post/<id>/edit`, `/post/<id>/delete`, analog für Projekte.
- [ ] **Follow-System**
  - Neues Modell `Follow(follower_id, target_user_id)` oder `ProjectFollow(follower_id, project_id)`.
  - Feed-Modus „nur meine Abos" auf der Mainpage.
  - Kern-Mechanik für „Social Motivation" aus dem README-Pitch.
- [ ] **Kommentare / Reactions**
  - Modell `Comment(entry_id, owner_id, text, created_at)`.
  - Likes als zweite Stufe (`Like(user_id, entry_id)`).
  - Voraussetzung für Feature 3 (Lösungs-Sektionen).

---

## Phase 2 – Differenzierer (die 8 Features)

Reihenfolge: aufsteigend nach Aufwand / Abhängigkeiten.

### Feature 1 – Festes Post-Format (Steckbrief)
- [ ] `Entry`-Modell um strukturierte Felder erweitern (Migration nötig):
  - `done` (was wurde gemacht), `next` (was als Nächstes), `problems` (offene Probleme), `mood`/`progress`-Score.
  - Optional: zusätzlich ein „Freitext"-Feld behalten für unstrukturierte Notizen.
- [ ] Create-Formular und Templates anpassen, Posts einheitlich rendern.
- [ ] Migration via Alembic, alte Posts: `done = bisheriger text`, restliche Felder nullable.

### Feature 2 – Timeline pro Projekt
- [ ] Auf der Projekt-Detailseite Posts als vertikale Timeline rendern (Datum-Achse, Karten links/rechts oder einzeln chronologisch).
- [ ] Aggregations-Insights anzeigen: Posts pro Woche, längste Pause, Streak.
- [ ] Sortier-/Filter-Optionen (nur Posts mit Bildern, nur mit offenen Problemen, …).

### Feature 3 – Lösungs-Sektionen
- [ ] Setzt Kommentar-System aus Phase 1 voraus.
- [ ] Kommentare erhalten Typ-Tag: `comment` vs. `solution`.
- [ ] Auf Posts mit `problems`-Feld eigene „Lösungen"-Sektion rendern; gefilterte Kommentar-Ansicht.
- [ ] Ersteller kann eine vorgeschlagene Lösung als „angenommen" markieren — sichtbares Badge.

### Feature 5 – Projekt-Rating (Auto-Score)
- [ ] Faktoren definieren (Fortschrittsgeschwindigkeit = Posts/Woche, Risiken = Anzahl ungelöster `problems`, Schwierigkeit = Community-Bewertung).
- [ ] Tagging für „Schwierigkeitsgrad" durch Follower (Skala 1–5, Median).
- [ ] Score-Komponente serverseitig berechnen, im Projekt-Header anzeigen.
- [ ] Erstmal simple Heuristik, später ggf. tunen.

### Feature 7 – Project-Challenges
- [ ] Modell `Challenge(project_id, author_id (user|bot), title, description, deadline, status)`.
- [ ] UI auf der Projekt-Seite: offene Challenges + abgeschlossene.
- [ ] Annahme / Ablehnung durch den Projekt-Owner; bei Annahme verlinkbar mit einem Post.
- [ ] Vorbereitung für Feature 4 (Bots als Challenge-Quelle).

### Feature 8 – Cooperation-Funktion
- [ ] Modell `HelpOffer(project_id, user_id, message, status)` für „ich biete Hilfe an".
- [ ] Modell / Flag `looking_for_collaborators` am `Project`.
- [ ] Discover-Seite `/cooperate` mit Projekten, die Mitstreiter suchen.
- [ ] Privates Messaging (späte Phase) oder zunächst nur Kontakt via Profil-E-Mail.

### Feature 6 – Project-Blueprint (Fork / Clone)
- [ ] `Project.parent_id` ergänzen (Self-FK) für Fork-Beziehung.
- [ ] Fork-Aktion: kopiert Projekt-Stammdaten, kopiert optional Initial-Posts; neuer Owner, Referenz zum Original.
- [ ] „Forks of this project"-Liste auf der Projekt-Detailseite.
- [ ] Klären: dürfen Forks gelöscht werden, wenn das Original entfernt wird? (vermutlich ja, Beziehung lösen statt kaskadieren).

### Feature 4 – Bots
- [ ] Letztes Feature, weil aufwendig: braucht stabile Foundation + Domänen-Modelle.
- [ ] Bot-User-Typ: `User.is_bot`-Flag, kein Login, generiert über interne API/Worker.
- [ ] Erste Bot-Idee: „Cheerleader"-Bot, der gefolgte Projekte kommentiert, wenn länger als X Tage kein Post.
- [ ] Zweite Bot-Idee: „Researcher"-Bot, der zu in `problems` genannten Begriffen Quellen vorschlägt (LLM-Integration → separate Architektur-Entscheidung).
- [ ] Dritte Bot-Idee: „Challenger"-Bot, der für Feature 7 Challenges generiert.

---

## Phase 3 – Polish & Infrastruktur

- [ ] **Search / Discovery:** Volltextsuche über Projekte, Tags pro Projekt.
- [ ] **Bilder ins Filesystem / Objekt-Storage** statt SQLite-LargeBinary (DB wird sonst riesig, Backups schmerzhaft).
- [ ] **Rate-Limiting** auf `create_post` / `create_projects` / `signup`.
- [ ] **E-Mail-Verifikation** beim Signup.
- [ ] **Passwort-Reset-Flow.**
- [ ] **Pagination** auf der Mainpage (aktuell `.limit(10)` hart).
- [ ] **Mobile-Pass** über alle Seiten (Top-Leiste, Statistics, Create-Forms).
- [ ] **Tests:** mindestens Smoke-Tests pro Route mit Flask-Test-Client.

---

## Bekannte Bugs / kleine Aufräumarbeiten

- [ ] `create_project` redirected zur Mainpage statt zu einer „Mein Projekt" / Statistics-Seite — UX-Bruch.
- [ ] Kein Auth-Guard auf `/create_projects` GET (Form ist erreichbar ohne Login, POST würde an `owner_id=None` scheitern).
- [ ] `Entry.title`-Länge nicht validiert (DB-Limit 200, kein Server-Check).
- [ ] Im SSE-Stream wird `dic` initial geyieldet, auch wenn leer, aber das Initial-Pull-Verzweig setzt `last_id = 0` nur im Else — Logik prüfen.
- [ ] `/image/<id>` antwortet immer mit `Content-Type: image/jpeg`, auch wenn PNG hochgeladen wurde. MIME-Type aus Bilddaten ableiten oder beim Upload speichern.
