from math import sqrt
from app.car import Car
from app.shop import Shop


class Customer:

    def __init__(self,
                 name: str,
                 product_cart: dict,
                 location: list,
                 money: int,
                 car: dict) -> None:

        self.name = name
        self.product_cart = product_cart
        self.location = location
        self.money = money
        self.car = Car(**car)

    def trip_cost_counter(self,
                          shop: Shop,
                          fuel_cost: int | float) -> tuple:

        cost = 0
        distance = sqrt((shop.location[0] - self.location[0]) ** 2
                        + (shop.location[1] - self.location[1]) ** 2)
        fuel_per_distance = (self.car.fuel_consumption * distance) / 100
        cost += fuel_per_distance * fuel_cost * 2

        for product, amount in self.product_cart.items():
            cost += shop.products.get(product) * amount

        cost = round(cost, 2)
        print(f"{self.name}'s trip to the {shop.name} costs {cost}")

        return shop, cost
