import os
from pathlib import Path

import PyPDF2


class PdfReader:
    def __init__(self) -> None:
        # Initialize a list to store page texts
        self.all_pages = []
        self.current_page = []
        self.opening_letter = None
        self.bullet = None
        self.sentence = ""

    def visitor_body(self, text: str, cm, tm, fontDict, fontSize):
        y = tm[5]
        if not (y > 50 and y < 750):
            return

        self.current_page.append(text)

    def extract_pdf_text(self, pdf_path):
        try:
            # Open the PDF file in binary mode
            with open(pdf_path, "rb") as pdf_file:
                # Create a PDF object
                pdf = PyPDF2.PdfReader(pdf_file)

                # Iterate through each page of the PDF
                for page in pdf.pages:
                    # Extract the text from the page and append to the list
                    page.extract_text(visitor_text=self.visitor_body)
                    self.all_pages.append("".join(self.current_page))
                    self.current_page = []
                return self.all_pages

        except FileNotFoundError:
            print(f"The file '{pdf_path}' was not found.")
        except Exception:
            print(f"Error reading '{pdf_path}'")
            raise


# File Locations
current_dir = Path(__file__).parent
input_pdf_path = current_dir / "postgis-3.4.pdf"
output_txt_path = current_dir / "manual.txt"

if os.path.exists(output_txt_path):
    with open(output_txt_path, "r") as file:
        output_txt = file.read()
else:
    # Call the function to extract PDF text
    reader = PdfReader()
    reader.extract_pdf_text(input_pdf_path)
    output_txt = "".join(reader.all_pages)
    with open(output_txt_path, "w") as file:
        file.write(output_txt)


if output_txt:
    # Create a JSON object with a 'text' key containing the extracted text
    pdf_text_json = {"text": output_txt}
