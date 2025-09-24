import pypandoc

pypandoc.download_pandoc()

output = pypandoc.convert_file("myDoc.docx", "md", outputfile="myDoc.md")
print("Conversion terminée :", output)
