/* Expense Tracker */

// let expenses = [];

// let count = Number(prompt("Enter number of expenses:"));

// if (isNaN(count) || count <= 0) {
//     console.log("Invalid number of expenses");
// } else {

//     for (let i = 1; i <= count; i++) {

//         let name = prompt(`Enter expense ${i} name:`);
//         let amount = Number(prompt(`Enter amount for ${name}:`));

//         if (isNaN(amount) || amount <= 0) {
//             console.log("Invalid amount, skipping...");
//             continue;
//         }

//         expenses.push(amount);
//     }

//     function calculateTotal(arr) {
//         let total = 0;
//         for (let i = 0; i < arr.length; i++) {
//             total += arr[i];
//         }
//         return total;
//     }

//     function findMax(arr) {
//         let max = arr[0];
//         for (let i = 0; i < arr.length; i++) {
//             if (arr[i] > max) {
//                 max = arr[i];
//             }
//         }
//         return max;
//     }

//     console.log("Expenses:", expenses);
//     console.log("Total Expense:", calculateTotal(expenses));
//     console.log("Highest Expense:", findMax(expenses));
// }

/* Quiz Game */

// let questions = ["What is 2 + 2?", "Which language runs in browser", "What is capital of India?"];

// let options = [["1. 3", "2. 4", "3. 5"], ["1. Python", "2. Java", "3. JavaScript"], ["1. Mumbai", "2. Delhi", "3. Pune"]];

// let answers = [2, 3, 2];

// let score = 0;

// function startQuiz(){
//     for (let i=0; i<questions.length; i++){
//         console.log(`\nQ${i + 1}: ${questions[i]}`);

//         for (let j=0; j<options[i].length; j++){
//             console.log(options[i][j]);
//         }

//         let useranswer = Number(prompt("Enter your answers (1-3): "));

//         if (useranswer < 1 || useranswer > 3 || isNaN(useranswer)){
//             console.log("Invalid input.");
//             continue;
//         }

//         if (useranswer === answers[i]){
//             console.log("Correct");
//             score++;
//         } else {
//             console.log("Wrong")
//         }
//     }

//     console.log("\nQuiz Finished");
//     console.log(`Your score ${score}/${questions.length}`);

// }

// startQuiz()

/* Contact Book */

let contacts = [];

function showMenu() {
    console.log("\n==== CONTACT BOOK ====");
    console.log("1. Add Contact");
    console.log("2. View Contacts");
    console.log("3. Search Contact");
    console.log("4. Update Contact");
    console.log("5. Delete Contact");
    console.log("6. Exit");
}

function addContact() {
    let name = prompt("Enter name:");
    let phone = prompt("Enter phone number:");

    if (name === "" || phone === "") {
        console.log("Invalid input!");
        return;
    }

    contacts.push(name + " - " + phone);
    console.log("Contact added!");
}

function viewContacts() {
    if (contacts.length === 0) {
        console.log("No contacts found.");
        return;
    }

    console.log("\nContact List:");
    for (let i = 0; i < contacts.length; i++) {
        console.log(i + 1 + ". " + contacts[i]);
    }
}

function searchContact() {
    let search = prompt("Enter name to search:");
    let found = false;

    for (let i = 0; i < contacts.length; i++) {
        if (contacts[i].includes(search)) {
            console.log("Found:", contacts[i]);
            found = true;
        }
    }

    if (!found) {
        console.log("Contact not found.");
    }
}

function updateContact() {
    let index = Number(prompt("Enter contact number to update:")) - 1;

    if (index < 0 || index >= contacts.length) {
        console.log("Invalid contact number.");
        return;
    }

    let newName = prompt("Enter new name:");
    let newPhone = prompt("Enter new phone:");

    contacts[index] = newName + " - " + newPhone;
    console.log("Contact updated!");
}

function deleteContact() {
    let index = Number(prompt("Enter contact number to delete:")) - 1;

    if (index < 0 || index >= contacts.length) {
        console.log("Invalid contact number.");
        return;
    }

    contacts.splice(index, 1);
    console.log("Contact deleted!");
}

while (true) {
    showMenu();

    let choice = Number(prompt("Enter your choice:"));

    switch (choice) {
        case 1:
            addContact();
            break;
        case 2:
            viewContacts();
            break;
        case 3:
            searchContact();
            break;
        case 4:
            updateContact();
            break;
        case 5:
            deleteContact();
            break;
        case 6:
            console.log("Exiting...");
            break;
        default:
            console.log("Invalid choice!");
    }

    if (choice === 6) break;
}