
class Restaurant:
    def __init__(self, name):
        self._name = name
        self.reviews = []


    @property
    def name(self):
        return self._name

    # @name.setter
    # def name(self, new_name):
    #     print("Error: Cannot change restaurant name.")

    # Object Relationship Methods
    def add_review(self, review):
            self._reviews.append(review)

    def reviews(self):
        return self.reviews

    def customers(self):
        unique_customers = set()
        for review in self.reviews:
            unique_customers.add(review.customer())
        return list(unique_customers)


# Aggregate and Association Methods
    def average_star_rating(self):
            if len(self.reviews) == 0:
                return 0
            total_ratings = sum(review.rating() for review in self.reviews)
            return total_ratings / len(self.reviews)
    
# # Example usage:
# restaurant = Restaurant("Tasty Eats")
# print(restaurant.name)  # Output: Tasty Eats

# Attempting to change the name will raise an error
# restaurant.name = "New Name"  # This will result in an AttributeError