// Singleton
// Object.create

// object literals

// const jsUsers = {
//     name: "Yash",
//     age: 22, 
//     location: "Pune",
//     email: "yash@gmail.com",
//     isLoggedIn: false
// }

// console.log(jsUsers.email);
// console.log(jsUsers["email"]);
// console.log(jsUsers["name"]);

// jsUsers.email = "yash@google.com"
// console.log(jsUsers["email"]);

const tinderUser = {}

tinderUser.id = "abc12"
tinderUser.name = "Yash"
tinderUser.isLoggedIn = false

// console.log(tinderUser);

const regularUser = {
    email: "someone@gmail.com",
    fullName: {
        userFullName: {
            firstName: "Yash",
            lastName: "Bansode"
        }
    }
}

// console.log(regularUser.fullName.userFullName.firstName);

const obj1 = {1: "A", 2: "B"}
const obj2 = {3: "C", 4: "D"}

// const obj3 = {obj1, obj2}
// const obj3 = Object.assign({}, obj1, obj2)
const obj3 = {...obj1, ...obj2}
console.log(obj3);





// const students = {
//     name: "Yash",
//     age: 22,
//     marks: 95
// }

// console.log(students.name)
// console.log(students.age)

// students.name = "Sakshi"

/* Nested Objects */

// const classInfo = {
//     yash: {
//         grade: "A",
//         city: "Pune"
//     },

//     sakshi: {
//         grade: "A",
//         city: "Nashik"
//     }
// }

// classInfo.sakshi.city = "Pune"

/* Array of objects */

// const classInfo = [
//     {
//         name: "Yash",
//         age: 22,
//         city: "Pune"
//     },

//     {
//         name: "Sakshi",
//         age: 21,
//         city: "Pangari"
//     },

//     {
//         name: "Shwetali",
//         age: 25,
//         city: "Pune"
//     }
// ]

// console.log(classInfo[0])
// console.log(classInfo[1])

/* Generate random num from 1 to 10 */

// let random = Math.floor(Math.random() * 10) + 1;
// console.log(random)

/* Guessing Game */
// const max = prompt("Enter the max num: ");
// const random = Math.floor(Math.random() * max) + 1;
// let guess = prompt("Enter your guess num: ");

// while (true){
//     if(guess == "quit"){
//         console.log("User quit..!")
//         break;
//     } 

//     if(guess == random){
//         console.log("Congratulations your guess is correct!");
//         break;
//     } else if (guess < random){
//         guess = prompt("Hint: your guess was too small!");
//     } else {
//         guess = prompt("Hint: your guess was too large!")
//     }
// }