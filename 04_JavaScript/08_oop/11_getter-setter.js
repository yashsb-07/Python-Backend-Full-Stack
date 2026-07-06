class User {
    constructor(username, password){
        this.username = username;
        this.password = password;
    }

    get password () {
        return this._password.toUpperCase()
    }

    set password (value) {
        return this._password = value
    }
}

const user = new User("yash@gmail.com", "ascde")
console.log(user.password);
