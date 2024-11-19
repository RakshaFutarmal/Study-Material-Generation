import cv2
import os
from pdf2image import convert_from_path


def convert_ppt_to_pdf(ppt_path, pdf_output):
    os.system(f"libreoffice --headless --convert-to pdf --outdir {os.path.dirname(pdf_output)} {ppt_path}")


def convert_pdf_to_images(pdf_path, output_folder):
    os.makedirs(output_folder, exist_ok=True)

    images = convert_from_path(pdf_path)

    for i, image in enumerate(images):
        slide_image_path = os.path.join(output_folder, f'slide_{i + 1}.png')
        image.save(slide_image_path, 'PNG')
        print(f"Slide {i + 1} saved as {slide_image_path}")


def images_to_video(image_folder, video_file, fps=5, display_time=2):
    images = [img for img in os.listdir(image_folder) if img.endswith(".png")]
    images.sort()

    if not images:
        print("No images found in the specified folder.")
        return

    first_image = cv2.imread(os.path.join(image_folder, images[0]))
    height, width, layers = first_image.shape

    frames_per_image = fps * display_time

    video = cv2.VideoWriter(video_file, cv2.VideoWriter_fourcc(*'mp4v'), fps, (width, height))

    for image in images:
        img_path = os.path.join(image_folder, image)
        img = cv2.imread(img_path)

        for _ in range(frames_per_image):
            video.write(img)

    video.release()
    print(f"Video saved as {video_file}")


def main():
    ppt_file_path = '/home/tntra/Documents/NeoTech/professional-mobility-test-develop/Opencv/History_of_Aeronautics.pptx'
    pdf_file_path = '/home/tntra/Documents/NeoTech/professional-mobility-test-develop/Opencv/History_of_Aeronautics.pdf'
    output_folder = 'output_images'
    video_file = 'output_video.mp4'

    convert_ppt_to_pdf(ppt_file_path, pdf_file_path)

    convert_pdf_to_images(pdf_file_path, output_folder)

    images_to_video(output_folder, video_file, fps=30, display_time=2)


if __name__ == "__main__":
    main()