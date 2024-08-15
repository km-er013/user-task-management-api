// script.js

document.getElementById('userForm').addEventListener('submit', async function(e) {
    e.preventDefault();
    const name = document.getElementById('userName').value;
    const email = document.getElementById('userEmail').value;

    const response = await fetch('http://localhost:5000/users', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ name, email })
    });

    if (response.ok) {
        alert('User added successfully');
        loadUsers();
    } else {
        alert('Failed to add user');
    }
});

document.getElementById('taskForm').addEventListener('submit', async function(e) {
    e.preventDefault();
    const title = document.getElementById('taskTitle').value;
    const description = document.getElementById('taskDescription').value;
    const user_id = document.getElementById('taskUser').value;

    const response = await fetch('http://localhost:5000/tasks', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ title, description, user_id })
    });

    if (response.ok) {
        alert('Task added successfully');
        loadTasks();
    } else {
        alert('Failed to add task');
    }
});

async function loadUsers() {
    const response = await fetch('http://localhost:5000/users');
    const users = await response.json();
    const usersDiv = document.getElementById('users');
    usersDiv.innerHTML = '';

    users.forEach(user => {
        usersDiv.innerHTML += `<div class="user">
            <strong>ID:</strong> ${user.id} <br>
            <strong>Name:</strong> ${user.name} <br>
            <strong>Email:</strong> ${user.email}
        </div>`;
    });
}

async function loadTasks() {
    const response = await fetch('http://localhost:5000/tasks');
    const tasks = await response.json();
    const tasksDiv = document.getElementById('tasks');
    tasksDiv.innerHTML = '';

    tasks.forEach(task => {
        tasksDiv.innerHTML += `<div class="task">
            <strong>ID:</strong> ${task.id} <br>
            <strong>Title:</strong> ${task.title} <br>
            <strong>Description:</strong> ${task.description} <br>
            <strong>Completed:</strong> ${task.completed} <br>
            <strong>User ID:</strong> ${task.user_id}
        </div>`;
    });
}

// Load initial data
loadUsers();
loadTasks();
