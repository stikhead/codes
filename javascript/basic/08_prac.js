const prompt = require('prompt-sync')({ sigint: true })

// Q1
// let arr = [8, 3, 23, 34, 2];
// let userInput = prompt("Enter no of elements to be inserted in the array: ")
// userInput = Number.parseInt(userInput);
// for(let i=0; i<userInput; i++){
//     let arrayInput = prompt(`Enter ${i}th element: `);
//     arr.push(Number.parseInt(arrayInput));
// }
// console.log(arr);

// Q2
let arr = [8, 3, 23, 34, 2];
while(true){
    let userInput = prompt("Guess the correct element to stop adding elements in the array: ")
    userInput = Number.parseInt(userInput);
    arr.push(userInput);
    if(userInput==0){
        break;
    }
}
console.log(arr);


// Q3

let filteredArray = arr.filter((value)=>{
    return value%10==0
})
console.log(filteredArray)

let sqrArray = filteredArray.map((value)=>{
    return value*value
})
console.log(sqrArray);


// Q4
let naturalNumbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15];
let inputFactorial = prompt("Enter the number to calculatw factorial: ");
let fact = naturalNumbers.reduce((int1, int2)=>{
    return int1*int2;
})
console.log(fact);