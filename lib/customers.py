from reviews import Review

class Customer:
    all_customers = []

    def __init__(self, given_name, family_name):
        self.given_name = given_name
        self.family_name = family_name
        self.reviews = []
        Customer.all_customers.append(self)

    def given_name(self):
        return self.given_name

    def family_name(self):
        return self.family_name

    def full_name(self):
        return f"{self.given_name} {self.family_name}"

    @classmethod
    def all(cls):
        return cls.all_customers
    
   
    # Object Relationship Methods
    def add_review(self, restaurant, rating):
        review = Review(self, restaurant, rating)
        self.reviews.append(review)

    def restaurants(self):
        reviewed_restaurants = set()
        for review in self.reviews:
            reviewed_restaurants.add(review.restaurant())
        return list(reviewed_restaurants)

# Aggregate and Association Methods
    def num_reviews(self):
        return len(self.reviews)

    @classmethod
    def find_by_name(cls, full_name):
        for customer in cls._all_customers:
            if customer.full_name() == full_name:
                return customer
        return None

    @classmethod
    def find_all_by_given_name(cls, given_name):
        matching_customers = []
        for customer in cls.all_customers:
            if customer.given_name() == given_name:
                matching_customers.append(customer)
        return matching_customers

