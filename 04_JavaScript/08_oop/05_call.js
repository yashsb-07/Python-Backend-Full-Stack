function Setusername(username){
    this.username = username
    console.log("called");
}

function createUser(username, email, pass){
    Setusername.call(this, username)

    this.email = email
    this.pass = pass
}

const yash = new createUser("Yash", "yash@gmail.com", "123")
console.log(yash);
