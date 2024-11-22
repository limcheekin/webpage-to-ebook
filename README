# **Webpage to eBook Converter**

A Python script to convert any webpage into an EPUB eBook file. This tool uses `requests` to fetch webpage content, `BeautifulSoup` to parse HTML, and `ebooklib` to generate an EPUB file.

## **Features**
- Fetch webpage content from a URL.
- Automatically formats the HTML into a readable EPUB structure.
- Creates an eBook with a specified title.
- Easy-to-use CLI and a helper Bash script for automation.

---

## **Getting Started**

### **Prerequisites**
- Python 3.8 or higher installed.
- A virtual environment setup (recommended).
- Install required Python packages.

### **Setup**
1. Clone the repository:
   ```bash
   git clone https://github.com/limcheekin/webpage-to-ebook.git
   cd webpage-to-ebook
   ```

2. Create and activate a virtual environment:
   ```bash
   python -m venv .venv
   source .venv/bin/activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

---

## **Usage**

### **Run Python Script**
Use the Python script directly from the CLI:

```bash
python create_ebook.py <URL> <TITLE>
```

**Example**:
```bash
python create_ebook.py "https://example.com/article" "My First eBook"
```

### **Use the Bash Script**
For convenience, use the provided Bash script to activate the virtual environment and run the Python script:

1. Ensure the Bash script is executable:
   ```bash
   chmod +x create_ebook.sh
   ```

2. Run the script:
   ```bash
   ./create_ebook.sh <URL> <TITLE>
   ```

**Example**:
```bash
./create_ebook.sh "https://example.com/article" "My First eBook"
```

---

## **File Structure**
```
webpage-to-ebook/
├── create_ebook.py        # Python script to create EPUB eBook
├── create_ebook.sh    # Bash script for automation
├── requirements.txt       # Python dependencies
└── README.md              # Project documentation
```

---

## **Dependencies**
The project uses the following Python libraries:
- `requests`
- `beautifulsoup4`
- `ebooklib`

Install them with:
```bash
pip install -r requirements.txt
```

---

## **Contributing**
Contributions are welcome! To contribute:
1. Fork the repository.
2. Create a new branch:
   ```bash
   git checkout -b feature-name
   ```
3. Commit your changes:
   ```bash
   git commit -m "Add feature description"
   ```
4. Push to the branch:
   ```bash
   git push origin feature-name
   ```
5. Open a pull request.

---

## **License**
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

## **Acknowledgments**
- [Ebooklib](https://github.com/aerkalov/ebooklib) for the EPUB generation library.
- [BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/) for HTML parsing.
- Original inspiration for the `create_ebook.py` script was adapted from the article [20 Python Scripts That Will Give You Superpowers](https://blog.stackademic.com/20-python-scripts-that-will-give-you-superpowers-4c6f4b15fe63) by Stackademic.