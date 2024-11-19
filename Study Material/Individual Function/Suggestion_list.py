import integrated_function
from subtopics import SubtopicGeneration, topics


class AutoSuggestion:
    def __init__(self, topics):
        self.topics = topics
        self.subtopic_generator = SubtopicGeneration()

    def get_suggestion(self):
        suggestions = []

        for topic in self.topics:
            domain_query = f"""I have just completed 
            {topic} and I am looking for the
            next level domains to focus on. 
            As an expert, please provide only a 
            list of the most suitable 
            domains I can explore next, 
            without any descriptions."""

            suggestion_list = integrated_function.mistral_search(domain_query)
            suggestions.append(suggestion_list)
            breakpoint()
        return suggestions


result = AutoSuggestion(topics).get_suggestion()
print(result)