import pakiet
from pakiet import fun
import pakiet.fun as pk

# trzy niezależne sposoby
# po dodaniu w pliku __init__.py
pakiet.powitanie()  # Cześć
fun.powitanie()
pk.powitanie()
# pakiet.info()  # AttributeError: module 'pakiet' has no attribute 'info'
fun.info()
pk.info()
# Cześć
# Cześć
# Cześć
# Jestem pakietem
# Jestem pakietem
