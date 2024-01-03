import tabula

# Read pdf into list of DataFrame
#dfs = tabula.read_pdf("pdfs/NCR_T-309-ND_122923.pdf", pages='3')

# Read remote pdf into list of DataFrame
#dfs2 = tabula.read_pdf("https://github.com/tabulapdf/tabula-java/raw/master/src/test/resources/technology/tabula/arabic.pdf")

# convert PDF into CSV file
tabula.convert_into("pdfs/NCR_T-309-ND_122923.pdf", "output.csv", output_format="csv", pages='4')

# convert all PDFs in a directory
#tabula.convert_into_by_batch("input_directory", output_format='csv', pages='all')