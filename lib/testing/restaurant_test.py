import unittest
from restaurant import Restaurant
from reviews import Review
from customers import Customer

class TestRestaurantMethods(unittest.TestCase):

    def test_add_review(self):
        restaurant = Restaurant("X Cafe")
        customer = Customer("Eric", "Muthui")
        review = Review(customer, restaurant, 4)

        # Add the review to the restaurant
        restaurant.add_review(review)

        # Check if the review is in the restaurant's reviews list
        self.assertIn(review, restaurant.reviews)

    def test_average_star_rating(self):
        restaurant = Restaurant("Y Cafe")
        customer1 = Customer("Eric", "Muthui")
        customer2 = Customer("Denzel", "Morales")

        # Create reviews with different ratings
        review1 = Review(customer1, restaurant, 4)
        review2 = Review(customer2, restaurant, 5)

        # Add the reviews to the restaurant
        restaurant.add_review(review1)
        restaurant.add_review(review2)

        # Calculate the average star rating
        average_rating = restaurant.average_star_rating()

        # Check if the average rating is calculated correctly
        self.assertEqual(average_rating, 4.5)

if __name__ == '__main__':
    unittest.main()
