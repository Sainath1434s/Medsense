# 💊 MedSense - Medicine Info Finder

**MedSense** is an intelligent Flask-based web application that helps users quickly retrieve detailed information about medicines using Natural Language Processing (NLP) techniques. It allows users to enter medicine names (even with spelling errors), and it returns the most relevant matches from a preprocessed dataset using fuzzy matching.

---

## 🧠 Project Overview

MedSense is designed to enhance healthcare accessibility by simplifying the way users search for medicine-related information. By applying **NLP-based fuzzy string matching**, the system can interpret and match user inputs even if they are misspelled or incomplete.

---

## 🚀 Features

- 🔍 **Fuzzy Search using NLP**: Handles typos, misspellings, and partial names.
- 🧾 Displays detailed information for each medicine:
  - Medicine Name
  - Composition
  - Uses
  - Side Effects
  - Manufacturer
  - User Review Percentages (Excellent, Average, Poor)
  - Image Preview
- ✨ **Animated UI** for an engaging user experience
- ⚡ Fast, responsive and lightweight Flask application

---

## 🛠️ Tech Stack

| Layer       | Technology           |
|-------------|----------------------|
| **Frontend**| HTML5, CSS3 (Animations) |
| **Backend** | Python (Flask)       |
| **Libraries**| pandas, fuzzywuzzy, Jinja2 |
| **NLP**     | Fuzzy Matching using `fuzzywuzzy` (Levenshtein Distance) |

---

## 🧪 NLP in Action

MedSense leverages **fuzzy string matching**, an NLP-based method that measures the similarity between user input and known medicine names using:

- **Levenshtein Distance**: Calculates how many edits (insertions, deletions, substitutions) are needed to change one word into another.
- **Token Sort Ratio** (from `fuzzywuzzy`): Reorders tokens alphabetically before comparing, improving matching for reordered words.

This makes the search robust and user-friendly, especially in real-world scenarios where inputs may be imperfect.

---

## 📁 Folder Structure

MedSense/
├── app.py                           # Main Flask application
├── Preprocessed_Medicine_Details.csv # Cleaned medicine dataset (input data)
├── requirements.txt                # Python dependencies
├── README.md                       # Project documentation
│
├── templates/
│   └── index.html                  # Jinja2 HTML template for frontend
│
├── static/
│   └── style.css                   # External CSS file with animations
