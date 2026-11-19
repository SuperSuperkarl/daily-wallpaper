# Daily Wallpaper

Ein automatisch wechselndes iPhone-Sperrbildschirm-Bild. Die Bereitstellung läuft über GitHub Pages und die vorhandene Apple-Kurzbefehle-Automation.

## Status

- GitHub Pages: eingerichtet, unter `https://supersuperkarl.github.io/daily-wallpaper/lockscreen.png`
- GitHub Actions: Veröffentlichung bei Push, manuellem Start und täglich um **04:05 UTC** (05:05 Uhr MEZ / 06:05 Uhr MESZ)
- KI-Bilder: **vorbereitet**, aber nur mit separat kostenpflichtigem OpenAI-API-Zugriff aktivierbar
- Ohne API-Schlüssel wird das vorhandene Bild beibehalten bzw. das Demo-Bild erzeugt; es erfolgt **kein** kostenpflichtiger API-Aufruf.
- ChatGPT-Aufgaben können die Bildergalerie nicht dokumentiert direkt und autonom in dieses Repository synchronisieren.

## Einmalige Einrichtung für automatisch generierte Bilder

1. Bei https://platform.openai.com/api-keys einen API-Schlüssel anlegen. OpenAI API ist **nicht** im ChatGPT-Plus-Preis enthalten. Vorher Budget-/Ausgabenlimit im OpenAI-API-Projekt konfigurieren.
2. In diesem Repository **Settings → Secrets and variables → Actions** öffnen.
3. Unter **Repository secrets → New repository secret** den Namen `OPENAI_API_KEY` eintragen und den API-Schlüssel als Wert hinterlegen. **Niemals in GitHub-Dateien, Issues oder Chats veröffentlichen.**
4. Den Workflow unter **Actions → Publish wallpaper to GitHub Pages → Run workflow** einmal manuell ausführen.
5. Nach erfolgreichem Lauf die öffentliche Bild-URL mit `?v=2` aufrufen, damit der Browser nicht das alte Bild aus dem Cache nutzt.
6. Danach läuft die Generierung täglich vor dem iPhone-Kurzbefehl. Hinweis: GitHub-Schedule-Jobs können sich verzögern; der Zeitplan ist keine harte Echtzeitgarantie.

## Bestehender iPhone-Kurzbefehl

Der Kurzbefehl ruft täglich das Bild von
`https://supersuperkarl.github.io/daily-wallpaper/lockscreen.png`
ab und legt es als Sperrbildschirm fest. Für Cache-Busting empfiehlt sich, den Parameter `?v=` plus das aktuelle Datum im Format `yyyyMMdd` dynamisch anzuhängen.

## Technische Dateien

- `.github/workflows/publish.yml`: tägliche KI-Generierung und GitHub-Pages-Veröffentlichung
- `scripts/generate_wallpaper.py`: OpenAI-Images-API, PNG-Ausgabe `public/lockscreen.png`
- `scripts/create_demo_wallpaper.py`: kostenfreies Testbild, solange keine PNG-Datei vorhanden ist
- `public/index.html`: öffentliche Bildvorschau

Das Bild selbst und die GitHub-Pages-Website sind **öffentlich**, da das Repository öffentlich ist. Keine privaten oder sensiblen Motive hochladen.

## Fehlerdiagnose

Unter **Actions** den letzten Lauf öffnen. Wenn die API-Konfiguration fehlt, zeigt der Schritt "Generate new wallpaper" die Meldung, dass der Schlüssel fehlt. Fehler bei Quota, API-Modell oder Abrechnung erscheinen dort. Bei einem API-Fehler wird das bisherige Bild beibehalten.

## Kosten

GitHub Pages und der Workflow sind im Rahmen der jeweiligen GitHub-Freikontingente nutzbar. Die OpenAI-API-Bildgenerierung verursacht separat nutzungsabhängige Kosten. Das verwendete Standardmodell ist `gpt-image-2.5-flare` mit Qualität `medium` und Größe `1024x1536`; bei Bedarf in der Workflow-Datei ändern.
