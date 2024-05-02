import silo as s
import pdf_download as pd
import os
def write_s(file,data,directory_path):
    filename=directory_path+data+".pdf"
    print(data)
    file.write("Subject code: "+data)
    file.write('\n')
    link = 'https://handbook.latrobe.edu.au/subjects/2024/' + data
    if not os.path.isfile(filename):
        pd.pdf_download(link, filename)
    temp,s_name=s.silo_extaction(filename,data)
    for i in temp:
        file.write(i)
        file.write('\n')
    file.write('\n')
    return s_name,link

