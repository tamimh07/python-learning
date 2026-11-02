# Week 2: f-strings in detail

site = 'Karnaphuli River'
ph = 7.4
temp_c = 29
samples = 12
conc = 0.000345
x = 3.14159265

# 1. Without and with f
print('Site is {site}')
print(f'Site is {site}')

# 2. Expressions inside the braces
print(f'{temp_c} C = {temp_c * 9 / 5 + 32} F')
print(f'{samples} samples, double is {samples * 2}')
print(f'{site.upper()} has {len(site)} letters')

# 3. Number formats
print(f'{x:.2f}')
print(f'{x:.0f}')
print(f'{x:.4f}')
print(f'{1234567:,}')
print(f'{0.256:.1%}')
print(f'{conc:.2e}')
print(f'Site {7:03d}')

# 4. Width and alignment
print(f' |{site:<20}|')
print(f' |{site:>20}|')
print(f' |{site:^20}|')
print(f' |{ph:8.2f}|')

# 5. A small table
print(f'{"Site":<10}{"pH":>6}{"DO":>8}')
print(f'{"Site A":<10}{7.2:>6.1f}{6.1:>8.1f}')
print(f'{"Site B":<10}{6.4:>6.1f}{4.8:8.1f}')

# 6. Debug shorcut: name and value together
print(f'{ph=}')

# 7. Dictionary values (use different quote types inside and outside)
sample = {'site': 'Karnaphuli River', 'ph': 7.4}
print(f"{sample['site']} has pH {sample['ph']}")

# 8. Printing literal braces
print(f'Use {{ph}} for the variable, value {ph}')

# Remainder (%) and whole-number division (//)
rain_mm = 135
print(rain_mm // 25, rain_mm % 25)

minutes = 135
print(f'{minutes} minutes = {minutes //60} h {minutes % 60} min')

days = 45
print(f'{days}days = {days // 7} weeks {days % 7} days')

print (10 % 2, 11 % 2)
