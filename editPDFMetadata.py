from PyPDF2 import PdfFileWriter, PdfFileReader

output = PdfFileWriter()
#This in the file to be input
input1 = PdfFileReader(open("Sept_19th_2017_Minutes_Approved1.pdf", "rb"))

#prints total number of pages
print(input1.getNumPages())
#grab the pages from the original file
output.addPage(input1.getPage(0))
output.addPage(input1.getPage(1))
output.addPage(input1.getPage(2))

#add new metadata to new pages
output.addMetadata({u'/Title': u'Sept_19th_2017_Minutes_Approved'})

#output file name
outputStream = open("Sept_19th_2017_Minutes_Approved.pdf", "wb")
output.write(outputStream)
