const asyncHandler = require('express-async-handler');
const { Parser } = require('json2csv');
const { PassThrough } = require('stream');

const balanceHandler = asyncHandler(async (req, res) => {
    const { download, type } = req.method === 'GET' ? req.query : req.body;

    try {
        const balance = await req.mb.getBalance();
        if (download === 'true') {
            let contentType = 'application/json';
            let contentDisposition = 'attachment; filename=balance.json';
            let responseStream = PassThrough();

            if (type === 'csv') {
                const parser = new Parser();
                responseStream = PassThrough();
                responseStream.end(parser.parse(balance.balances));
                contentType = 'text/csv';
                contentDisposition = 'attachment; filename=balance.csv';
            } else {
                responseStream.end(JSON.stringify(balance, null, 2));
            }

            res.setHeader('Content-disposition', contentDisposition);
            res.setHeader('Content-type', contentType);
            responseStream.pipe(res);
        } else {
            res.json({ balance });
        }
    } catch (error) {
        console.error('Error fetching balance:', error);
        res.status(400).json({ error: error.message });
    }
});

module.exports = { balanceHandler };
