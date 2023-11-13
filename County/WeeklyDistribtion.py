import pandas as pd
import matplotlib.pyplot as plt

SignWeeks = pd.read_csv('./WeeklyAvg.csv')
print(SignWeeks)

ax = SignWeeks.plot.bar(x='Week_Number',y='window')
ax.set_title("Average window size across weeks")
ax.set_xlabel("Week Number")
ax.set_ylabel("avg window size")
plt.show()

