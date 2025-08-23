import sys
from PySide6.QtCore import Qt
from PySide6.QtGui import QPixmap, QImage
from PySide6.QtWidgets import (
    QApplication, QWidget, QLabel, QPushButton, QRadioButton,
    QComboBox, QLineEdit, QGroupBox, QHBoxLayout, QVBoxLayout, QScrollArea, QMessageBox
)
import tkinter
from tkinter import filedialog
import imgconvert
import textwrap
from PIL import Image
import os

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        # State-Variablen
        self.name = "File"
        self.file_path = ""
        self.format = "PNG"
        self.setWindowTitle("ImgConvert")
        self.resize(700, 400)

        # ---------------- Layouts ----------------
        main_layout = QHBoxLayout(self)  # Hauptlayout: links Controls, rechts Bild

        # --- Linke Seite (Controls) ---
        controls_layout = QVBoxLayout()

        # Radio-Buttons File/Folder
        file_radio = QRadioButton("Single File")
        folder_radio = QRadioButton("Folder")
        file_radio.setChecked(True)
        file_radio.clicked.connect(lambda: (self.save_name("File"), self.update_button_text()))
        folder_radio.clicked.connect(lambda: (self.save_name("Folder"), self.update_button_text()))

        controls_layout.addWidget(file_radio)
        controls_layout.addWidget(folder_radio)

        # Button zum Auswählen
        self.button = QPushButton(f"Select {self.get_name()}")
        self.button.setStyleSheet("""
            QPushButton {
                background-color: #D3D3D3;
                color: black;
                border-radius: 20px;
                padding: 10px 20px;
                font-size: 14px;
            }
            QPushButton:hover {
                background-color: #0056b3;
                color: white;
            }
        """)
        self.button.clicked.connect(self.select_input)
        controls_layout.addWidget(self.button)

        # Info-Label
        self.info = QLabel("Selected:")
        controls_layout.addWidget(self.info)

        self.info_selected_file = QLabel("Nothing selected")
        self.info_selected_file.setWordWrap(True)
        self.info_selected_file.setFixedWidth(300)
        self.info_selected_file.setTextInteractionFlags(Qt.TextSelectableByMouse)

        self.info_selected_file_size = QLabel("Size: Unknown")


        controls_layout.addWidget(self.info_selected_file)
        controls_layout.addWidget(self.info_selected_file_size)

        # Format-Label + Combobox
        format_layout = QHBoxLayout()
        format_label = QLabel("Format")
        combobox2 = QComboBox()
        combobox2.addItems(["PNG", "JPG", "WEBP", "GIF", "JPEG", "BMP"])
        combobox2.currentTextChanged.connect(self.set_format)
        format_layout.addWidget(format_label)
        format_layout.addWidget(combobox2)
        controls_layout.addLayout(format_layout)

        # --- Resize Group ---
        resize_group = QGroupBox("Resize")
        resize_group.setFixedSize(250, 100)

        # Option 1: Factor
        self.factor_radio = QRadioButton("By Factor")
        self.factor_input = QLineEdit()
        self.factor_input.setPlaceholderText("e.g. 0.5 for 50%")
        factor_layout = QHBoxLayout()
        factor_layout.addWidget(self.factor_radio)
        factor_layout.addWidget(self.factor_input)

        # Option 2: Width/Height
        self.wh_radio = QRadioButton("By Width/Height")
        self.width_input = QLineEdit()
        self.width_input.setPlaceholderText("Width")
        self.height_input = QLineEdit()
        self.height_input.setPlaceholderText("Height")
        wh_layout = QHBoxLayout()
        wh_layout.addWidget(self.wh_radio)
        wh_layout.addWidget(self.width_input)
        wh_layout.addWidget(self.height_input)

        resize_layout = QVBoxLayout()
        resize_layout.addLayout(factor_layout)
        resize_layout.addLayout(wh_layout)
        resize_group.setLayout(resize_layout)
        controls_layout.addWidget(resize_group)

        # Convert-Button
        self.convert = QPushButton("Convert")
        self.convert.setStyleSheet("""
            QPushButton {
                background-color: #0056b3;
                color: white;
                border-radius: 20px;
                padding: 10px 20px;
                font-size: 14px;
            }
            QPushButton:hover {
                background-color: #28a745;
            }
        """)
        self.convert.clicked.connect(self.convert_image)
        controls_layout.addWidget(self.convert)

        controls_layout.addStretch()  # Abstand nach unten

        # --- Rechte Seite (Bild) ---
        self.label = QLabel()
        self.label.setMinimumHeight(200)
        self.label.setMinimumWidth(300)
        self.label.setAlignment(Qt.AlignCenter)

        # ScrollArea, falls Bild zu groß ist
        self.scroll_area = QScrollArea()
        self.scroll_area.setWidgetResizable(True)
        self.scroll_area.setWidget(self.label)

        # --- Hauptlayout zusammenfügen ---
        main_layout.addLayout(controls_layout)
        main_layout.addWidget(self.scroll_area)

        self.show()

    # ---------------- Methoden ----------------
    def save_name(self, name):
        self.name = name

    def get_name(self):
        return self.name

    def set_format(self, format):
        self.format = format

    def get_format(self):
        return self.format

    def update_button_text(self):
        self.button.setText(f"Select {self.get_name()}")

    def select_input(self):
        tkinter.Tk().withdraw()
        if self.get_name() == "File":
            path = filedialog.askopenfilename(
                filetypes=[("Images", "*.png *.jpg *.jpeg *.bmp *.gif *.jpeg")]
            )
            if path:
                self.file_path = path
                wrapped_text = "\n".join(textwrap.wrap(self.file_path, width=50))
                self.info_selected_file.setText(wrapped_text)

                # Größe auslesen und im Label anzeigen
                with Image.open(self.file_path) as img:
                    width, height = img.size
                    self.info_selected_file_size.setText(f"Size: {width} x {height}")

                self.show_image()
            else:
                self.file_path = ""
                self.info_selected_file.setText("No File selected")
                self.info_selected_file_size.setText("Size: Unknown")
        else:
            folder_path = filedialog.askdirectory()
            if folder_path:
                self.file_path = folder_path
                self.info_selected_file.setText(self.file_path)
                self.info_selected_file_size.setText("Size: N/A (folder)")
                self.show_image()
            else:
                self.file_path = ""
                self.info_selected_file.setText("No Folder selected")
                self.info_selected_file_size.setText("Size: Unknown")


    def show_image(self):
        if not self.file_path:
            return

        if os.path.isdir(self.file_path):
            files = [f for f in os.listdir(self.file_path) if f.lower().endswith((".jpg", ".jpeg", ".png", ".webp", ".bmp", ".gif"))]

            container = QWidget()
            vbox = QVBoxLayout(container)

            for f in files:
                img_path = os.path.join(self.file_path, f)
                img = QImage(img_path)
                lbl = QLabel()
                lbl.setPixmap(QPixmap.fromImage(img).scaledToWidth(300, Qt.SmoothTransformation))  # Skaliert
                vbox.addWidget(lbl)

            self.scroll_area.setWidget(container)
        else:
            pixmap = QPixmap(self.file_path)
            scaled = pixmap.scaled(self.label.width(), self.label.height(),
                                Qt.KeepAspectRatio, Qt.SmoothTransformation)
            self.label.setPixmap(scaled)

    def convert_image(self):
        if not self.file_path:
            self.info_selected_file.setText("No file or folder selected")
            return

        if os.path.isdir(self.file_path):  # 🟢 Ordner
            for file in os.listdir(self.file_path):
                if file.lower().endswith((".jpg", ".jpeg", ".png", ".webp", ".bmp", ".gif")):
                    imgconvert.convert_image(
                        os.path.join(self.file_path, file),
                        self.get_format(),
                        float(self.factor_input.text()) if self.factor_radio.isChecked() and self.factor_input.text() else 1.0,
                        (int(self.width_input.text()), int(self.height_input.text())) if self.wh_radio.isChecked() and self.width_input.text() and self.height_input.text() else None
                    )
            msgBox = QMessageBox()
            msgBox.setText("Convertion successful")
            msgBox.exec()
        else:  # 🟢 Einzeldatei
            if self.factor_radio.isChecked():
                try:
                    factor = float(self.factor_input.text()) if self.factor_input.text() else 1.0
                except ValueError:
                    factor = 1.0
                imgconvert.convert_image(self.file_path, self.get_format(), factor, None)
            
                msgBox = QMessageBox()
                msgBox.setText("Convertion successful")
                msgBox.exec()
            elif self.wh_radio.isChecked():
                try:
                    width = int(self.width_input.text()) if self.width_input.text() else 0
                    height = int(self.height_input.text()) if self.height_input.text() else 0
                except ValueError:
                    width, height = 0, 0
                if width > 0 and height > 0:
                    imgconvert.convert_image(self.file_path, self.get_format(), None, (width, height))
                else:
                    imgconvert.convert_image(self.file_path, self.get_format(), 1.0, None)
            else:
                imgconvert.convert_image(self.file_path, self.get_format(), 1.0, None)
            msgBox = QMessageBox()
            msgBox.setText("Convertion successful")
            msgBox.exec()


def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec())
