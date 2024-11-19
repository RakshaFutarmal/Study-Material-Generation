from fpdf import FPDF


class PresentationContentService:
    def __init__(self):

        self.pdf = FPDF()
        self.pdf.set_auto_page_break(auto=True, margin=15)
        self.pdf.set_left_margin(20)
        self.pdf.set_right_margin(20)
        self.pdf.add_page()
        self.current_page_name = ""
        self.sections = []

    def header(self):

        self.pdf.image('/home/tntra/Information details/Study Material/assests/Shruti_logo_black.png', 10, 8, 33)
        self.pdf.set_font('Arial', 'B', 15)
        self.pdf.cell(80)

        self.pdf.cell(30, 10, 'Presentation Content', 0, 0, 'C')
        self.pdf.ln(20)

    def footer(self):
        self.pdf.set_y(-15)
        self.pdf.set_font('Arial', 'I', 10)
        self.pdf.cell(0, 10, f'Page {self.pdf.page_no()} - {self.current_page_name}', 0, 0, 'C')

    def add_toc_entry(self, title, page_no):
        """
        Add an entry to the table of contents (TOC).
        """
        self.sections.append({'title': title, 'page': page_no})

    def add_section(self, section_title):

        self.current_page_name = section_title
        self.add_toc_entry(section_title, self.pdf.page_no())

        self.pdf.set_font('Arial', 'B', 16)
        self.pdf.set_text_color(0, 102, 204)
        self.pdf.cell(0, 10, section_title, ln=True, align='L', border=0)
        self.pdf.ln(5)
        self.pdf.set_text_color(0, 0, 0)

    def add_txt_content_to_pdf(self, txt_filename):
        """
        Add text content from a file to the PDF, recognizing section titles and regular content.
        """
        with open(txt_filename, 'r') as file:
            content = file.readlines()

        self.pdf.set_font("Arial", size=12)
        for line in content:
            if line.strip().isupper():
                self.add_section(line.strip())
            else:
                self.pdf.multi_cell(0, 10, txt=line.strip(), border=0, align='L')

    def generate_pdf_from_txt(self, txt_filename):
        self.header()

        self.add_txt_content_to_pdf(txt_filename)

        pdf_filename = "inter.pdf"
        self.pdf.output(pdf_filename)
        return f"PDF generated and saved as {pdf_filename}"


presentation_service = PresentationContentService()
txt_filename = "/home/tntra/Documents/NeoTech/professional-mobility-test-develop/NeoTech Video Content/History of Aeronautics_content.txt"
content_status = presentation_service.generate_pdf_from_txt(txt_filename)
print(content_status)


