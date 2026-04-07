####Readme.md####




StrawberryFi utility token"s main Server 






const express = require('express');
const { addTransaction, getChain } = require('./ledger/engine');
const { validateTransaction } = require('./ledger/validator');
const { detectPatterns } = require('./ledger/intelligence');

const app = express();
app.use(express.json());

app.post('/transaction', (req, res) => {
  const tx = req.body;

  const validation = validateTransaction(tx);

  if (!validation.valid) {
    return res.status(400).json({
      error: validation.reason
    });
  }

  const block = addTransaction(tx);

  res.json({
    message: "🍓 Transaction secured",
    block
  });
});

app.get('/ledger', (req, res) => {
  const chain = getChain();
  const alerts = detectPatterns(chain);

  res.json({
    chain,
    intelligence: alerts
  });
});

app.listen(3000, () => {
  console.log('🍓 StrawberryFi Intelligence System LIVE');
});