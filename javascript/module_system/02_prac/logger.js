const { time } = require('console');
const fs = require('fs').promises;

const loginUser = (user) => {
    return new Promise((resolve, reject) => {
        setTimeout(() => resolve(`Welcome, ${user.name}`), 2000)
    });
}
const user = {
    name: 'Anirudh',
    token: 'buswwiw*3h32nd'
}
let runCode = async () => {
    try {
        console.log("Processing...")
        const data = await loginUser(user);
        console.log(data);
        await fs.appendFile('./login.txt', `${user.name} logged in at ${new Date().toISOString()}`);
        console.log("Write finished!");
    } catch (err){
        console.log("Error: ", err)
        await fs.writeFile('./error.txt', (err));
    }
}

runCode();