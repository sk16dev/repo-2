def create_prompt(question, context):
    prompt_template = f"""
    Question: {question}
    Context: {context}
    Answer: Let's delve into the topic in detail.

    ### Key Points:

    1. **Introduction**:
       - Provide an overview of the topic.
       - Define any key terms or concepts.

    2. **Details**:
       - Explain the main aspects in detail.
       - Include relevant examples or case studies.
       - Discuss any important subtopics.

    3. **Applications**:
       - Describe practical applications or use cases.
       - Mention any industries or fields where it is particularly relevant.

    4. **Advantages and Challenges**:
       - List the benefits and advantages.
       - Address any potential challenges or drawbacks.

    5. **Conclusion**:
       - Summarize the main points.
       - Provide a final thought or recommendation.

    Answer:
    """
    return prompt_template
