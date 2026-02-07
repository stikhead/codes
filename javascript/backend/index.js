require('dotenv').config()
const express = require('express')  // importing the library / framework 
const app = express()          
const port = process.env.port   // 65,535 ports in network used for TCP/IP communication  (\(2^{16}-1\))

app.get('/', (req, res) => {    
  res.send('Hello World!')     // send response to a request on / (home route) 
  console.log(res)
})

app.get('/twitter', (req, res)=>{
  res.send('enm')
})

app.get('/login', (req, res)=>{
  res.send('<h1>please login at here<h1>')
})

app.get('/youtube', (req, res)=>{
  res.send('<h2>youtube<h2>')
})

app.listen(port, () => {
  console.log(`Example app listening on port http://127.0.0.1:${port}`)
})
