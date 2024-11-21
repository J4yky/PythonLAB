import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data = pd.read_csv('wig20_d.csv')

data['Data'] = pd.to_datetime(data['Data'], format='%Y-%m-%d')

dates = data['Data']
close_val = data['Zamkniecie']

days = (dates - dates.min()).dt.days

degree = 4
coefficients = np.polyfit(days, close_val, degree)

polynomial = np.poly1d(coefficients)
approx_values = polynomial(days)

plt.figure(figsize=(10,6))
plt.plot(dates, close_val, label='Real data (WIG20)', color='blue', linewidth=1.5)
plt.plot(dates, approx_values, label=f'Approximation with a polynomial of the {degree} degree', color='red', linestyle='--', linewidth=2)

plt.title('WIG20 value on close and approximation with a polynomial')
plt.xlabel('Date')
plt.ylabel('Value on close')
plt.legend()
plt.grid(True)
plt.xticks(rotation=45)

plt.tight_layout()
plt.show()