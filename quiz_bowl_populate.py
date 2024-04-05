import sqlite3


conn = sqlite3.connect('quiz_bowl.db')
cursor = conn.cursor()


# Sample questions and answers for each category
sample_questions_answers = {
    "Business Ethics": [
        ("What is the definition of business ethics?", "The application of ethical values to business activities", "The study of how to maximize profits", "The process of marketing products", "The study of corporate law"),
        ("What are the key principles of ethical decision making in business?", "Honesty, fairness, integrity", "Profit maximization at all costs", "Taking advantage of competitors", "Exploiting workers"),
        ("How does business ethics contribute to a company's reputation?", "It enhances trust and credibility with customers and stakeholders.", "It has no impact on reputation.", "It damages reputation and brand image.", "It is irrelevant to business success."),
        ("Give an example of an ethical dilemma in business.", "Environmental pollution vs. cost-saving measures", "Discrimination in hiring practices", "Offering discounts to preferred customers", "Complying with government regulations"),
        ("What is the importance of corporate social responsibility?", "It demonstrates commitment to society and sustainability.", "It helps increase profits.", "It is unnecessary in business.", "It hinders business growth."),
        ("How do ethical values influence leadership in business?", "Ethical leaders promote a culture of integrity and responsibility.", "Ethical behavior is not relevant to leadership.", "Ethical leaders are less effective in achieving business goals.", "Ethical values hinder business growth."),
        ("Discuss the role of whistleblowing in maintaining ethical standards in business.", "It helps expose wrongdoing and prevent harm.", "Whistleblowing is unethical and disloyal.", "Whistleblowing is illegal and punishable.", "Whistleblowers face no consequences for speaking up."),
        ("Explain the concept of stakeholder theory in business ethics.", "Businesses should consider the interests of all stakeholders, not just shareholders.", "The main goal of business is to maximize shareholder wealth.", "Companies should prioritize shareholder returns over all else.", "Stakeholders have no influence on business decisions."),
        ("How does globalization affect business ethics?", "Globalization can pose challenges in maintaining consistent ethical standards.", "Globalization has no impact on business ethics.", "Ethical standards are higher in globalized markets.", "Ethical standards are irrelevant in global business."),
        ("What are the ethical considerations in marketing and advertising?", "Truthfulness, transparency, and avoiding deceptive practices.", "Maximizing profits at any cost", "Manipulating consumer perceptions", "Ignoring consumer rights and privacy.")
    ],
    "Business Database Mgmt": [
        ("What is the purpose of a database management system (DBMS)?", "To manage and organize data efficiently", "To create colorful charts and graphs", "To browse the internet", "To send emails"),
        ("What is a primary key in a database?", "A unique identifier for each record in a table", "A key used for opening doors", "The first key created in a database", "The most important key in a database"),
        ("What is SQL?", "Structured Query Language used for managing relational databases", "A computer programming language for creating video games", "A type of database", "A software tool for designing databases"),
        ("What does CRUD stand for in database management?", "Create, Read, Update, Delete", "Crazy, Random, Unpredictable, Data", "Create, Record, Undo, Delete", "Computerized Record Update and Deletion"),
        ("What is normalization in database design?", "The process of organizing data to minimize redundancy", "The process of making data abnormal", "The process of encrypting data", "The process of backing up data"),
        ("What is an index in a database?", "A data structure used for quick lookup of data", "A book index", "A key used for encryption", "A type of database table"),
        ("What is the purpose of a foreign key in a database?", "To establish a relationship between two tables", "To prevent unauthorized access to data", "To generate random numbers", "To create a backup of the database"),
        ("What is a database schema?", "The structure that represents the logical view of the entire database", "A type of database query", "A database administrator", "A type of database software"),
        ("What is data integrity in a database?", "The accuracy, consistency, and reliability of data", "The speed of data access", "The size of the database", "The security of the database"),
        ("What is the purpose of a database transaction?", "To ensure data consistency and integrity", "To delete data from a database", "To encrypt data", "To transfer data between databases")
    ],
    "Business Communications": [
        ("What is effective communication?", "The exchange of information in a clear and concise manner", "Talking loudly", "Talking as much as possible", "Using jargon and technical terms"),
        ("What are the key components of effective communication?", "Sender, message, receiver, feedback, and noise", "Sender, message, receiver", "Message, receiver, feedback", "Sender, feedback, noise"),
        ("What are the benefits of effective communication in business?", "Improved productivity, better decision-making, and stronger relationships", "Decreased productivity, confusion, and conflicts", "Higher costs, slower growth, and lower profits", "None of the above"),
        ("What are the barriers to effective communication?", "Language barriers, cultural differences, physical barriers, and emotional barriers", "High productivity, clear goals, and effective leadership", "Good intentions, trust, and transparency", "Frequent communication, active listening, and empathy"),
        ("What is non-verbal communication?", "Communication without using words, such as body language, facial expressions, and gestures", "Communication using written words only", "Communication using only verbal words", "Communication using technical terms"),
        ("What is active listening?", "Fully concentrating on what is being said rather than just passively hearing the message", "Interrupting the speaker and providing immediate feedback", "Agreeing with everything the speaker says", "Thinking about what to say next while the speaker is talking"),
        ("Why is feedback important in communication?", "It helps clarify messages, correct misunderstandings, and improve relationships", "It slows down the communication process", "It is not necessary in communication", "It can create conflicts and misunderstandings"),
        ("What is the difference between formal and informal communication?", "Formal communication follows prescribed rules and procedures, while informal communication is spontaneous and casual", "Formal communication is more effective than informal communication", "Formal communication is always written, while informal communication is always verbal", "There is no difference between formal and informal communication"),
        ("What is the purpose of business writing?", "To communicate information clearly and professionally", "To entertain the reader", "To express personal opinions", "To confuse the reader with technical jargon"),
        ("What are the characteristics of effective business writing?", "Clarity, conciseness, professionalism, and correctness", "Complexity, verbosity, informality, and ambiguity", "Subjectivity, emotionality, redundancy, and errors", "Simplicity, brevity, informality, and creativity")
    ],
    "Principles of Macroeconomics": [
        ("What is macroeconomics?", "The study of the economy as a whole, including topics such as inflation, unemployment, and economic growth", "The study of individual consumers and firms", "The study of microorganisms in the economy", "The study of the economy's smallest components"),
        ("What are the key goals of macroeconomic policy?", "Full employment, stable prices, and economic growth", "High unemployment, high inflation, and economic contraction", "Low inflation, high government spending, and income inequality", "Low taxes, high government spending, and income inequality"),
        ("What is gross domestic product (GDP)?", "The total value of all goods and services produced within a country's borders in a specific time period", "The total value of all imports and exports of a country", "The total value of all government expenditures", "The total value of all goods and services consumed by households"),
        ("What is inflation?", "A general increase in the price level of goods and services over time", "A general decrease in the price level of goods and services over time", "A sudden increase in the price of a specific good or service", "A sudden decrease in the price of a specific good or service"),
        ("What is unemployment?", "The state of being without a job, but actively seeking employment", "The state of being employed, but not actively seeking employment", "The state of being employed, but underpaid", "The state of being without a job and not seeking employment"),
        ("What are fiscal policy tools?", "Government spending and taxation", "Monetary policy and interest rates", "Trade policy and tariffs", "Exchange rates and currency values"),
        ("What is monetary policy?", "The control of the money supply and interest rates by a central bank", "The control of government spending and taxation by the legislature", "The control of trade and tariffs by the executive branch", "The control of exchange rates by the treasury department"),
        ("What is the Federal Reserve System?", "The central banking system of the United States", "A system of state-run banks", "A system of private banks", "A system of international banks"),
        ("What is the business cycle?", "The recurring pattern of economic expansion and contraction", "The steady growth of the economy over time", "The random fluctuations in economic activity", "The government's control over the economy"),
        ("What are the causes of economic growth?", "Increases in productivity, technology, and investment", "Increases in government spending and consumption", "Increases in population and natural resources", "Increases in taxes and regulation")
    ],
    "Business Applications": [
        ("What are the key features of Microsoft Excel?", "Spreadsheets, charts, graphs, and data analysis tools", "Word processing, email, and internet browsing", "Programming, database management, and web development", "Video editing, graphic design, and animation"),
        ("What is the purpose of Microsoft Word?", "Word processing for creating documents such as letters, reports, and resumes", "Creating spreadsheets and analyzing data", "Creating presentations with slides and graphics", "Managing emails and contacts"),
        ("What is the function of Microsoft PowerPoint?", "Creating presentations with slides, graphics, and animations", "Word processing for creating documents", "Analyzing data and creating charts", "Creating databases and managing information"),
        ("What are the key features of Microsoft Outlook?", "Email, calendar, contacts, and task management", "Word processing and document creation", "Creating presentations with slides and graphics", "Analyzing data and creating charts"),
        ("What is the purpose of Microsoft Access?", "Database management for storing, querying, and analyzing data", "Word processing and document creation", "Creating presentations with slides and graphics", "Email, calendar, contacts, and task management"),
        ("What are the main functions of Microsoft PowerPoint?", "Creating slideshows, presentations, and visual aids", "Creating spreadsheets and analyzing data", "Word processing and document creation", "Database management and data analysis"),
        ("What is the function of Microsoft Publisher?", "Designing and publishing marketing materials such as brochures, flyers, and newsletters", "Word processing and document creation", "Creating presentations with slides and graphics", "Analyzing data and creating charts"),
        ("What are the key features of Microsoft OneNote?", "Note-taking, organization, and collaboration", "Word processing and document creation", "Creating spreadsheets and analyzing data", "Creating presentations with slides and graphics"),
        ("What is the purpose of Microsoft Teams?", "Collaboration and communication for teams and organizations", "Word processing and document creation", "Creating spreadsheets and analyzing data", "Creating presentations with slides and graphics"),
        ("What are the main functions of Microsoft SharePoint?", "Document management, collaboration, and content management", "Word processing and document creation", "Creating presentations with slides and graphics", "Creating databases and managing information")
    ]
}

# Connect to the database
conn = sqlite3.connect('quiz_bowl.db')
c = conn.cursor()

# Create the table if not exists
c.execute('''CREATE TABLE IF NOT EXISTS quiz (
               id INTEGER PRIMARY KEY AUTOINCREMENT,
               category TEXT,
               question TEXT,
               correct_answer TEXT,
               answer1 TEXT,
               answer2 TEXT,
               answer3 TEXT,
               answer4 TEXT
            )''')

# Insert questions and answers into the database for each category
for category, questions_answers in sample_questions_answers.items():
    print(f"Adding data for {category}...")
    for question_answer in questions_answers:
        c.execute('''INSERT INTO quiz (category, question, correct_answer, answer1, answer2, answer3, answer4)
                     VALUES (?, ?, ?, ?, ?, ?, ?)''', (category,) + question_answer)

# Commit changes and close connection
conn.commit()
conn.close()

# Print statement indicating data added
print("Data added for all categories")
