class Researcher:
    def generate_literature(self, topic):
        # Generates structured mock literature based on topic
        papers = [
            {
                "title": f"Foundational Approaches to {topic}",
                "summary": f"This paper explains classical and theoretical foundations behind {topic}, including key algorithms and principles.",
                "keywords": ["foundations", topic, "baselines"],
                "url": "https://example.com/paper1"
            },
            {
                "title": f"Modern Machine Learning Techniques for {topic}",
                "summary": f"Explores modern ML and data-driven methods used in {topic}, focusing on model improvements and performance gains.",
                "keywords": ["state-of-the-art", topic, "advanced methods"],
                "url": "https://example.com/paper2"
            },
            {
                "title": f"Challenges and Future Directions in {topic}",
                "summary": f"Highlights limitations, open problems, and future research paths related to {topic}.",
                "keywords": ["future work", topic, "limitations"],
                "url": "https://example.com/paper3"
            }
        ]
        return papers
