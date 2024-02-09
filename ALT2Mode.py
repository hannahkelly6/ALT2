# Initialise a list of ages
L = [41.37, 27.73, 40.75, 10.35, 32, 16.37, 19.13, 38.9, 76.28, 29.72, 30]

# Build up a list of unique values
unique_values = []
for value in L:
    if value not in unique_values:
        unique_values.append(value)

# Build up a list of frequencies
frequencies = []
for value in unique_values:
    frequency = L.count(value)
    frequencies.append(frequency)

# Find the mode
max_frequency = max(frequencies)
max_frequency_pos = frequencies.index(max_frequency)
mode = unique_values[max_frequency_pos]

print("Mode is", mode)
#print("Max_Freq", max_frequency)
#print("Max_Freq_Pos", max_frequency_pos)