# Client Account Data Extraction and Validation Program

## Project Overview

This project is designed to automate the extraction of client account data from PDF reports generated by the company's old financial planning software. The extracted data is then filtered into a structured database and cross-examined with the company's existing database to ensure accuracy and data integrity during a transition to new financial planning software.

By automating this process, the project improves data migration efficiency, reducing manual errors and saving time.

## Key Features

- **PDF Data Extraction**: The program extracts the following client account information from PDFs:
  - Client Name
  - Account Number
  - Internal Rate of Return (IRR)
  - Net Inflows and Outflows
- **Data Structuring**: The extracted data is stored in a dictionary, where the account number serves as the key and a custom `Account` class stores the account information.
- **Cross-Validation**: The structured data is compared with records from an existing database to verify the accuracy of client account information.
- **Efficient Data Lookup**: The account information is stored in a dictionary, enabling constant time (O(1)) lookup by account number.
- **Discrepancy Reporting**: The program generates a report highlighting any mismatches between the PDF-extracted data and the existing database, allowing for corrections before migration.

## Technologies Used

- **Python**: Primary programming language for data extraction, manipulation, and validation.
- **PyPDF2**: Python library used to extract text data from PDF files.
- **Pandas**: For reading and handling CSV/Excel files as well as structuring the extracted data.


## How It Works

### 1. PDF Extraction
The program uses the `PyPDF2` library to read PDF files and extract key information such as client names, account numbers, IRR, and net inflows/outflows.

### 2. Data Structuring
After extracting data from the PDFs, the program organizes it into a Python dictionary. Each key in the dictionary is an account number, and the value is an instance of the `CustomerAccount` class, which contains the following attributes:
- **Client Name**
- **Account Number**
- **Internal Rate of Return (IRR)**
- **Net Inflows/Outflows**

### 3. Data Cross-Validation
The program reads data from an existing database (which could be stored in CSV, Excel, or a relational database) and compares it against the extracted PDF data. This ensures that the migrated data is accurate and consistent.

### 4. Reporting Discrepancies
Any discrepancies found between the extracted PDF data and the existing database are logged and reported, allowing for manual review and correction if necessary.

