# Täglicher persönlicher Gedanke – iPhone Any Text

Dieses Repository stellt **nur einen kurzen Text** für das Sperrbildschirm-Widget **Any Text** auf dem iPhone bereit. Es wird **kein Hintergrundbild** generiert oder gewechselt.

## Ablauf

1. Eine geplante ChatGPT-Aufgabe erstellt täglich einen **neuen, individuell formulierten Gedanken** auf Basis der zuletzt abgeschlossenen Morgen- und Abendroutinen.
2. ChatGPT aktualisiert über die verbundene GitHub-Integration `public/daily-text.txt` auf `main` (eine Zeile mit abschließendem Zeilenumbruch).
3. Ein Push auf `main` veröffentlicht die Datei automatisch über GitHub Pages.
4. Der bestehende iPhone-Kurzbefehl ruft um **05:00 Uhr (Europe/Berlin)** die öffentliche Textdatei ab und setzt den Text im **Any Text**-Widget.

**Text-URL:** https://supersuperkarl.github.io/daily-wallpaper/daily-text.txt

**Vorschau:** https://supersuperkarl.github.io/daily-wallpaper/

## Datenschutz

Das Repository und GitHub Pages sind öffentlich. Keine Namen, Beziehungsdetails, intimen Inhalte oder Gesundheitsdaten in die Textdatei schreiben. Geeignet sind wenige allgemeine, persönlich passende Wörter.

## Grenzen

- Die ChatGPT-Aufgabe soll den Text vor 05:00 Uhr veröffentlichen. Unbeaufsichtigte GitHub-Schreibzugriffe aus geplanten Aufgaben sind nicht garantiert; die Ausführung und den Commit bei Problemen prüfen.
- GitHub Pages kann zeitversetzt ausliefern; die iOS-Anzeige kann zwischengespeicherte Inhalte verwenden.
- Bei einem Fehler bleibt der letzte erfolgreich veröffentlichte Text erhalten.
- Es ist **keine** OpenAI-API-Abrechnung oder GitHub-interne Spruchliste nötig.

Der GitHub-Actions-Workflow veröffentlicht ausschließlich die Dateien aus `public/`. Er wählt und generiert keine Gedanken selbst.
