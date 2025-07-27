from PIL import Image
import os


def convert_image(image_path, output_format):
    img = Image.open(image_path)
    output_path = "output/converted." + output_format.lower()
    img.save(output_path)



def main():
    image_path = "Original.png"
    output_format = "jpg"  # Desired output format
    convert_image(image_path, output_format)


if __name__ == "__main__":
    main()