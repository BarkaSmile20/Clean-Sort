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
```

---

## 🛠️ Requirements & Prerequisites

- **Python 3.8+**
- Python packages:
  - `nltk`
  - `matplotlib`
  - `pandas`

---

## 🚀 Installation & Setup

1. **Clone or download the repository**:
   ```bash
   git clone [https://github.com/your-username/text-index-generator.git](https://github.com/your-username/text-index-generator.git)
   cd text-index-generator
   ```

2. **Create and activate a virtual environment (optional but recommended)**:
   ```bash
   python -m venv venv
   # On macOS/Linux:
   source venv/bin/activate
   # On Windows:
   venv\Scripts\activate
   ```

3. **Install required dependencies**:
   ```bash
   pip install nltk matplotlib pandas
   ```

4. **Download required NLTK resources**:
   Uncomment lines 2–4 in `clean&sort.py` or run the following once in Python:
   ```python
   import nltk
   nltk.download('punkt')
   nltk.download('punkt_tab')
   nltk.download('averaged_perceptron_tagger_eng')
   nltk.download('wordnet')
   ```

---

## 📂 Input & Output Preparation

1. **Input Directory (`Chapters/`)**:
   - Place your input text files inside a folder named `Chapters/`.
   - Ensure the input files are text documents encoded in UTF-8.

2. **Output Directory (`WordLists/`)**:
   - Check the folder named `WordLists/` when you have run the program to see the output.

---

## 🏃 Usage

Run the main analysis script:

```bash
python clean&sort.py
```

### Script Execution Workflow:
1. Iterates through every text file inside `Chapters/`.
2. Cleans, tokenizes, POS-tags, lemmatizes, and removes stopwords.
3. Prints word frequencies and the mean word frequency to the console.
4. Generates a horizontal bar chart displaying term occurrences.
5. Exports candidate index terms to `WordLists/<FileName>Index-Candidates.txt` formatted as:
   ```text
   term, count
   ...
   average, average as a number
   ```

---

## ⚙️ Core Functions

- **`get_wordnet_pos(treebank_tag)`**: Translates NLTK Penn Treebank POS tags into WordNet format (`ADJ`, `VERB`, `NOUN`, `ADV`) for context-aware lemmatization.
- **`lemmatize(text)`**: Tokenizes text, performs POS tagging, and returns a lemmatized string.
- **`clean(text)`**: Applies regular expressions to strip unnecessary punctuation and contractions, lowercases text, calls `lemmatize()`, and filters out stopwords.
- **`sort(text)`**: Counts term frequencies via `collections.Counter`, computes average term frequency, inserts `"average"`, and sorts terms alphabetically.
- **`plot(sorted_text, maximum)`**: Converts term counts to a `pandas.DataFrame` and renders a horizontal bar chart with `matplotlib`      .
