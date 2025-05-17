#Smart finance tracker
#### Video Demo:  <https://youtu.be/EYNaFB0aaoQ>
#### Description:
Smart Budget Tracker is a simple yet powerful command-line Python application designed to help users keep track of their personal finances. It allows users to record income and expenses, categorize their spending, and view a summary of their financial transactions—all stored in a CSV file for easy access and portability.

Features
Add Transactions: Easily log income or expenses by entering the amount, date, and category.

View Transactions: Display all recorded transactions sorted from oldest to newest.

View Summary: See an overview of total income, total expenses, and the net balance.

Data Persistence: All transaction data is saved to a CSV file (data.csv) for persistent storage.

Input Validation: The program validates user input for amounts and dates to ensure data accuracy.

User-Friendly Interface: Simple command-line interface that guides users through each action.

Why This Project?
Managing personal finances is crucial for everyone. Many people struggle to keep track of their spending and saving habits, often losing sight of where their money goes. This project aims to provide a straightforward tool that can be easily used and extended for more advanced features like budgeting, graphs, or even integration with bank APIs in the future.

For beginners in Python programming, this project consolidates important concepts such as:

Working with files (CSV)

Input validation and error handling

Functions and modular programming

Data sorting and formatting

Basic command-line interface design

How It Works
The main script (project.py) serves as the entry point and interface. When launched, it presents users with a menu offering four options:

Add a transaction

View all transactions

View summary

Exit

When adding a transaction, users first specify whether it’s an income or expense. Income transactions have a fixed category ("Income"), while expenses require a category input (e.g., food, rent, bills). Users then enter the amount and date (with an option to use today’s date by default). The program validates these inputs to prevent errors and ensures only positive amounts are recorded.

Transactions are saved in a CSV file with the following fields:

Type (income or expense)

Category (e.g., food, rent)

Amount

Date (YYYY-MM-DD format)

Viewing transactions reads the CSV file and displays all records sorted by date, making it easy to review financial history chronologically.

The summary option aggregates the data, calculating total income, total expenses, and the net balance, giving users an instant snapshot of their financial health.

Project Structure
graphql
Copy
Edit
project.py            # Main program file handling user interaction
storage.py            # Module responsible for saving and reading CSV data
data.csv              # CSV file storing transaction data (created at runtime)
How to Use
Clone or download this repository.

Ensure you have Python 3 installed on your system.

Run the main program:

bash
Copy
Edit
python project.py
Follow on-screen prompts to add transactions, view history, or check your summary.

Future Improvements
This project provides a strong foundation but can be enhanced in many ways, such as:

Adding categories for income

Supporting editing or deleting transactions

Exporting reports or visual charts

Adding password protection for privacy

Developing a GUI or web-based interface

Integrating with bank APIs for automatic transaction importing

Testing
The project includes simple tests to verify key functionalities like input validation and sorting transactions by date. You can run tests to ensure everything is working correctly before using the app extensively.

Conclusion
Smart Budget Tracker is a practical and educational project, perfect for anyone beginning their journey with Python programming and looking to build something useful. It demonstrates essential programming skills, such as file handling, user input processing, and data manipulation, wrapped in an easy-to-use command-line application.
