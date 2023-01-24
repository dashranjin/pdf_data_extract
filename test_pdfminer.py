from io import StringIO
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfpage import PDFPage
def extract_text_from_pdf(pdf_path):
    resource_manager = PDFResourceManager()
    string_io = StringIO()
    converter = TextConverter(resource_manager, string_io, laparams=LAParams())
    page_interpreter = PDFPageInterpreter(resource_manager, converter)

    with open(pdf_path, 'rb') as fh:
        for page in PDFPage.get_pages(fh, caching=True, check_extractable=True):
            page_interpreter.process_page(page)

        text = string_io.getvalue()

    # close open handles
    converter.close()
    string_io.close()

    if text:
        return text

# Usage
pdf_text = extract_text_from_pdf("./2072600.pdf")
print(pdf_text)
# df = pd.read_csv(StringIO(pdf_text))
# df.to_excel('demomine.xlsx', index=False)


# Split the text by newlines
lines = pdf_text.split('\n')

# Create an empty list to store the data
# data = []

# # Iterate over the lines of text
# for line in lines:
#     # Split the line by commas
   
#     # Append the columns to the data list
#     data.append(line)

# print(data)

# # Create a DataFrame from the data
# df = pd.DataFrame(data)
# # df.to_excel("demo.xlsx", index=False)
# # Print the DataFrame
# print(df)
