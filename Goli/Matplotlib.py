# import numpy as np
# import pandas as pd
import matplotlib.pyplot as plt
sub = ['English', 'Telugu', 'hindi', 'Science', 'social', 'Maths']
values = [73, 95, 72, 98, 99, 100]
plt.title("Percentages of the marks for the students")
plt.pie(values, labels=sub, autopct="%1.2f%%", explode=(0, 0, 0, 0, 0, 0.1), shadow=True)
plt.legend()
plt.show()

