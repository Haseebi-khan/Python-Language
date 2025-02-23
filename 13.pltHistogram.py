# import matplotlib.pyplot as plt

# # Assuming life_exp is already defined as a list or array of values
# plt.hist(life_exp)  # Python will use 10 bins by default
# plt.show()
# plt.clft()

# something = [34,23,54,12,21,34,21,43,231,23,23,23,2,3,23,1,2]
# plt.hist(something, 5)
# plt.show()
# plt.clft()



# # Scatter plot
# plt.scatter(gdp_cap, life_exp)

# # Previous customizations
# plt.xscale('log') 
# plt.xlabel('GDP per Capita [in USD]')
# plt.ylabel('Life Expectancy [in years]')
# plt.title('World Development in 2007')

# # Definition of tick_val and tick_lab
# tick_val = [1000, 10000, 100000]
# tick_lab = ['1k', '10k', '100k']

# # Adapt the ticks on the x-axis


# # After customizing, display the plot

# Import numpy as np
import numpy as np

# Store pop as a numpy array: np_pop
np_pop = np.array(pop)

# Double np_pop
np_pop = np_pop * 2

# Update: set s argument to np_pop
plt.scatter(gdp_cap, life_exp, np_pop)

# Previous customizations
plt.xscale('log') 
plt.xlabel('GDP per Capita [in USD]')
plt.ylabel('Life Expectancy [in years]')
plt.title('World Development in 2007')
plt.xticks([1000, 10000, 100000],['1k', '10k', '100k'])

# Display the plot
plt.show()





# Scatter plot
plt.scatter(x = gdp_cap, y = life_exp, s = np.array(pop) * 2, c = col, alpha = 0.8)

# Previous customizations
plt.xscale('log') 
plt.xlabel('GDP per Capita [in USD]')
plt.ylabel('Life Expectancy [in years]')
plt.title('World Development in 2007')
plt.xticks([1000,10000,100000], ['1k','10k','100k'])

# Additional customizations
plt.text(1550, 71, 'India')
plt.text(5700, 80, 'China')

# Add grid() call
plt.grid(True)

# Show the plot
plt.show()

