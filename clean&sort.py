import nltk
# nltk.download('punkt_tab')
# nltk.download('averaged_perceptron_tagger_eng')
# nltk.download('wordnet')
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import word_tokenize
from nltk.corpus import wordnet
import re
import matplotlib.pyplot as plt
from pandas import DataFrame
from collections import Counter
from pathlib import Path

dir_path = Path("Chapters")

lemmatizer = WordNetLemmatizer()

stopwords = ["a", "an", "the", "this", "that", "these", "those", "each", "every", "either", "neither", "some", "any", "no", "all", "both", "half", "i", "you", "he", "she", "it", "we", "they", "me", "him", "her", "u", "us", "them", "my", "your", "his", "their", "our", "mine", "yours", "hers", "ours", "theirs", "who", "whom", "whose", "which", "what", "someone", "somebody", "something", "anyone", "anybody", "anything", "everyone", "everybody", "everything", "nobody", "nothing", "oneself", "about", "above", "across", "after", "against", "along", "among", "around", "at", "before", "behind", "below", "beneath", "beside", "between", "beyond", "by", "down", "during", "except", "for", "from", "in", "inside", "into", "like", "near", "of", "off", "on", "onto", "out", "outside", "over", "past", "since", "through", "throughout", "till", "to", "toward", "towards", "under", "underneath", "until", "up", "upon", "with", "within", "without", "and", "but", "or", "yet", "so", "for", "nor", "although", "as", "because", "if", "unless", "whereas", "while", "though", "since", "whether", "be", "have", "do", "will", "shall", "can", "may", "must", "ought", "get", "go", "make", "take", "say", "come", "see", "know", "think", "give", "find", "use", "tell", "seem", "keep", "show", "want", "become", "need", "let", "feel", "hear", "would", "could", "live", "consider", "claim", "believe", "assume", "relate", "reason", "point", "not", "never", "always", "often", "sometimes", "seldom", "rarely", "ever", "just", "only", "even", "also", "too", "very", "quite",  "rather", "almost", "nearly", "already", "yet", "still", "maybe", "perhaps", "here", "there", "where", "when", "how", "why", "now", "then", "again", "thence", "thereby", "therefore", "thus", "good", "new", "right", "alive", "basic", "legal", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten", "first", "second", "third", "last", "next", "many", "much", "few", "little", "more", "most", "less", "least", "several", "other", "another", "such", "own", "same", "different", "body", "attitude", "role", "life", "emotion", "discussion", "problem", "issue", "pain", "person", "people", "etc", "eg", "ie", "versus", "vs", "via", "re", "per", "pro"]

def get_wordnet_pos(treebank_tag):
    if treebank_tag.startswith("J"):
        return wordnet.ADJ
    elif treebank_tag.startswith("V"):
        return wordnet.VERB
    elif treebank_tag.startswith("N"):
        return wordnet.NOUN
    elif treebank_tag.startswith("R"):
        return wordnet.ADV
    else:
        return wordnet.NOUN

def lemmatize(text):
    word_pos = nltk.pos_tag(word_tokenize(text))
    lemmatized_words = [lemmatizer.lemmatize(word, get_wordnet_pos(pos_tag)) for word, pos_tag in word_pos]
    return " ".join(lemmatized_words)

def clean(text):
    text = re.sub(r'[-–—/]', ' ', text)
    text = re.sub(r"[^‘’\w\s]", '', text)
    text = re.sub(r"\b\w*[‘’](?!s\b)\w*\b", '', text)
    text = re.sub(r"’s", '', text)
    text = re.sub(r'\s+', ' ', text).strip()
    cleaned_text = [word for word in lemmatize(text.lower()).split() if word not in stopwords]
    return cleaned_text

maximum = 0

def sort(text):
    global maximum
    counts = Counter(text)
    if counts:
        maximum = max(counts.values())
    sorted_text = dict(sorted(counts.items()))
    mean = sum(sorted_text.values()) / len(sorted_text) if sorted_text else 0
    sorted_text["average"] = mean
    print(sorted_text)
    return sorted_text

def plot(sorted_text, maximum):
    df = DataFrame(sorted_text.items(), columns=["Word", "Count"])
    plt.barh(df["Word"], df["Count"])
    plt.xlabel("Word")
    plt.ylabel("Word Count")
    plt.title("Word Occurrence in the Text")
    plt.ylim(-0.5, 25.5)
    plt.xlim(-0.5, maximum + 0.5)
    plt.show()

for path in dir_path.iterdir():
    if path.is_file():
        with open(path, "r", encoding='utf-8-sig', errors="replace") as file:
            input_text = file.read()

        sorted_text = sort(clean(input_text))
        plot(sorted_text, maximum)
        output_text = []
        for key, value in sorted_text.items():
            output_text.append(", ".join([key, str(value)]))

        with open(f"WordLists/{path.name[:-6]}Index-Candidates.txt", "w", encoding="utf-8-sig", errors="replace") as file2:
            file2.writelines("\n".join(output_text))