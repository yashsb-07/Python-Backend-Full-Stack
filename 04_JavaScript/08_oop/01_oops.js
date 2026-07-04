/* Class */

class ToyotaCar{
    constructor() {
        console.log("Creating a new object.");
    }

    start(){
        console.log("Car started..");
    }

    stop(){
        console.log("Car stopped..");
    }

    setBrand(brand){
        this.brand = brand;
    }
}

// let fortuner = new ToyotaCar();
// let lexus = new ToyotaCar();

/* Inheritance */

// class Person {
//     eat(){
//         console.log("Eat");
//     }

//     sleep(){
//         console.log("Sleep")
//     }
// }

// class Engineer extends Person {
//     work(){
//         console.log("Solve problems, build something.")
//     }
// }

// let yash = new Engineer();
// console.log(yash.eat());

/* API */

const URI = "https://cat-fact.herokuapp.com/facts";
const factPara = document.querySelector("#fact");
const btn = document.querySelector("#btn");

const getFacts = async () => {
    console.log("Getting data..");
    let responce = await fetch(URI);
    console.log(responce);
    let data = await responce.json();
    factPara.innerText = data[2].text;
};

// Using Promice Chain

// function getFacts() {
//     fetch(URI)
//         .then((responce) => {
//             return responce.json();
//         })
//         .then((data) => {
//             console.log(data);
//             factPara.innerText = data[2].text;
//         });
// }

btn.addEventListener("click", getFacts);