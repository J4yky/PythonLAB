import pandas as pd
import matplotlib.pyplot as plt

file_path = "wig20_d.csv"

try:
    data = pd.read_csv(file_path, delimiter=',')

    data['Data'] = pd.to_datetime(data['Data'], format='%Y-%m-%d', errors='coerce')

    last_year = pd.Timestamp.now().year - 1
    start_date = pd.Timestamp(f"{last_year}-01-01")
    end_date = pd.Timestamp(f"{last_year}-12-31")
    filtered_data = data[(data['Data'] >= start_date) & (data['Data'] <= end_date)]

    if filtered_data.empty:
        print(f"No data for {start_date.date()} - {end_date.date()}.")
    else:
        plt.figure(figsize=(10, 6))
        plt.plot(filtered_data['Data'], filtered_data['Zamkniecie'], label='Value on close', color='blue',
                 linewidth=1.5)

        plt.title(f"Chart of WIG20 values on close ({last_year})")
        plt.xlabel("Date")
        plt.ylabel("Value on close")
        plt.grid(True)
        plt.legend()
        plt.tight_layout()

        plt.show()

except FileNotFoundError:
    print(f"File '{file_path}' not found.")
except Exception as e:
    print(f"ERROR: {e}")