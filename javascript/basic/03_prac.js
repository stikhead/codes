const prompt = require('prompt-sync')({ sigint: true })
// Q1
const obj = {
    math: 98,
    phy: 93,
    dsa: 100
}
// for(let i; i<Object.keys(obj).length; i++){
//    console.log("the marks " + Object.keys(obj)[i] + " are " + obj[Object.keys(obj)[i]])
// }
for(let i in obj){ 
    console.log(i + " " + obj[i]);
}

// Q3
let cn = 4
let i
while(i!=cn){
    i = prompt("Enter a number: ")
    i = Number.parseInt(i);
}
console.log("Correct Number! ")

// Q4
let mean = (a, b, c, d) => {
    return (a+b+c+d)/4
}

console.log(mean(4, 5, 6, 7))