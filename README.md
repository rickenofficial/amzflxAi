# New AI for Reading Prices, Scrolling, and Selecting Blocks

## Description

This project implements an artificial intelligence (AI) designed to detect prices in screenshots, automatically scroll, and select blocks that meet certain price criteria. The project uses Tesseract OCR for optical character recognition and PyAutoGUI for graphical interface automation.

## Project Structure

mi_bot/ ├── .venv/ │ ├── Lib/ │ ├── Scripts/ │ ├── .gitignore │ ├── pyvenv.cfg├── main.py├── requirements.txt├── utils.py├── README.md├── config.py├── data/ ├── models/ ├── notebooks/ ├── tests/


## Requirements

- Python 3.12 or higher
- Tesseract OCR
- Python Libraries: PyAutoGUI, Pytesseract, Pillow

## Installation

### Step 1: Clone the Repository

Clone this repository to your local machine:

```bash
git clone https://github.com/YOUR_USERNAME/YOUR_REPOSITORY.git
cd YOUR_REPOSITORY
```
### Step 2: Create and Activate a Virtual Environment
Create and activate a virtual environment to manage dependencies:

python -m venv .venv
source .venv/bin/activate  # On Windows use: .venv\Scripts\activate

### Step 3: Install Dependencies
Install the necessary dependencies using requirements.txt:
```
pip install -r requirements.txt
```
### Step 4: Install Tesseract OCR:

Download and install Tesseract OCR from UB Mannheim.

## Usage

### Configure Tesseract OCR

If Tesseract is not installed in the default path, make sure to configure the correct path in your Python code:

```typescript
import pytesseract from 'pytesseract';
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe';
```

Run the Main Script
To run the main script and start detecting prices, scrolling, and selecting blocks:

import { exec } from 'child_process';

exec('python main.py', (error, stdout, stderr) => {
    if (error) {
        console.error(`Error: ${error.message}`);
        return;
    }
    if (stderr) {
        console.error(`Stderr: ${stderr}`);
        return;
    }
    console.log(`Output: ${stdout}`);
});

## Contributions

Contributions are welcome. Please follow these steps:

1. Fork the repository
2. Create a new branch (`git checkout -b feature/new-feature`)
3. Make your changes (`git commit -am 'Add new feature'`)
4. Push the branch (`git push origin feature/new-feature`)
5. Create a Pull Request

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.

## Contact

If you have any questions or suggestions, feel free to contact the repository administrator.

Thank you for your interest in this project!


