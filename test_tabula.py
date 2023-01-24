import tabula

# Read tables from the PDF
df = tabula.read_pdf("2072600.pdf", multiple_tables=True)

# Write the tables to an Excel file
df[0].to_excel("document.xlsx", index=False)
