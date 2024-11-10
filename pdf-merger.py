import PyPDF2
import os

def reverse_and_merge_pdfs(pdf1_path, pdf2_path, output_path):
    """
    Reverses the pages in the second PDF and merges it with the first PDF alternately.
    
    Args:
        pdf1_path (str): Path to the first PDF file
        pdf2_path (str): Path to the second PDF (pages to be reversed)
        output_path (str): Path where the merged PDF will be saved
    """
    try:
        # Open both PDF files
        pdf1 = PyPDF2.PdfReader(pdf1_path)
        pdf2 = PyPDF2.PdfReader(pdf2_path)
        
        # Create a PDF writer object
        pdf_writer = PyPDF2.PdfWriter()
        
        # Get the pages from second PDF in reverse order
        pdf2_pages = list(range(len(pdf2.pages)))
        pdf2_pages.reverse()
        
        # Calculate the maximum number of pages needed
        max_pages = max(len(pdf1.pages), len(pdf2.pages))
        
        # Merge pages alternately
        for i in range(max_pages):
            # Add page from first PDF if available
            if i < len(pdf1.pages):
                pdf_writer.add_page(pdf1.pages[i])
            
            # Add reversed page from second PDF if available
            if i < len(pdf2.pages):
                pdf_writer.add_page(pdf2.pages[pdf2_pages[i]])
        
        # Save the merged PDF
        with open(output_path, 'wb') as output_file:
            pdf_writer.write(output_file)
            
        return True, "PDFs successfully reversed and merged!"
        
    except Exception as e:
        return False, f"An error occurred: {str(e)}"

# Example usage
if __name__ == "__main__":
    # Replace these with your actual file paths
    pdf1_path = "1.pdf"
    pdf2_path = "2.pdf"
    output_path = "merged_output.pdf"
    
    # Check if input files exist
    if not os.path.exists(pdf1_path):
        print(f"Error: File {pdf1_path} not found!")
    elif not os.path.exists(pdf2_path):
        print(f"Error: File {pdf2_path} not found!")
    else:
        success, message = reverse_and_merge_pdfs(pdf1_path, pdf2_path, output_path)
        print(message)
