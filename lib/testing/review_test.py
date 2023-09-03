import unittest
from reviews import Review 
from customers import Customer 
from restaurant import Restaurant

class TestReview(unittest.TestCase):

    def setUp(self):
        self.customer1 = Customer("Eric", "Muthui")
        self.customer2 = Customer("Chris", "Rock")
        self.restaurant1 = Restaurant("X Cafe")
        self.restaurant2 = Restaurant("Y Cafe")
        self.review1 = Review(self.customer1, self.restaurant1, 4)
        self.review2 = Review(self.customer2, self.restaurant2, 5)
        self.review3 = Review(self.customer1, self.restaurant2, 3)

    def test_rating_method(self):
        self.assertEqual(self.review1.rating(), 4)
        self.assertEqual(self.review2.rating(), 5)
        self.assertEqual(self.review3.rating(), 3)

    def test_customer_property(self):
        self.assertEqual(self.review1.customer, self.customer1)
        self.assertEqual(self.review2.customer, self.customer2)
        self.assertEqual(self.review3.customer, self.customer1)

    def test_restaurant_property(self):
        self.assertEqual(self.review1.restaurant, self.restaurant1)
        self.assertEqual(self.review2.restaurant, self.restaurant2)
        self.assertEqual(self.review3.restaurant, self.restaurant2)

    def test_all_reviews_classmethod(self):
        all_reviews = Review.all()
        self.assertEqual(len(all_reviews), 3)
        self.assertIn(self.review1, all_reviews)
        self.assertIn(self.review2, all_reviews)
        self.assertIn(self.review3, all_reviews)

if __name__ == '__main__':
    unittest.main()
