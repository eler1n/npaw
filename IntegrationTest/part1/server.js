const express = require('express');
const https = require('https');
const fs = require('fs');
const app = express();
const port = 3000;

// SSL certificate configuration
const options = {
    key: fs.readFileSync('certs/key.pem'),
    cert: fs.readFileSync('certs/cert.pem')
};

// Enable CORS for all routes
app.use((req, res, next) => {
    res.header('Access-Control-Allow-Origin', '*');
    res.header('Access-Control-Allow-Headers', 'Origin, X-Requested-With, Content-Type, Accept');
    next();
});

// Serve static files from the current directory
app.use(express.static('./', {
    setHeaders: (res, path) => {
        if (path.endsWith('.js')) {
            res.setHeader('Content-Type', 'application/javascript');
        }
    }
}));

// Create HTTPS server
https.createServer(options, app).listen(port, () => {
    console.log(`HTTPS Server running at https://localhost:${port}`);
});