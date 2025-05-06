let subjects = [];

function addSubject() {
    const name = document.getElementById("subject-name").value.trim();
    const priority = parseInt(document.getElementById("subject-priority").value);
    const examDate = document.getElementById("subject-date").value;

    if (!name || !examDate || isNaN(priority)) {
        alert("Please fill out all fields correctly.");
        return;
    }

    subjects.push({
        name,
        priority,
        examDate: new Date(examDate)
    });

    // Update UI
    const list = document.getElementById("subject-list");
    const li = document.createElement("li");
    li.className = "list-group-item d-flex justify-content-between align-items-center";
    li.innerHTML = `
    <span><strong>${name}</strong> (Priority: ${priority}) – Exam: ${examDate}</span>
    <button class="btn btn-sm btn-outline-danger" onclick="removeSubject(${subjects.length - 1})">Remove</button>
  `;
    list.appendChild(li);

    // Clear inputs
    document.getElementById("subject-name").value = "";
    document.getElementById("subject-priority").value = "5";
    document.getElementById("subject-date").value = "";
}

function removeSubject(index) {
    subjects.splice(index, 1);
    document.getElementById("subject-list").innerHTML = "";
    subjects.forEach((_, i) => addSubjectFromMemory(i));
}

function addSubjectFromMemory(i) {
    const {
        name,
        priority,
        examDate
    } = subjects[i];
    const list = document.getElementById("subject-list");
    const li = document.createElement("li");
    li.className = "list-group-item d-flex justify-content-between align-items-center";
    li.innerHTML = `
    <span><strong>${name}</strong> (Priority: ${priority}) – Exam: ${examDate.toISOString().split("T")[0]}</span>
    <button class="btn btn-sm btn-outline-danger" onclick="removeSubject(${i})">Remove</button>
  `;
    list.appendChild(li);
}

function generatePlan() {
    const hours = parseFloat(document.getElementById("study-time").value);
    const output = document.getElementById("study-plan-output");
    output.innerHTML = "";

    if (isNaN(hours) || hours <= 0 || subjects.length === 0) {
        alert("Please enter valid study hours and at least one subject.");
        return;
    }

    // Sort subjects by exam date (earlier first)
    subjects.sort((a, b) => a.examDate - b.examDate);

    const totalPriority = subjects.reduce((sum, subj) => sum + subj.priority, 0);
    let planHTML = "";

    const today = new Date();
    today.setHours(0, 0, 0, 0);

    subjects.forEach(subj => {
        const examDate = new Date(subj.examDate);
        examDate.setHours(0, 0, 0, 0);

        const msPerDay = 1000 * 60 * 60 * 24;
        const daysBeforeExam = Math.max(Math.floor((examDate - today) / msPerDay), 1);

        const dailyHours = ((subj.priority / totalPriority) * hours).toFixed(2);

        const startDate = new Date(examDate);
        startDate.setDate(examDate.getDate() - daysBeforeExam + 1);

        planHTML += `
        <div class="mb-4">
          <h5>📘 ${subj.name} (Priority: ${subj.priority})</h5>
          <ul>
            <li>Study for <strong>${daysBeforeExam}</strong> day(s) before the exam</li>
            <li>From <strong>${startDate.toDateString()}</strong> to <strong>${examDate.toDateString()}</strong></li>
            <li>Study <strong>${dailyHours} hour(s)</strong> per day</li>
          </ul>
        </div>
      `;
    });

    output.innerHTML = planHTML;
}
