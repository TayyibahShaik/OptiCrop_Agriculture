import pdfplumber
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from PyPDF2 import PdfReader, PdfWriter
import io

pdf_path = "Brainstorming_Idea_Prioritization.pdf"
output_pdf_path = "OptiCrop_Brainstorming.pdf"

header_data = {
    "Date": "10 July 2026",
    "Team ID": "xxxxxx",
    "Project Name": "OptiCrop: Smart Agricultural Production Optimization Engine",
    "Maximum Marks": "3 Marks"
}

step1_data = [
    ["1", "shaik Tayyibah", "Build an ML model to predict optimal crops based on NPK, temp, and rainfall.", "Machine Learning", "1"],
    ["2", "shaik Tayyibah", "Develop a Flask web application with a responsive user interface.", "Web Development", "2"],
    ["3", "shaik Tayyibah", "Use Logistic Regression and K-Means clustering for robust classification.", "Model Selection", "1"],
    ["4", "shaik Tayyibah", "Perform EDA to visualize seasonal conditions and nutrient patterns using Seaborn.", "Data Analysis", "3"],
    ["5", "shaik Tayyibah", "Implement Glassmorphism design and micro-animations for a premium UI.", "UI/UX Design", "2"],
    ["6", "shaik Tayyibah", "Compare KNN, K-Means, and Logistic Regression for the best recommendation accuracy.", "Model Eval", "1"]
]

step2_data = [
    ["1", "Build ML models for crop prediction", "High", "High", "1", "Yes"],
    ["2", "Develop a Flask web application", "High", "High", "2", "Yes"],
    ["3", "Perform Exploratory Data Analysis", "High", "Medium", "3", "Yes"],
    ["", "", "", "", "", ""],
    ["", "", "", "", "", ""],
    ["", "", "", "", "", ""]
]

packet = io.BytesIO()
page_height = 841.89
c = canvas.Canvas(packet, pagesize=A4)
c.setFont("Helvetica", 10)

with pdfplumber.open(pdf_path) as pdf:
    page = pdf.pages[0]
    tables_cells = page.find_tables()
    tables_text = page.extract_tables()
    
    # Table 0: Header
    table0_cells = tables_cells[0].cells
    table0_text = tables_text[0]
    for i, row_text in enumerate(table0_text):
        if not row_text: continue
        key_text = row_text[0].strip() if row_text[0] else ""
        if key_text in header_data:
            val_cell = table0_cells[i][1] if len(table0_cells[i]) > 1 else None
            if val_cell:
                x0, top, x1, bottom = val_cell
                c.setFillColorRGB(1, 1, 1)
                c.rect(x0, page_height - bottom, x1 - x0, bottom - top, stroke=0, fill=1)
                c.setFillColorRGB(0, 0, 0)
                c.drawString(x0 + 5, page_height - top - 15, header_data[key_text])

    # Table 1: Step 1
    table1_cells = tables_cells[1].cells
    for i, row in enumerate(table1_cells[1:]): # skip header
        if i < len(step1_data):
            row_data = step1_data[i]
            for j, cell in enumerate(row):
                if cell and j < len(row_data):
                    x0, top, x1, bottom = cell
                    c.setFillColorRGB(1, 1, 1)
                    c.rect(x0 + 1, page_height - bottom + 1, x1 - x0 - 2, bottom - top - 2, stroke=0, fill=1)
                    c.setFillColorRGB(0, 0, 0)
                    text = str(row_data[j])
                    if len(text) > 40:
                        c.setFont("Helvetica", 8)
                        c.drawString(x0 + 2, page_height - top - 12, text[:40])
                        c.drawString(x0 + 2, page_height - top - 24, text[40:80])
                        c.drawString(x0 + 2, page_height - top - 36, text[80:])
                        c.setFont("Helvetica", 10)
                    else:
                        c.drawString(x0 + 2, page_height - top - 15, text)

    # Table 2: Step 2
    table2_cells = tables_cells[2].cells
    for i, row in enumerate(table2_cells[1:]): # skip header
        if i < len(step2_data):
            row_data = step2_data[i]
            for j, cell in enumerate(row):
                if cell and j < len(row_data):
                    x0, top, x1, bottom = cell
                    c.setFillColorRGB(1, 1, 1)
                    c.rect(x0 + 1, page_height - bottom + 1, x1 - x0 - 2, bottom - top - 2, stroke=0, fill=1)
                    c.setFillColorRGB(0, 0, 0)
                    text = str(row_data[j])
                    if len(text) > 30:
                        c.setFont("Helvetica", 8)
                        c.drawString(x0 + 2, page_height - top - 12, text[:30])
                        c.drawString(x0 + 2, page_height - top - 24, text[30:])
                        c.setFont("Helvetica", 10)
                    else:
                        c.drawString(x0 + 2, page_height - top - 15, text)

c.save()
packet.seek(0)
new_pdf = PdfReader(packet)

original_pdf = PdfReader(pdf_path)
page = original_pdf.pages[0]
page.merge_page(new_pdf.pages[0])

output = PdfWriter()
output.add_page(page)

with open(output_pdf_path, "wb") as outputStream:
    output.write(outputStream)

print("PDF successfully updated and saved as OptiCrop_Brainstorming.pdf")
