import turtle
import math
import time

G = 0.1  #gravitational constant for stability (adjust)
TIME_STEP = 1  # time increment per frame
SUN_MASS = 10000

turtle.setup(1200, 800) #open resolution
screen = turtle.Screen()
screen.bgcolor("black")
screen.tracer(0, 0)

#planetclass
class CelestialBody(turtle.Turtle):
    def __init__(self, name, color, mass, radius, position, velocity):
        super().__init__()
        self.name = name
        self.mass = mass
        self.radius = radius
        self.position = list(position)
        self.velocity = list(velocity)
        self.shape("circle")
        self.color(color)
        self.shapesize(radius / 10)
        self.penup()
        self.goto(position[0], position[1])
        self.trail = turtle.Turtle()
        self.trail.hideturtle()
        self.trail.penup()
        self.trail.color(color)
        self.trail.pensize(1)
        self.trail.pendown()
    
    def update_position(self, force):
        ax = force[0] / self.mass
        ay = force[1] / self.mass
        self.velocity[0] += ax * TIME_STEP
        self.velocity[1] += ay * TIME_STEP
        self.position[0] += self.velocity[0] * TIME_STEP
        self.position[1] += self.velocity[1] * TIME_STEP
        self.goto(self.position[0], self.position[1])
        self.trail.goto(self.position[0], self.position[1])
    
    def compute_gravitational_force(self, other):
        dx = other.position[0] - self.position[0]
        dy = other.position[1] - self.position[1]
        distance = math.sqrt(dx**2 + dy**2)
        if distance == 0:
            return (0, 0)
        force_magnitude = (G * self.mass * other.mass) / (distance ** 2)
        force_x = force_magnitude * (dx / distance)
        force_y = force_magnitude * (dy / distance)
        return (force_x, force_y)

#planetcreat
sun = CelestialBody("Sun", "yellow", SUN_MASS, 30, (0, 0), (0, 0))
def orbital_velocity(distance):
    speed = math.sqrt(G * SUN_MASS / distance)#mathematical formula for spd using g/m/r
    return [0, speed]

#visualisation of planets
earth = CelestialBody("Earth", "blue", 100, 10, (300, 0), orbital_velocity(300))#temp arbitrry units
mars = CelestialBody("Mars", "red", 80, 8, (450, 0), orbital_velocity(450))
venus = CelestialBody("Venus", "orange", 90, 9, (200, 0), orbital_velocity(200))
jupiter = CelestialBody("Jupiter", "brown", 500, 20, (750, 0), orbital_velocity(750))
saturn = CelestialBody("Saturn", "gold", 400, 18, (950, 0), orbital_velocity(950))

bodies = [sun, earth, mars, venus, jupiter, saturn] #postioning order

#x-axis
def draw_x_axis():
    turtle.penup()
    turtle.color("white")
    turtle.goto(-600, -350)
    turtle.pendown()
    turtle.forward(1200)
    for i in range(-600, 601, 100):
        turtle.penup()
        turtle.goto(i, -370)
        turtle.pendown()
        turtle.write(f"{i} units", align="center", font=("Arial", 8, "normal"))
    turtle.penup()

draw_x_axis()

#the simulation function
def run_simulation():
    while True:
        forces = {body: [0, 0] for body in bodies}
        for i, body in enumerate(bodies):
            for j, other in enumerate(bodies):
                if i != j:
                    fx, fy = body.compute_gravitational_force(other)
                    forces[body][0] += fx
                    forces[body][1] += fy
        for body in bodies:
            body.update_position(forces[body])
        screen.update()
        time.sleep(0.01)

run_simulation()
turtle.done()
