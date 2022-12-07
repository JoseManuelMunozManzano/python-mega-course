import glob
from fpdf import FPDF
from pathlib import Path

filepaths = glob.glob("files/*.txt")
pdf = FPDF(orientation="P", unit="mm", format="A4")
pdf.set_font(family="Times", size=16, style="B")

for filepath in filepaths:
    pdf.add_page()
    filename = Path(filepath).stem
    animal_name = filename.capitalize();
    pdf.cell(w=50, h=8, txt=animal_name)

pdf.output("animals.pdf")
