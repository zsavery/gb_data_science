import csv

# Initialize an empty list to store the collected data
collected_data = []

# Collect data from interviews (replace this with your data collection logic)
for i in range(5):
    # Sample data collection for numerical data
    name = input("Enter the student's name: ")
    num_siblings = int(input("How many siblings do they have? "))
    collected_data.append([name, num_siblings])

    # Sample data collection for categorical data
    favorite_color = input("What is their favorite color? ")
    collected_data.append([name, favorite_color])

# Define the CSV file name
csv_file = "collected_data.csv"

# Write the collected data to the CSV file
with open(csv_file, mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["Name", "Data"])
    writer.writerows(collected_data)

print(f"Data has been saved to {csv_file}")
