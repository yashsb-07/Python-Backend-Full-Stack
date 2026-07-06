class User {
    constructor(username){
        this.username = username
    }

    logMe(){
        console.log(`Username: ${this.username}`);
    }

    createID(){
        return `123`
    }
}

const user = new User("Yash")
console.log(user.createID());