// let btn = document.querySelector("#btn");

// btn.onclick = (evt) => {
//     console.log("Button was clicked!");
// }

// let box = document.querySelector(".box");

// box.onmouseover = (evt ) => {
//     console.log("you are inside div.");
// }

/* EventListener */

// btn.addEventListener("click", () =>{
//     console.log("Button was clicked - handler 1");
// })

// btn.addEventListener("click", () =>{
//     console.log("Button was clicked - handler 2");
// })

// const handler3 = () => {
//     console.log("Button was clicked - handler 3");
// }

// btn.addEventListener("click", handler3);


// btn.addEventListener("click", () =>{
//     console.log("Button was clicked - handler 4");
// })

// btn.removeEventListener("click", handler3);

let modeBtn = document.querySelector("#mode");

let currentMode = "light-mode";

modeBtn.addEventListener("click", () => {
    if(currentMode === "light-mode") {
        currentMode = "dark-mode";
        document.querySelector("body").style.background = "black";
    } else {
        currentMode = "light-mode";
        document.querySelector("body").style.background = "white";
    }

    console.log(currentMode);
});