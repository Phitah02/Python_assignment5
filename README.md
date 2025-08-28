# Python Assignment 5 - Object-Oriented Programming

## Steps Followed During This Assignment

### Assignment 1: Design Your Own Class! 🏗️

**Step 1: Created Smartphone Class**
- Designed a `Smartphone` class with attributes: brand, model, storage, battery_level, is_on
- Implemented methods: __init__(), turn_on(), turn_off(), check_battery(), use_app()
- Used constructor to initialize objects with unique values

**Step 2: Implemented Inheritance**
- Created `GamingPhone` subclass that inherits from `Smartphone`
- Added gaming-specific features: game_mode attribute
- Implemented methods: enable_game_mode(), disable_game_mode()
- Demonstrated encapsulation through proper attribute access

### Activity 2: Polymorphism Challenge! 🎭

**Step 3: Created Animal Hierarchy**
- Designed abstract base class `Animal` with abstract method move()
- Created subclasses: Dog, Bird, Fish, Snake
- Each subclass implements move() method differently:
  - Dog: "Running" 🐕
  - Bird: "Flying" 🐦
  - Fish: "Swimming" 🐟
  - Snake: "Slithering" 🐍

**Step 4: Implemented Polymorphism**
- Used abstract base class (ABC) and abstractmethod decorator
- Demonstrated polymorphism through common interface (move() method)
- Each animal class defines move() differently while maintaining the same method signature

### Files Created:

1. **smartphone.py** - Contains Smartphone and GamingPhone classes
2. **animals.py** - Contains Animal hierarchy with polymorphism
3. **main.py** - Demonstration script showing both assignments
4. **assignment_plan.md** - Planning document outlining the approach

### Key OOP Concepts Demonstrated:

- **Encapsulation**: Private attributes with controlled access through methods
- **Inheritance**: GamingPhone inherits from Smartphone
- **Polymorphism**: Different animals implement move() method differently
- **Abstraction**: Abstract base class with abstract methods

### To Run the Demonstration:
```bash
python main.py
```

### Learning Outcomes:
- Designed custom classes with attributes and methods
- Used constructors for object initialization
- Implemented inheritance with subclass specialization
- Demonstrated polymorphism through method overriding
- Applied abstract base classes for interface definition
