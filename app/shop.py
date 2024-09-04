class Shop:

    def __init__(self,
                 name: str,
                 location: list,
                 products: dict) -> None:

        self.name = name
        self.location = location
        self.products = products

    def sell_products(self, customer: "Customer") -> None: # noqa
        print("Date: 04/01/2021 12:33:41")
        print(f"Thanks, {customer.name}, "
              f"for your purchase!\nYou have bought: ")
        _sum = 0

        for product, amount in customer.product_cart.items():
            product_cost = amount * self.products.get(product)
            plural = "s" if amount > 1 else ""
            if float(product_cost).is_integer():
                print(f"{amount} {product}{plural} for "
                      f"{int(product_cost)} dollars")
            else:
                print(f"{amount} {product}{plural} for "
                      f"{product_cost} dollars")
            _sum += product_cost

        print(f"Total cost is {_sum} dollars")
        print("See you again!\n")
