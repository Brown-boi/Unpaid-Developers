import silo as s
import pdf_download as pd

def write_s(file,data):
    link='https://handbook.latrobe.edu.au/subjects/2024/'+data
    filename=data+".pdf"
    print(data)
    file.write("Subject code: "+data)
    file.write('\n')
    pd.pdf_download(link, filename)
    temp=s.silo_extaction(filename)
    for i in temp:
        file.write(i)
        file.write('\n')
    file.write('\n')

