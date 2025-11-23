class Book:
    def __init__(self, title, author, price):
        self.title = title
        self.author = author
        self.price = price

    def display_details(self):
        print(f"Title : {self.title}")
        print(f"Author: {self.author}")
        print(f"Price : ₹{self.price:.2f}")
        print("-" * 30)

    def apply_discount(self, discount_percent):
        discount_amount = (discount_percent / 100) * self.price
        self.price -= discount_amount


# (a) Create two book objects
book1 = Book("The cafe of unspoken truth", "Isha Dave", 251)
book2 = Book("Ikigai: The Japanese Secret to a Long and Happy Life", "Héctor García and Francesc Miralles",500)

print("Book Details:")
book1.display_details()
book2.display_details()

# (b) Apply 10% discount to one book
print("After applying 10% discount on Book 2:")
book2.apply_discount(10)
book2.display_details()
