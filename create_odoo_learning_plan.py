from fpdf import FPDF

# Create a PDF document
pdf = FPDF()
pdf.set_auto_page_break(auto=True, margin=15)
pdf.add_page()

# Title
pdf.set_font("Arial", 'B', 16)
pdf.cell(0, 10, "Odoo Learning Plan", ln=True, align='C')

# Add table header
pdf.set_font("Arial", 'B', 12)
header = ["Week", "Day", "Topics/Activities", "Hours"]
pdf.set_fill_color(200, 220, 255)

# Column widths
col_widths = [25, 25, 120, 30]

# Add header row
for i in range(len(header)):
    pdf.cell(col_widths[i], 10, header[i], 1, 0, 'C', 1)
pdf.ln()

# Add data rows to the PDF
pdf.set_font("Arial", '', 12)
data = [
    ["1", "1", "Installation and Setup (Odoo)", "6"],
    ["", "2", "Familiarize with Interface and Navigation (Odoo)", "6"],
    ["", "3", "Core Concepts: Architecture, Models, Views (Odoo)", "6"],
    ["", "4", "Core Concepts: Controllers (Odoo)", "6"],
    ["", "5", "Basic Functionalities of Odoo", "6"],
    ["", "6", "Documentation Review (Odoo)", "6"],
    ["", "7", "Hands-On Practice: Sample Project (Odoo)", "6"],
    ["2", "8", "Sales Module: Sales Orders and Quotations (Odoo)", "6"],
    ["", "9", "Sales Module: Customer Management (Odoo)", "6"],
    ["", "10", "Practice Sales Orders (Odoo)", "6"],
    ["", "11", "Invoicing Module: Learn Invoicing Processes (Odoo)", "6"],
    ["", "12", "Practice Invoicing and Billing (Odoo)", "6"],
    ["", "13", "Integration of Sales and Invoicing (Odoo)", "6"],
    ["", "14", "Review and Practice Sales & Invoicing (Odoo)", "6"],
    ["3", "15", "PostgreSQL Basics: Installation and Setup", "6"],
    ["", "16", "PostgreSQL: Data Types and Tables", "6"],
    ["", "17", "PostgreSQL: Queries and Joins", "6"],
    ["", "18", "PostgreSQL: Functions and Indexing", "6"],
    ["", "19", "Inventory Management: Stock Control (Odoo)", "6"],
    ["", "20", "Inventory Management: Product Tracking (Odoo)", "6"],
    ["", "21", "Practice Inventory Management (Odoo)", "6"],
    ["4", "22", "Docker Basics: Installation and Setup", "6"],
    ["", "23", "Docker: Working with Containers", "6"],
    ["", "24", "Docker: Docker Compose for Odoo", "6"],
    ["", "25", "Basic Customization: Forms and Views (Odoo)", "6"],
    ["", "26", "Experiment with Custom Fields (Odoo)", "6"],
    ["", "27", "Explore Other Relevant Modules (Odoo)", "6"],
    ["", "28", "Assess Integration with Other Modules (Odoo)", "6"],
    ["", "29", "Real-World Case Studies (Odoo)", "6"],
    ["", "30", "Analyze Business Workflows (Odoo)", "6"],
    ["5", "31", "User Authentication: Registration & Login (Odoo)", "6"],
    ["", "32", "Implement Inventory Management Feature (Odoo)", "6"],
    ["", "33", "Develop Sales Module (Odoo)", "6"],
    ["", "34", "Implement Reporting Features (Odoo)", "6"],
    ["", "35", "Optimize Application: Code Review & Testing (Odoo)", "6"],
    ["", "36", "Prepare Documentation: Setup & Usage (Odoo)", "6"],
    ["", "37", "Final Review and Project Wrap-Up", "6"],
    ["", "38", "Plan Next Steps for Continuous Learning", "6"],
]

# Add data rows to the PDF
for row in data:
    for i in range(len(row)):
        pdf.cell(col_widths[i], 10, row[i], 1)
    pdf.ln()

# Save the PDF to a file
pdf_output_path = "Odoo_Learning_Plan.pdf"
pdf.output(pdf_output_path)

print(f"PDF generated and saved as {pdf_output_path}")
