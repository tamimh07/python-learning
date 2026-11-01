# Week 2, Part A: variables, numbers, text, True/False

# 1. variables
site = 'Karnaphuli River'
ph = 7.4
do_mg_1 = 6.2
samples = 12
is_polluted = False

print (site)
print(type(site), type(ph), type(samples), type(is_polluted))

# 2. Arithmetic
temp_c = 29
temp_f = temp_c * 9/5+32
temp_k = temp_c +273.15
print(temp_f, temp_k)

rain_mm = 135
print(rain_mm // 25)    # whole-number division
print (rain_mm % 25)    # remainder
print (2**3)            # power 

# 3. Text and f-strings
text = f'{site}: ph = {ph}, DO = {do_mg_1} mg/L'
print(text)
print(site.upper(), len(site))
print(f'Temperature: {temp_f: .1f} F')

# 4. comparisons and True/False
print(ph >= 6.5 and ph <=8.5)
print(do_mg_1 < 5)
is_safe = (6.5 <= ph <=8.5)
print ('safe for aquatic life?', is_safe)
