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

class Person {
    eat(){
        console.log("Eat");
    }

    sleep(){
        console.log("Sleep")
    }
}

class Engineer extends Person {
    work(){
        console.log("Solve problems, build something.")
    }
}

let yash = new Engineer();
console.log(yash.eat());