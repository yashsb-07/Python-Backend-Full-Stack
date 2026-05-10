/* Immediately Invoked Function Expression (IIEF)
    This functions are used to avoid global polluition
*/

(function database() {
    console.log(`Database Connected Successfully!`);
})();

( (name) => {
    console.log(`${name}, Database two Connected Successfully!`);
})('Yash');