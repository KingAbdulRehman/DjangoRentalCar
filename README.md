easy way way to run this project 

First of all verify you already installed python latest version, if you are not installed then visit: https://www.python.org/downloads/

Then open folder directory and just type cmd in file explorer, in cmd type

First command:
pip install django
// Its install django for the project

Second command:
python manage.py makemigrations
// This command sync all db relations, tables, columns and etc,

Third command:
python manage.py migrate
// This command execute your all db changes 

Fourth command:
python manage.py runserver
// This command start your project and give ip just copy and run it in browser
