
from utils.signature_extraction import extract_signatures
import sys
import os

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python main.py /path/to/input/image.jpg")
        sys.exit(1)

    input_image = sys.argv[1]
    output_dir = "./outputs"

    if not os.path.exists(input_image):
        print(f"Error: File '{input_image}' not found.")
        sys.exit(1)

    extract_signatures(input_image, output_dir)
    print(f"Signature extraction completed. Check the outputs directory.")
