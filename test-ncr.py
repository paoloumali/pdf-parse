import tabula
import PyPDF2

files = ["NCR_T-309-ND_122923", "NCR_T-307-ND_121523"]
for x in files:
  xFile = x+'.pdf'
  xObj = open('pdfs/'+xFile, 'rb')
  xReader = PyPDF2.PdfReader(xObj)
  # count pages
  xPages = len(xReader.pages)
  # cut 12 pages for NCR
  tabula.convert_into('pdfs/'+xFile, 'csvs/'+xFile+'.csv', output_format="csv", pages='4-'+str(xPages-12))