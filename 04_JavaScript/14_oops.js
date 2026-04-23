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

let fortuner = new ToyotaCar();
let lexus = new ToyotaCar();
