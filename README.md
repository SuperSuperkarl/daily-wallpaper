# Daily Wallpaper

Automatisches Hintergrundbild für den iPhone-Sperrbildschirm, bereitgestellt über GitHub Pages.

## Stand

- GitHub-Pages-Deployment per GitHub Actions ist eingerichtet.
- Solange `public/lockscreen.png` noch fehlt, erstellt das Deployment ein **lokal berechnetes Testbild** (kein ChatGPT-Bild).
- Die automatische Übertragung von ChatGPT-generierten Bildern aus einer geplanten ChatGPT-Aufgabe ist **noch nicht bestätigt**.
- Das Bild wird über `https://supersuperkarl.github.io/daily-wallpaper/lockscreen.png` bereitgestellt, **sobald Pages aktiviert ist und das Deployment erfolgreich läuft**.

## GitHub Pages aktivieren

1. Repository **Settings → Pages** öffnen.
2. Unter **Build and deployment → Source** die Option **GitHub Actions** wählen.
3. Unter **Actions** den Workflow **Publish wallpaper to GitHub Pages** gegebenenfalls einmal über **Run workflow** starten.
4. Nach erfolgreichem Lauf die Bild-URL im Browser prüfen.

## iPhone-Kurzbefehl (nach Aktivierung von Pages)

1. In **Kurzbefehle** einen neuen Kurzbefehl erstellen.
2. Aktion **URL**: `https://supersuperkarl.github.io/daily-wallpaper/lockscreen.png?refresh=2026` (bei täglicher Verwendung besser `Aktuelles Datum` als Query-Parameter einsetzen).
3. Aktion **Inhalt von URL abrufen**; Methode `GET`.
4. Optional: erhaltenes Bild vor der Übernahme mit **Schnellansicht** testen; danach für unbeaufsichtigten Betrieb entfernen.
5. Aktion **Hintergrundbild festlegen** mit dem abgerufenen Bild; **Sperrbildschirm** wählen und Bestätigungs-/Vorschauoptionen, sofern angeboten, deaktivieren.
6. Unter **Automation → Tageszeit** eine tägliche Ausführung einstellen und, sofern verfügbar, **Sofort ausführen** aktivieren.

Hinweis: Die Bezeichnungen einzelner Kurzbefehle-Aktionen können je nach iOS-Version abweichen. Prüfe die erste Ausführung am iPhone, bevor du eine unbeaufsichtigte Automation verwendest.

## Eigenes Bild hochladen

Wenn die Datei `public/lockscreen.png` im Repository liegt, liefert GitHub Pages **dieses Bild** statt des Testbilds aus. Mit einem neuen Commit startet die Veröffentlichung automatisch erneut.

Öffentliches Repository und öffentliches GitHub Pages: Keine sensiblen persönlichen Bilder veröffentlichen.
