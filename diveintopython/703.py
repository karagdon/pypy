# Checking for Thousands
import re
pattern = '^M?M?M?$'
re.search(pattern, 'M')
re.search(pattern, 'MM')
re.search(pattern, 'MMM')
re.search(pattern, 'MMMM')
re.search(pattern, '')

# Checking for Hundreds
import re
pattern = '^M?M?M?(CM|CD|D?C?C?C?)$'
re.search(pattern, 'MCM')
re.search(pattern, 'MD')
re.search(pattern, 'MMMCCC')
re.search(pattern, 'MCMC'
re.search(pattern, '')