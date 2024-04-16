# evalXai

This web application provides users with ML models and datasets, and evaluates their XAI methods.

# Requirements:

The only requirement needed for this project is docker, and enough local storage (~10 Gb).

# How to run the platform:

### building images

inside the folder containing the repository, please run the following command:

`docker compose up`

The first time you run it, it might take a few minutes to finish installing all dependencies and building the images.

### running Django migrations

When connecting to the database for the first time (e.g. after the docker volumes are created for the
first time or deleted), you will need to create and run the migration script.
For this step, you will need to know the name of your backend container name, in order to execute commands inside it.
After running `docker ps`, copy the name of the container with image `{root_folder}-backend`.
If your root folder is called "evalXai", and you used docker compose to instantiate all containers, you can use the
same container names we used in the default commands below.

`docker exec -it evalxai-backend-1 python manage.py makemigrations`

`docker exec -it evalxai-backend-1 python manage.py migrate`

Alternatively, if you have the docker desktop app, you can follow these steps:

- On the left sidebar, go to the containers section.
- click on the three dots on the right side.
- click on "open in terminal"
- run the following commands:

  `python manage.py makemigrations`

  `python manage.py migrate`

### You're done! You can now access the platform at: localhost:3000


