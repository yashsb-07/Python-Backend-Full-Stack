// const email = ""
// const userEmail = []

// if (email){
//     console.log("USer got email");
    
// } else {
//     console.log("Don't have an email");
    
// }

// if (userEmail.length == 0){
//     console.log("Array is empty");
    
// }


// Nullish Coalescing Operator (??): 

let val1;
// val1 = 5 ?? 10
// val1 = null ?? 10
// val1 =  undefined ?? 15
val1 = null ?? 10 ?? 20

console.log(val1);

// truthy values 
// "0", 'flase', " ", [], {}, function(){}

// flasy values
// flase, 0, -0, BigInt 0n, "", null, undefined, NaN