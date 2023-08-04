# Defining the Weapon class and Pistol subclass

import math
import random
from bullet import Bullet

class Weapon:
    def __init__(self):
        # Common attributes for all weapons can be defined here
        pass

    def fire(self, x, y, direction):
        bullets = []
        bullets.append(Bullet(x, y, direction, distance=self.bullet_distance, size=self.size, speed=self.speed))
        return bullets


class Pistol(Weapon):
    def __init__(self):
        super().__init__()
        
        # Machine Gun Stats
        self.fire_interval = 1000  # 1000 milliseconds = 1 second
        self.damage = 5
        self.bullet_count = 1  # Number of bullets to fire
        self.spread_angle = 0  # Angle of spread in degrees
        self.bullet_distance = 300
        self.size = 10
        self.speed = 2
    
class MachineGun(Weapon):
    def __init__(self):
        super().__init__()
        
        # Machine Gun Stats
        self.fire_interval = 100  # 1000 milliseconds = 1 second
        self.damage = 1
        self.bullet_count = 1  # Number of bullets to fire
        self.spread_angle = 0  # Angle of spread in degrees
        self.bullet_distance = 300
        self.size = 5
        self.speed = 5

    # def fire(self, x, y, direction):
    #     # Implementation for firing a bullet as a Machine Gun
    #     bullets = []
    #     bullets.append(Bullet(x, y, direction, distance=self.bullet_distance, size=self.size, speed=self.speed))
    #     return bullets

class Shotgun(Weapon):
    def __init__(self):
        super().__init__()
        
        # Shotgun Stats
        self.fire_interval = 1000  # 1000 milliseconds = 1 second
        self.damage = 1
        self.bullet_count = 10  # Number of bullets to fire
        self.spread_angle = 30  # Angle of spread in degrees
        self.bullet_distance = 0 # Random in Bullet Creation
        self.size = 4
        self.speed = 0 # Random in Bullet Creation
        

    def fire(self, x, y, direction):     
        bullets = []
        
        # Calculate the base angle based on player's direction
        base_angle = math.atan2(direction[1], direction[0]) * (180 / math.pi)
        
        # Create bullets with random angles within the spread
        for _ in range(self.bullet_count):
            # Calculate random angle within spread
            angle = base_angle + random.uniform(-self.spread_angle / 2, self.spread_angle / 2)
            
            # Convert angle back to radians
            angle = math.radians(angle)
            
            # Calculate direction based on angle
            new_direction = (math.cos(angle), math.sin(angle))
            
            # Create bullet and add to list
            bullet = Bullet(x, y, new_direction, distance=random.randint(100,300), size=self.size, speed=random.randint(6,10))
            bullets.append(bullet)
        
        return bullets