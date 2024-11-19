import os
import subprocess
from pdf2image import convert_from_path
from moviepy.editor import ImageSequenceClip, AudioFileClip, concatenate_audioclips
from gtts import gTTS
import integrated_function


class AudioService:

    def __init__(self):
        pass

    def generate_slide_content(self, prompt):
        result = integrated_function.mistral_search(prompt)
        if isinstance(result, str):
            return result.strip()
        elif isinstance(result, dict) and 'text' in result:
            return result['text'].strip()

    def generate_voiceover(self, text, audio_file):
        if text:
            tts = gTTS(text, lang='en')
            tts.save(audio_file)

    def get_audio(self, prompts):
        audio_files = []
        for i, prompt in enumerate(prompts):
            content = self.generate_slide_content(prompt)
            if content:
                audio_filename = f'audio_mistral_{i}.mp3'
                self.generate_voiceover(content, audio_filename)
                audio_files.append(audio_filename)
                print(f"Audio saved as {audio_filename}")
        return audio_files

    def audio_prompt(self, subtopics, levels):
        return f"""
        You are a subject teacher expert providing detailed 
        educational content to students. Provide a comprehensive 
        script that must be included in the explanation of any 
        subtopics for the following PowerPoint presentation slide 
        topics: {subtopics}. The course is designed for {levels}-level 
        learners. For each slide, include the following elements:

        Introduction: Briefly overview the topic of {subtopics} 
        in 1-2 bullet points and explain its importance 
        for a {levels} audience.

        Problem Statement : Describe the core problem 
        or challenge within {subtopics} using 1-2 concise bullet points.

        Importance of the Topic : Highlight why {subtopics} 
        matters with 1-2 key points, including relevant 
        statistics, studies, or expert opinions.

        Key Concepts : Define and explain 1-2 key ideas 
        or frameworks within {subtopics}, suitable 
        for the {levels} audience.

        Solution or Approach : Outline a proposed 
        solution or approach to the core challenges 
        in {subtopics}, focusing on 1-2 key points.

        Benefits of the Solution : Discuss why this 
        solution is effective, with 1-2 supporting points.

        Case Study/Example : Present a real-world 
        example or case study illustrating {subtopics},
         with 1-2 bullet points tailored to the audience's {levels}.

        Actionable Insights : Summarize practical 
        takeaways or insights in 1-2 points, emphasizing 
        actionable steps or strategies for the audience.

        Conclusion : Recap the most important points 
        from the presentation in 1-2 concise bullet points.

        Future Outlook: Provide 1-2 predictions or 
        recommendations for future trends in {subtopics}.
        
        """


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


def images_to_video_with_audio(image_paths, audio_files, video_output_path, fps=0.08):
    if len(image_paths) == 0:
        print("No images found.")
        return

    clip = ImageSequenceClip(image_paths, fps=fps)

    audio_clips = [AudioFileClip(audio_file) for audio_file in audio_files]

    final_audio = concatenate_audioclips(audio_clips)

    video = clip.set_audio(final_audio)

    video.write_videofile(video_output_path, codec="libx264", audio_codec="aac")
    print(f"Video with audio saved as {video_output_path}")


def ppt_to_images_and_video_with_audio(ppt_path, output_dir, video_output_path, subtopics, levels):
    pdf_output_dir = os.path.dirname(output_dir)
    pdf_path = ppt_to_pdf(ppt_path, pdf_output_dir)

    image_paths = pdf_to_images(pdf_path, output_dir)

    prompts = AudioService().audio_prompt(subtopics, levels)
    audio_files = AudioService().get_audio([prompts])

    images_to_video_with_audio(image_paths, audio_files, video_output_path, fps=0.1)


ppt_path = "/home/tntra/Documents/NeoTech/professional-mobility-test-develop/NeoTech Video Content/History_of_Aeronautics.pptx"
output_dir = "/home/tntra/Documents/NeoTech/professional-mobility-test-develop/NeoTech Video Content/output_images"
video_output_path = "/home/tntra/Documents/NeoTech/professional-mobility-test-develop/NeoTech Video Content/history_of_aeronautics_with_audio.mp4"

subtopics = ['What is aeronautics?']
levels = ['Basics']

ppt_to_images_and_video_with_audio(ppt_path, output_dir, video_output_path, subtopics, levels)




