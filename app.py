import streamlit as st
import pandas as pd
from fpdf import FPDF
from pathlib import Path

def convert_to_pdf(uploaded_file):
    """
    Convert the uploaded file to PDF
    """
    # Create a PDF object
    pdf = FPDF(orientation="P", unit="mm", format="A4")
    pdf.add_page()

    # Set font
    pdf.set_font(family="Times", size=12)

    # Get the filename without extension
    filename = Path(uploaded_file.name).stem.title()

    # Add filename as title
    pdf.set_font(family="Times", size=16, style="B")
    pdf.cell(w=0, h=10, txt=filename, ln=1, align="C")

    # Reset font for content
    pdf.set_font(family="Times", size=12)

    # Handle different file types
    try:
        if uploaded_file.type == 'text/plain':
            # Read text file
            content = uploaded_file.getvalue().decode('utf-8')
            pdf.multi_cell(0, 10, content)
        
        elif uploaded_file.type in ['application/vnd.ms-excel', 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet']:
            # Read Excel file
            df = pd.read_excel(uploaded_file)
            content = df.to_string()
            pdf.multi_cell(0, 10, content)
        
        elif uploaded_file.type == 'text/csv':
            # Read CSV file
            df = pd.read_csv(uploaded_file)
            content = df.to_string()
            pdf.multi_cell(0, 10, content)
        
        else:
            st.error("Unsupported file type")
            return None

    except Exception as e:
        st.error(f"Error converting file: {e}")
        return None

    # Generate output filename
    output_filename = f"{filename}_converted.pdf"
    
    # Save PDF
    pdf.output(output_filename)
    return output_filename

def main():
    # Set page title and icon
    st.set_page_config(page_title="Universal File to PDF Converter", page_icon="📄")

    # Add title and description
    st.title("🔄 Universal File Converter")
    st.write("Convert your TXT, CSV, and Excel files to PDF easily!")

    # File uploader with specific file types
    uploaded_file = st.file_uploader(
        "Choose a file", 
        type=['txt', 'csv', 'xlsx', 'xls'],
        accept_multiple_files=False
    )

    # Convert button with custom styling
    if uploaded_file is not None:
        # Custom blue button with color change on click
        convert_button = st.button("Convert to PDF", type="primary")
        
        if convert_button:
            with st.spinner('Converting file...'):
                # Attempt conversion
                output_filename = convert_to_pdf(uploaded_file)
                
                if output_filename:
                    # Success message
                    st.success(f"File successfully converted to {output_filename}")
                    
                    # Provide download option
                    with open(output_filename, "rb") as file:
                        st.download_button(
                            label="Download PDF",
                            data=file,
                            file_name=output_filename,
                            mime="application/pdf"
                        )

if __name__ == "__main__":
    main()