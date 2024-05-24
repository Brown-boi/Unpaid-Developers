import silo as s
import pdf_download as pd
import os
import Subject_instances as si
def write_s(file,data,directory_path):
    filename=directory_path+data+".pdf"
    print(data)
    file.write("Subject code: "+data)
    file.write('\n')
    link = 'https://handbook.latrobe.edu.au/subjects/2024/' + data
    ins_file = open('subject_instances.txt', 'a')
    if not os.path.isfile(filename):
        pd.pdf_download(link, filename)
    temp,s_name=s.silo_extaction(filename,data)
    for i in temp:
        file.write(i)
        file.write('\n')
    file.write('\n')
    if data !="ABS0WOM" and data !="CSE1OOF" and data!= "CSE3PPE" and data!="CSE3PSD" and data!="CSE3SMT":
        ins_file.write('\n')
        ins_file.write("Subject_code: "+data)
        ins_file.write('\n')
        ins_file.write("Subject_name: "+s_name)
        ins_file.write('\n')
        si.subject_instances(ins_file, link)
        ins_file.close()
    return s_name,link

