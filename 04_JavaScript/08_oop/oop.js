const user = {
    username: "yash",
    loginCount: 7,
    signIn: true,

    getUserDetials: function() {
        console.log(`Username: ${this.username}`);
        
        console.log("Got user details from database");
    }
}

// console.log(user.username);
console.log(user.getUserDetials());