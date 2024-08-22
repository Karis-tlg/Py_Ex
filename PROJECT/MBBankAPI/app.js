const express = require('express');
const cors = require('cors');
const path = require('path');
const axios = require('axios');
const fs = require('fs');

const app = express();
    const config = JSON.parse(fs.readFileSync('config.json', 'utf8'));
    const port = config.port || 80;
    console.log(`Server is running on http://localhost:${port}`);
    app.use(cors());
    app.use(express.json());
    app.use(express.static(path.join(__dirname, 'public'))); 

    const mbbankRoutes = require('./routes/mbbank');
    app.use('/api/mbbank', mbbankRoutes);

    app.get('*', (req, res) => {
        res.redirect('/');
    });

    const errorHandler = (err, req, res, next) => {
        console.error('Error:', err.message);
        res.status(500).json({ error: 'Internal Server Error' });
    };
    app.use(errorHandler);
    app.listen(port, () => {
        console.log(`Server is running on http://localhost:${port}`);
        console.log(`javalorant discord: 127.0.0.3107`);
    });
