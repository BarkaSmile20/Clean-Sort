# Text Analysis & Index Candidate Generator

A Python-based Natural Language Processing (NLP) pipeline that analyzes text documents (such as book chapters), performs custom text cleaning, POS-tagged lemmatization, stop-word removal, frequency distribution analysis, visual plotting, and exports word occurrence data as candidate terms for indexing.

---

## 📌 Features

- **Text Processing & Cleaning**:
  - Replaces hyphens, dashes, and slashes with spaces.
  - Removes non-alphanumeric punctuation while retaining single apostrophes appropriately.
  - Normalizes contractions and possessive markers (e.g., removing `'s`).
  - Converts text to lowercase and strips extraneous whitespace.

- **POS-Tagged Lemmatization**:
  - Leverages NLTK's `word_tokenize` and `pos_tag` to determine parts of speech.
  - Maps Treebank POS tags to WordNet POS tags (`NOUN`, `VERB`, `ADJ`, `ADV`) for context-aware lemmatization.

- **Custom Stopword Filtering**:
  - Uses an extensive custom stopword list to filter out common functional words, pronouns, auxiliary verbs, generic terms, and filler words.

- **Word Frequency Analysis**:
  - Computes exact word occurrences across cleaned chapter files.
  - Sorts unique lemmatized terms alphabetically.
  - Computes summary metrics such as the average word occurrence frequency per file.

- **Visualizations**:
  - Generates horizontal bar charts (`matplotlib`) displaying term occurrence counts.

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
