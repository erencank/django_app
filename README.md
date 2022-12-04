# Scores App

## How to setup

1. Run `docker-compose up --build -d` to build and start the docker image.
2. Get in the container with `docker-compose exec django bash`.
3. Create a new superuser with `python src/manage.py createsuperuser`
4. Login the admin panel at `localhost:8000/admin`

## How to use

1. In the login panel create a new user under the `scores.users` section.
2. Add scores in the `scores.scores` section. As only admins can do that.
3. Navigate to `localhost:8000/scores` and fill in start and end date in format `yyyy-mm-dd`.
4. Enjoy the results.