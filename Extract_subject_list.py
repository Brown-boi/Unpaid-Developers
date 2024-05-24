import re
import pdfplumber
import pandas as pd
import comparision as com
def extract_pdf_to_excel(pdf_path,data,courses):
    # Open the PDF file
    #pdf_path=filename+".pdf"
    with pdfplumber.open(pdf_path) as pdf:
        # Initialize an empty list to store extracted data
        extracted_data = []
        # Iterate over each page in the PDF
        for page in pdf.pages:
            # Extract text from the page
            text = page.extract_text()
            text = text.replace("\x00", "fi")
            # Split the text into lines
            lines = text.split('\n')
            #print(lines)
            extracted_data.extend(lines)
        outcome=[]

        # Define a regular expression pattern to match credit points
        credit_pattern = re.compile(r'\d+\s*CP')
        # Initialize an empty list to store core subjects
        core_subjects = []
        # Iterate through each line in the list
        for line in extracted_data:
              if re.search(credit_pattern, line):
                # If it does, it's likely a core subject, so add it to the core_subjects list
                core_subjects.append(line)
        split_data = [entry.split(' ', 2) for entry in core_subjects]
        df = pd.DataFrame(split_data, columns=['code', 'CP', 'Subject'])
        df['Subject'] = df['Subject'].apply(lambda x: x.replace('CP', ''))
        #print(df['Subject'])
        print("Sucessfully Extracted Subject list")
        #print("Extracting data from below subject code's")
        for index, item in enumerate(extracted_data):
            if data in item:
                break
        s_name = ' '.join(extracted_data[2:index])
        if data in courses:
            outcome=com.comparision_extraction(extracted_data,data)
            #col=outcome.pop(0)
        else:
            outcome=com.major_job_list(extracted_data,s_name.upper())
        return df,s_name.upper(),outcome
