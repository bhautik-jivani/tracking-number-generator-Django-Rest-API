# Tracking Number Generator - Backend

## Installation

create an `.env.local` file in root directory of project

Inside `.env.local` have to mention below details:

```
POSTGRES_DB=<db_name>
POSTGRES_USER=<db_username>
POSTGRES_PASSWORD=<db_password>
POSTGRES_HOST=postgres_db //docker service name
POSTGRES_PORT=5432

PGADMIN_DEFAULT_EMAIL=<custom_email>  // Replace with your preferred email
PGADMIN_DEFAULT_PASSWORD=<custom_password>
```
Run below code to start docker services
```
docker compose up -d
```

Create initial migrations and apply the migrations
```
docker exec -it tracking_number_generator_project_backend bash -c "python manage.py makemigrations"

docker exec -it tracking_number_generator_project_backend bash -c "python manage.py migrate"
```

Create static files for admin and rest framework
```
docker exec -it tracking_number_generator_project_backend bash -c "python manage.py collectstatic --no-input" 
```

Check Nginx Logs using below command
```
docker exec -it tracking_number_generator_project_backend bash -c "tail -f /var/log/nginx/access.log -n 500"

docker exec -it tracking_number_generator_project_backend bash -c "tail -f /var/log/nginx/error.log -n 500"
```

Check Gunicorn Logs using below command
```
docker exec -it tracking_number_generator_project_backend bash -c "tail -f /var/log/gunicorn/access.log -n 500"

docker exec -it tracking_number_generator_project_backend bash -c "tail -f /var/log/gunicorn/error.log -n 500"
```

Use attached postman collection to run apis

[Attachment](./Tracking_Number_Generator.json)