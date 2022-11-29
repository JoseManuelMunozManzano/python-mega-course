from fpdf import FPDF

pdf = FPDF(orientation="P", unit="mm", format="A4")

pdf.add_page()

# size y height se recomienda mantenerse con el mismo valor
# El valor border está bien para desarrollar, paro luego dejarlo o quitarlo en función de si quedará en el
# desarrollo final o no
# pdf.set_font(family="Times", style="B", size=12)
# pdf.cell(w=0, h=12, txt="Hello There!", align="L", ln=1, border=1)

pdf.set_font(family="Times", style="B", size=12)
pdf.cell(w=0, h=12, txt="Hello There!", align="L", ln=1)

pdf.set_font(family="Times", size=10)
pdf.cell(w=0, h=10, txt="Hi There!", align="L", ln=1)

# Otra hoja
pdf.add_page()

pdf.set_font(family="Times", size=10)
pdf.cell(w=0, h=10, txt="Hi There!", align="L", ln=1)

pdf.output("output.pdf")
