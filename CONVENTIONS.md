# LLM Conventions

Here are conventions when edit different files.

---

## General Programming

- Prefer consist, unique variable names for easy text search & replace
- keep methods arguments under 8

## 1. Markdown

- Header should be similar to markdown filename
- Have `## Table of Contents` after markdown header
- Fix grammar mistakes

---

## 2. Python

- Organized helper methods into utilities folder obj_utl.py, arr_utl.py, num_utl.py ..

---

## 3. React

- Prefer functional component
- decouple UI component from data fetching logics

- 1st: Destructuring only necessary props, assign default value.
- 2nd: Get other global/3rd party variables
- 3rd: Define component's state
- 4th: Define event handler & other business logic
- 5th: Define early exit
- 6th: Define Sub UI variables
- 7th: Avoid complex logic in Final Return
