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

let questions = ["What is 2 + 2?", "Which language runs in browser", "What is capital of India?"];

let options = [["1. 3", "2. 4", "3. 5"], ["1. Python", "2. Java", "3. JavaScript"], ["1. Mumbai", "2. Delhi", "3. Pune"]];

let answers = [2, 3, 2];

let score = 0;

function startQuiz(){
    for (let i=0; i<questions.length; i++){
        console.log(`\nQ${i + 1}: ${questions[i]}`);

        for (let j=0; j<options[i].length; j++){
            console.log(options[i][j]);
        }

        let useranswer = Number(prompt("Enter your answers (1-3): "));

        if (useranswer < 1 || useranswer > 3 || isNaN(useranswer)){
            console.log("Invalid input.");
            continue;
        }

        if (useranswer === answers[i]){
            console.log("Correct");
            score++;
        } else {
            console.log("Wrong")
        }
    }

    console.log("\nQuiz Finished");
    console.log(`Your score ${score}/${questions.length}`);

}

startQuiz()