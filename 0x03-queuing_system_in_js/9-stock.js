import express from 'express';
import redis from 'redis';
import { promisify } from 'util';

// List of products
const listProducts = [
  { itemId: 1, itemName: 'Suitcase 250', price: 50, initialAvailableQuantity: 4 },
  { itemId: 2, itemName: 'Suitcase 450', price: 100, initialAvailableQuantity: 10 },
  { itemId: 3, itemName: 'Suitcase 650', price: 350, initialAvailableQuantity: 2 },
  { itemId: 4, itemName: 'Suitcase 1050', price: 550, initialAvailableQuantity: 5 },
];

// Function to get an item by ID
function getItemById(id) {
  return listProducts.find((product) => product.itemId === id);
}

// Initialize Redis client
const client = redis.createClient();
const getAsync = promisify(client.get).bind(client);

// Reserve stock in Redis
function reserveStockById(itemId, stock) {
  client.set(`item.${itemId}`, stock);
}

// Get current reserved stock from Redis
async function getCurrentReservedStockById(itemId) {
  const stock = await getAsync(`item.${itemId}`);
  return stock ? parseInt(stock, 10) : 0;
}

// Express server setup
const app = express();
const PORT = 1245;

// Route: GET /list_products
app.get('/list_products', (req, res) => {
  res.json(listProducts);
});

// Route: GET /list_products/:itemId
app.get('/list_products/:itemId', async (req, res) => {
  const itemId = parseInt(req.params.itemId, 10);
  const product = getItemById(itemId);

  if (!product) {
    res.json({ status: 'Product not found' });
    return;
  }

  const currentReservedStock = await getCurrentReservedStockById(itemId);
  const currentQuantity =
    product.initialAvailableQuantity - currentReservedStock;

  res.json({
    ...product,
    currentQuantity,
  });
});

// Route: GET /reserve_product/:itemId
app.get('/reserve_product/:itemId', async (req, res) => {
  const itemId = parseInt(req.params.itemId, 10);
  const product = getItemById(itemId);

  if (!product) {
    res.json({ status: 'Product not found' });
    return;
  }

  const currentReservedStock = await getCurrentReservedStockById(itemId);
  const currentQuantity =
    product.initialAvailableQuantity - currentReservedStock;

  if (currentQuantity <= 0) {
    res.json({
      status: 'Not enough stock available',
      itemId,
    });
    return;
  }

  // Reserve one item
  reserveStockById(itemId, currentReservedStock + 1);

  res.json({
    status: 'Reservation confirmed',
    itemId,
  });
});

// Start server
app.listen(PORT, () => {
  console.log(`Server running on http://localhost:${PORT}`);
});

