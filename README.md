# Daily Wallpaper / Daily Text

Persönlicher täglicher Text für ein Any-Text-Widget auf dem iPhone-Sperrbildschirm.

## Gewünschter Ablauf

1. Eine **geplante ChatGPT-Aufgabe** versucht jeden Morgen um **04:10 Europe/Berlin**, einen neuen kurzen Satz aus den jüngsten Morgen- und Abendroutinen zu formulieren. Es gibt keine vorgefertigte Spruchliste.
2. Die Aufgabe versucht, mit der verbundenen GitHub-Integration `public/daily-text.txt` zu überschreiben und den erfolgreichen Commit zu prüfen.
3. Der GitHub-Pages-Workflow veröffentlicht bei jedem Push die Datei öffentlich unter `https://supersuperkarl.github.io/daily-wallpaper/daily-text.txt`.
4. Ein vorhandener iPhone-Kurzbefehl liest täglich um **05:00 Uhr** die Textdatei und aktualisiert **Any Text** auf dem Sperrbildschirm.

**Wichtig:** Der erste unbeaufsichtigte ChatGPT-Aufgabenlauf und dessen GitHub-Schreibzugriff sind noch nicht bestätigt. Ein einzelner funktionierender Chat-Commit garantiert nicht, dass die Automationsausführung den GitHub-Connector ebenfalls aufrufen darf. Bei Fehlern bleibt der zuletzt gespeicherte Satz stehen. Die Aufgabe läuft um 04:10 Uhr, also **vor** der jeweiligen Morgenroutine; sie verwendet die jüngsten bereits abgeschlossenen Routinen.

## Datenschutz

Dieses Repository und seine GitHub-Pages-Seite sind öffentlich. Es dürfen nur kurze, allgemein formulierte Stärkungssätze veröffentlicht werden. Keine Namen, intime Details, konkreten Beziehungsereignisse, Gesundheits- oder anderen privaten Inhalte. Die Routinegespräche selbst bleiben außerhalb des Repositorys.

## GitHub Pages

`https://supersuperkarl.github.io/daily-wallpaper/daily-text.txt`

Der Workflow `.github/workflows/publish.yml` führt **keine** tägliche Spruchauswahl mehr aus, sondern veröffentlicht nur die jeweils neu gespeicherten Dateien bei Commit oder manuellem Start. Das Bild `lockscreen.png` bleibt davon unberührt.

## Weitere Dateien

`scripts/generate_wallpaper.py` ist ein früherer, **nicht zeitgesteuerter** Versuch für API-Bildgenerierung. Für den Textbetrieb wird kein OpenAI-API-Schlüssel gebraucht.
