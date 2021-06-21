import docx

document = docx.Document("files/section-14/read_word.docx")
paragraph = document.paragraphs[1]

print("text:", paragraph.text)
print("style:", paragraph.style)
print("first run text:", paragraph.runs[0].text) # runs are sections within a paragraph where the style changes
print("first run bold?", "yes" if paragraph.runs[0].bold else "no") # .bold .italic .underline

paragraph.runs[0].underline = True
paragraph.runs[0].italic = True
paragraph.runs[0].bold = True
# enable all style changes

paragraph.style = "Title"

document.save("files/section-14/edit_word.docx")