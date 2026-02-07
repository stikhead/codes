import express from 'express';
import env from 'dotenv';
const app = express();
env.config(); 

const port = process.env.port;
app.get('/', (req, res)=>{
    res.send("Server is ready")
})

app.listen(port, ()=>{
    console.log(`listening on ${port}`)
})