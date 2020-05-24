const express = require('express');

const app = express();

app.post('/', (req, res) => {
        res.send(`Goods received from factory, sending out for delivery!`);
});

app.listen(8081, () => {
    console.log('Listening on port 8081');
});