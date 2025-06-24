
# 🌐 DetectLangPy – Language Detection with Python

**DetectLangPy** is a simple yet powerful Python utility that detects the language of any input text using the `langdetect` library. Ideal for NLP beginners, automation tasks, and real-time input classification.

---

## 🚀 Features

- 🔍 Detects over 55 languages
- 💡 Simple command-line interface
- ⚙️ Based on Google's `langdetect` algorithm
- 🎯 Returns ISO 639-1 language codes (e.g., `en`, `ml`, `ta`, `hi`)

---

## 🧰 Requirements

Install the required package using pip:

```bash
pip install langdetect


---

🧑‍💻 How to Use

Run the script:

python language_detector.py

Example:

Enter a sentence to detect: இது தமிழ்
The detected language is: ta

> ta stands for Tamkl




---

🧠 Code Overview

from langdetect import detect, DetectorFactory

DetectorFactory.seed = 0  # Ensures consistent results

text = input("Enter a sentence to detect: ")
detected_language = detect(text)

print(f"The detected language is: {detected_language}")


---

🌍 Supported Languages

Some examples of detected language codes:

en → English

ml → Malayalam

hi → Hindi

ta → Tamil

fr → French

es → Spanish

ar → Arabic

de → German


Full list available here


---

📁 Project Structure

DetectLangPy/
├── language_detector.py
└── README.md


---

📌 Use Cases

📝 Detect language from user-submitted content

🌐 Pre-processing for multilingual apps

🤖 Training NLP models with labeled languages

📚 Language auto-labeling in datasets



---

📄 License

This project is licensed under the MIT License.


---

👤 Author

Developed by Kiran Kumar Vel

---

> If you like this project, give it a ⭐ on GitHub and feel free to fork and build upon it!
