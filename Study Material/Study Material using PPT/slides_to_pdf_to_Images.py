import os
import subprocess
from pdf2image import convert_from_path


def ppt_to_pdf(ppt_path, pdf_output_dir):
    if not os.path.exists(pdf_output_dir):
        os.makedirs(pdf_output_dir)

    command = [
        'libreoffice',
        '--headless',
        '--convert-to', 'pdf',
        '--outdir', pdf_output_dir,
        ppt_path
    ]

    subprocess.run(command, check=True)

    pdf_filename = os.path.splitext(os.path.basename(ppt_path))[0] + '.pdf'
    return os.path.join(pdf_output_dir, pdf_filename)


def pdf_to_images(pdf_path, output_dir):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    images = convert_from_path(pdf_path)

    for i, image in enumerate(images, start=1):
        img_path = os.path.join(output_dir, f'slide_{i}.png')
        image.save(img_path, 'PNG')
        print(f"Slide {i} saved as image: {img_path}")


def ppt_to_images(ppt_path, output_dir):
    pdf_output_dir = os.path.dirname(output_dir)
    pdf_path = ppt_to_pdf(ppt_path, pdf_output_dir)

    pdf_to_images(pdf_path, output_dir)


ppt_path = "/home/tntra/Documents/NeoTech/professional-mobility-test-develop/NeoTech Video Content/History_of_Aeronautics.pptx"
output_dir = "/home/tntra/Documents/NeoTech/professional-mobility-test-develop/NeoTech Video Content/output_images"

ppt_to_images(ppt_path, output_dir)
