#ArbitraryData
# Mass is * 10^24 kg
#MercuryMass 0.330
#VenusMass 4.87
#EarthMass 5.97
#MarsMass 0.642
#JupiterMass 1898
#MoonMass 0.073
#sun 1,988,400


import turtle
import math
import time

ScaleFactor = 1 #Adjustable Scaling Factor
InvScaleFactor = 1/ScaleFactor #Inverse scale factor to adjust the x-axis
G = 6.67*10**-11 #1*10**-6  #gravitational constant for stability (adjust)
TIME_STEP = 1  # time increment per frame
SUN_MASS = 1.989*10**11 #Arbitrary value for the oslar mass to make the simulation stable
#Distance in million km * Scaling Factor
EarthDistance = 149 * ScaleFactor
VenusDistance = 107 * ScaleFactor
MarsDistance = 227 * ScaleFactor
JupiterDistance = 763 * ScaleFactor
MercuryDistance = 46 * ScaleFactor
MoonDistance = 150 * ScaleFactor

#Eccenstricity, Multiplication factor using planetary eccentricity
Earth_e = 1 #+ 0.017
Venus_e = 1 #+ 0.007
Mars_e = 1 #+ 0.094
Jupiter_e = 1 #+ 0.049
Mercury_e = 1 #+ 0.206

#ArbitraryVelocities
EarthOrbVel_e = 149 * ScaleFactor * Earth_e #Prior Value: 149
VenusOrbVel_e = 107 * ScaleFactor * Venus_e #Prior Value: 107
MarsOrbVel_e = 227 * ScaleFactor * Mars_e #Prior Value: 227
JupiterOrbVel_e = 763 * ScaleFactor * Jupiter_e #Prior Value: 763
MercuryOrbVel_e = 46 * ScaleFactor * Mercury_e #Prior Value: 46

#Radi
RadScaleFactor = 0.001 #Integar used to downscale the radius of planets
EarthRadius = 6378 * RadScaleFactor
MarsRadius = 3389.5 * RadScaleFactor
SunRadius = 10 #696340 * RadScaleFactor #Sun radius set to 10 to avoid chaos : )
VenusRadius = 6051.8 * RadScaleFactor
JupiterRadius = 69911 * RadScaleFactor
MercuryRadius = 2439.7 * RadScaleFactor


turtle.setup(900, 900) #open resolution
screen = turtle.Screen()
screen.bgcolor("black") #Background color
screen.tracer(0, 0)

#planetclass
class CelestialBody(turtle.Turtle): #Defines the class celestial body using turtle
    def __init__(self, name, color, mass, radius, position, velocity): # definition using an array of data required
        super().__init__()
        self.name = name #name of the given body i.e. self = mars, moon etc
        self.mass = mass #second parametar mass
        self.radius = radius #third parametar radius
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
        #print(other.position[0])
        #print(dx,dy)
        distance = math.sqrt(dx**2 + dy**2)
        #print(distance)
        if distance == 0:
            return (0, 0)
        force_magnitude = (G * self.mass * other.mass) / (distance ** 2)
        force_x = force_magnitude * (dx / distance)
        force_y = force_magnitude * (dy / distance)
        return (force_x, force_y)

Me_M = 0.330*10**4
V_M = 4.87*10**4
E_M = 5.97*10**4
Ma_M = 0.642*10**4
J_M = 1898*10**4
Mo_M = 0.073*10**4

sun = CelestialBody("Sun", "yellow", SUN_MASS, SunRadius, (0, 0), (0, 0)) #Creates the sun as a celestial body class
def orbital_velocity(distance):
    speed = math.sqrt(G * SUN_MASS / distance)#mathematical formula for spd using g/m/r
    return [0, speed]
def morbital_velocity(distance):
    speed = math.sqrt(G * E_M / distance)#mathematical formula for spd using g/m/r
    return [0, speed]
#Variables for the masses of celestial bodies in *10^24 kg

#sun 1,988,400

#visualisation of planets
mercury = CelestialBody("Mercury", "green", Me_M, MercuryRadius, (MercuryDistance, 0), orbital_velocity(MercuryOrbVel_e))
earth = CelestialBody("Earth", "blue", E_M, EarthRadius, (EarthDistance, 0), orbital_velocity(EarthOrbVel_e))#temp arbitrry units
EarthX = earth.position[0]
EarthY = earth.position[1]
mars = CelestialBody("Mars", "red", Ma_M, MarsRadius, (MarsDistance, 0), orbital_velocity(MarsOrbVel_e))
venus = CelestialBody("Venus", "orange", V_M, VenusRadius, (VenusDistance, 0), orbital_velocity(VenusOrbVel_e))
jupiter = CelestialBody("Jupiter", "brown", J_M, JupiterRadius, (JupiterDistance, 0), orbital_velocity(JupiterOrbVel_e))
#saturn = CelestialBody("Saturn", "gold", 400, 18, (950, 0), orbital_velocity(950))
#moon = CelestialBody("Moon", "White", Mo_M, 3, (MoonDistance, 0), orbital_velocity(1))
#EccentricityTest = CelestialBody("Test", "Purple", 400, 10, (150, 0), orbital_velocity(300))

#bodies = [sun, mercury, venus, earth, moon, mars, jupiter] #postioning order
bodies = [sun, venus, mercury, earth, mars, jupiter] #Planets in Sim, Remove whenever

#x-axis
def draw_x_axis(): #Defines a created function
    turtle.penup()
    turtle.color("white") #Color of the x axis
    turtle.goto(-800, -350)
    turtle.pendown() #Makes the drawing visible
    turtle.forward(1600) #Draws the initial line of the x axis
    for i in range(-800, 801, 100):
        turtle.penup()
        turtle.goto(i, -370)
        turtle.pendown()
        turtle.write(f"{i*InvScaleFactor} mkm", align="center", font=("Arial", 8, "normal"))
    turtle.penup()
    
def draw_stats(): #Defines a created function
    turtle.hideturtle()
    turtle.penup()
    turtle.color("white") #Color of the x axis
    turtle.goto(300, 400)
    turtle.penup()
    turtle.pendown()
    turtle.write(f"{earth.name}", align="center", font=("Arial", 8, "normal"))
    turtle.penup()
    turtle.goto(300, 380)
    turtle.pendown()
    turtle.write(f"{earth.mass} kg", align="center", font=("Arial", 8, "normal"))
    turtle.penup()
    turtle.goto(300, 360)
    turtle.pendown()
    turtle.write(f"X = {earth.position[0]}, Y = {earth.position[1]}", align="center", font=("Arial", 8, "normal"))
    turtle.penup()
        

draw_x_axis() #Runs the function draw_x_axis which draws the x axis : o

#the simulation function
def run_simulation(): #creates a function for begining of the program
    while True:
        forces = {body: [0, 0] for body in bodies}
        for i, body in enumerate(bodies):
            for j, other in enumerate(bodies):
                #if other.name == "Sun":
                    #print("Test")
                if i != j:
                    fx, fy = body.compute_gravitational_force(other)
                    forces[body][0] += fx
                    forces[body][1] += fy
        for body in bodies:
            body.update_position(forces[body]) #Updates the positio n via function for each celestial body
            #print(sun.position)
        screen.update()
        time.sleep(0.01)
      
#print(earth.position) Allows to print earths position i x and y
run_simulation()
turtle.exitonclick()
turtle.done()
