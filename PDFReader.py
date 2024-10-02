
import re
import pandas as pd
from PyPDF2 import PdfReader

def extract_pdf_info(pdf_path):
    reader = PdfReader(pdf_path)
    num_pages = len(reader.pages)

    extracted_data = []

    for page_num in range(num_pages):
        page = reader.pages[page_num]
        text = page.extract_text()

        # Using regular expressions to find specific information
        account_holder_match = re.search(r'FOR:\s*(.+)\s\((\w+)\)', text)
        irr = re.search(r'Internal Rate of Return\s*([\d\.]+%)', text)
        net_inflows_outflows = re.search(r'Net Inflows and Outflows\s*\(see details below\)\s*([\d\.,]+)', text)

        # Append the data if found
        if account_holder_match and irr and net_inflows_outflows:
            extracted_data.append({
                "For": account_holder_match.group(1),
                "Account Number": account_holder_match.group(2),
                "Internal Rate of Return (IRR)": irr.group(1),
                "Net Inflows and Outflows (CAD)": net_inflows_outflows.group(1)
            })

    return extracted_data


def save_to_spreadsheet(data, output_path):

    df = pd.DataFrame(data)

    df.to_excel(output_path, index = False)

# Example usage
# pdf_path = input("Enter full path to file: ")
pdf_path = "FullNDEX.pdf"  # Replace with your PDF file path
data = extract_pdf_info(pdf_path)



output_path = "NBINData.xlsx"
save_to_spreadsheet(data, output_path)

