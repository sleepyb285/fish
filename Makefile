ifneq (,$(wildcard ./.env))
    include .env
    export
endif


.PHONY:m
m:
	cd app && python manage.py makemigrations
.PHONY:dm

dm:
	cd app && python manage.py migrate

mdm: m dm

start:
	cd app && python manage.py runserver ${PORT}

freeze:
	cd app && pip freeze > r.txt