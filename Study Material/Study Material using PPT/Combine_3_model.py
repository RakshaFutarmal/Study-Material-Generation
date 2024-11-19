import integrated_function

class PresentationContentService:

    def content(self, subtopic, level):
        """
        Generate the content for a subtopic and level.
        """
        query = f""" 
                    "presentation_title": "Understanding {subtopic}",

                    "slides": 

                            "slide_title": "Introduction to {subtopic}",
                            "key_points": [
                                "Provide a brief definition or introduction to {subtopic}.",
                                "Explain why {subtopic} is important in the context of {level} audience.",
                                "Mention any key applications or uses of {subtopic}."                                                   

                            "slide_title": "Core Problem in {subtopic}",
                            "key_points": [
                                "Outline the main problem or challenge related to {subtopic}.",
                                "Why is this problem significant for {level} audience?",
                                "Provide examples of this challenge in real-world scenarios."

                            "slide_title": "Importance of {subtopic}",
                            "key_points": [
                                "Highlight why {subtopic} is important for professionals or learners at the {level} level.",
                                "Discuss its impact on the industry, technology, or society.",
                                "Include statistics or research data if available."

                            "slide_title": "Key Concepts in {subtopic}",
                            "key_points": [
                                "Define and explain 3-5 key concepts or terms within {subtopic}.",
                                "Provide explanations at a {level}-appropriate level of detail.",
                                "Use analogies, if necessary, for easier understanding at the {level} level."

                            "slide_title": "Proposed Solution for {subtopic} Challenges",
                            "key_points": [
                                "Describe a known solution or approach to address challenges in {subtopic}.",
                                "Explain why this solution is effective at the {level} of understanding.",
                                "Provide any implementation examples or case studies."

                            "slide_title": "Benefits of the Proposed Solution",
                            "key_points": [
                                "Explain the benefits of the proposed solution in {subtopic}.",
                                "Provide evidence of its effectiveness, tailored to the {level} audience.",
                                "Compare this solution to alternative methods, if applicable."

                            "slide_title": "Real-World Example of {subtopic}",
                            "key_points": [
                                "Present a real-world case study where {subtopic} was applied successfully.",
                                "Discuss the challenges faced and how they were overcome.",
                                "Include relevant metrics or outcomes to demonstrate impact."

                            "slide_title": "Actionable Insights in {subtopic}",
                            "key_points": [
                                "Summarize the key takeaways for {level} learners or professionals.",
                                "Provide practical steps they can apply to their work or studies.",
                                "Discuss how {subtopic} can be integrated into real-life scenarios for their benefit."

                            "slide_title": "Conclusion",
                            "key_points": [
                                "Recap the most important points from the presentation.",
                                "Tailor the conclusion to the {level} audience, focusing on what they need to retain.",
                                "Encourage further exploration or study of {subtopic}."

                            "slide_title": "Future Outlook for {subtopic}",
                            "key_points": [
                                "Provide predictions or recommendations for future trends in {subtopic}.",
                                "Explain how the field may evolve, especially for the {level} audience.",
                                "Highlight any opportunities for further research or innovation."

                """

        # Call multiple search engines and combine results
        result1 = integrated_function.mistral_search(query)
        result2 = integrated_function.llama2_search(query)
        result3 = integrated_function.llama3_search(query)

        # Combine the results into a single content string
        combined_result = f"Result from Model1:\n{result1}.add_page_break() Result from Model2:\n{result2}.add_page_break() Result from Model3:\n{result3}.add_page_break()"

        return combined_result

    def save_to_text_file(self, subtopic, content):
        """
        Save the generated content into a text file.
        """
        filename = f"{subtopic}_content.txt"
        with open(filename, 'w') as file:
            file.write(content)
        return f"Content saved to {filename}"


presentation_service = PresentationContentService()

subtopics = ['History of Aeronautics']
levels = ['Basics']

for subtopic, level in zip(subtopics, levels):
    content = presentation_service.content(subtopic, level)
    status = presentation_service.save_to_text_file(subtopic, content)
    print(status)