"""Publish a short, human-readable daily thought for Any Text.

All phrases were written in ChatGPT during setup; this script rotates the
curated collection for free without using an OpenAI API key.
"""
from __future__ import annotations

import hashlib
from datetime import datetime
from pathlib import Path
from zoneinfo import ZoneInfo

THOUGHTS = [
    "Heute darf ein kleiner Schritt genügen.",
    "Du darfst freundlich mit dir sein.",
    "Nicht alles braucht heute eine Antwort.",
    "Deine Bedürfnisse haben ihren Platz.",
    "Du kannst neu beginnen, auch ganz leise.",
    "Ein ruhiger Moment gehört auch dir.",
    "Du musst nicht alles zugleich schaffen.",
    "Was dir guttut, darf wichtig sein.",
    "Heute zählt auch das Unscheinbare.",
    "Ein Schritt nach dem anderen reicht.",
    "Du darfst deine Grenzen achten.",
    "Ein guter Tag braucht keine Perfektion.",
    "Deine Zeit ist wertvoll.",
    "Du darfst innehalten und weitergehen.",
    "Auch langsam ist eine Richtung.",
    "Heute darfst du auf dich hören.",
    "Nicht jede Frage muss sofort geklärt sein.",
    "Du bist mehr als deine Aufgaben.",
    "Ruhe ist kein Stillstand.",
    "Wähle heute, was wirklich zählt.",
    "Du darfst dir Leichtigkeit erlauben.",
    "Deine Gefühle dürfen Raum haben.",
    "Ein neuer Tag, ein neuer Anfang.",
    "Du kannst mit dem beginnen, was da ist.",
    "Manches wächst in kleinen Schritten.",
    "Du darfst auch etwas liegen lassen.",
    "Heute darf einfach heute sein.",
    "Dein Tempo ist in Ordnung.",
    "Achte auf einen guten Augenblick.",
    "Was dir wichtig ist, verdient Zeit.",
    "Du darfst dich selbst ernst nehmen.",
    "Ein bisschen Mut kann genügen.",
    "Du musst dich nicht beeilen.",
    "Heute ist Raum für etwas Gutes.",
    "Gönn dir einen Moment ohne Müssen.",
    "Auch eine Pause kann ein Fortschritt sein.",
    "Du darfst klar und freundlich sein.",
    "Ein kleiner Anfang kann viel bewegen.",
    "Wichtiges darf in Ruhe entstehen.",
    "Du kannst heute gut für dich sorgen.",
    "Du darfst Hilfe annehmen.",
    "Es muss nicht alles perfekt sein.",
    "Dein Blick auf dich darf sanft sein.",
    "Ein Atemzug. Dann der nächste Schritt.",
    "Du darfst Nein sagen und Ja meinen.",
    "Heute beginnt mit einer Möglichkeit.",
    "Auch Ungewissheit darf da sein.",
    "Du darfst stolz auf kleine Schritte sein.",
    "Nicht alles liegt in deiner Hand.",
    "Heute gehört auch ein Moment dir.",
]

def daily_text(now: datetime) -> str:
    # Daily rotation, including a year-specific offset; stable for one day.
    date_key = now.date().isoformat().encode("utf-8")
    index = int.from_bytes(hashlib.sha256(date_key).digest()[:8], "big") % len(THOUGHTS)
    return THOUGHTS[index]

def main() -> None:
    now = datetime.now(ZoneInfo("Europe/Berlin"))
    path = Path("public/daily-text.txt")
    path.parent.mkdir(parents=True, exist_ok=True)
    phrase = daily_text(now)
    path.write_text(phrase + "\n", encoding="utf-8")
    print("Published daily text for", now.date().isoformat(), "-", phrase)

if __name__ == "__main__":
    main()
