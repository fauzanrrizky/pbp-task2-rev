release: sh -c 'python manage.py makemigrations && python manage.py migrate && python manage.py loaddata initial_mywatchlist_data.json'
web: gunicorn project_django.wsgi --log-file -