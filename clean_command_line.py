import sys
import clean_text as ct

# Reading command line arguments
inputFile=sys.argv[1]
outputFile=sys.argv[2]
ct.getStemmedDocument(inputFile, outputFile)
