import os
from fpdf import FPDF

def generate_document(data):
    """
    Webhook 데이터를 기반으로 PDF 문서를 생성
    """
    document_name = f"record_{data['record_id']}.pdf"
    document_path = os.path.join("/tmp", document_name)

    # PDF 생성
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    pdf.cell(200, 10, txt="Document for Record", ln=True, align="C")
    pdf.cell(200, 10, txt=f"Record ID: {data['record_id']}", ln=True)
    pdf.cell(200, 10, txt=f"Name: {data.get('name', 'N/A')}", ln=True)
    pdf.output(document_path)

    return document_path
