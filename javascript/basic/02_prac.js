const prompt = require('prompt-sync')({ sigint: true }); // added { sigint: true } to allow Ctl+C exit
// Q1
let age = prompt("Enter your age: ")
// age = Number.parseInt(age)
console.log((age>=10 && age<=20) ? "Minor" : "Adult")

// Q2
switch(age){
    case '15':
        console.log("Good")
        break
    case '16':
        console.log("good")
        break
    default:
        console.log("bad")
        break;
}