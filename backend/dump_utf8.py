import os
import django
import io
from django.core.management import call_command


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "portfolio.settings") 

django.setup()


with io.open("data.json", "w", encoding="utf-8") as f:
    call_command("dumpdata", "--natural-primary", "--natural-foreign", "--indent", "4", stdout=f)

print("Dumped data.json in UTF-8 successfully.")
