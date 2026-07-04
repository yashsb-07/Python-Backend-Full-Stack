// const user = {
//     username: "yash",
//     loginCount: 7,
//     signIn: true,

//     getUserDetials: function() {
//         console.log(`Username: ${this.username}`);
        
//         console.log("Got user details from database");
//     }
// }

// console.log(user.username);
// console.log(user.getUserDetials());

function User(username, loginCount, signIn){
    this.username = username;
    this.loginCount = loginCount;
    this.signIn = signIn

    return this
}

const userOne = new User("Yash", 7, true)
const userTwo = new User("Sakshi", 12, false)
console.log(userOne);
console.log(userTwo);
