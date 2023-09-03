from customers import Customer  
from restaurant import Restaurant

class Review:
    all_reviews = []

    def __init__(self, customer, restaurant, rating):
        self._customer = customer
        self._restaurant = restaurant
        self._rating = rating
        Review.all_reviews.append(self)

    def rating(self):
        return self._rating

    @classmethod
    def all(cls):
        return cls.all_reviews


    # Object Relationship Methods
    @property
    def customer(self):
        return self._customer
    
    @property
    def restaurant(self):
        return self._restaurant


# Example usage:

# Create some customers, restaurants, and reviews
customer1 = Customer("John", "Doe")
customer2 = Customer("Jane", "Smith")
restaurant1 = Restaurant("Bistro X")
restaurant2 = Restaurant("Cafe Y")

# Create reviews
review1 = Review(customer1, restaurant1, 4)
review2 = Review(customer2, restaurant2, 5)
review3 = Review(customer1, restaurant2, 3)

customer1.customer = "New Name"

# Get all reviews and print them
reviews = Review.all()
for review in reviews:
    print(f"Customer: {review.customer.full_name()},Rating: {review.rating()}")



# Get the rating for a specific review (e.g., the first review)
rating = review1._rating
print(f"Rating for review1: {rating}")