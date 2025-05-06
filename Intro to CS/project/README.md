# Smart Study Planner
#### Video Demo: <[URL HERE](https://youtu.be/CGXslGQQBDY)>
#### Description:

**Smart Study Planner** is a responsive web application designed to help students manage their time and exam preparation more effectively. The goal is to eliminate the stress of manual planning and provide students with a smart, personalized study schedule based on their individual needs and constraints.

The core functionality of the app revolves around three user inputs: the subjects they are studying, the priority of each subject, and the date of the subject’s exam. In addition, users specify how many hours per day they are available to study. With this information, the app generates a study plan that fairly and intelligently allocates study hours across each subject based on its importance and how close its exam date is. This tool can be particularly helpful during exam season when students have multiple exams approaching and need to maximize their time and focus.

---

## Functionality:

Upon loading the webpage, users are presented with a clean and minimalistic interface styled using Bootstrap. Students begin by entering each subject they need to study for. For each subject, they must specify:
- The **name** of the subject (e.g., "Math")
- The **priority**, from 1 (lowest) to 5 (highest), representing how difficult or important the subject is to them
- The **exam date**, which the system uses to calculate how soon to begin preparing

Once subjects are added, users input the number of hours they can dedicate to studying each day. With a click of the "Generate Study Plan" button, the system outputs a personalized schedule for each subject that includes:
- How many days before the exam they should begin studying
- The date range for studying
- How many hours per day should be dedicated to that subject

The plan is displayed in a structured, readable format, with each subject in its own section for clarity. Subjects are automatically sorted so that those with the nearest exam dates are listed first.

---

## File Breakdown:

### `index.html`
This is the main structure of the web application. It includes:
- The form for inputting subjects and their data
- A field for entering daily study hours
- Buttons for submitting and generating the plan
- A div for dynamically showing the final study plan

Bootstrap is linked via CDN in the `<head>` to provide a consistent and responsive design across devices. Semantic HTML elements are used to improve accessibility and structure.

### `style.css`
The stylesheet defines custom styles to complement Bootstrap and improve readability. It ensures:
- Spacing between subject blocks
- Clean typography for headers and lists
- Margins and paddings for better layout
- Visual grouping of form elements and output blocks

The design philosophy was minimal yet modern — to reduce distraction and maintain focus on content.

### `script.js`
This file contains all the logic of the app. It:
- Manages subject entries in an array
- Validates inputs before adding a subject or generating the plan
- Sorts subjects based on exam dates
- Calculates each subject's proportional share of study time, factoring in both priority and urgency (based on how soon the exam is)
- Outputs a detailed, readable plan to the HTML

All logic runs client-side using plain JavaScript — no external libraries were needed beyond Bootstrap for styling.

---

## Design Decisions:

One of the most important design decisions was how to fairly allocate study time among different subjects. Originally, I considered splitting hours evenly among all subjects. However, that approach didn’t account for priority or exam urgency, which are both essential in real-life situations. Instead, I developed a simple algorithm that:
- Calculates the total "weight" of all subjects based on their priority
- Allocates a share of the total daily study hours to each subject based on its weight
- Adjusts the study window so that subjects are studied in the days leading up to their actual exam date

This logic was implemented in JavaScript, which allowed all calculations to happen instantly in the browser without needing a server or database.

Another decision was to keep the project purely front-end. While using Python with Flask and SQL would have allowed data persistence and user accounts, I chose to limit the tech stack to HTML/CSS/JavaScript to focus on mastering core web technologies and keep the project lightweight and easily deployable.

I also debated whether to use visualizations such as charts or calendars, but decided that text-based output would be clearer and more accessible for now. However, this would be a good future enhancement.

---

## Future Improvements:

If I were to continue developing this project, I would consider:
- Using `localStorage` to save subjects so the user doesn’t lose them on refresh
- Adding the ability to edit or delete subjects
- Allowing users to export their plan as a downloadable PDF or calendar event
- Including subject-specific notes or subtopics
- Creating a mobile-first version with enhanced UI for small screens
- Integrating AI to provide personalized study tips or time suggestions

---

## Conclusion:

This project was built as my final project for CS50, and it represents the skills I’ve gained in web development, user interface design, and algorithmic thinking. I’m proud of how it turned out — it’s functional, user-focused, and addresses a real-world problem faced by students. I hope others find it helpful and that it can continue to grow in functionality and usefulness in the future.
