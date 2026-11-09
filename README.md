# Protex

**Careful changes. Protected files. Verified results.**

Protex ist ein Agent Skill für sorgfältige und nachvollziehbare Code- und Projektarbeit. Er legt einen klaren Arbeitsstandard fest: erst verstehen, dann nur den freigegebenen Bereich ändern, vorhandene Dateien schützen, echte Tests ausführen und Ergebnisse ehrlich berichten.

## Direktzugriff

- **[Protex auf GitHub öffnen](https://github.com/SPX8k/Protex/tree/main/.agents/skills/protex)**
- **[SKILL.md direkt öffnen (Raw-Link)](https://raw.githubusercontent.com/SPX8k/Protex/main/.agents/skills/protex/SKILL.md)**

Der Raw-Link ist die direkte Textdatei des Skills. Du kannst ihn einer KI geben, die externe Links lesen kann.

## Schnellinstallation für unterstützte Agenten

Voraussetzung: Node.js und npm müssen installiert sein.

Installiere Protex aus GitHub in das aktuell geöffnete Projekt:

```bash
npx skills add https://github.com/SPX8k/Protex/tree/main/.agents/skills/protex
```

Installiere Protex stattdessen global für deinen Benutzer:

```bash
npx skills add https://github.com/SPX8k/Protex/tree/main/.agents/skills/protex --global
```

Der Installer fragt gegebenenfalls, für welchen Agenten und in welchem Umfang der Skill installiert werden soll. Prüfe die Auswahl, bevor du sie bestätigst. Die CLI unterstützt direkte GitHub-Verzeichnispfade und installiert Skills in die vom jeweiligen Agenten unterstützten Skill-Verzeichnisse. Siehe die [offizielle CLI-Dokumentation](https://www.skills.sh/docs/cli).

## Verwendung mit ChatGPT über den GitHub-Link

Kopiere diesen Auftrag in einen Chat, in dem die KI externe Links öffnen kann:

```text
Bitte öffne und lies den vollständigen Protex-Skill über diesen Raw-GitHub-Link:

https://raw.githubusercontent.com/SPX8k/Protex/main/.agents/skills/protex/SKILL.md

Verwende die darin enthaltenen Regeln für meine Programmier-, Fehlerbehebungs- und Dateiänderungsaufgaben in dieser Unterhaltung. Lies auch die referenzierten Dateien aus dem GitHub-Repository, wenn sie für die Aufgabe benötigt werden.

Behaupte nicht, den Skill gelesen zu haben, wenn du den Link nicht tatsächlich öffnen konntest. Bitte mich in diesem Fall um die SKILL.md-Datei.
```

**Wichtig:** Einen GitHub-Link in einen normalen Chat einzufügen ist keine dauerhafte Installation. Die KI muss den Link tatsächlich abrufen können. OpenAI beschreibt eigenständige Skills für die ChatGPT-Desktop-App, Codex CLI und IDE-Erweiterung; für die Verteilung in ChatGPT Chat und Work über Web und Mobilgeräte ist laut OpenAI die Verpackung als Plugin vorgesehen. Siehe [OpenAI: Skills erstellen und verwenden](https://learn.chatgpt.com/docs/build-skills).

## Verwendung mit Codex

### In diesem Repository

Codex erkennt projektbezogene Skills unter `.agents/skills/`. Klone dieses Repository und öffne den Repository-Ordner als Arbeitsverzeichnis. Protex liegt dann unter:

```text
.agents/skills/protex/SKILL.md
```

Falls der Skill nach dem Öffnen nicht angezeigt wird, starte Codex neu. Du kannst ihn in Codex auch mit `$protex` explizit aufrufen, sobald er installiert und erkannt wurde.

### Installation über den Codex Skill Installer

Öffne Codex und starte den eingebauten Skill Installer mit:

```text
$skill-installer
```

Bitte den Installer anschließend, den Skill aus diesem GitHub-Verzeichnis zu installieren:

```text
https://github.com/SPX8k/Protex/tree/main/.agents/skills/protex
```

## Verwendung mit GitHub Copilot

Das Repository enthält `.github/copilot-instructions.md`. Diese Datei weist GitHub Copilot an, bei Programmier-, Fehlerbehebungs-, Test- und Dateiänderungsaufgaben zuerst den vollständigen Protex-Skill zu lesen und anzuwenden.

Der Skill selbst liegt unter `.agents/skills/protex/`. GitHub Copilot unterstützt Skills in diesem Projektverzeichnis. Weitere Informationen: [GitHub-Dokumentation zu Agent Skills](https://docs.github.com/en/copilot/how-tos/copilot-on-github/customize-copilot/customize-cloud-agent/add-skills).

## Für alle eigenen Projekte unter Windows

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

Starte den Agenten danach neu, falls der Skill noch nicht angezeigt wird.

## Für Linux und macOS

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

## Was Protex festlegt

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
│   ├── copilot-instructions.md
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

Protex ist eine Arbeitsanweisung, keine technische Sandbox. Er macht ein Modell nicht unfehlbar und kann keine höherrangigen System-, Sicherheits- oder Plattformregeln überschreiben. Tatsächliche Datei- und Systemberechtigungen müssen zusätzlich durch die verwendete Agent-Umgebung begrenzt werden. Ob ein Host Skills lädt und wann er sie auswählt, hängt von der jeweiligen Agent-Umgebung ab.

## Lizenz

Dieses Projekt steht unter der MIT-Lizenz. Siehe [LICENSE](LICENSE).
