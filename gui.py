import sys
from PySide6.QtCore import Qt
from PySide6.QtGui import QPixmap
from PySide6.QtWidgets import (
    QApplication, QWidget, QLabel, QPushButton, QRadioButton,
    QComboBox, QLineEdit, QGroupBox, QHBoxLayout, QVBoxLayout, QScrollArea
)
import tkinter
from tkinter import filedialog
import imgconvert
import textwrap


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

        self.info_selected_file = QLabel("No file selected")
        self.info_selected_file.setWordWrap(True)
        self.info_selected_file.setFixedWidth(300)
        self.info_selected_file.setTextInteractionFlags(Qt.TextSelectableByMouse)
        controls_layout.addWidget(self.info_selected_file)

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
        self.label.setFixedSize(300, 200)
        self.label.setAlignment(Qt.AlignCenter)

        # ScrollArea, falls Bild zu groß ist
        scroll_area = QScrollArea()
        scroll_area.setWidgetResizable(True)
        scroll_area.setWidget(self.label)

        # --- Hauptlayout zusammenfügen ---
        main_layout.addLayout(controls_layout)
        main_layout.addWidget(scroll_area)

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
                self.show_image()
            else:
                self.file_path = ""
                self.info_selected_file.setText("No file selected")
        else:
            folder_path = filedialog.askdirectory()
            if folder_path:
                self.file_path = folder_path
                self.info_selected_file.setText(self.file_path)
            else:
                self.file_path = ""
                self.info_selected_file.setText("No file selected")

    def show_image(self):
        if not self.file_path:
            return
        pixmap = QPixmap(self.file_path)
        scaled = pixmap.scaled(self.label.width(), self.label.height(),
                               Qt.KeepAspectRatio, Qt.SmoothTransformation)
        self.label.setPixmap(scaled)

    def convert_image(self):
        if not self.file_path:
            self.info_selected_file.setText("No file selected")
            return

        if self.factor_radio.isChecked():
            try:
                factor = float(self.factor_input.text()) if self.factor_input.text() else 1.0
            except ValueError:
                factor = 1.0
            imgconvert.convert_image(self.file_path, self.get_format(), factor, None)
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


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec())
