import pdf_download as pd
import Extract_subject_list as esl
import write_silo as ws
import pandas as p
courses=['SBCS','SBIT','SBCY']
#courses=['SBCY']
import os
for c in courses:
    print('Extracting data for '+c + ' Course')
    # Directory path you want to check or create
    directory_path = "E:/7th sem/major project/programs/patato/paperimages/idp/"+c
    # Check if the directory exists
    if not os.path.exists(directory_path):
        # If the directory doesn't exist, create it
        os.makedirs(directory_path)
    directory_path=directory_path+'/'
    file_path=directory_path+c+'.pdf'
    if not os.path.isfile(file_path):
        link='https://handbook.latrobe.edu.au/courses/2024/'+c
        pd.pdf_download(link,file_path)
    excel_path = directory_path +c+ ".xlsx"
    data,c_name,outcome = esl.extract_pdf_to_excel(file_path,c,courses)
    excel_writer = p.ExcelWriter(excel_path, engine='xlsxwriter')
    text_path=directory_path + c + ".txt"
    file = open(text_path,'w')
    Cp=list(data['CP'])
    subject=list(data['Subject'])
    code=list(data['code'])
    m_name=[]
    m_link=[]
    for i in range(len(Cp)):
        if int(Cp[i])>100:
            s_name=[]
            s_link=[]
            M_directory_path = directory_path+code[i]
            # Check if the directory exists
            if not os.path.exists(M_directory_path):
                # If the directory doesn't exist, create it
                os.makedirs(M_directory_path)
            M_directory_path=M_directory_path+'/'
            filename = M_directory_path+code[i]+'.pdf'
            link = 'https://handbook.latrobe.edu.au/aos/2024/' + code[i]
            m_link.append(link)
            if not os.path.isfile(filename):
                pd.pdf_download(link, filename)
            Spec,m,o = esl.extract_pdf_to_excel(filename,code[i],courses)
            outcome[0]=outcome[0]+o[0]
            outcome[1]=outcome[1]+o[1]
            print("extracting data for : ", m)
            file.write("Major subject name: " + m + '\n')
            m_name.append(m)
            for t in Spec['code']:
                s,l=ws.write_s(file, t,M_directory_path)
                s_name.append(s)
                s_link.append(l)
            Spec['Subject']=s_name
            Spec['Link']=s_link
            Spec.to_excel(excel_writer, sheet_name=m, index=False)
            flag=1
        else:
            m, li = ws.write_s(file, code[i],directory_path)
            m_name.append(m)
            m_link.append(li)
            flag=0
    if flag==0:
        outcome.pop(1)
    outcome = p.DataFrame(outcome)
    outcome = outcome.transpose()
    outcome.columns = outcome.iloc[0]
    outcome = outcome[1:]
    outcome = outcome.reset_index(drop=True)
    outcome.to_excel(excel_writer, sheet_name='Comparision', index=False)
    data['Subject'] = m_name
    data['Link'] = m_link
    data.to_excel(excel_writer,sheet_name='Core_Subjects', index=False)
    file.close()
    excel_writer.save()
    print('Sucessfully Extracted data for '+ c + ' Course')
    print("please find the data at this location: ",directory_path)