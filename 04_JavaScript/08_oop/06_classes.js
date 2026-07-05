// class User {
//     constructor(username, email, password){
//         this.username = username;
//         this.email = email;
//         this.password = password
//     }

//     encryptPassword(){
//         return `${this.password}abc`
//     }

//     changeUsername(){
//         return `${this.username.toUpperCase()}`
//     }
// }

// const user = new User("Yash", "yash@gmail.com", "12345")

// console.log(user.encryptPassword());
// console.log(user.changeUsername());

// Behind the scene or without using classes

function User(username, email, password){
    this.username = username;
    this.email = email;
    this.password = password
}

User.prototype.encryptPassword = function(){
    return `${this.password}abc`
}

User.prototype.changeUsername = function(){
    return `${this.username.toUpperCase()}`
}

const user = new User("Yash Bansode", "yash@gmail.com", "09870")

console.log(user.encryptPassword());
console.log(user.changeUsername());
