from smartphone import Smartphone, GamingPhone
from animals import Dog, Bird, Fish, Snake

def demonstrate_smartphone():
    """Demonstrate the Smartphone class and inheritance."""
    print("=" * 50)
    print("ASSIGNMENT 1: SMARTPHONE CLASS DEMONSTRATION BY PETER MWAURA")
    print("=" * 50)
    
    # Create a regular smartphone
    phone1 = Smartphone("Samsung", "Galaxy S23", 256)
    phone1.turn_on()
    phone1.check_battery()
    phone1.use_app("Instagram")
    phone1.check_battery()
    phone1.turn_off()
    
    print("\n" + "-" * 30)
    
    # Create a gaming phone (inheritance example)
    gaming_phone = GamingPhone("ASUS", "ROG Phone 7", 512)
    gaming_phone.turn_on()
    gaming_phone.enable_game_mode()
    gaming_phone.use_app("Call of Duty Mobile")
    gaming_phone.check_battery()
    gaming_phone.disable_game_mode()
    gaming_phone.turn_off()

def demonstrate_polymorphism():
    """Demonstrate polymorphism with animal classes."""
    print("\n" + "=" * 50)
    print("ACTIVITY 2: POLYMORPHISM DEMONSTRATION")
    print("=" * 50)
    
    # Create different animals
    animals = [
        Dog("Bosco"),
        Bird("Tweety"),
        Fish("Nemo"),
        Snake("Slither")
    ]
    
    # Demonstrate polymorphism - same method, different behavior
    for animal in animals:
        animal.speak()
        animal.move()
        print()

def main():
    """Main function to run both demonstrations."""
    demonstrate_smartphone()
    demonstrate_polymorphism()
    
    print("=" * 50)
    print("ASSIGNMENT COMPLETE! 🎉")
    print("=" * 50)

if __name__ == "__main__":
    main()
