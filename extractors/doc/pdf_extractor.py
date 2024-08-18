import PyPDF2

def pdf_to_text(path) : 

    pdf_file = open(path , 'rb')
    reader = PyPDF2.PdfReader(pdf_file)
    num_pages = len(reader.pages)
    text = ''

    for page_num in range(num_pages):
        page = reader.pages[page_num]
        text += page.extract_text()

    pdf_file.close()

    return text