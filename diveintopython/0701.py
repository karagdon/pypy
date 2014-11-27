s = '100 NORTH MAIN ROAD'
s.replace('ROAD', 'RD.')
s = '100 NORTH BROAD ROAD'
s.replace('ROAD', 'RD.')
s[:-4] + s[-4:].replace('ROAD', 'RD.')
import re
re.sub('ROAD$', 'RD.', s)