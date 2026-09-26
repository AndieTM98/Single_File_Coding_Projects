# This program accepts a PDF, TXT, or Doc file and reads it aloud
import pyttsx3
import PyPDF2
import docx

# GUI file picker for selecting the file to read aloud
from tkinter import Tk
from tkinter.filedialog import askopenfilename


def read_pdf(file_path):
    with open(file_path, "rb") as file:
        reader = PyPDF2.PdfReader(file)
        text = ""
        for page in reader.pages:
            text += page.extract_text()
    return text


def read_docx(file_path):
    doc = docx.Document(file_path)
    text = ""
    for paragraph in doc.paragraphs:
        text += paragraph.text + "\n"
    return text


def read_txt(file_path):
    with open(file_path, "r") as file:
        text = file.read()
    return text


def speak_and_display(text):
    lines = text.splitlines()
    for line in lines:
        if not line.strip():
            continue  # skip blank lines
        print(line)
        engine = pyttsx3.init()
        engine.say(line)
        engine.runAndWait()
        engine.stop()
        del engine


def main():
    Tk().withdraw()  # Hide the root window
    file_path = askopenfilename(
        title="Select a file",
        filetypes=[
            ("PDF files", "*.pdf"),
            ("Word files", "*.docx"),
            ("Text files", "*.txt"),
        ],
    )
    if not file_path:
        print("No file selected")
        return
    if file_path.endswith(".pdf"):
        text = read_pdf(file_path)
    elif file_path.endswith(".docx"):
        text = read_docx(file_path)
    elif file_path.endswith(".txt"):
        text = read_txt(file_path)
    else:
        print("Unsupported file format")
        return
    speak_and_display(text)


if __name__ == "__main__":
    main()
