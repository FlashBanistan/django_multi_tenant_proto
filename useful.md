Database Setup:
- run "python manage.py sync_schemas"
- run "python manage.py migrate_schemas"

Create A Tenant:
- first create a public tenant, run, "tenant = Client(domain_url='localhost', schema_name='public', name='public')"
  - tenant.save()
- run "tenant = Client(domain_url='aaron.localhost', schema_name='aaron_schema', name='aaron')"
  - tenant.save()

Create A Superuser On Specific Tenant:
- run "python manage.py createsuperuser --username=aaron --schema=aaron_schema"

Useful Shell Commands:
- to perform a query on a specific schema run the following:
  - "from django.db import connection"
  - "connection.set_schema('schema_name')"
  - run the query like normal i.e., 'users = User.objects.all()'
