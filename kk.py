from pdf2image import convert_from_path
from PIL import Image

# Path to the PDF file
pdf_path = 'new.pdf'
output_pdf_path = 'output_pdf_of_images.pdf'

# Convert PDF pages to images
images = convert_from_path(pdf_path)

# Save images as a PDF
image_list = []
for image in images:
    # Ensure all images are in RGB mode (some might be in RGBA or L mode)
    if image.mode != 'RGB':
        image = image.convert('RGB')
    image_list.append(image)

# Save the list of images as a PDF
image_list[0].save(output_pdf_path, save_all=True, append_images=image_list[1:])
print(f'Saved new PDF of images as {output_pdf_path}')
