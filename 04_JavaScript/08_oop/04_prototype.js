let myName = "Yash      ";
let myChannel = "Gaming     ";

String.prototype.trueLength = function(){
    console.log(`${this}`);
    console.log(`True length is: ${this.trim().length}`);
}

myChannel.trueLength()


let heroes = ["thor", "ironman"]

let heroPower = {
    thor: "hammer",
    ironman: "sling",

    getIronManPower: function(){
        console.log(`IronMan Power is ${this.ironman }`);
    }
}

Object.prototype.yash = function(){
    console.log(`Yash is present in all object`);
}

Array.prototype.heyYash = function(){
    console.log(`Yash says hello`);
}
// heroPower.yash()
// heroes.yash()
// heroes.heyYash()
// heroPower.heyYash()