const asyncHandler = require('express-async-handler');
const { Parser } = require('json2csv');
const { PassThrough } = require('stream');

const transactionsHandler = asyncHandler(async (req, res) => {
    const { accountNumber, fromDate, toDate, download, type } = req.method === 'GET' ? req.query : req.body;

    if (!accountNumber || !fromDate || !toDate) {
        return res.status(400).json({ error: 'Missing required parameters' });
    }

    try {
        const transactionsHistory = await req.mb.getTransactionsHistory({ accountNumber, fromDate, toDate });

        if (download === 'true') {
            let contentType = 'application/json';
            let contentDisposition = 'attachment; filename=transactions_history.json';
            let responseStream = PassThrough();

            if (type === 'csv') {
                const parser = new Parser();
                responseStream = PassThrough();
                responseStream.end(parser.parse(transactionsHistory));
                contentType = 'text/csv';
                contentDisposition = 'attachment; filename=transactions_history.csv';
            } else {
                responseStream.end(JSON.stringify(transactionsHistory, null, 2));
            }

            res.setHeader('Content-disposition', contentDisposition);
            res.setHeader('Content-type', contentType);
            responseStream.pipe(res);
        } else {
            res.status(200).json(transactionsHistory);
        }
    } catch (error) {
        console.error('Error fetching transactions history:', error);
        res.status(500).json({ error: error.message });
    }
});

module.exports = { transactionsHandler };
