import wikipediaapi
from faker import Faker
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
import random
import os

# Initialize Faker to generate random data
fake = Faker()

# Initialize Wikipedia API with a proper user-agent
user_agent = 'FakePDFBot/1.0 (https://github.com/CodedCrow6/fake-pdf-generator; fakepdfbot@example.com)'
wiki_wiki = wikipediaapi.Wikipedia( user_agent=user_agent)
# Function to fetch random Wikipedia article text
def get_wikipedia_paragraphs():
    # Pick a random Wikipedia page title from a list of topics (you can extend this list)
    topics = ['Python_(programming_language)', 'Artificial_intelligence', 'Machine_learning', 'Data_science', 'History_of_computing']
    random_topic = random.choice(topics)
    page = wiki_wiki.page(random_topic)
    
    # Fetch sections and paragraphs
    paragraphs = []
    for section in page.sections:
        # Append first 2-3 sentences of each section (for better readability)
        paragraphs.append(section.text[:500])  # Adjust the length as necessary
    
    # Combine all paragraphs into one large text block
    return '\n\n'.join(paragraphs)

# Function to generate random filename
def generate_random_filename():
    random_name = fake.name().replace(" ", "_")  # Replace spaces with underscores
    return f"{random_name}_report.pdf"

# Function to generate random text (e.g., personal info)
def generate_random_text():
    # Generate fake data for various sections
    name = fake.name()
    address = fake.address().replace("\n", ", ")
    email = fake.email()
    phone_number = fake.phone_number()
    company = fake.company()
    job = fake.job()
    
    # Construct a random personal information section
    random_text = f"Name: {name}\n"
    random_text += f"Address: {address}\n"
    random_text += f"Email: {email}\n"
    random_text += f"Phone: {phone_number}\n"
    random_text += f"Company: {company}\n"
    random_text += f"Job: {job}\n\n"
    
    return random_text

# Function to create PDF with random and informative content
def create_pdf(pdf_filename):
    # Create a canvas object (a blank page)
    c = canvas.Canvas(pdf_filename, pagesize=letter)
    
    # Title and metadata for the PDF
    c.setFont("Helvetica-Bold", 16)
    c.drawString(72, 750, "Random Information Report")

    # Add a long introductory paragraph with random information
    c.setFont("Helvetica", 10)
    random_content = generate_random_text()
    
    # Set margins
    left_margin = 72  # 1-inch left margin
    right_margin = 72  # 1-inch right margin
    page_width = 612  # Letter page width
    max_text_width = page_width - left_margin - right_margin  # Calculate available width for text

    # Start writing the random content on the page
    y_position = 730
    for line in random_content.split("\n"):
        if y_position < 72:
            c.showPage()  # Create a new page if we run out of space
            y_position = 750
        c.drawString(left_margin, y_position, line)
        y_position -= 12  # Move down for the next line

    # Fetch and add multiple paragraphs from Wikipedia (informative content)
    wiki_paragraphs = get_wikipedia_paragraphs()
    
    # Write Wikipedia content to the PDF
    for line in wiki_paragraphs.split("\n"):
        if y_position < 72:
            c.showPage()  # Create a new page if we run out of space
            y_position = 750
        c.drawString(left_margin, y_position, line)
        y_position -= 12  # Move down for the next line

    # Save the PDF to the file
    c.save()

# Main function to create the PDF
if __name__ == "__main__":
    pdf_filename = generate_random_filename()  # Generate random filename
    create_pdf(pdf_filename)
    print(f"PDF created successfully with filename: {pdf_filename}")
