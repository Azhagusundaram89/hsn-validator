# hsn-validator
# HSN Code Validator Flask App

This Flask web app allows users to validate HSN codes against a dataset loaded from an Excel file (`HSN_SAC.xlsx`). It supports validating multiple codes at once and displays their descriptions if found.

## Features

- Validates HSN codes (2 to 8 digit numeric codes)
- Supports multiple comma-separated HSN codes
- Shows validation status and description
- Beautiful background image styling with CSS

## How to Run

1. Clone this repository:

```bash
git clone https://github.com/your-username/hsn-validator.git
cd hsn-validator
python -m venv venv
source venv/bin/activate   # Linux/Mac
venv\Scripts\activate      # Windows

pip install flask pandas openpyxl

hsn-validator/
├── app.py              # Flask app code
├── HSN_SAC.xlsx        # Excel data file with HSN codes and descriptions
├── static/
│   └── background.jpg  # Background image file for the webpage
└── templates/
    └── index.html      # HTML template with styling and form

