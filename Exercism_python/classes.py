class Alien:
    total_aliens_created = 0
    def __init__(self, x_coordinate, y_coordinate):
        self.x_coordinate = x_coordinate
        self.y_coordinate = y_coordinate
        self.health = 3
        Alien.total_aliens_created += 1

    def hit(self):
        total_health = self.health = self.health - 1
        return total_health

    def is_alive(self):
        return self.health > 0

    def teleport(self,x_coordinate, y_coordinate):
        self.x_coordinate = x_coordinate
        self.y_coordinate = y_coordinate

    def collision_detection(self, other_object):
        self.other_object = other_object
        pass

def new_aliens_collection(coordinates):
    return [Alien(x_coord, y_coord) for x_coord, y_coord in coordinates]

alien1 = Alien(2,4)
print(alien1.health)
print(alien1.x_coordinate)
print(alien1.y_coordinate)
print(alien1.hit())
print(alien1.is_alive())
print(alien1.hit())
print(alien1.hit())
print(alien1.is_alive())
alien1.teleport(5,-2)
print(alien1.x_coordinate)
print(alien1.y_coordinate)
print(f"Total objects created: {Alien.total_aliens_created}")
#20


