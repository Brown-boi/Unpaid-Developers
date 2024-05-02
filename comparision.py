import pdfplumber
import pandas as pd
def comparision_extraction(extracted_data):
        index=extracted_data.index("Location(s)")
        loc=extracted_data[index:index+2]
        index=extracted_data.index("Course duration (full time)")
        co=extracted_data[index:index+2]
        exchange=["Exchange program: "]
        if "Other opportunities" not in extracted_data:
            exchange.append("No")
        else:
            exchange.append("Yes")
        index=extracted_data.index("Career outcomes")
        end=extracted_data.index("Professional recognition")
        career=extracted_data[index+1:end]
        outcome=["Job opportunities:"]
        major=["Major Needed?"]
        for i in career:
            if len(i) < 40:
                if not i.endswith(".") and not i.endswith(":"):
                    outcome.append(i)
                    major.append("Not needed")
        if "Course duration (part time)" in extracted_data:
            index=extracted_data.index("Course duration (part time)")
            cop=extracted_data[index:index+2]
        else:
            cop=["Course duration (part time)","Not Available"]
        cre=extracted_data[4]
        credit=["Course credit points ",cre[5:]]
        return [outcome,major,exchange,loc,co,cop,credit]

def major_job_list(extracted_data,data):
        index=extracted_data.index("Career opportunities")
        end=extracted_data.index("\ue89e \ue89e \ue89e")
        career=extracted_data[index+1:end]
        outcome=[]
        major=[]
        for i in career:
            #print(len(i))
            if len(i) < 40:
                if not i.endswith(".") and not i.endswith(":"):
                    outcome.append(i)
                    major.append(data)
        return [outcome,major]

