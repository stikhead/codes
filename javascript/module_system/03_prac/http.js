const http = require('http');

const server = http.createServer((req, res) => {
    console.log("Someone visited the server!");
    res.writeHead(200, {'Content-Type': 'text/plain'});
    res.end("Hello from your first backend")
});

server.listen(3000, () => {
    console.log(`server is running on port 3000...`);
})