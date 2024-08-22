const { MB } = require('.././MBAPI/dist/index');

const auth = async (req, res, next) => {
    const { username, password } = req.body;
    const { username: queryUsername, password: queryPassword } = req.query;

    if (!username && !password) {
        if (!queryUsername || !queryPassword) {
            return res.status(401).json({ error: 'Missing username or password' });
        }
        req.username = queryUsername;
        req.password = queryPassword;
    } else {
        req.username = username;
        req.password = password;
    }

    try {
        req.mb = new MB({ username: req.username, password: req.password });
        next();
    } catch (error) {
        console.error('Failed to initialize MB instance:', error);
        res.status(500).json({ error: 'Failed to initialize MB instance' });
    }
};

module.exports = auth;
