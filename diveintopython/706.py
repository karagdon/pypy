phonePattern = re.compile(r'^(\d{3}-(\d{3})-(\d{4})$')
phonePattern.search('800-555-1212').groups()
phonePattern.search('800-555-1212-1234)