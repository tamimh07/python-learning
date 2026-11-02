# Week 2, Part B: lists, tuples, dictionaries, sets

# 1. List
ph_values = [7.2, 6.8, 7.5, 8.1, 6.9]
print(ph_values)
print(ph_values[0])     # first item (counting starts at 0)
print(ph_values[-1])    # last item
print(ph_values[1:3])   # slice: items 1 and 2
ph_values.append(7.0)   # add an item to the end
print(len(ph_values), max(ph_values), min(ph_values))
print(round(sum(ph_values) / len(ph_values), 2))
ph_values.sort()
print(ph_values)

# 2. Tuple
station = (22.34, 91.81)     #example latitude, longitude
print(station[0], station[1])

# 3. Dictionary
sample = {
    'site': 'Karnaphuli River',
    'ph': 7.4,
    'do_mg_l': 6.2, 
    'polluted': False,
}
print (sample['site'])
sample['turbidity_ntu'] = 15   # add a new field
print(sample.keys())
print(sample.get('salinity', 'not measured'))

# 4. Set
sites = ['A', 'B', 'A', 'C', 'B']
unique_sites = set(sites)
print(unique_sites, len(unique_sites))

# 5. A list of dictionaries: how real datasets are shaped
samples = [
    {'site': 'A', 'ph': 7.2},
    {'site': 'B', 'ph': 6.4},
    {'site': 'C', 'ph': 8.9}
]
print(samples[1]['ph'])