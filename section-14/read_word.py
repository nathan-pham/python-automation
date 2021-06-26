import docx

def get_text(filename):
    document = docx.Document(filename)
    body = []

    for paragraph in document.paragraphs:
        body.append(paragraph.text)

    return "\n".join(body)

print(get_text("files/section-14/make_word.docx"))