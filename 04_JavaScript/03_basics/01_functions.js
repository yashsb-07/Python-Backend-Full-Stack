/* Functions */

// function printHello() {
//     console.log("Hello Yash! How are you?")
// };

// function rollDice() {
//     let dice = Math.floor(Math.random() * 6 ) + 1;
//     console.log(dice)
// }

// rollDice()
// rollDice()
// rollDice()
// rollDice()
// rollDice()
// rollDice()

/* Function Arguments */

// function printInfo(name, age) {
//     console.log(`${name}'s age is ${age}`)
// }

// printInfo("Yash", 22)

// function calcSum(a, b) {
//     console.log(`${a}+${b} = `, a+b)
// }

// calcSum(5,10)

// function calcAvg(a,b,c) {
//     console.log((a+b+c)/3)
// }

// calcAvg(3,3,3)

function calculateCartPrice(val, val1, ...num){
    return num
}

// console.log(calculateCartPrice(200, 400, 600, 800));

const user = {
    userName: "Yash",
    price: 199
}

function getUsername(find){
    console.log(`Username is ${find.userName} and price is ${find.price}`);   
}

// getUsername(user)
// getUsername({
//     userName: "yashsb07",
//     price: 299
// })


const myArray = [200, 400, 600, 800]

function returnSecondVal(getArray){
    return getArray[1]
}

// console.log(returnSecondVal(myArray));

/* Get Sum of n numbers */

// function getSum(n){
//     let sum = 0;

//     for(let i = 1; i <= n; i++){
//         sum += i;
//     }

//     return sum
// }

// console.log(getSum(1000))

/* Concat string */

// let str = ["Hello", "Yash", "!"]

// function concatStr(str){
//     let result = "";

//     for(let i = 0; i < str.length; i++){
//         result += str[i];
//     }

//     return result;
// }

// console.log(concatStr(str))

/* Higher Order Function */

// function multipleGreet(func, count){
//     for(let i=1; i<=count; i++){
//         func();
//     }
// }

// let greet = function(){
//     console.log("Hello Yash!")
// }

// console.log(multipleGreet(greet, 5))

/* SetTimeout Function */

// console.log("Hello yash..")

// setTimeout(() => {
//     console.log("Apna College");
    
// }, 2000);

// console.log("Welcome to")

/* setInterval Function */

// let id = setInterval(() => {
//     console.log("Hello, Yash Bansode!");
// }, 1000)

// clearInterval(id)

/* Question */

// let id2 = setInterval(() => {
//     console.log("Hello World!")
// }, 1000);

// setTimeout(() => {
//     clearInterval(id2)
// }, 5000);