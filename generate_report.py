from fpdf import FPDF

class PDF(FPDF):
    def header(self):
        self.set_font('helvetica', 'B', 15)
        self.cell(0, 10, 'UPI Leak Detector - Project Report', border=False, align='C', new_x="RIGHT", new_y="TOP")
        self.ln(20)

    def footer(self):
        self.set_y(-15)
        self.set_font('helvetica', 'I', 8)
        self.cell(0, 10, f'Page {self.page_no()}', 0, 0, 'C', new_x="RIGHT", new_y="TOP")

def generate_report():
    pdf = PDF()
    pdf.add_page()
    
    # Title Page
    pdf.set_font("helvetica", 'B', 24)
    pdf.cell(0, 40, "", new_x="LMARGIN", new_y="NEXT") # Spacer
    pdf.cell(0, 10, "Project Report", align='C', new_x="LMARGIN", new_y="NEXT")
    pdf.set_font("helvetica", 'B', 32)
    pdf.set_text_color(29, 78, 216) # Primary blue
    pdf.cell(0, 20, "UPI LEAK DETECTOR", align='C', new_x="LMARGIN", new_y="NEXT")
    pdf.set_font("helvetica", '', 14)
    pdf.set_text_color(100, 100, 100)
    pdf.cell(0, 10, "Automated AI-Powered Financial Tracking System", align='C', new_x="LMARGIN", new_y="NEXT")
    
    pdf.ln(30)
    pdf.set_font("helvetica", 'B', 14)
    pdf.set_text_color(0, 0, 0)
    pdf.cell(0, 10, "Prepared By: Anant Soni", align='C', new_x="LMARGIN", new_y="NEXT")
    pdf.set_font("helvetica", '', 12)
    pdf.cell(0, 10, "Date: April 2026", align='C', new_x="LMARGIN", new_y="NEXT")
    
    pdf.add_page()
    
    def add_section(title, content):
        pdf.set_font("helvetica", 'B', 16)
        pdf.set_fill_color(240, 248, 255)
        pdf.cell(0, 10, title, fill=True, new_x="LMARGIN", new_y="NEXT")
        pdf.ln(5)
        pdf.set_font("helvetica", '', 11)
        pdf.multi_cell(0, 7, content)
        pdf.ln(10)

    add_section("1. Introduction", 
    "UPI Leak Detector is a smart financial application designed to help users track their UPI and bank expenses effortlessly. "
    "In the modern digital economy, keeping track of numerous small UPI transactions is challenging. By leveraging Artificial Intelligence, "
    "the application automatically extracts transaction data from bank statements (PDFs), receipts (Images), and CSV files. "
    "It categorizes spending and identifies hidden 'money leaks' to help users maintain a healthy budget and improve their financial health.")

    add_section("2. Core Features", 
    "- AI-Powered Statement Parsing: Uses Google Gemini 2.5 Flash AI to intelligently extract and format debits from complex bank statements.\n"
    "- Universal Regex Fallback: A robust custom regex engine that works offline to extract dates, merchants, and amounts from any bank PDF.\n"
    "- Automated Categorization: Sorts transactions into predefined categories (Food, Shopping, Transport, etc.) using keyword heuristics and AI.\n"
    "- Receipt Scanner: Users can upload an image of a bill, and the AI extracts the merchant and amount instantly.\n"
    "- Spend Leak Detection: Automatically flags frequent small transactions at the same merchant and unusually large expenses.\n"
    "- AI Financial Advisor: A built-in, context-aware chatbot that provides personalized financial advice based on the user's recent spending history.\n"
    "- PDF Export: Users can generate customizable PDF reports of their monthly spending directly from the dashboard.\n"
    "- Bank-Grade Security: App handles encrypted PDFs safely without storing user passwords. Passwords for user accounts are hashed using bcrypt.")

    add_section("3. Technology Stack", 
    "- Backend Framework: Python, Flask\n"
    "- Database: PostgreSQL (Relational Database)\n"
    "- Frontend: HTML5, CSS3, JavaScript, Bootstrap 5 (Glassmorphism UI Design)\n"
    "- AI Engine: Google Gemini GenAI API\n"
    "- Data Extraction: pdfplumber, pandas, Python re (Regex)\n"
    "- Authentication: Flask-Login, Flask-Bcrypt\n"
    "- PDF Generation: FPDF")

    add_section("4. System Architecture",
    "The application follows a standard Client-Server architecture. The frontend, built with responsive Bootstrap 5 and a premium dark/light mode toggle, communicates with the Flask backend. "
    "The backend manages user sessions via Flask-Login. When a user uploads a statement, the backend routes the file to the parsing module. "
    "If an API key is available, the AI parser is used; otherwise, the system falls back to the robust Regex parser. "
    "Data is structured and safely stored in PostgreSQL. The dashboard securely queries this database to present dynamic analytics, charts, and financial alerts.")

    add_section("5. Implementation Details",
    "The core logic resides in 'app.py'. The upload module securely parses multiple file types. PDFs are decoded using 'pdfplumber', and the extracted text is processed. "
    "If the PDF is encrypted, the application uses the user-provided password strictly in-memory. The AI chatbot is implemented as a sticky widget that retains conversation context using the user's 50 most recent transactions. "
    "The Leak Detector runs an algorithmic scan during dashboard load, grouping transactions by merchant to calculate frequency and average ticket size to flag anomalies.")

    add_section("6. Future Enhancements",
    "- Multi-bank Aggregation: Integrating with the Account Aggregator Framework for real-time syncing.\n"
    "- Predictive Budgeting: Using machine learning on historical data to predict next month's expenses.\n"
    "- SMS Parsing: Creating a companion Android app to parse SMS for real-time transaction updates.\n"
    "- Cloud Deployment: Containerizing the application with Docker for seamless AWS/GCP deployment.")

    add_section("7. Conclusion",
    "UPI Leak Detector successfully bridges the gap between raw financial data and actionable insights. "
    "By automating the tedious process of expense tracking and utilizing advanced AI for categorization and personalized advice, "
    "the project provides a comprehensive, secure, and user-friendly personal finance management tool.")

    pdf.output("Project_Report_UPI_Leak_Detector.pdf")
    print("Report generated successfully as 'Project_Report_UPI_Leak_Detector.pdf'")

if __name__ == '__main__':
    generate_report()
