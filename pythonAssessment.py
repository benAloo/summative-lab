import spacy
from collections import Counter
from docx import Document
from functools import cached_property


class NewsArticleAnalyzer:
    def __init__(self, text: str, nlp):
        self.text = text
        self.nlp = nlp
        self.doc = self.nlp(text)

    @cached_property
    def words(self):
        """Filtered words (no stopwords, punctuation)."""
        return [
            token.text.lower()
            for token in self.doc
            if token.is_alpha and not token.is_stop
        ]

    def count_specific_word(self, target_word: str) -> int:
        return sum(token.text.lower() == target_word.lower() for token in self.doc)

    def identify_most_common_word(self) -> tuple:
        counter = Counter(self.words)
        return counter.most_common(1)[0] if counter else ("", 0)

    def calculate_average_word_length(self) -> float:
        lengths = [len(token.text) for token in self.doc if token.is_alpha]
        return sum(lengths) / len(lengths) if lengths else 0

    def count_paragraphs(self) -> int:
        return sum(1 for p in self.text.split("\n") if p.strip())

    def count_sentences(self) -> int:
        return sum(1 for _ in self.doc.sents)


# -------------------------------
# Utility: Read .docx file
# -------------------------------
def read_docx(file_path: str) -> str:
    doc = Document(file_path)
    return "\n".join(paragraph.text for paragraph in doc.paragraphs)


# -------------------------------
# Main Execution
# -------------------------------
if __name__ == "__main__":
    # Load spaCy ONCE (efficient)
    nlp = spacy.load("en_core_web_sm")
    print("spaCy model loaded:", nlp.meta["name"])
    
    # Read actual file
    file_path = "News Article for Python Assessment.docx"
    text = read_docx(file_path)

    analyzer = NewsArticleAnalyzer(text, nlp)

    target_word = "apple"

    print(f"Occurrences of '{target_word}':", analyzer.count_specific_word(target_word))
    print("Most common word:", analyzer.identify_most_common_word())
    print("Average word length:", round(analyzer.calculate_average_word_length(), 2))
    print("Number of paragraphs:", analyzer.count_paragraphs())
    print("Number of sentences:", analyzer.count_sentences())