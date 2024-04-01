import sys
from pathlib import Path
sys.path.append(Path(__file__).resolve().parent.parent.__str__())
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','locallibrary.settings')
import django
django.setup()  

from catalog.models import MyModelName 
        # Create a new record using the model's constructor.
record = MyModelName(my_field_name="Instance #1")

# Save the object into the database.
record.save()


# Access model field values using Python attributes.
print(record.id) # should return 1 for the first record.
print(record.my_field_name) # should print 'Instance #1'

# Change record by modifying the fields, then calling save().
record.my_field_name = "New Instance Name"
record.save()
  