import history

import re
result = re.search(r"aza", "plaza")
print(result)
print(re.search(r"aza", "bazaar"))
print(re.search(r"aza", "maze"))
print(re.search(r"^x", "xenon"))
print(re.search(r"p.ng", "penguine"))
print(re.search(r"p.ng", "clapping"))
print(re.search(r"p.ng", "sponge"))
print(re.search(r"p.ng", "Pangaea", re.IGNORECASE))
#see the different results from the regular expressions
#NOTICE the IGNORECASE parameter in the last instance

history.save()
