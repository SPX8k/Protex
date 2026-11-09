# Protex

**Careful changes. Protected files. Verified results.**

Protex ist ein Agent Skill für sorgfältige und nachvollziehbare Code- und Projektarbeit. Er legt einen klaren Arbeitsstandard fest: erst verstehen, dann nur den freigegebenen Bereich ändern, vorhandene Dateien schützen, echte Tests ausführen und Ergebnisse ehrlich berichten.

## Was Protex durchsetzt

- **Ehrlichkeit:** Keine erfundenen Erfolgsmeldungen, Testergebnisse oder Fähigkeiten.
- **Dateischutz:** Keine Datei wird ohne konkrete Bestätigung gelöscht, verschoben, umbenannt oder destruktiv ersetzt.
- **Enger Änderungsumfang:** Keine ungefragten Änderungen an anderen Dateien, Funktionen, Einstellungen oder Abhängigkeiten.
- **Vollständigkeit:** Keine stillschweigend ausgelassenen Dateien, Funktionen oder Codeabschnitte und keine Platzhalter in vollständigen Dateien.
- **Sorgfältige Arbeit:** Projekt und vorhandene Änderungen zuerst prüfen, minimale Änderungen umsetzen und Diffs kontrollieren.
- **Tests:** Passende Tests tatsächlich ausführen und genau angeben, was bestanden, fehlgeschlagen oder nicht geprüft wurde.
- **Transparenz:** Einschränkungen und zusätzliche notwendige Änderungen offen benennen.

## Projektstruktur

```text
Protex-GitHub-Project/
├── .agents/
│   └── skills/
│       └── protex/
│           ├── SKILL.md
│           ├── agents/
│           │   └── openai.yaml
│           └── references/
│               ├── safe-file-operations.md
│               └── testing-and-verification.md
├── .github/
│   └── workflows/
│       └── validate.yml
├── scripts/
│   └── validate_skill.py
├── tests/
│   └── test_validate_skill.py
├── CHANGELOG.md
├── CONTRIBUTING.md
├── LICENSE
├── SECURITY.md
└── README.md
```

## Installation in Codex

### Für dieses Repository

Codex erkennt projektbezogene Skills unter `.agents/skills/`. Öffne dieses Repository als Arbeitsverzeichnis. Falls Protex nicht in der Skill-Auswahl erscheint, starte Codex neu.

### Für alle eigenen Projekte unter Windows

Öffne PowerShell im entpackten Repository und führe Folgendes aus. Der Befehl bricht ab, falls bereits ein Protex-Ordner existiert, damit nichts überschrieben wird.

```powershell
$source = Join-Path (Get-Location) ".agents\skills\protex"
$skillsDirectory = Join-Path $HOME ".agents\skills"
$destination = Join-Path $skillsDirectory "protex"

if (-not (Test-Path $source)) {
    throw "Der Protex-Skill-Ordner wurde nicht gefunden: $source"
}

New-Item -ItemType Directory -Force -Path $skillsDirectory | Out-Null

if (Test-Path $destination) {
    throw "Protex ist bereits installiert. Der vorhandene Ordner wurde nicht verändert: $destination"
}

Copy-Item -Recurse -Path $source -Destination $destination
Write-Host "Protex wurde installiert unter: $destination"
```

Starte Codex danach neu, falls der Skill noch nicht angezeigt wird.

### Für Linux und macOS

```bash
SOURCE=".agents/skills/protex"
DESTINATION="$HOME/.agents/skills/protex"

if [ ! -d "$SOURCE" ]; then
  echo "Protex-Skill-Ordner nicht gefunden: $SOURCE" >&2
  exit 1
fi

mkdir -p "$HOME/.agents/skills"

if [ -e "$DESTINATION" ]; then
  echo "Protex ist bereits installiert. Vorhandener Ordner bleibt unverändert: $DESTINATION" >&2
  exit 1
fi

cp -R "$SOURCE" "$DESTINATION"
printf 'Protex wurde installiert unter: %s\n' "$DESTINATION"
```

## Protex verwenden

Beispiele für konkrete Aufträge:

```text
Nutze Protex. Prüfe zuerst mein Projekt und sage mir, welche Dateien für diesen Fehler relevant sind. Ändere noch nichts.
```

```text
Nutze Protex. Ändere ausschließlich die Funktion `load_config` in `src/config.py`. Andere Funktionen und Dateien bleiben unverändert. Führe passende Tests aus.
```

```text
Nutze Protex. Untersuche, warum der Test fehlschlägt. Lösche oder überschreibe keine Datei. Frage mich, bevor du Änderungen außerhalb von `src/api.py` vornimmst.
```

## Validierung und Tests

Protex benötigt zur Laufzeit keine zusätzlichen Python-Pakete. Die Projektprüfungen verwenden ausschließlich die Python-Standardbibliothek.

```bash
python scripts/validate_skill.py
python -m unittest discover -s tests -v
```

## Wichtige Grenze

Protex ist ein Satz wiederverwendbarer Agent-Anweisungen. Er macht ein Modell nicht unfehlbar und kann keine höherrangigen System-, Sicherheits- oder Plattformregeln überschreiben. Ob ein Host Skills lädt und wann er sie auswählt, hängt von der jeweiligen Agent-Umgebung ab.

## Lizenz

Dieses Projekt steht unter der MIT-Lizenz. Siehe [LICENSE](LICENSE).
