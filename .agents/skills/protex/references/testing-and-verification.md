# Protex – Test- und Verifikationsstandard

## Grundsatz

Ein Ergebnis gilt nur in dem Umfang als geprüft, in dem die entsprechenden Kontrollen tatsächlich ausgeführt wurden. Eine plausible Codeänderung ist kein Nachweis für erfolgreiche Funktion.

## Reihenfolge

1. Testumgebung erkennen: vorhandene Tests, Framework, Paketmanager, Projektanweisungen und CI-Konfiguration lesen.
2. Risiken beurteilen: prüfen, ob Tests Datenbanken, Netzwerkdienste, Konten, Kosten oder Produktivsysteme beeinflussen können.
3. Gezielte Tests für die geänderte Funktion ausführen.
4. Relevante Testsuite, Build und statische Prüfungen ausführen, sofern sicher und praktikabel.
5. Diff prüfen und sicherstellen, dass Änderungen im freigegebenen Umfang liegen.
6. Ergebnisse mit Testbefehl, Exit-Code und Einschränkungen berichten.

## Statusbegriffe

- BESTANDEN: Der konkrete Test wurde ausgeführt und endete erfolgreich.
- FEHLGESCHLAGEN: Der konkrete Test wurde ausgeführt und meldete einen Fehler oder unerwarteten Exit-Code.
- NICHT AUSGEFÜHRT: Der Test wurde nicht gestartet.
- NICHT VERFÜGBAR: Benötigtes Werkzeug, Zugang oder Testumgebung fehlt.
- NICHT VERIFIZIERT: Die Behauptung konnte mit den verfügbaren Werkzeugen nicht geprüft werden.

## Umgang mit Fehlern

- Lies Fehlermeldungen vollständig und suche die Ursache.
- Ändere nicht weitere Dateien, nur weil ein Test fehlschlägt.
- Liegt die notwendige Korrektur außerhalb des freigegebenen Umfangs, nenne die konkrete Stelle und frage nach Zustimmung.
- Wiederhole relevante Tests nach einer Korrektur.
- Berichte auch dann fehlgeschlagene Tests, wenn die Änderung plausibel aussieht.

## Abschlussbericht

Nenne:
- geänderte Dateien und konkrete Änderungen;
- tatsächlich ausgeführte Testkommandos mit Ergebnissen;
- nicht ausgeführte oder nicht verifizierbare Prüfungen samt Grund;
- verbleibende Einschränkungen.

Erfinde keine Testausgaben oder Beispielresultate und stelle sie nicht als echte Ergebnisse dar.
