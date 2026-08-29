import spacy
import re
import matplotlib.pyplot as plt
from pandas import DataFrame
from collections import Counter
from pathlib import Path

nlp = spacy.load('en_core_web_trf')

dir_path = Path("Chapters")

stopwords = ["'", "'s", "a", "an", "the", "this", "that", "these", "those", "each", "every", "either", "neither", "some", "any", "no", "all", "both", "half", "i", "you", "he", "she", "it", "we", "they", "me", "him", "her", "u", "us", "them", "my", "your", "his", "their", "our", "mine", "yours", "hers", "ours", "theirs", "who", "whom", "whose", "which", "what", "someone", "somebody", "something", "anyone", "anybody", "anything", "everyone", "everybody", "everything", "nobody", "nothing", "oneself", "about", "above", "across", "after", "against", "along", "among", "around", "at", "before", "behind", "below", "beneath", "beside", "between", "beyond", "by", "down", "during", "except", "for", "from", "in", "inside", "into", "like", "near", "of", "off", "on", "onto", "out", "outside", "over", "past", "since", "through", "throughout", "till", "to", "toward", "towards", "under", "underneath", "until", "up", "upon", "with", "within", "without", "and", "but", "or", "yet", "so", "for", "nor", "although", "as", "because", "if", "unless", "whereas", "while", "though", "since", "whether", "be", "have", "do", "will", "shall", "can", "may", "must", "ought", "get", "go", "make", "take", "say", "come", "see", "know", "think", "give", "find", "use", "tell", "seem", "keep", "show", "want", "become", "need", "let", "feel", "hear", "would", "could", "live", "consider", "claim", "believe", "assume", "relate", "reason", "point", "not", "never", "always", "often", "sometimes", "seldom", "rarely", "ever", "just", "only", "even", "also", "too", "very", "quite",  "rather", "almost", "nearly", "already", "yet", "still", "maybe", "perhaps", "here", "there", "where", "when", "how", "why", "now", "then", "again", "thence", "thereby", "therefore", "thus", "good", "new", "right", "alive", "basic", "legal", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten", "first", "second", "third", "last", "next", "many", "much", "few", "little", "more", "most", "less", "least", "several", "other", "another", "such", "own", "same", "different", "body", "attitude", "role", "life", "emotion", "discussion", "problem", "issue", "pain", "person", "people", "etc", "eg", "ie", "versus", "vs", "via", "re", "per", "pro"]

def clean(text):
    text = re.sub(r'[-–—/]', ' ', text)
    text = re.sub(r"[\r\n]+", '. ', text)
    text = re.sub(r"[^\S\r\n]+", ' ', text).strip()
    doc = nlp(text)
    cleaned_text = []
    i = 0
    for ent in doc.ents:
        for token in doc[i: ent.start]:
            lemma = token.lemma_.lower()
            if not token.is_space and not token.is_punct and not token.is_digit and lemma not in stopwords:
                cleaned_val = re.sub(r'[^a-zA-Z]', '', re.sub(r"'s", '', re.sub(r' s$', '', lemma)))
                if cleaned_val and not cleaned_val.isdigit():
                    cleaned_text.append(cleaned_val)
        if ent.text.lower() not in stopwords:
            entity_lemmas = [token.lemma_ for token in ent]
            entity_str = " ".join(entity_lemmas)
            cleaned_val = re.sub(r'^\s+|\s+$', '', re.sub(r'[^a-zA-Z0-9\s]', '', re.sub(r"'s", '', re.sub(r' s$', '', entity_str))))
            if cleaned_val and not cleaned_val.isdigit():
                cleaned_text.append(cleaned_val)
        i = ent.end
    for token in doc[i:]:
        lemma = token.lemma_.lower()
        if not token.is_space and not token.is_punct and not token.is_digit and lemma not in stopwords:
            cleaned_val = re.sub(r'[^a-zA-Z]', '', re.sub(r"'s", '', re.sub(r' s$', '', lemma)))
            if cleaned_val:
                cleaned_text.append(cleaned_val)
    return [word for word in cleaned_text if word]

def sort(text):
    counts = Counter(text)
    if counts:
        maximum = max(counts.values())
    sorted_text = dict(sorted(counts.items()))
    mean = sum(sorted_text.values()) / len(sorted_text) if sorted_text else 0
    sorted_text["average"] = mean
    print(sorted_text)
    return sorted_text, maximum, mean

for path in dir_path.iterdir():
    if path.is_file():
        with open(path, "r", encoding='utf-8-sig', errors="replace") as file:
            input_text = file.read()
        tokens = clean(input_text)
        sorted_text, maximum, mean = sort(tokens)
        #plot(sorted_text, maximum)
        output_text = [f"{key}, {value}" for key, value in sorted_text.items()]
        output_text.append(f"average, {mean}")
        with open(f"WordLists/{path.name[:-6]}Index-Candidates.txt", "w", encoding="utf-8-sig", errors="replace") as file2:
            file2.writelines("\n".join(output_text))
