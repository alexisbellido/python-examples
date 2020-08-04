def get_green_lights(lights):
    """
    Return a list of light keys to indicate which ones can go green.
    Give preference to North and South lights.
    A light should go green if it has max number of cars.
    """
    green_lights = []
    ns_cars = 0
    ns_lights = []
    ew_cars = 0
    ew_lights = []
    for k, cars in lights.items():
        if k % 2 == 0:
            ew_cars += sum(cars)
            ew_lights.append(k)
        else:
            ns_cars += sum(cars)
            ns_lights.append(k)
    # print('ns', ns_cars)
    # print('ew', ew_cars)
    if ns_cars >= ew_cars:
        # let north-south cars go
        green_lights = ns_lights
    else:
        # let east-west cars go
        green_lights = ew_lights
    return green_lights

if __name__ == '__main__':

    # lights = {
    #     1: 0, # north
    #     2: 0, # west
    #     3: 0, # south
    #     4: 0  # east
    # }
    # print(get_green_lights(lights))

    lights = {
        1: [1, 2], # north-south and north-east
        2: [0, 4], # west-east and west-north
        3: [1, 2], # south-north and south-west
        4: [2, 2]  # east-west and east-south
    }

    print(get_green_lights(lights))

# PROBLEM
# There is a four-way intersection with four stoplights. 
# # Each light has a sensor which reports the number of cars waiting for this light.

# # Write a function that takes in the sensor states of all the lights and determines 
# # which lights should be green at this moment in time.

# You can determine how the sensor data is structured and how the function's output is structured.

