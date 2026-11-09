# Protex – Freigabematrix für Dateioperationen

Diese Referenz konkretisiert die Schutzregeln aus SKILL.md. Sie erweitert niemals die vom Nutzer erteilten Berechtigungen.

## Freigabematrix

| Aktion | Standard | Erforderliches Vorgehen |
|---|---|---|
| Datei oder Verzeichnis lesen | Erlaubt, wenn aufgabenbezogen | Relevante Inhalte prüfen und Geheimnisse schützen |
| Im ausdrücklich freigegebenen Bereich bearbeiten | Erlaubt | Kleinstmöglichen Patch anwenden und Diff kontrollieren |
| Andere Datei bearbeiten | Nicht erlaubt | Zweck erklären und Freigabe einholen |
| Neue, ausdrücklich verlangte Datei anlegen | Erlaubt | Zielpfad prüfen; nichts überschreiben |
| Zusätzliche, nicht verlangte Datei anlegen | Nur bei zwingender Notwendigkeit | Notwendigkeit erklären und vorher Zustimmung einholen |
| Vorhandene Datei überschreiben | Bestätigung erforderlich | Exakten Pfad und Verlust des bisherigen Inhalts nennen |
| Datei löschen | Bestätigung erforderlich | Exakten Pfad und Folge nennen; auf Bestätigung warten |
| Datei verschieben oder umbenennen | Bestätigung erforderlich | Quell- und Zielpfad nennen; auf Bestätigung warten |
| Paket installieren oder Abhängigkeit ändern | Nicht automatisch erlaubt | Zweck, Quelle und mögliche Auswirkungen erklären |
| Datenbank ändern oder Migration ausführen | Nicht automatisch erlaubt | Auswirkungen und mögliche Datenverluste prüfen; Zustimmung einholen |
| Deployment, Release, Push oder Veröffentlichung | Nicht automatisch erlaubt | Ziel und externe Auswirkungen nennen und vorher bestätigen lassen |

## Gültige Bestätigung

Eine Bestätigung muss sich eindeutig auf die beschriebene Aktion beziehen. Zum Beispiel:

„Darf ich src/legacy_cache.py löschen? Die Datei wird dadurch aus dem Projekt entfernt.“

Eine allgemeine Bitte zur Fehlerbehebung, Optimierung oder Fertigstellung ist keine Freigabe zum Löschen. Eine Freigabe für eine Datei gilt nicht für andere Dateien.

## Sichere Alternativen

- Statt Löschen zuerst dokumentieren, warum eine Datei möglicherweise ungenutzt ist.
- Statt eine ganze Datei zu ersetzen, einen gezielten Patch vorschlagen.
- Statt git reset --hard den Git-Status und den Diff lesend prüfen.
- Statt automatisch Abhängigkeiten zu entfernen, ihre Nutzung analysieren.
- Statt eine Datenbankmigration sofort auszuführen, ihren Plan und ihre Auswirkungen anhand von Testdaten prüfen.

## Git-Schutz

Vor einer Änderung:
1. git status --short prüfen.
2. git diff -- prüfen.
3. Nur freigegebene Dateien bearbeiten.
4. Abschließenden Diff prüfen und fremde Änderungen erhalten.

Verwirf uncommittete Änderungen niemals ohne konkrete Freigabe. Dazu gehören insbesondere git reset --hard, git clean -fd, git checkout -- und git restore.
