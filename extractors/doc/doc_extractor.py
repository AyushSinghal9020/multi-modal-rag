from docx import Document

def docx_to_text(path) : 

    doc = Document(path)
    text = ''

    for paragraph in doc.paragraphs : text += paragraph.text

    return text
