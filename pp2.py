import fillpdf
from fillpdf import fillpdfs


data_dict = {'Name': 'Ashish', 'Dropdown1': 12}

fillpdfs.print_form_fields('input.pdf', sort=False, page_number=None)
#
# fillpdfs.write_fillable_pdf('input.pdf', 'new.pdf', data_dict)
#
# fillpdfs.flatten_pdf('new.pdf', 'newflat.pdf', as_images=True)



