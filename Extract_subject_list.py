import re
import pdfplumber
import pandas as pd

def extract_pdf_to_excel(filename):
    # Open the PDF file
    pdf_path=filename+".pdf"
    with pdfplumber.open(pdf_path) as pdf:
        # Initialize an empty list to store extracted data
        extracted_data = []
        # Iterate over each page in the PDF
        for page in pdf.pages:
            # Extract text from the page
            text = page.extract_text()

            # Split the text into lines
            lines = text.split('\n')
            #print(lines)
            extracted_data.extend(lines)

        # Define a regular expression pattern to match credit points
        credit_pattern = re.compile(r'\d+\s*CP')
        # Initialize an empty list to store core subjects
        core_subjects = []
        # Iterate through each line in the list
        for line in extracted_data:
              if re.search(credit_pattern, line):
                # If it does, it's likely a core subject, so add it to the core_subjects list
                core_subjects.append(line)
        # Print the core subjects
        """for subject in core_subjects:
            print(subject)"""
        split_data = [entry.split(' ', 2) for entry in core_subjects]
        df = pd.DataFrame(split_data, columns=['code', 'CP', 'Subject'])
        df['Subject'] = df['Subject'].apply(lambda x: x.replace('CP', ''))
        print(df)
        #df = pd.DataFrame(core_subjects, columns=['Data'])
        # Write the DataFrame to an Excel file
        return df
        # Example usage
