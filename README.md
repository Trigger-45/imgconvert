# 📸 imgconvert – Dein Bild, dein Format, deine Größe!

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

## 📜 Lizenz
Dieses Projekt steht unter der [MIT-Lizenz](LICENSE).


