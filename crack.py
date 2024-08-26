import PyPDF2


def try_decrypt_pdf(file_path, passwords):
    # Open the PDF file
    with open(file_path, "rb") as pdf_file:
        # Create a PDF reader object
        pdf_reader = PyPDF2.PdfReader(pdf_file)

        # Check if the PDF is encrypted
        if not pdf_reader.is_encrypted:
            print("The PDF is not encrypted.")
            return pdf_reader

        # Try each password
        for password in passwords:
            if pdf_reader.decrypt(password):
                print(f"Successfully decrypted the PDF with password: {password}")
                return pdf_reader

        # If no password worked
        print("Failed to decrypt the PDF. None of the provided passwords worked.")
        return None


def process_pdf(pdf_reader):
    if pdf_reader:
        # Get the number of pages in the PDF
        print(pdf_reader.pages)
        num_pages = len(pdf_reader.pages)
        print(f"The PDF has {num_pages} pages.")

        # Extract text from the first page
        first_page = pdf_reader.pages[0]
        text = first_page.extract_text()
        print("Text from the first page:")
        print(text[:500] + "...")  # Print first 500 characters
    else:
        print("Cannot process the PDF as it couldn't be decrypted.")


# Usage
pdf_path = "pdf_example.pdf"
password_combinations = [f"{i:04d}" for i in range(10000)]

pdf_reader = try_decrypt_pdf(pdf_path, password_combinations)
process_pdf(pdf_reader)
