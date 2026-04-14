import datetime
import os
from fpdf import FPDF

class PDF(FPDF):
    def header(self):
        self.set_font('Arial', 'B', 12)
        self.cell(0, 10, 'Project Report', 0, 1, 'C')

    def footer(self):
        self.set_y(-15)
        self.set_font('Arial', 'I', 8)
        self.cell(0, 10, f'Page {self.page_no()}', 0, 0, 'C')

def generate_report():
    pdf = PDF()
    pdf.add_page()

    pdf.set_font('Arial', '', 12)

    # Current date and time
    current_datetime = 'Report Generated on: {}' .format(datetime.datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S'))
    pdf.cell(0, 10, current_datetime, 0, 1)

    # Project details
    pdf.cell(0, 10, 'Project Name: DDDS', 0, 1)
    pdf.cell(0, 10, 'Author: mithunj7999-cyber', 0, 1)
    pdf.cell(0, 10, 'Summary: This project involves generating reports using Python.', 0, 1)

    # Package information
    packages = ['fpdf']  # Add other packages as needed
    pdf.cell(0, 10, 'Required Packages:', 0, 1)
    for package in packages:
        pdf.cell(0, 10, f'- {package}', 0, 1)

    # Summary section
    pdf.cell(0, 10, 'Project Summary:', 0, 1)
    pdf.multi_cell(0, 10, "This report summarizes the project details and its packages. ")

    # Save the PDF
    pdf_filename = 'DDDS_Report.pdf'
    pdf.output(pdf_filename)
    print(f'Report saved as {pdf_filename}')

if __name__ == '__main__':
    generate_report()