

// Q1
console.log("har\"".length) // 4

// Q2
let n = "Anirudh"
console.log(n.startsWith('A'))
console.log(n.includes("h"));


//Q3
let m = "thiS is A STRING"
console.log(m.toLowerCase() +'\n'+ m)
m = m.toLowerCase()
console.log(m)

//Q4
let s = "Please give Rs 1000"
let amount = s.slice("Please give Rs ".length)
console.log(amount)

s[3] = 'q' // not possible bc strings are immutable
console.log(s) 