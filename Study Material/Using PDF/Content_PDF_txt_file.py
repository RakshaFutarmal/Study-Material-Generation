import integrated_function


class PresentationContentService:

    def content(self, subtopic, level):
        """
        Generate and add content for a specific subtopic and level to the PDF.
        """
        query = f""" 
                    Title: Presenting {subtopic}

                    Your task is to develop a comprehensive PDF study material for the subtopic {subtopic} at level {level}. The purpose of this material is to provide a structured learning experience for students. It will include an outline of section requirements with detailed explanations, covering the fundamental concepts of the subtopic informative.

                    This study material will be structured around the following subheadings:

                    Introduction to {subtopic}

                    Provide an overview of the subtopic, explaining its scope, significance, and where it fits into the broader context of the subject.
                    Core Problem in {subtopic}

                    Identify and explain the central issue or challenge related to the subtopic. Discuss the complexity or the key challenge that the subtopic addresses.
                    Importance of {subtopic}

                    Explain why this subtopic is important, both in the academic context and in real-world applications. Discuss its relevance to the current subject of study and its long-term significance.
                    Key Concepts in {subtopic}

                    Highlight the core theories, principles, or definitions relevant to the subtopic. Explain these concepts in detail, ensuring clarity for the target learning level.
                    Proposed Solution for {subtopic} Challenge

                    Provide a well-researched solution or strategy that addresses the core problem discussed earlier. Break down how this solution can be practically applied or theoretically understood at the given level.
                    Benefits of the Proposed Solution

                    Outline the positive outcomes or advantages of implementing the proposed solution. Discuss how it resolves the issue and its impact on the subject or related fields.
                    Real-World Example of {subtopic}

                    Present a relevant real-world example or case study to demonstrate the application of the subtopic in practical settings. This will help students relate theoretical learning to real-life scenarios.
                    Actionable Insights in {subtopic}

                    Offer actionable advice or insights derived from the study of this subtopic. What should students take away from this section, and how can they apply this knowledge effectively?
                    Conclusion

                    Summarize the key points covered in the section. Reinforce the learning objectives and provide a final reflection on the subtopic’s importance in the broader academic or real-world context.
                    Additional Requirements:
                    Structured Content: Ensure that the study material is organized logically according to the subheadings. Each section should provide relevant and engaging content that aids understanding.

                    Key Considerations:

                    Make the content engaging and appropriate for the target academic level.
                    Focus on clarity, structured presentation, and depth of explanation."""

        # result = integrated_function.mistral_search(query)
        result1 = integrated_function.mistral_search(query)
        # result2 = integrated_function.llama2_search(query)
        # result3 = integrated_function.llama3_search(query)

        return result1

    def save_to_text_file(self, subtopic, content):
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