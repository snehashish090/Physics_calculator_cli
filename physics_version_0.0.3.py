# Made By Snehashish Laskar
# Made on 11-03-2021
# This can be used to calculate usefull things using physics formulae
# This can be used By teachers if they want to correct the exam pappers easily and without doing any calculations!
'''
	Instructions:
	-> Please follow the notes written below for help!
	-> Please do not enter the Units of the numbers below!
'''


class acceleration:

    def __init__(self):
        pass

    def calculate_acceleration_with_force(self, force, mass):
        # Please enter the net force and mass as parameters
        # it can be used to calculate acceleration from net force and mass
        self.equation1 = force/mass
        print(f"The acceleratin is equal to : {self.equation1} m/s squared")

    def calculate_acceleration_with_velocity(self, velocity, time):
        # Please enter the change in velocity with the time intervals as parameters
        # Please give the velocity in m/s
        # This can be used to calculate the acceleration from change in velocity and time intervals
        self.equation2 = velocity/time
        print(f"acceleration is equal to {self.equation2} m/s squared")


class motion:

    def __init__(self):
        pass

    def calculate_avg_speed(self, distance, time):
        # Please enter the toatal distance and time intervals as parameters
        # Please give the distance in meters only
        # This can be used to calculate average speed from toatl distamce and time
        self.equation3 = distance/time
        print(f" the average speed is equal to {self.equation3}m/s ")

    def calculate_distance(self, avg_speed, time):
        # Please pass the average speed and time as parameters
        # Please give speed in m/s only!
        # This Function can be used to calculate the distance from Average speed and time
        self.equation5 = avg_speed*time
        print(f"disctance covered id equal to {self.equation5}m")

    def calculate_distance_from_acceleration(self, acceleration, time):
        # Please pass the acceleration and time as parameters
        # Please give the acceleration in m/s
        # This Function can be used to calculate the distance from acceleration and time
        self.equation6 = (acceleration*(time*time))/2
        print(f"disctance covered is equal to {self.equation6}m ")


class momentum:

    def __init__(self):
        pass

    def calculate_momentum(self, mass, velocity):
        # Please pass the mass and the velocity as parameters
        # Please give mass on Kg's only!
        # this Function can be used to calaculate the momentum of an object from its velocity and mass!
        self.equation4 = mass*velocity
        print(f"The momentum of this object is {self.equation4} kg m/s")

    def calculate_impulse(self, force, time):
        # Please pass the force and time as parameters
        # This function can be used to calculate the impulse applied on an object
        self.equation7 = force*time
        print(f"Impulse is equal to {self.equation7}N ")


momentum = momentum()
acceleration = acceleration()
motion = motion()

motion.calculate_avg_speed(1000, 100)
