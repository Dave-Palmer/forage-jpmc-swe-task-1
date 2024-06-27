import unittest
from client3 import getDataPoint

class ClientTest(unittest.TestCase):
  def test_getDataPoint_calculatePrice(self):
    quotes = [
      {'top_ask': {'price': 121.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
      {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
    ]
    """ ------------ Add the assertion below ------------ """
    def getDataPoint(quote):
        stock = quote['stock']
        bid_price = quote['top_bid']['price']
        ask_price = quote['top_ask']['price']
        price = (bid_price + ask_price) / 2
        return stock, bid_price, ask_price, price

    dataPoint1 = getDataPoint(quotes[0])
    dataPoint2 = getDataPoint(quotes[1])

    self.assertEqual(dataPoint1, ('ABC', 120.48, 121.2, (120.48 + 121.2) / 2))
    self.assertEqual(dataPoint2, ('DEF', 117.87, 121.68, (117.87 + 121.68) / 2))
  def test_getDataPoint_calculatePriceBidGreaterThanAsk(self):
    quotes = [
      {'top_ask': {'price': 119.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
      {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
    ]
    """ ------------ Add the assertion below ------------ """
    for quote in quotes:
        bid_price = quote['top_bid']['price']
        ask_price = quote['top_ask']['price']
        self.assertGreater(bid_price, ask_price, f"Bid price {bid_price} is not greater than ask price {ask_price} for stock {quote['stock']}")

  """ ------------ Add more unit tests ------------ """



if __name__ == '__main__':
    unittest.main()
