import streamlit as st

from fpdf import FPDF

import base64

def create_download_link(val, filename):

  b64 = base64.b64encode(val)

  # val looks like b'...'

  return f'<a href="data:application/octet-stream;base64,{b64.decode()}" download="{filename}.pdf">Download file</a>'

# Create a text input field

report_text = st.text_input("Report Text")

# Create a button to export the report as a PDF

export_as_pdf = st.button("Export Report")

# If the user clicks the button, export the report as a PDF

if export_as_pdf:

  pdf = FPDF()

  pdf.add_page()

  pdf.set_font('Arial', 'B', 16)

  pdf.cell(40, 10, report_text)

  # Convert the PDF to a base64 string

  pdf_bytes = pdf.output(dest="S").encode("latin-1")

  # Create a download link for the PDF

  st.markdown(create_download_link(pdf_bytes, "report.pdf"), unsafe_allow_html=True)

