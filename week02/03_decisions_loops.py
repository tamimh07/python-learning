# Week 2, Part C: decisions and loops
# (thresholds here are examples for practice, not official standards)

# 1. if/ elif / else
ph= 7.4
if ph < 6.5: print ('Acidic: below the usual range')
elif ph > 8.5: print('Alkaline: above the usual range')
else:print('Within the usual range') 

# 2. for loop: repeat for every item in a list
ph_values = [7.2, 6.8, 7.5, 8.1, 6.9]
for value in ph_values: print(f'pH {value}')

# 3. Accumulating a total
total = 0
for value in ph_values: 
    total = total + value
mean_ph = total / len(ph_values)
print(f'Mean pH: {mean_ph: .2f}')

#4. A loop with a decision inside
readings = [7.2, 6.4, 7.5, 8.9, 6.9]
count_out = 0
for value in readings: 
    if value in readings: 
        if value < 6.5 or value > 8.5: 
            print (f'{value} is out of range')
            count_out = count_out +1
            print(f'{count_out} of {len(readings)} readings out of range')


# 5. range () makes a sequence of numbers
print(list(range(5)))
print(list(range(1, 6)))
print(list(range(0, 10, 2)))

# 6. enumerate(): position and value together
for i, value in enumerate (readings, start=1):
    print(f'Reading {i}: {value}')
# 7. Looping over a list of dictionaries
samples = [
    {'site': 'A', 'ph': 7.2},
    {'site': 'B', 'ph': 6.4},
    {'site': 'C', 'ph': 8.9},
]
for s in samples:
    if s['ph'] < 6.5:
        status = 'acidic'
    elif s['ph'] > 8.5:
        status = 'alkaline'
    else:
        status = 'normal'
    print(f"{s['site']}: pH {s['ph']} -> {status}")

# 8. while loop: repeat until a condition stops being true
conc = 100.0
days = 0
while conc > 10:
    conc = conc / 2
    days = days + 1
    print(f'Day {days}: {conc} mg/L')
print(f'Below 10 mg/L after {days} days')
