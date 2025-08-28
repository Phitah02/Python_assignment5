class Smartphone:
    def __init__(self, brand, model, storage, battery_level=100):
        """Initialize the smartphone with brand, model, storage, and battery level."""
        self.brand = brand
        self.model = model
        self.storage = storage
        self.battery_level = battery_level
        self.is_on = False

    def turn_on(self):
        """Turn on the smartphone."""
        self.is_on = True
        print(f"{self.brand} {self.model} is now ON.")

    def turn_off(self):
        """Turn off the smartphone."""
        self.is_on = False
        print(f"{self.brand} {self.model} is now OFF.")

    def check_battery(self):
        """Check the current battery level."""
        print(f"Battery level: {self.battery_level}%")

    def use_app(self, app_name):
        """Simulate using an app."""
        if self.is_on:
            print(f"Using {app_name} on {self.brand} {self.model}.")
            self.battery_level -= 10
        else:
            print("Please turn on the smartphone first.")

class GamingPhone(Smartphone):
    def __init__(self, brand, model, storage, battery_level=100, game_mode=False):
        """Initialize the gaming phone with additional game mode feature."""
        super().__init__(brand, model, storage, battery_level)
        self.game_mode = game_mode

    def enable_game_mode(self):
        """Enable game mode."""
        self.game_mode = True
        print(f"Game mode enabled on {self.brand} {self.model}.")

    def disable_game_mode(self):
        """Disable game mode."""
        self.game_mode = False
        print(f"Game mode disabled on {self.brand} {self.model}.")
