from PyPDF2 import PdfFileWriter, PdfFileReader

output = PdfFileWriter()

input2 =PdfFileReader(open("Sept_19th_2017_Minutes_Approved.pdf", "rb"))
print(input2.getDocumentInfo())
print("Number of pages, Use this number to edit the Metadata changer: ")
print(input2.getNumPages())

