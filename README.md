# Game-project

The project is a small game made with pygame that first enters the user into a main menu. Pressing the play button in this menu allows the user to control a character. The character can move across the playing field and gather points by collecting sprites, which will increment the user's points. The points are visible to the user and are inserted into a database when the game window is closed.

[specification](https://github.com/TrollRoll2/ot-harjoitustyo/blob/main/documentation/specification.md)

[time tracking](https://github.com/TrollRoll2/ot-harjoitustyo/blob/main/documentation/timetracking.md)

[changelog](https://github.com/TrollRoll2/ot-harjoitustyo/blob/main/documentation/changelog.md)

In order to run the project, the user must first clone the project. After cloning the project, create a .env file inside the folder src/db and insert the following:
```
DATABASE_URL=<YOUR PSQL URL>
SECRET_KEY=<YOUR SECRET KEY>
```
Where you replace <YOUR PSQL URL> with your databases url, and <YOUR SECRET KEY> with a secret key that you have generated.
After this you will have to run poetry install. Enter a virtual environment with poetry shell.
The game can be run  with the command poetry run invoke start, or by running the file src/index.py. Running the tests can be done with poetry run invoke coverage, and the report can be created with poetry run invoke coverage-report.
Linting is accomplished with poetry run invoke lint.
