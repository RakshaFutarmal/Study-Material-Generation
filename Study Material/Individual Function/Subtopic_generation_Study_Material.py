import integrated_function

"""
This is the function for the subtopic generation.
"""

def get_subtopics(topics, levels):
    subtopics = []

    for topic in topics:
        for level in levels:
            subtopic_query = f"You are a subject matter expert providing detailed educational content. Your task is to generate a list of subtopics for the topic '{topic}' and categorize the subtopics into the '{level}' level. These subtopics will form the foundation of a learning module. Please ensure that the subtopics are relevant and comprehensive.and only 2 number of subtopics are generated."
            sub_topic_list = integrated_function.mistral_search(subtopic_query)
            subtopics.append(sub_topic_list)
    Breakpoint()
    return subtopics

topics = ['Basics of Algorithms and Mathematics']
levels = ['Basics']

result = get_subtopics(topics, levels)

