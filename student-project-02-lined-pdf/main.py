# Se usa fpdf2
from fpdf import FPDF
from fpdf.enums import XPos, YPos
import pandas as pd

pdf = FPDF(orientation="P", unit="mm", format="A4")
pdf.set_auto_page_break(auto=False, margin=0)

df = pd.read_csv("topics.csv")


def lines():
    for y in range(20, 280, 10):
        pdf.line(10, y, 190, y)


def footer_text():
    pdf.ln(260)
    pdf.set_font(family="Times", style="I", size=8)
    pdf.set_text_color(180, 180, 180)
    pdf.cell(w=0, h=10, txt=row["Topic"], align="R", new_x=XPos.LMARGIN, new_y=YPos.NEXT)


for index, row in df.iterrows():
    pdf.add_page()

    # Set the header
    pdf.set_font(family="Times", style="B", size=24)
    pdf.set_text_color(100, 100, 100)
    pdf.cell(w=0, h=12, txt=row["Topic"], align="L", new_x=XPos.LMARGIN, new_y=YPos.NEXT)

    # Set the lines
    lines()

    # Set the footer
    footer_text()

    for i in range(row["Pages"] - 1):
        pdf.add_page()

        # Set the lines
        lines()

        # Set the footer
        footer_text()

pdf.output("output.pdf")
