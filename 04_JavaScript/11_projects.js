let expenses = [];

let count = Number(prompt("Enter number of expenses:"));

if (isNaN(count) || count <= 0) {
    console.log("Invalid number of expenses");
} else {

    for (let i = 1; i <= count; i++) {

        let name = prompt(`Enter expense ${i} name:`);
        let amount = Number(prompt(`Enter amount for ${name}:`));

        if (isNaN(amount) || amount <= 0) {
            console.log("Invalid amount, skipping...");
            continue;
        }

        expenses.push(amount);
    }

    function calculateTotal(arr) {
        let total = 0;
        for (let i = 0; i < arr.length; i++) {
            total += arr[i];
        }
        return total;
    }

    function findMax(arr) {
        let max = arr[0];
        for (let i = 0; i < arr.length; i++) {
            if (arr[i] > max) {
                max = arr[i];
            }
        }
        return max;
    }

    console.log("Expenses:", expenses);
    console.log("Total Expense:", calculateTotal(expenses));
    console.log("Highest Expense:", findMax(expenses));
}