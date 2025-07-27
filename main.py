from PIL import Image
import os


def convert_image(image_path, output_format, resize_factor=1.0, resize_to=None):
    img = Image.open(image_path)

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
    path = input("Pfad zum Bild: ")
    fmt = input("Ziel-Format (z. B. jpg, png): ")
    factor = 1.0
    size = None

    factor_choice = input("Möchten Sie die Größe ändern? (ja/nein): ").strip().lower()
    if factor_choice == "ja":
        size_choice = input("Wie möchten Sie die Größe ändern angeben? (Prozent(P)/Messungen(M)): ").strip().lower()
        if size_choice == "p":
            factor = float(input("Größe in Prozent (z. B. 0.5 für 50%): "))
        elif size_choice == "m":
            width = int(input("Breite (z. B. 100 für 100px): "))
            height = int(input("Höhe (z. B. 100 für 100px): "))
            size = (width, height)

    convert_image(path, fmt, resize_factor=factor, resize_to=size)



if __name__ == "__main__":
    main()