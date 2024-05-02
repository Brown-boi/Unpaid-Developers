import pdfplumber
import pandas as pd

def silo_extaction(filename,data):
    # Open the PDF file
    with pdfplumber.open(filename) as pdf:
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
        silo=["Subject intended learning outcomes"]
        indx=extracted_data.index("Subject intended learning outcomes")
        if "Enrolment rules" in extracted_data:
            end=extracted_data.index("Enrolment rules")
        else:
            end=1000
        if "Learning activities" in extracted_data:
            end1=extracted_data.index("Learning activities")
            end=min(end,end1)
        else:
            end1=999
        if '\ue89e \ue89e \ue89e' in extracted_data:
            end2 = extracted_data.index("\ue89e \ue89e \ue89e")
            end = min(end, end1,end2)
        else:
            end2 = 998
        if "Requisite rules" in extracted_data:
            end3=extracted_data.index("Requisite rules")
            end=min(end,end1,end2,end3)
        silo=extracted_data[indx:end]
        for index, item in enumerate(extracted_data):
            if data in item:
                break
        s_name = ' '.join(extracted_data[2:index])
        return silo,s_name