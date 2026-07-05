class User{
    constructor(username){
        this.username = username
    }

    logMe(){
        console.log(`Username is ${this.username}`);
    }
}

class Teacher extends User{
    constructor(username, email){
        super(username)
        this.email;
    }

    addCource(){
        console.log(`The new cource is added by ${this.username}`);
    }
}

const user = new Teacher("Yash", "yash@gmail.com")

user.addCource()
user.logMe()