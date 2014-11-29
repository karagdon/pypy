import re
pattern = ^M?M?M?$'
re.search(pattern, 'M')
pattern = '^M?M?M?$'
re.search(pattern, 'MM')
pattern = '^M?M?M?$'
re.search(pattern, 'MMM')
re.search(pattern, 'MMMM')

pattern = '^M{0,3}$'
re.search(pattern, 'M')
re.search(pattern, 'MM')
re.search(pattern, 'MMM')
re.search(pattern, 'MMMM')

pattern = '^M?M?M?M?(CM|CD|D?C?C?C?)(XC|XL|L?X?X?X?)$'

re.search(pattern, 'MCMXL')
re.search(pattern, 'MCML')
re.search(pattern, 'MCMLX')
re.search(pattern, 'MCMLXXX')
re.search(pattern, 'MCMLXXXX')

pattern = '^M?M?M?M?(CM|CD|D?C?C?C?)(XC|XL|L?X?X?X?)(IX|IV|V?I?I?I?)$'