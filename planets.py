# Name: Nicole Arcolino
# Section: 202-07

def weight_on_planets():
   print("What do you weigh on earth? ")
   weight = input()
   mars_weight = int(weight) * 0.38
   jupiter_weight = int(weight) * 2.34
   print("On Mars you would weigh " + str(mars_weight) + " pounds.")
   print("On Jupiter you would weigh " + str(jupiter_weight) + " pounds.")


if __name__ == '__main__':
   weight_on_planets()