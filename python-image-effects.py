from PIL import Image
from random import randint

NUMBER_OF_ITERATIONS = 100
PERCENTAGE_OF_NOISE = 20

for i in range(0, NUMBER_OF_ITERATIONS):
    print("-------------Starting: " + str(i))

    image = Image.open("images/sources/test_2.jpg")
    pixels = image.load()

    width = image.width
    height = image.height

    for y in range(height):
        for x in range(width):
            random_x = randint(x, width - 1)
            random_y = randint(y, height - 1)
            random_chance = randint(0, 99)

            if random_chance <= i:
                pixels[random_x, random_y] = pixels[x, y]

    image.save("images/results/result_" + str(i) + ".jpg")
