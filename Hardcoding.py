import matplotlib.pyplot as plt

def quadratic_temperature_model(day, a, b, c):
      # Quadratic equation for temperature
      temperature = a * day**2 + b * day + c
      return temperature

def main():
      # Fixed coefficients for the quadratic equation: ax^2 + bx + c
      a = 1
      b = 5
      c = 6

      # Fixed number of days to model
      num_days = int(input("Enter the number of days to model: "))

      # Lists to store day and corresponding temperature values
      days = list(range(1, num_days + 1))
      temperatures = [quadratic_temperature_model(day, a, b, c) for day in days]

      # Plotting
      plt.plot(days, temperatures, label=f'Temperature: {a}x^2 + {b}x + {c}')
      plt.title('Weather Modeling')
      plt.xlabel('Day')
      plt.ylabel('Temperature (°C)')
      plt.legend()
      plt.show()
      
main()