from fpdf import FPDF
name = input('Enter your name: ')

# Create a PDF object
pdf = FPDF()
pdf.add_page()

pdf.image('shirtificate.png', x=10, y=50, w=190)  # Adjust the x, y, and width as needed
# Set font and write text at the top
pdf.set_font("Times", size=36)
pdf.cell(0, 20, 'CS50 Shirtificate', align='C', ln=True)  # ln=True moves to the next line

pdf.set_text_color(255, 255, 255)  # White text, assuming the shirt background is dark
pdf.set_xy(55, 120)  # Adjust these coordinates to position the text inside the shirt
pdf.cell(100, 10, f'{name} took CS50', align='C')

# Move down and add the image
pdf.set_y(50)  # Adjust Y-position for the image

# Save the PDF
pdf.output('shirtificate.pdf')

