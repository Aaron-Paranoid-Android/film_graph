import matplotlib.pyplot as plt
import numpy as np

print("This code will graph the worldwide Box Office earnings of a few Stanley Kubrick movies.")
print("Data is from https://www.the-numbers.com/person/80270401-Stanley-Kubrick#tab=technical")
fig, ax = plt.subplots()             # Create a figure containing a single Axes.
ax.plot(["A Clockwork Orange", "Dr. Strangelove", "2001: A Space Odyssey", "The Shining"], [31079470, 9261253, 71777922, 46805191] )  # Plot some data on the Axes.
ax.set_xlabel('Movies')    #Titles
ax.set_ylabel('Worldwide Box Office Dollars (in tens of millions)')
ax.set_title('Stanley Kubrick Movies')
plt.show()                           # Show the figure.
