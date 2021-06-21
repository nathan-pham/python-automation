import docx

document = docx.Document("files/section-14/read_word.docx")
paragraph = document.paragraphs[1]

print(paragraph.text)
print(paragraph.runs[0].text) # runs are sections within a paragraph where the style changes
print(paragraph.runs[0].bold) # .bold .italic .underline

paragraph.runs[0].underline = True
paragraph.runs[0].italic = True
paragraph.runs[0].bold = True

document.save("files/section-14/edit_word.docx")