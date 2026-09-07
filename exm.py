"""Vehicle rental example demonstrating inheritance and encapsulation."""
# Child classes only change the service charge; they reuse all Vehicle behavior.


class Vehicle:
    service_charge = 0.0

    def __init__(self, number: str, brand: str, model: str, daily_rate: float) -> None:
        self.number, self.brand, self.model, self.daily_rate = number, brand, model, daily_rate
        self._available = True

    @property
    def available(self) -> bool:
        return self._available

    def rent(self) -> bool:
        if not self._available:
            return False
        self._available = False
        return True

    def return_vehicle(self) -> None:
        self._available = True

    def calculate_rent(self, days: int) -> float:
        if days <= 0:
            raise ValueError("Days must be positive.")
        base = self.daily_rate * days
        return base * (1 + self.service_charge)


class Car(Vehicle):
    service_charge = 0.10


class Bike(Vehicle):
    service_charge = 0.05


if __name__ == "__main__":
    car = Car("KL01AB1234", "Toyota", "Innova", 2000)
    bike = Bike("KL05CD5678", "Honda", "Activa", 800)
    for vehicle in (car, bike):
        print(f"{vehicle.brand} {vehicle.model}: ₹{vehicle.calculate_rent(2):.0f} for 2 days")
