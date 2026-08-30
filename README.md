# Text Analysis & Index Candidate Generator

A Python-based Natural Language Processing (NLP) pipeline that analyzes text documents (such as book chapters), performs custom text cleaning, transformer-based spaCy lemmatization and entity recognition, stop-word removal, frequency distribution analysis, and exports word occurrence data as candidate terms for indexing.

---

## 📌 Features

- **Text Processing & Cleaning**:
  - Replaces hyphens, dashes, and slashes with spaces.
  - Normalizes whitespace and line breaks.
  - Removes non-alphanumeric characters, punctuation, and possessive markers (e.g., 's).

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

.
├── clean&sort.py            # Primary analysis & processing script
├── Chapters/                # Directory containing input text files (e.g., Chapter1.txt)
├── WordLists/               # Directory where index candidate text files are saved
└── README.md                # Project documentation

---

## 🛠️ Requirements & Prerequisites

- **Python 3.8+**
- Python packages:
  - `spacy`

---

## 🚀 Installation & Setup

1. Clone or download the repository:
   git clone https://github.com/your-username/text-index-generator.git
   cd text-index-generator

2. Create and activate a virtual environment (optional but recommended):
   python -m venv venv
   # On macOS/Linux:
   source venv/bin/activate
   # On Windows:
   venv\Scripts\activate

3. Install required dependencies:
   pip install spacy

4. Download the spaCy Transformer Model:
   python -m spacy download en_core_web_trf

---

## 📂 Input & Output Preparation

1. **Input Directory (`Chapters/`)**:
   - Place your input text files inside a folder named `Chapters/`.
   - Ensure the input files are text documents encoded in UTF-8 (or UTF-8-SIG).

2. **Output Directory (`WordLists/`)**:
   - Outputs are automatically saved to the `WordLists/` directory. Ensure this folder exists before running the script.

---

## 🏃 Usage

Run the main analysis script:

python clean&sort.py

### Script Execution Workflow:
1. Iterates through every text file inside `Chapters/` using `pathlib.Path`.
2. Cleans text, processes it via spaCy, extracts named entities, lemmatizes tokens, and removes stopwords.
3. Prints the resulting dictionary of word frequencies to the console.
4. Computes the average term frequency.
5. Exports candidate index terms to `WordLists/<FileName>Index-Candidates.txt` formatted as:
   term, count
   ...
   average, average as a number

---

## ⚙️ Core Functions

- **`clean(text)`**: Cleans raw text, processes tokens and entities with `en_core_web_trf`, strips punctuation/possessives, and removes stopwords.
- **`sort(text)`**: Calculates term frequencies using `collections.Counter`, sorts keys alphabetically, and computes the mean term occurrence.
