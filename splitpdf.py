# Splits PDF 
from PyPDF2 import PdfFileReader, PdfFileWriter
import pandas as pd

df = pd.read_csv('musicalcsv.csv')

df['seat_num'] = df['seats'].str[1:].astype(int)
df['seat_row'] = df['seats'].str[:1]
df = df.sort_values(by=['seat_row','seat_num']).reset_index()
print(df['seats'].to_string())

# Takes in the path of pdf to split, and the column in csv to name the pdf
# ei. df['seats']
def split(path, names_of_split):
    pdf = PdfFileReader(path)
    for page in range(pdf.getNumPages()):
        pdf_writer = PdfFileWriter()
        pdf_writer.addPage(pdf.getPage(page))

        output = f'{names_of_split[page]}.pdf'
        with open(output, 'wb') as output_pdf:
            pdf_writer.write(output_pdf)

split("merged.pdf", df['seats'])