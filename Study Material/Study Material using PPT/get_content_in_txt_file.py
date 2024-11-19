import integrated_function


class PresentationContentService:

    def content(self, subtopic, level):
        """
        Generate and add content for a specific subtopic and level to the PDF.
        """
        query = f""" 
                    "Title": {subtopic},
                    "Table of content" : Generate 3-4 points for {subtopic},

                            "slide_1": Introduction to {subtopic},
                            "key_points": [
                                Provide a brief definition or introduction to {subtopic}.,
                                Explain why {subtopic} is important in the context of {level} audience.,
                                Mention any key applications or uses of {subtopic}.                                                  

                            "slide_2": Core Problem in {subtopic},
                            "key_points": [
                                Outline the main problem or challenge related to {subtopic}.,
                                Why is this problem significant for {level} audience?,
                                Provide examples of this challenge in real-world scenarios.

                            "slide_3": Importance of {subtopic},
                            "key_points": [
                                Highlight why {subtopic} is important for professionals or learners at the {level} level.,
                                Discuss its impact on the industry, technology, or society.,
                                Include statistics or research data if available.

                            "slide_4": Key Concepts in {subtopic},
                            "key_points": [
                                Define and explain 3-5 key concepts or terms within {subtopic}.,
                                Provide explanations at a {level}-appropriate level of detail.,
                                Use analogies, if necessary, for easier understanding at the {level} level.

                            slide_5": Proposed Solution for {subtopic} Challenges",
                            "key_points": [
                                Describe a known solution or approach to address challenges in {subtopic}.,
                                Explain why this solution is effective at the {level} of understanding.,
                                Provide any implementation examples or case studies.

                            "slide_6": Benefits of the Proposed Solution,
                            "key_points": [
                                Explain the benefits of the proposed solution in {subtopic}.,
                                Provide evidence of its effectiveness, tailored to the {level} audience.,
                                Compare this solution to alternative methods, if applicable.

                            "slide_7": Real-World Example of {subtopic},
                            "key_points": [
                                Present a real-world case study where {subtopic} was applied successfully.,
                                Discuss the challenges faced and how they were overcome.,
                                Include relevant metrics or outcomes to demonstrate impact.

                            "slide_8": Actionable Insights in {subtopic},
                            "key_points": [
                                Summarize the key takeaways for {level} learners or professionals.,
                                Provide practical steps they can apply to their work or studies.,
                                Discuss how {subtopic} can be integrated into real-life scenarios for their benefit.

                            "slide_9": Conclusion,
                            "key_points": [
                                Recap the most important points from the presentation.,
                                Tailor the conclusion to the {level} audience, focusing on what they need to retain.,
                                Encourage further exploration or study of {subtopic}.

                            "slide_10": Future Outlook for {subtopic},
                            "key_points": [
                                Provide predictions or recommendations for future trends in {subtopic}.,
                                Explain how the field may evolve, especially for the {level} audience.,
                                Highlight any opportunities for further research or innovation.

                        INSTRUCTIONS: The table of content should be a list based on the slide titles."""

        result1 = integrated_function.mistral_search(query)
        return result1

    def save_to_text_file(self, subtopic, content):
        if content:
            filename = f"{subtopic}_content.txt"
            with open(filename, 'w') as file:
                file.write(content)
            return f"Content saved to {filename}"
        else:
            return "No content to save."


presentation_service = PresentationContentService()

subtopics = ['History of Aeronautics']
levels = ['Basics']

for subtopic, level in zip(subtopics, levels):
    content = presentation_service.content(subtopic, level)
    status = presentation_service.save_to_text_file(subtopic, content)
    print(status)
