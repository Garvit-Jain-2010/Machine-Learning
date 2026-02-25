import matplotlib.pyplot as plt

x = [1, 2, 3, 4]
y = [1, 2, 4, 4]
plt.step(x, y, marker = 'o', ms = 10, mfc="g", label = "Python")
plt.grid()
plt.show()

# ----------------------------------

days = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
temperature = [36.6, 37, 37.7, 39, 40.1, 43, 43.4, 45, 45.6, 40.1, 44]

plt.title("Gwalior Temperature")
plt.xlabel("Days")
plt.ylabel("Temperature")
plt.bar(days,temperature, color = "red")
plt.show()

