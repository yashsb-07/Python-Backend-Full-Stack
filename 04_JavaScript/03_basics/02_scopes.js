let a = 100

if (true) {
    let a = 5
    const b = 10
    var c = 15

    // console.log("Inner: ", a);
    
}

// console.log(a);
// console.log(b);
// console.log(c);

function one(){
    const userName = "Yash"

    function two(){
        const website = "YouTube"
        console.log(userName);
    }

    // console.log(website);

    two()
}

// one()

function addone(num){
    return num + 1
}

console.log(addone(5));

const addtwo = function(num1){
    return num1 + 5 
}

console.log(addtwo(5));
