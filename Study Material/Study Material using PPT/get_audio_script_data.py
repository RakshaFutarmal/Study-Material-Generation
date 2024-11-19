from gtts import gTTS
import integrated_function


class AudioService:

    def __init__(self):
        """
        This is the AudioService class.
        """
        pass

    def generate_slide_content(self, prompt):

        result = integrated_function.mistral_search(prompt)

        if isinstance(result, str):
            return result.strip()
        elif isinstance(result, dict) and 'text' in result:
            return result['text'].strip()

    def generate_voiceover(self, text, audio_file):
        """
        Text to speech using Google Text-to-Speech (gTTS) API.
        """

        if text:
            tts = gTTS(text, lang='en')
            tts.save(audio_file)

    def get_audio(self, prompts):
        """
        Method to generate the audio for each slide in the ppt.
        """

        for i, prompt in enumerate(prompts):
            content = self.generate_slide_content(prompt)
            if content:
                audio_filename = f'audio_mistral_{i}.mp3'
                self.generate_voiceover(content, audio_filename)
                print(f"Audio saved as {audio_filename}")

    def create_prompts(self, subtopics, levels):

        return f"""
        You are a subject teacher expert providing detailed educational content to students. Provide a comprehensive script that must be included in the explanation of any subtopics for the following PowerPoint presentation slide topics: {subtopics}. The course is designed for {levels}-level learners. For each slide, include the following elements:

        Introduction (Slide 1): Briefly overview the topic of {subtopics} in 2-3 bullet points and explain its importance for a {levels} audience.

        Problem Statement (Slide 2): Describe the core problem or challenge within {subtopics} using 3-4 concise bullet points.

        Importance of the Topic (Slide 3): Highlight why {subtopics} matters with 3-4 key points, including relevant statistics, studies, or expert opinions.

        Key Concepts (Slide 4): Define and explain 3-5 key ideas or frameworks within {subtopics}, suitable for the {levels} audience.

        Solution or Approach (Slide 5): Outline a proposed solution or approach to the core challenges in {subtopics}, focusing on 3-4 key points.

        Benefits of the Solution (Slide 6): Discuss why this solution is effective, with 3-4 supporting points.

        Case Study/Example (Slide 7): Present a real-world example or case study illustrating {subtopics}, with 4-5 bullet points tailored to the audience's {levels}.

        Actionable Insights (Slide 8): Summarize practical takeaways or insights in 3-4 points, emphasizing actionable steps or strategies for the audience.

        Conclusion (Slide 9): Recap the most important points from the presentation in 3-4 concise bullet points.

        Future Outlook (Slide 10): Provide 3-4 predictions or recommendations for future trends in {subtopics}.
        """


audio_service = AudioService()

subtopics = ['What is an algorithm?']
levels = ['Basics']

prompts = audio_service.create_prompts(subtopics, levels)
audio_service.get_audio([prompts])