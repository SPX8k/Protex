# Mitwirken an Protex

Danke für Beiträge zu Protex. Ziel ist es, die Regeln eindeutig, testbar und praktisch anwendbar zu halten.

## Grundsätze

- Bewahre den Fokus des Skills: Ehrlichkeit, Datei- und Datenschutz, begrenzte Änderungen und tatsächliche Verifikation.
- Ergänze keine Regel, die dem Agenten stillschweigende Lösch- oder Änderungsrechte gibt.
- Dokumentiere neue Verhaltensregeln in SKILL.md oder einer passenden Referenz.
- Vermeide Dopplungen und widersprüchliche Anforderungen.
- Behaupte nicht, dass Protex absolute Fehlerfreiheit garantiert.

## Vor einem Pull Request

Führe im Repository-Root aus:

- python scripts/validate_skill.py
- python -m unittest discover -s tests -v

Prüfe danach den Diff und stelle sicher, dass keine unbeabsichtigten Dateien geändert wurden.

## Pull Requests

Beschreibe Zweck, betroffene Dateien, ausgeführte Tests und bekannte Einschränkungen. Füge keine Zugangsdaten, Tokens oder privaten Projektdaten hinzu.
