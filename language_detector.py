# Detect the language of a given sentence using langdetect

from langdetect import detect, DetectorFactory

# For consistent results across runs
DetectorFactory.seed = 0

# Input from user
text = input("Enter a sentence to detect: ")

# Detect language
detected_language = detect(text)

# Output
print(f"The detected language is: {detected_language}")
