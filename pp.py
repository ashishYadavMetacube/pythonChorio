from PyPDF2 import PdfReader

def extract_pdf_form_data(pdf_path):
    # Open the PDF file
    pdf_reader = PdfReader(pdf_path)

    form_data = {}

    # Iterate through the pages
    for page_number in range(len(pdf_reader.pages)):
        page = pdf_reader.pages[page_number]
        if page.get('/Annots'):
            for annot in page['/Annots']:
                field = annot.get_object()  # Updated method
                if field.get('/T') and field.get('/V'):
                    field_name = field.get('/T')
                    field_value = field.get('/V')
                    print(field_value)
                    form_data[field_name] = field_value.decode('utf-8') if isinstance(field_value, bytes) else field_value

    return form_data

# Example usage
pdf_path = 'input.pdf'
data = extract_pdf_form_data(pdf_path)
print(data)
