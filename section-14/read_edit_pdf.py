import PyPDF2 as pdf

pdf_handle = open("files/section-14/read_edit_pdf.pdf", "rb")
reader = pdf.PdfFileReader(pdf_handle)

for i in range(reader.numPages):
    page = reader.getPage(0)
    text = page.extractText()