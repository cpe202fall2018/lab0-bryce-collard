#Lab 0
#Bryce Collard
#CPE 202 (Parkinson)
def weight_on_planets():
   userWeight = int(input("What do you weigh on earth? "))
   weightOnMars = .38 * userWeight
   weightOnJupiter = 2.34 * userWeight
   print("\nOn Mars you would weigh {} pounds.\nOn Jupiter you would weigh {} pounds.".format(weightOnMars, weightOnJupiter))
    
if __name__ == '__main__':
   weight_on_planets()