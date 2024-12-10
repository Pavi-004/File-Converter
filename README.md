# 📄 Universal File to PDF Converter

## 🌟 Project Overview

### Introduction
The **Universal File to PDF Converter** is a user-friendly Streamlit application designed to simplify the process of converting various file types (TXT, CSV, and Excel) into PDF format. This tool provides a *seamless, intuitive interface* for quick file conversions, making document management more efficient.

## 📋 Objectives
The main objectives of this project are to:
- **Provide a simple, web-based solution** for file conversion
- **Support multiple input file types**
- **Offer a user-friendly conversion process**
- **Ensure easy file download** after conversion

## 🛠 Requirements

### System Requirements
- **Python 3.7+**
- **Streamlit**
- **FPDF**
- **Pandas**

### Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/universal-file-to-pdf-converter.git
cd universal-file-to-pdf-converter
```

2. Create a virtual environment *(optional but recommended)*:
```bash
python -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
```

3. Install required dependencies:
```bash
pip install -r requirements.txt
```

### Dependencies
Create a `requirements.txt` file with the following content:
```
streamlit
fpdf
pandas
```

## 🚀 How to Run the Application

```bash
streamlit run app.py
```

## 💡 Features
- **Support for multiple file types:**
  - Text (`.txt`)
  - CSV (`.csv`)
  - Excel (`.xlsx`, `.xls`)
- **Simple, intuitive user interface**
- **Real-time file conversion**
- **Easy PDF download**

## 🔍 How It Works

### File Upload
- Users can upload files through a *drag-and-drop or file selection interface*
- **Supported file types are automatically filtered**
- **Only one file can be uploaded at a time**

### Conversion Process
1. Upload a supported file type
2. Click the "**Convert to PDF**" button
3. Wait for the conversion process
4. Download the generated PDF

### Technical Details
- Uses `fpdf` for PDF generation
- Utilizes `pandas` for reading different file formats
- Leverages **Streamlit** for the web interface

## 🛡 Error Handling
- **Validates file types** before conversion
- Provides *user-friendly error messages*
- Handles potential conversion issues *gracefully*

## 📸 Screenshots
*[You can add screenshots of the application here]*

## 🤝 Contributing
**Contributions are welcome!** Please feel free to submit a Pull Request.

### Steps to Contribute
1. Fork the repository
2. Create your feature branch `git checkout -b feature/AmazingFeature`
3. Commit your changes `git commit -m 'Add some AmazingFeature'`
4. Push to the branch `git push origin feature/AmazingFeature`
5. Open a Pull Request

## 📜 License
*[Specify your license here, e.g., MIT License]*

## 👥 Contact
**Pavi Shanker**
- **pavishanker72@gmail.com:** 
- **Repo Link:** https://github.com/yourusername/universal-file-to-pdf-converter

## 🙏 Acknowledgements
- [Streamlit](https://streamlit.io/)
- [FPDF](https://pyfpdf.readthedocs.io/)
- [Pandas](https://pandas.pydata.org/)