from customers import Customer
from restaurant import Restaurant

# Create some customers
customer1 = Customer("Eric", "Muthui")
customer2 = Customer("Chris", "Rock")
customer3 = Customer("Denzel", "Morales")

# Test the given_name() method
assert customer1.given_name() == "Eric"

# Test the family_name() method
assert customer2.family_name() == "Rock"

# Test the full_name() method
assert customer3.full_name() == "Denzel Morales"

# Test the all() method
all_customers = Customer.all()
assert len(all_customers) == 3

# Create some restaurants
restaurant1 = Restaurant("X Cafe")
restaurant2 = Restaurant("Y Cafe")

# Test the add_review() method
customer1.add_review(restaurant1, 4)
customer2.add_review(restaurant2, 5)
customer3.add_review(restaurant2, 3)

# Test the restaurants() method
reviewed_restaurants = customer1.restaurants()
assert len(reviewed_restaurants) == 1
assert reviewed_restaurants[0].name == "X Cafe"
# Test the num_reviews() method
assert customer2.num_reviews() == 1

# Test the find_by_name() class method
found_customer = Customer.find_by_name("Denzel Morales")
assert found_customer is not None
assert found_customer.full_name() == "Denzel Morales"

# Test the find_all_by_given_name() class method
matching_customers = Customer.find_all_by_given_name("Eric")
assert len(matching_customers) == 2
