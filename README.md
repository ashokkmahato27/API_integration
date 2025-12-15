# Gemini Few‑Shot Prompting (Python)

## Overview

This script demonstrates **few‑shot prompting** using Google Gemini. The model is given 2 example Q&A pairs and asked to answer a new question in the **same short style**.

---

## Code

```python
import os
from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv()

GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

genai.configure(api_key=GOOGLE_API_KEY)

gemini_model = genai.GenerativeModel("gemini-2.5-flash")

gemini_response = gemini_model.generate_content("""
Example 1:
Q: What is photosynthesis?
A: Plants make food from sunlight.

Example 2:
Q: What is gravity?
A: A force that pulls objects toward Earth.

Q: In the same style, what is condensation?
""")

print(gemini_response.text)
```


## Concept Used: Few‑Shot Prompting


Few‑shot prompting = giving a few examples
so the AI follows the same pattern.

---

## Requirements

```bash
pip install python-dotenv google-generativeai
```

---

## Environment Setup

Create `.env` file:

```env
GOOGLE_API_KEY=your_api_key_here
```

---

## Run

```bash
python few_short_prompting.py
```

---

## Sample Output

<img width="1107" height="332" alt="image" src="https://github.com/user-attachments/assets/83669e07-9344-4070-a00f-867c22e17120" />


---

## Use Case

```text
• Learn prompt engineering
• Practice few-shot prompting
• Generate short factual answers
```
