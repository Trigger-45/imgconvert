<h1 align="center">📸 imgconvert</h1>
<p align="center"><i>Dein Bild, dein Format, deine Größe!</i></p>

<p align="center">
  <img src="https://img.shields.io/badge/status-CLI_done-brightgreen" alt="CLI Status">
  <img src="https://img.shields.io/badge/status-GUI_in_progress-yellow" alt="GUI Status">
  <img src="https://img.shields.io/badge/license-MIT-blue" alt="License">
</p>

---

**imgconvert** ist ein leichtgewichtiges, ultraschnelles CLI-Tool, mit dem du Bilder **konvertieren, verkleinern, vergrößern und in neue Formate umwandeln** kannst – alles mit nur einem einzigen Befehl.  
Egal ob JPG zu PNG, PNG zu WEBP oder gleich ein ganzer Ordner voll – **imgconvert** macht’s in Sekunden.

---


## Project Files & Features 📂

| Datei / Feature | Status |
|-----------------|--------|
| `imgconvert.py` | ![Done](https://img.shields.io/badge/status-done-brightgreen) |
| `gui.py` | ![In Progress](https://img.shields.io/badge/status-in_progress-yellow) |

## ✨ Features

- 🔄 **Format wechseln** – JPG → PNG, PNG → WEBP, BMP → JPG … was du willst.
- 📏 **Größe ändern** – prozentual oder direkt auf feste Breite/Höhe.
- 📂 **Batch-Modus** – kompletten Ordner voller Bilder in einem Rutsch konvertieren.
- 🛠 **Simpel & schnell** – nur ein paar Argumente und los geht’s.
- 💡 **Kein Photoshop nötig** – CLI reicht völlig.

---

## 🚀 Installation

1. **Repository klonen**  
   ```bash
   git clone https://github.com/Trigger-45/imgconvert.git
   cd imgconvert
   ```
2. **Abhängigkeiten installieren**
    ```bash
    pip install -r requirements.txt
    ```

---


## ⚙️ Tool einrichten (optional)

### 💻 Windows – EXE erstellen und PATH hinzufügen

1. EXE mit PyInstaller erstellen
    1. Öffne die Eingabeaufforderung (CMD) oder PowerShell.
    2. Navigiere in dein Projektverzeichnis:
    ```bash
    cd C:\Pfad\zu\imgconvert
    ```
    3. Erstelle die ausführbare Datei
    ```bash
    pyinstaller --onefile imgconvert.py
    ```
    - --onefile → alles in einer Datei
    - Die EXE landet danach in dist\imgconvert.exe.
2. Ordner zum PATH hinzufügen
    1.  Drücke Win + S, tippe Systemumgebungsvariablen und öffne „Systemumgebungsvariablen bearbeiten“.

    2. Klicke unten auf „Umgebungsvariablen…“.

    3. Suche in Systemvariablen nach Path → Bearbeiten.

    4. Klicke Neu → füge C:\Pfad\zu\dist ein → OK schließen.

    5. CMD/PowerShell neu starten, damit die Änderung aktiv wird.

3. EXE von überall aufrufen

    - Jetzt kannst du das Tool von jedem Verzeichnis aus nutzen
    - Die EXE ist jetzt global verfügbar, kein Python mehr nötig

### 🐧 Linux – EXE erstellen und PATH hinzufügen

1. EXE mit PyInstaller erstellen

    1. Öffne das Terminal.
    2. Navigiere in dein Projektverzeichnis:
    ```bash
    cd /pfad/zu/imgconvert
    ```
    3. Erstelle die ausführbare Datei:
    ```bash
    pyinstaller --onefile imgconvert.py
    ```
    - Die fertige EXE landet danach in dist/imgconvert.

2. Ausführbar machen
```bash
chmod +x dist/imgconvert
```
- Das macht die Datei ausführbar

3. Ordner zum PATH hinzufügen
    - Damit du sie von überall aufrufen kannst, füge einfach den dist/-Ordner deinem PATH hinzu:
    ```bash
    echo 'export PATH="/pfad/zu/imgconvert/dist:$PATH"' >> ~/.bashrc
    source ~/.bashrc
    ```
    - Ersetze /pfad/zu/imgconvert durch den absoluten Pfad zu deinem Projekt.


4. EXE von überall aufrufen
    - Jetzt kannst du das Tool von jedem Verzeichnis aus nutzen
    - Die EXE ist jetzt global verfügbar, kein Python mehr nötig

## 🖥️ Nutzung

1. Einzelnes Bild konvertieren
    ```bash
    python main.py -i bild.png jpg
    ```
    ➡ bild.png wird zu output/bild.jpg
2.  Größe prozentual ändern
    ```bash
    python main.py -i bild.png jpg -rf 0.5
    ```
    ➡ bild.png wird zu output/bild.jpg mit 50% Größe
3. Größe auf feste Werte setzen
    ```bash
    python main.py -i bild.png jpg -rt 800 600
    ```
    ➡ bild.png wird zu output/bild.jpg mit 800x600
4. Kompletten Ordner konvertieren
    ```bash
    python imgconvert.py png -d /path/to/ordner
    ```

5. Bilder mit GUI konvertieren
    ```bash
    python imgconvert.py
    ```

> **_NOTE:_**  Wenn das Tool eingerichtet wurde (Path hinzugefügt) ändert sich nur der Anfang von `python imgconvert.py` zu `imgconvert`. Die Argumente bleiben gleich.

## ⚡ Beispiele

| Eingabe | Ausgabe | Aktion |
|---------|---------|--------|
| `-i urlaub.jpg png` | `urlaub.png` | JPG → PNG |
| `-i bild.png webp -rf 0.25` | `bild.webp` | 75% kleiner |
| `png -d ./fotos` | Alle PNGs im Output | Batch-Ordner |

---

## 🧩 Geplante Features
- [ ] Transparenz-Handling verbessern
- [ ] Exif-Daten optional erhalten
- [ ] Mehr Bildformate (TIFF, ICO, etc.)
- [ ] Vollwertige **CLI-Version** mit erweiterten Optionen
- [ ] Benutzerfreundliche **GUI-Version** für einfaches Klicken statt Tippen

---

## 📝 To-Do

- [ ] Tests für verschiedene Bildformate schreiben  
- [ ] Fehlerbehandlung verbessern (ungültige Eingaben, kaputte Dateien)  
- [ ] Logging hinzufügen (optional mit `--verbose`)  
- [ ] Performance-Benchmarking bei großen Ordnern  
- [ ] GUI weiterentwickeln und erste Beta releasen 
- [ ] Bildvorschau bei Ordner anzeigen (Gui mithilfe von QScrollArea)

---

## 📜 Lizenz
Dieses Projekt steht unter der [MIT-Lizenz](LICENSE).


