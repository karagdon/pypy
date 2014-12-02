phonePattern = re.compile(r'^(\d{3}-(\d{3})-(\d{4})$')
phonePattern.search('800-555-1212').groups()
phonePattern.search('800-555-1212-1234)

phonePattern = re.compile(r'^(\d{3})-(\d{4})-(\d+)$)
phonePattern.search('800-555-1212-1234').groups()
phonePattern.search('800 555 1212 1234')
phonePattern.search('800-555-1212')

phonePattern = re.compile(r'^(\d{3}-(\d{3})-(\d+)$')
phonePattern.search('800-555-1212-1234').groups()
phonePattern.search('800 555 1212 1234')
phonePattern.search('800-555-1212)