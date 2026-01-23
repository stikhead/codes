let loginUser = (user) => {
    return new Promise((resolve, reject) => {
        setTimeout(() => resolve(`Welcome ${user}`), 2000);
    });
}

const user = "Anirudh";
const runCode = async () => {
    try {
        console.log("Fetching...");
        const data = await loginUser(user);
        console.log(data);
    } catch (error) {
        console.log(error)
    }
};

runCode();