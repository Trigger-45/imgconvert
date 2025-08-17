import os
import argparse
import subprocess
from PIL import Image

# ArgumentParser für Kommandozeilenargumente
parser = argparse.ArgumentParser()
parser.add_argument("-i", "--image_path", help="Pfad zum Bild")
parser.add_argument("-o", "--output_format", help="Ziel-Format (z. B. jpg, png)")
parser.add_argument("-rf", "--resize_factor", type=float, default=1.0, help="Faktor zur Größenänderung (z. B. 0.5 für 50%)")
parser.add_argument("-rt","--resize_to", type=int, nargs=2, metavar=("WIDTH", "HEIGHT"), help="Größe ändern auf (Breite, Höhe)")
parser.add_argument("-d", "--directory", help="Ordner mit Bildern konvertieren")
args = parser.parse_args()

def convert_image(image_path, output_format, resize_factor=1.0, resize_to=None):
    img = Image.open(image_path).convert("RGB")

    if resize_to: 
        img = img.resize(resize_to)
    elif resize_factor != 1.0:
        new_size = (int(img.width * resize_factor), int(img.height * resize_factor))
        img = img.resize(new_size)

    output_name = os.path.splitext(os.path.basename(image_path))[0]
    output_path = f"output/{output_name}.{output_format.lower()}"

    os.makedirs("output", exist_ok=True)
    img.save(output_path)

def main():
    # Wenn Argumente übergeben werden, führe das Bildkonvertierungs-Programm aus
    if len(os.sys.argv) > 1:
        path = args.image_path
        fmt = args.output_format
        factor = args.resize_factor
        size = args.resize_to

        if args.directory:
            for file in os.listdir(args.directory):
                if file.lower().endswith((".jpg", ".jpeg", ".png", ".webp", ".bmp", ".gif")):
                    convert_image(os.path.join(args.directory, file), fmt, resize_factor=factor, resize_to=size)
        else:
            convert_image(path, fmt, resize_factor=factor, resize_to=size)

    # Wenn keine Argumente übergeben werden, starte die GUI
    else:
        subprocess.run(["python", "gui.py"])

if __name__ == "__main__":
    main()
