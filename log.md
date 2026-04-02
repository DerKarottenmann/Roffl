19. März 2026
- Grundlagen HTML, CSS und Flask erarbeitet. Erste Tests mit Routen und Templates ausgeführt.

20.–21. März 2026
- Feste obere Leiste (`top_panel`) und Logo hinzugefügt.
- Basis-Styling (`static/style/main.css`) eingerichtet (Hintergrund, Farben, Leistenhöhe).

22. März 2026
- `base.html` als globales Layout eingerichtet; Inhalts-Templates erstellt.
- Create-Button (`+`) in Top-Leiste integriert.

23. März 2026
- Sign-up Formular angelegt; Datenbank-Modelle und Alembic-Migrationen vorbereitet.

24. März 2026
- Header-Aktionen in Container `.top_actions` gruppiert, damit Logo links und Aktionen rechts stehen.
- `base.html` strukturell angepasst: Aktionsgruppe mit `create_button` und `prlink`.
- `static/style/main.css` erweitert:
  - `.top_panel`: Padding/Höhe optimiert, `box-sizing` gesetzt.
  - `.top_actions`: Flex-Container mit gap und Ausrichtung.
  - `.create_button`: rundes Icon-Design (40×40), Hover-Effekte und Schatten.
  - `.top_panel .prlink`: weißer Link mit Umrandung und Hover-Hintergrund.
  - `.content`: `margin-top` erhöht (80px) um Überlappung zu vermeiden.
  - Media Query für kleine Bildschirme (Größen/Padding).
- Verifikation: Server neu starten und Hard-Refresh; erwartetes Layout: Logo links, runder `+`-Button und `Sign Up` rechts; Inhalt nicht überlappt.

19. März 2026
- Grundlagen HTML/CSS/Flask gelernt.

20.–21. März 2026
- Top-Leiste und Logo hinzugefügt.

22. März 2026
- Templates strukturiert; Create-Button ergänzt.

23. März 2026
- Sign-up begonnen; Datenbank-Modelle und Migrationen vorbereitet.

24. März 2026
- Top-Leiste, Create-Button und Sign-Up-Link angelegt und initial gestylt.
- Aktionen in `top_actions` gruppiert und CSS aktualisiert (runder Create-Button, responsive Anpassungen).

28/29. März 2026
- Login-System gebaut(ohne Sessions)
- CSS für Login
- url-for gelernt und eingebaut

31. März 2026
- Schutzfunktion gegen XSS, SQL Injection
- Cookies mit Session ID
- Grundlegendes LoginSys fertig

1. April 2026
- Create Button funktioniert
- "Formular" für die Projektideen ausführbar und wird gespeichert
- CSS für Login verbessert
