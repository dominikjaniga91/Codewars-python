#https://www.codewars.com/kata/58649884a1659ed6cb000072

lights = ["green", "yellow", "red"]

def update_light(current):
    index = lights.index(current)
    return lights[0] if index == len(lights) - 1 else lights[index + 1]


print(update_light("green"))