#ArbitraryData
# Mass is * 10^24 kg
#MercuryMass 0.330
#VenusMass 4.87
#EarthMass 5.97
#MarsMass 0.642
#JupiterMass 1898
#MoonMass 0.073


import turtle
import math
import time

ScaleFactor = 1 #Adjustable Scaling Factor
InvScaleFactor = 1/ScaleFactor #Inverse scale factor to adjust the x-axis
G = 0.0001  #gravitational constant for stability (adjust)
TIME_STEP = 1  # time increment per frame
SUN_MASS = 1000000 #Arbitrary value for the oslar mass to make the simulation stable
#Distance in million km * Scaling Factor
EarthDistance = 149 * ScaleFactor
VenusDistance = 107 * ScaleFactor
MarsDistance = 227 * ScaleFactor
JupiterDistance = 763 * ScaleFactor
MercuryDistance = 46 * ScaleFactor

#Eccenstricity, Multiplication factor using planetary eccentricity
Earth_e = 1 + 0.017
Venus_e = 1 + 0.007
Mars_e = 1 + 0.094
Jupiter_e = 1 + 0.049
Mercury_e = 1 + 0.206

#ArbitraryDist
EarthOrbVel_e = 149 * ScaleFactor * Earth_e
VenusOrbVel_e = 107 * ScaleFactor * Venus_e
MarsOrbVel_e = 227 * ScaleFactor * Mars_e
JupiterOrbVel_e = 763 * ScaleFactor * Jupiter_e
MercuryOrbVel_e = 46 * ScaleFactor * Mercury_e

#Radi
RadScaleFactor = 0.001 #Integar used to downscale the radius of planets
EarthRadius = 6378 * RadScaleFactor
MarsRadius = 3389.5 * RadScaleFactor
SunRadius = 10 #696340 * RadScaleFactor #Sun radius set to 10 to avoid chaos : )
VenusRadius = 6051.8 * RadScaleFactor
JupiterRadius = 69911 * RadScaleFactor
MercuryRadius = 2439.7 * RadScaleFactor


turtle.setup(800, 800) #open resolution
screen = turtle.Screen()
screen.bgcolor("black") #Background color
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
        print(len(self.position))
        #global Data
        #Data = self.position
        #print(Data)
        #print(Data[0])
        


    
        #EarthX
        #EarthY
        #print(EarthX)
        #print(EarthY)
    
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
        #print(self.position)
        #print(self.name)
        #print(self.name[0, 1])
        if self.name == "E":
            print("Hey")
        distance = math.sqrt(dx**2 + dy**2)
        if distance == 0:
            return (0, 0)
        force_magnitude = (G * self.mass * other.mass) / (distance ** 2)
        force_x = force_magnitude * (dx / distance)
        force_y = force_magnitude * (dy / distance)
        return (force_x, force_y)

#planetcreat
sun = CelestialBody("Sun", "yellow", SUN_MASS, SunRadius, (0, 0), (0, 0))
def orbital_velocity(distance):
    speed = math.sqrt(G * SUN_MASS / distance)#mathematical formula for spd using g/m/r
    return [0, speed]

#MoonTestCode (Continue Here)
#moon = CelestialBody("Moon", "White", 1, 3, (0,149), (0, 149))
def moon_orbital_velocity(distance):
    mspeed = math.sqrt(G * 100 / distance)#mathematical formula for spd using g/m/r
    return [0, mspeed]


#visualisation of planets
mercury = CelestialBody("Mercury", "green", 30, MercuryRadius, (MercuryDistance, 0), orbital_velocity(MercuryOrbVel_e))
earth = CelestialBody("Earth", "blue", 100, EarthRadius, (EarthDistance, 0), orbital_velocity(EarthOrbVel_e))#temp arbitrry units
EarthX = earth.position[0]
EarthY = earth.position[1]
mars = CelestialBody("Mars", "red", 80, MarsRadius, (MarsDistance, 0), orbital_velocity(MarsOrbVel_e))
venus = CelestialBody("Venus", "orange", 90, VenusRadius, (VenusDistance, 0), orbital_velocity(VenusOrbVel_e))
jupiter = CelestialBody("Jupiter", "brown", 500, JupiterRadius, (JupiterDistance, 0), orbital_velocity(JupiterOrbVel_e))
#saturn = CelestialBody("Saturn", "gold", 400, 18, (950, 0), orbital_velocity(950))
moon = CelestialBody("Moon", "White", 400, 3, (EarthX, EarthY), orbital_velocity(EarthOrbVel_e))
#EccentricityTest = CelestialBody("Test", "Purple", 400, 10, (150, 0), orbital_velocity(300))

bodies = [sun, mercury, venus, earth, moon, mars, jupiter] #postioning order

#x-axis
def draw_x_axis(): #Defines a created function
    turtle.penup()
    turtle.color("white") #Color of the x axis
    turtle.goto(-800, -350)
    turtle.pendown()
    turtle.forward(1200)
    for i in range(-800, 801, 100):
        turtle.penup()
        turtle.goto(i, -370)
        turtle.pendown()
        turtle.write(f"{i*InvScaleFactor} mkm", align="center", font=("Arial", 8, "normal"))
    turtle.penup()

draw_x_axis() #Runs the function draw_x_axis which draws the x axis : o

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
      
#print(earth.position) Allows to print earths position i x and y


run_simulation()
turtle.done()
