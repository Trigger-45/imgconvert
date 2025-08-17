import sys
from PySide6.QtCore import Qt
from PySide6.QtGui import QPixmap
from PySide6.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QRadioButton
import tkinter
from tkinter import filedialog

    


def open_file_explorer():
    tkinter.Tk().withdraw() # prevents an empty tkinter window from appearing

    file_path = filedialog.askopenfilename()



def open_folder_explorer():
    tkinter.Tk().withdraw() # prevents an empty tkinter window from appearing

    folder_path = filedialog.askdirectory()




class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        # Initialisiere self.name
        self.name = "File"  # Standardwert
        self.file_path = ""
        self.label = QLabel(self)
        # self.label.move(150, 10, 200)  # Position des Labels im Fenster
        self.label.setGeometry(300, 10, 300, 200)  # Position + Größe

        # Fenster-Einstellungen
        self.setWindowTitle("ImgConvert")
        self.resize(700, 400)  # Fenstergröße einstellen

        # Position des Fensters auf dem Bildschirm (zentriert)
        screen = QApplication.primaryScreen()
        screen_geometry = screen.geometry()
        window_geometry = self.geometry()

        # Berechnung der Position, um das Fenster zu zentrieren
        x = (screen_geometry.width() - window_geometry.width()) // 2
        y = (screen_geometry.height() - window_geometry.height()) // 2
        self.move(x, y)

        # Radio-Buttons für "Single File" und "Folder"
        file_radio = QRadioButton("Single File", self)
        folder_radio = QRadioButton("Folder", self)

        file_radio.setChecked(True)  # standardmäßig aktiv

        # Verbinde die Radio-Buttons mit der save_name-Methode und Button-Textaktualisierung
        file_radio.clicked.connect(lambda: (self.save_name("File"), self.update_button_text()))
        folder_radio.clicked.connect(lambda: (self.save_name("Folder"), self.update_button_text()))

        file_radio.move(10, 10)  # Position des Radio-Buttons im Fenster
        folder_radio.move(10, 40)  # Position des Radio-Buttons im Fenster

        # Button zum Auswählen von Dateien oder Ordnern
        self.button = QPushButton(f"Select {self.get_name()}", self)
        self.button.setStyleSheet("""
            QPushButton {
                background-color: #D3D3D3;   /* Light Grey */
                color: black;
                border-radius: 20px;        
                padding: 10px 20px;
                font-size: 14px;
                min-width: 80px;
                min-height: 20px;
            }
            QPushButton:hover {
                background-color: #0056b3;
            }
        """)
        self.button.move(10, 100)  # Position des Buttons im Fenster
        self.button.clicked.connect(self.select_input)  


        label = QLabel("Format", self)
        label.move(300, 220)  

        # Fenster anzeigen
        self.show()

    # Methode zum Setzen des Namens basierend auf der Auswahl
    def save_name(self, name):
        self.name = name

    # Methode zum Abrufen des Namens
    def get_name(self):
        return self.name

    # Methode zum Aktualisieren des Button-Texts
    def update_button_text(self):
        self.button.setText(f"Select {self.get_name()}")

    def select_input(self):
        tkinter.Tk().withdraw()
        if self.get_name() == "File":
            path = filedialog.askopenfilename(filetypes=[("Images", "*.png *.jpg *.jpeg *.bmp *.gif")])
            if path:
                self.file_path = path
                self.show_image()
        else:
            folder_path = filedialog.askdirectory()

    def show_image(self):
        pixmap = QPixmap(self.file_path)
        # Bild passend ins Label skalieren
        scaled = pixmap.scaled(self.label.width(), self.label.height(),
                            Qt.KeepAspectRatio, Qt.SmoothTransformation)
        self.label.setPixmap(scaled)
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec())
