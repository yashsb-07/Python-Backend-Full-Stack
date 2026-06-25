// For of

const arr = [1,2,3,4,5,6,7]

for (const num of arr){
    // console.log(num);
}

const greetings = "Hello Yash How are you"

for (let greet of greetings){
    // console.log(greet);
}

const map = new Map()
map.set('IN', 'India')
map.set('USA', 'Unnited States of America')
map.set('FR', 'France')
map.set('RU', 'Russia')
map.set('IN', 'India')

// console.log(map);

for (const [key, value] of map){
    // console.log(key, ':-', value );
    
}

const myObject = {
    js: "JavaScript",
    cpp: "C++",
    rb: "Ruby",
    py: "Python" 
}

// For in

for (const key in myObject){
    // console.log(myObject[key]);
}

// ForEach

const coding = ["java", "python", "javascript", "c", "c++"]

coding.forEach (function (val) {
    // console.log(val);  
})

const myCoding = [
    {
        languageName: "JavaScript",
        LanguageFile: "js"
    },

    {
        languageName: "Python",
        LanguageFile: "py"
    },

    {
        languageName: "CPP",
        LanguageFile: "c++"
    }
]

myCoding.forEach( (item) => {
    
    console.log(item.languageName);    

} )