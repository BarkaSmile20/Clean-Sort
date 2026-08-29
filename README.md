# Text Analysis & Index Candidate Generator

A Python-based Natural Language Processing (NLP) pipeline that analyzes text documents (such as book chapters), performs custom text cleaning, transformer-based spaCy lemmatization and entity recognition, stop-word removal, frequency distribution analysis, visual plotting, and exports word occurrence data as candidate terms for indexing.

---

## 📌 Features

- **Text Processing & Cleaning**:
  - Replaces hyphens, dashes, and slashes with spaces.
  - Normalizes whitespace and line breaks.
  - Removes non-alphanumeric characters, punctuation, and possessive markers (e.g., `'s`).

- **spaCy Transformer NLP Pipeline**:
  - Uses spaCy's `en_core_web_trf` transformer model for high-accuracy tokenization, lemmatization, and Named Entity Recognition (NER).
  - Preserves recognized named entities as single multi-word terms while lemmatizing general vocabulary.

- **Custom Stopword Filtering**:
  - Filters out common functional words, pronouns, auxiliary verbs, generic terms, and filler words using a custom stopword list.

- **Word Frequency Analysis**:
  - Computes exact word and entity occurrences across cleaned text files.
  - Sorts unique lemmatized terms and entities alphabetically.
  - Computes the average occurrence frequency per file.

- **Export & Output**:
  - Saves term frequency outputs as `.txt` index candidates in the `WordLists/` directory for downstream book indexing or terminology analysis.

---

## 📁 Project Structure

```text
.
├── clean&sort.py            # Primary analysis & processing script
├── Chapters/                # Directory containing input text files (e.g., Chapter1.txt)
├── WordLists/               # Directory where index candidate text files are saved
└── README.md                # Project documentation
