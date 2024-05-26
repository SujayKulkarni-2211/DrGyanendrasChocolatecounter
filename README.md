# DrGyanendrasChocolatecounter
Dr. Gyanendra's Chocolate Counter Application
Purpose
Dr. Gyanendra Tiwari, a Data Structures and Algorithms professor, has a unique policy of awarding chocolates to students who successfully answer his special questions, known as "chocolate questions". The goal of the Chocolate Counter application is to digitize and streamline the process of tracking which students have answered these questions and how many chocolates each student has accumulated. This application replaces the traditional notebook and digital notes method, offering a more efficient and automated way to manage this rewarding system.

Key Features
Database Initialization:

Initializes an SQLite database (chocolate_counter.db) and sets up the leaderboard table to store student names and their corresponding chocolate counts.
Search and Add:

Allows the user to search for a student's name. If the student is found in the database, their chocolate count is updated. If the student is not found, a new entry is created for the student with the specified number of chocolates.
Add Chocolates:

Updates the chocolate count for an existing student by adding the specified number of chocolates.
Display Leaderboard:

Opens a new window displaying the leaderboard, sorted in descending order based on the number of chocolates. This provides a clear view of the top performers in the class.
Search and Return Chocolates:

Enables the user to search for a student's name and view the number of chocolates they have accumulated.
Export to CSV:

Exports the leaderboard data to a CSV file (leaderboard.csv). This feature is useful for sharing and analyzing the data outside the application.
User Interface
The user interface is designed to be simple and intuitive, allowing easy interaction for both the professor and the students.

Title: The application title, "Dr. Gyanendra's Chocolate Counter", is prominently displayed at the top.
Image: An image of Dr. Gyanendra Tiwari is displayed to add a personal touch to the application.
Slogan: A slogan "📚 Encouraging Learning Every Day 🍫" is displayed to emphasize the purpose of the rewarding system.
Search Functionality: Provides input fields and a button for searching a student's name to check their chocolate count.
Add Chocolates: Allows input of the number of chocolates and a button to update the count for a student.
Show Leaderboard Button: A button that opens a new window displaying the leaderboard.
Export to CSV Button: A button that exports the leaderboard data to a CSV file for external use.
