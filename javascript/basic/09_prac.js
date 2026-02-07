let p1 = new Promise((resolve, reject)=>{
    setTimeout(()=>{
        reject("rejected")
    }, 3000)
})
try {
    let valueOfPromise = await p1;
    console.log(valueOfPromise)
}
catch (error){
    console.log(error);
}