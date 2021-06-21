import PyPDF2 as pdf

handle_1 = open("files/section-14/meeting_1.pdf", "rb")
handle_2 = open("files/section-14/meeting_2.pdf", "rb")

reader_1 = pdf.PdfFileReader(handle_1)
reader_2 = pdf.PdfFileReader(handle_2)

combined_writer = pdf.PdfFileWriter()

def add_pages(reader, writer):
    for i in range(reader.numPages):
        page = reader.getPage(i)
        writer.addPage(page)

add_pages(reader_1, combined_writer)
add_pages(reader_2, combined_writer)

output = open("files/section-14/combined_meeting.pdf", "wb")
combined_writer.write(output)

handle_1.close()
handle_2.close()
output.close()