#How to install Postgres for Django: https://djangocentral.com/using-postgresql-with-django/
#Portable postgres: https://garethflowers.dev/postgresql-portable/

#SQL to execute in PostGres: 
#   CREATE DATABASE itea_crossfit_project_db1;
#   CREATE USER django_user WITH ENCRYPTED PASSWORD 'PASS_IS_IN_.env_file';
#   ALTER ROLE django_user SET client_encoding TO 'utf8';
#   ALTER ROLE django_user SET default_transaction_isolation TO 'read committed';
#   ALTER ROLE django_user SET timezone TO 'EET';
#   GRANT ALL PRIVILEGES ON DATABASE itea_crossfit_project_db1 TO django_user;
