/* Functions */

function printHello() {
    console.log("Hello Yash! How are you?")
};

function rollDice() {
    let dice = Math.floor(Math.random() * 6 ) + 1;
    console.log(dice)
}

rollDice()
rollDice()
rollDice()
rollDice()
rollDice()
rollDice()

/* Function Arguments */

function printInfo(name, age) {
    console.log(`${name}'s age is ${age}`)
}

printInfo("Yash", 22)

function calcSum(a, b) {
    console.log(`${a}+${b} = `, a+b)
}

calcSum(5,10)

function calcAvg(a,b,c) {
    console.log((a+b+c)/3)
}

calcAvg(3,3,3)


/* Get Sum of n numbers */

function getSum(n){
    let sum = 0;

    for(let i = 1; i <= n; i++){
        sum += i;
    }

    return sum
}

console.log(getSum(1000))

/* Concat string */

let str = ["Hello", "Yash", "!"]

function concatStr(str){
    let result = "";

    for(let i = 0; i < str.length; i++){
        result += str[i];
    }

    return result;
}

console.log(concatStr(str))

/* Higher Order Function */

function multipleGreet(func, count){
    for(let i=1; i<=count; i++){
        func();
    }
}

let greet = function(){
    console.log("Hello Yash!")
}

console.log(multipleGreet(greet, 5))


/* Arrow Function */

let arrowSum = (a,b) =>{
    console.log(a+b);
}

arrowSum(5,5)

let arrowMul = (a,b) => {
    console.log(a*b);
}

arrowMul(5,4)

/* Foreach method */

let arr = ["yash", "sakshi"]

arr.forEach(function printVal(val){
    console.log(val);
})

/* This Keyword */

let students = {
    name: "Yash",
    age: 22,
    eng: 95,
    phy: 95,
    chem: 65,
    getAvg(){
        let avg = (this.eng + this.phy + this.chem) / 3
        console.log(avg)
    }
}

console.log(students.getAvg())