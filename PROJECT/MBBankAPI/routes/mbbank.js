const express = require('express');
const router = express.Router();
const authenticate = require('../auth/auth');
const { balanceHandler } = require('../manager/balance');
const { transactionsHandler } = require('../manager/transactions');

router.route('/getbalance')
    .get(authenticate, balanceHandler)
    .post(authenticate, balanceHandler);

router.route('/getTransactionsHistory')
    .get(authenticate, transactionsHandler)
    .post(authenticate, transactionsHandler);

module.exports = router;
