import os
import subprocess
from pdf2image import convert_from_path
import cv2


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

    image_paths = []
    for i, image in enumerate(images, start=1):
        img_path = os.path.join(output_dir, f'slide_{i}.png')
        image.save(img_path, 'PNG')
        image_paths.append(img_path)
        print(f"Slide {i} saved as image: {img_path}")

    return image_paths


def images_to_video(image_paths, video_output_path, fps=0.3):
    if len(image_paths) == 0:
        print("No images found")
        return

    frame = cv2.imread(image_paths[0])
    height, width, layers = frame.shape

    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    video = cv2.VideoWriter(video_output_path, fourcc, fps, (width, height))

    for image_path in image_paths:
        frame = cv2.imread(image_path)
        video.write(frame)

    video.release()
    print(f"Video saved as {video_output_path}")


def ppt_to_images_and_video(ppt_path, output_dir, video_output_path, fps=0.3):
    pdf_output_dir = os.path.dirname(output_dir)
    pdf_path = ppt_to_pdf(ppt_path, pdf_output_dir)

    image_paths = pdf_to_images(pdf_path, output_dir)

    images_to_video(image_paths, video_output_path, fps)


ppt_path = "/home/tntra/Documents/NeoTech/professional-mobility-test-develop/NeoTech Video Content/History_of_Aeronautics.pptx"
output_dir = "/home/tntra/Documents/NeoTech/professional-mobility-test-develop/NeoTech Video Content/output_images"
video_output_path = "/home/tntra/Documents/NeoTech/professional-mobility-test-develop/NeoTech Video Content/history_of_aeronautics.mp4"

ppt_to_images_and_video(ppt_path, output_dir, video_output_path, fps=0.3)
