# Game-project

The project ended up as a small game. Launching the application leads the user to a main menu. The main menu consists of a list of highscores and 3 buttons. The buttons allow the user to start the game, exit the application or edit the game configuration. Starting the game, the player can control a blue square on the screen. Differently sized and colored squares enter the screen from left and right. The objective of the player is to run into squares smaller than oneself in order to grow larger. Running into larger squares, however, leads to a game over.

[specification](https://github.com/TrollRoll2/ot-harjoitustyo/blob/main/documentation/specification.md)

[time tracking](https://github.com/TrollRoll2/ot-harjoitustyo/blob/main/documentation/timetracking.md)

[changelog](https://github.com/TrollRoll2/ot-harjoitustyo/blob/main/documentation/changelog.md)

In order to run the project, the user must first clone the project. After cloning the project, create a .env file inside the folder src/db and insert the following:
```
DATABASE_URL=<YOUR PSQL URL>
SECRET_KEY=<YOUR SECRET KEY>
```
Where you replace <YOUR PSQL URL> with your databases url, and <YOUR SECRET KEY> with a secret key that you have generated.
After this you will have to run poetry install. Enter a virtual environment with poetry shell. Run src/db/db_helper.py to set up the database.
The game can be run with the command poetry run invoke start, or by running the file src/index.py. Running the tests can be done with poetry run invoke coverage, and the report can be created with poetry run invoke coverage-report.
Linting is accomplished with poetry run invoke lint.
