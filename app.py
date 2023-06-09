import streamlit as st

from fpdf import FPDF

def create_pdf(text):

    pdf = FPDF()

    pdf.add_page()

    pdf.set_font("Arial", size=12)

    lines = text.split("\n")  # Split text into lines

    for line in lines:

        pdf.cell(0, 10, txt=line, ln=True)  # Add each line to the PDF

    return pdf

def main():

    st.title("Text to PDF Converter")

    # Input text

    st.subheader("Enter your text:")

    text_input = st.text_area("Text")

    # Convert to PDF button

    if st.button("Convert to PDF"):

        if text_input:

            # Create PDF object and save file

            pdf = create_pdf(text_input)

            pdf_file = pdf.output(dest="S").encode("latin-1")

            st.download_button("Download PDF", pdf_file, file_name="converted_pdf.pdf")

            st.success("PDF created successfully!")

        else:

            st.warning("Please enter some text.")

if __name__ == "__main__":

    main()



    
    


