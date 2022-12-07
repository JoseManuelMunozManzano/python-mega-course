import glob
from fpdf import FPDF
from pathlib import Path

filepaths = glob.glob("files/*.txt")
pdf = FPDF(orientation="P", unit="mm", format="A4")

for filepath in filepaths:
    # Add a page to the PDF document for each text file
    pdf.add_page()

    # Get the filename without the extension
    # and convert it to title case
    filename = Path(filepath).stem
    animal_name = filename.capitalize();

    # Add the name to the PDF
    pdf.set_font(family="Times", size=16, style="B")
    pdf.cell(w=50, h=8, txt=animal_name, ln=1)

    # Get the content of each text file
    with open(filepath, "r") as file:
        content = file.read()
    # Add the text content to the PDF
    pdf.set_font(family="Times", size=12)
    pdf.multi_cell(w=0, h=6, txt=content)


pdf.output("animals.pdf")
