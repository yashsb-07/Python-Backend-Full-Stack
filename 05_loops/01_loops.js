/* For Loop */

/* Print 1 to 20 */

// for (let i = 2; i<= 20; i=i+2){
//     console.log(i)
// }

let arr = ['krrish', 'hrithik', 'priyanka', 'rohit']

for (let i = 0; i < arr.length; i++){
    
    console.log(arr[i]);

}

/* While Loops */

// i = 0

// while (i<=10){
//     console.log(i)
//     i = i+2;
// }

/* Guessing Game */

// let fav_movie = "knph";

// let guess = prompt("Enter my guess movie: ");

// while ((guess != fav_movie) && (guess != "quit")){
//     guess = prompt("Wrong guess. Please try again!")
// }

// if (guess == fav_movie){
//     console.log("congratulations..!")
// } else {
//     console.log("You quit. ")
// }

/* Break Keyword */

// i = 1

// while (i<=10){
    // if(i == 3){
    //     break
    // }

//     console.log(i)
// }

// let heros = [["spiderman", "ironman", "captain america"], ["wonder women", "flash", "superman"]]

// for (let i = 0; i < heros.length; i++){
//     console.log(i, heros[i], heros[i].length);
//     for(let j = 0; j<heros[i].length; j++){
//         console.log(`j=${j}, ${heros[i][j]}`);
//     }
// }

/* Todo App */

// let todo = [];

// let req = prompt("Enter your request: ")

// while(true){
//     if (req == "quit"){
//         console.log("Quitting app..");
//         break;
//     }

//     if (req == "add"){
//         let task = prompt("Please enter your task to add: ");
//         todo.push(task);
//         console.log("Task added.");
//     } else if (req == "list"){
//         console.log("----------")
//         for (let i = 0; i<todo.length; i++){
//             console.log(i, todo[i]);
//         }
//     } else if (req == "delete"){
//         let idx = prompt("Please enter task to delete: ");
//         todo.splice(idx, 1);
//         console.log("Task deleted.. ")
//     } else {
//         console.log("Wrond request.")
//     }
// }



