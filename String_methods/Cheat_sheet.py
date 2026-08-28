# notes/cheatsheet.md content

# CASE METHODS
.upper()          → HELLO
.lower()          → hello
.capitalize()     → Hello world
.title()          → Hello World
.swapcase()       → hELLO wORLD
.casefold()       → aggressive lowercase

# SEARCH METHODS
.find()           → index or -1
.rfind()          → right side find
.index()          → index or ValueError
.count()          → number of occurrences
.startswith()     → True/False
.endswith()       → True/False

# STRIP METHODS
.strip()          → remove both sides
.lstrip()         → remove left
.rstrip()         → remove right

# REPLACE METHODS
.replace()        → replace substring
.removeprefix()   → remove from start
.removesuffix()   → remove from end

# SPLIT & JOIN
.split()          → string to list
.rsplit()         → split from right
.splitlines()     → split by newlines
.join()           → list to string

# VALIDATION
.isalpha()        → only letters
.isdigit()        → only digits
.isnumeric()      → numeric chars
.isalnum()        → letters + numbers
.isspace()        → only whitespace
.isupper()        → all uppercase
.islower()        → all lowercase
.istitle()        → title case
.isidentifier()   → valid variable name

# ALIGNMENT
.center()         → center align
.ljust()          → left align
.rjust()          → right align
.zfill()          → zero padding

# FORMAT
.format()         → string formatting
.format_map()     → format with dict
.encode()         → string to bytes

# OTHER
.maketrans()      → create mapping table
.translate()      → apply mapping
.expandtabs()     → replace tabs
