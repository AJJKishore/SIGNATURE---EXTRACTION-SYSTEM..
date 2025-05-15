
# Signature Extraction Project

This project automates the extraction of handwritten signatures from document images using image processing techniques.

## Features
- Automated signature extraction from scanned documents
- Noise filtering for cleaner outputs
- Customizable thresholds for component size
- Scalable for batch processing

## Directory Structure
```
Signature-Extraction-Project/
├── README.md
├── requirements.txt
├── main.py
├── utils/
│   └── signature_extraction.py
├── examples/
│   └── input_image.png
├── outputs/
│   └── output_image.jpg
└── LICENSE
```

## Installation
Clone the repository and install the required packages:
```
git clone https://github.com/your-username/Signature-Extraction-Project.git
cd Signature-Extraction-Project
pip install -r requirements.txt
```

## Usage
Run the main script to extract signatures:
```
python main.py ./examples/input_image.png
```

## Example
Input Image:  
![Input Image](./examples/input_image.png)  

Output Image:  
![Output Image](./outputs/output_image.jpg)  

## License
This project is licensed under the MIT License - see the LICENSE file for details.
