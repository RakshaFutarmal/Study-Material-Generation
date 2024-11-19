import integrated_function
from Subtopic_generation_Study_Material import get_subtopics, topics, levels

class PresentationContentService:

    def content(self, subtopic, level):
        """
        Generate the content for presentation
        """
        query = f""" 
                    "Title": {subtopic},
                    "Table of content" : Generate 3-4 points for {subtopic},

                            1: Introduction to {subtopic},
                            "key_points": [
                                Provide a brief definition or introduction to {subtopic}.,
                                Explain why {subtopic} is important in the context of {level} audience.,
                                Mention any key applications or uses of {subtopic}.                                                  

                            2: Core Problem in {subtopic},
                            "key_points": [
                                Outline the main problem or challenge related to {subtopic}.,
                                Why is this problem significant for {level} audience?,
                                Provide examples of this challenge in real-world scenarios.

                            3: Importance of {subtopic},
                            "key_points": [
                                Highlight why {subtopic} is important for professionals or learners at the {level} level.,
                                Discuss its impact on the industry, technology, or society.,
                                Include statistics or research data if available.

                            4: Key Concepts in {subtopic},
                            "key_points": [
                                Define and explain 3-5 key concepts or terms within {subtopic}.,
                                Provide explanations at a {level}-appropriate level of detail.,
                                Use analogies, if necessary, for easier understanding at the {level} level.

                            5: Proposed Solution for {subtopic} Challenges",
                            "key_points": [
                                Describe a known solution or approach to address challenges in {subtopic}.,
                                Explain why this solution is effective at the {level} of understanding.,
                                Provide any implementation examples or case studies.

                            6: Benefits of the Proposed Solution,
                            "key_points": [
                                Explain the benefits of the proposed solution in {subtopic}.,
                                Provide evidence of its effectiveness, tailored to the {level} audience.,
                                Compare this solution to alternative methods, if applicable.

                            7: Real-World Example of {subtopic},
                            "key_points": [
                                Present a real-world case study where {subtopic} was applied successfully.,
                                Discuss the challenges faced and how they were overcome.,
                                Include relevant metrics or outcomes to demonstrate impact.

                            8: Actionable Insights in {subtopic},
                            "key_points": [
                                Summarize the key takeaways for {level} learners or professionals.,
                                Provide practical steps they can apply to their work or studies.,
                                Discuss how {subtopic} can be integrated into real-life scenarios for their benefit.

                            9: Conclusion,
                            "key_points": [
                                Recap the most important points from the presentation.,
                                Tailor the conclusion to the {level} audience, focusing on what they need to retain.,
                                Encourage further exploration or study of {subtopic}.

                            10: Future Outlook for {subtopic},
                                Provide predictions or recommendations for future trends in {subtopic}.,
                                Explain how the field may evolve, especially for the {level} audience.,
                                Highlight any opportunities for further research or innovation.

                        INSTRUCTIONS: The table of content should be a list based on the slide titles.Ensure that content for each section is structured with clear bullet points."""

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


subtopics = get_subtopics(topics, levels)

for subtopic, level in subtopics:
    content = PresentationContentService().content(subtopic, level)
    status = PresentationContentService().save_to_text_file(subtopic, content)

    print(status)
