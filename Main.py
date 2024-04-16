import pdf_download as pd
import Extract_subject_list as esl
import write_silo as ws
import pandas as p
#link='https://handbook.latrobe.edu.au/courses/2024/SBCS'
#filename='BCS.pdf'
#pd.pdf_download(link,filename)
name='BCS'
excel_path = name + ".xlsx"
data = esl.extract_pdf_to_excel(name)
excel_writer = p.ExcelWriter(excel_path, engine='xlsxwriter')
data.to_excel(excel_writer,sheet_name='All_Subjects', index=False)
file = open('CS.txt','w')
Cp=list(data['CP'])
subject=list(data['Subject'])
code=list(data['code'])
for i in range(len(Cp)):
    if int(Cp[i])>100:
        link='https://handbook.latrobe.edu.au/aos/2024/'+code[i]
        filename=code[i]+'.pdf'
        file.write("Major code: "+subject[i]+'\n')
        pd.pdf_download(link,filename)
        Spec = esl.extract_pdf_to_excel(code[i])
        Spec.to_excel(excel_writer, sheet_name=subject[i], index=False)
        for i in Spec['code']:
            ws.write_s(file, i)
    else:
        ws.write_s(file, code[i])
file.close()
excel_writer.save()