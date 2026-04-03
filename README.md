# 🔐 Secret Code Language – Python Encoder & Decoder CLI Tool

## 📌 Overview
Secret Code Language is a Python-based command-line project that encodes normal sentences into a custom secret format and decodes them back to original text.

It uses simple string manipulation combined with random token insertion to create a reversible encryption-style system.

---

## 🚀 Features
- Encode normal sentences into secret code
- Decode secret code back to original text
- Randomized encryption tokens for added uniqueness
- Handles short words differently
- Interactive CLI menu system (C / D / E)
- Error detection for invalid encoded words

---

## 🧠 How It Works

### 🔐 Encoding Logic:
- Words with length < 3 → characters are swapped
- Words with length ≥ 3 → placed first letter to last add 3 character as suffix and prefix 

  
### 📥 Decoding Logic:
- Short words are reversed back
- Encoded words are cleaned by removing prefix/suffix and restoring original order

---

## 🛠️ Technologies Used
- Python 3
- random module
- string manipulation
- loops & conditionals


👨‍💻 Author

 Nikhil Kumar
