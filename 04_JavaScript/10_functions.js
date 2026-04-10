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