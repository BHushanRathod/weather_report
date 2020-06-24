# weather_report

Get weather details using openweather.com api's

Source Code:
------------

`<https://github.com/BHushanRathod/weather_report>`_


Installation and Usage
======================

Download the souce code::
       
    $ git clone https://github.com/BHushanRathod/weather_report.git
    $ cd weather_report
   
Activate the Virtual Environment::

    source ~/path/to/ve/bin/activate

Install the Dependencies::

    pip install -r requirements.txt

Run Migrations (Not required)::
    
    ./manage.py makemigrations
    ./manage.py migrate
    
Run TestCases::

    python manage.py test
        
Steps to follow:
    
    * Run python3 weather.py.
    * Select the option from menu. 1 for selecting city from databse. 2 for manually entering lat, long.
    * Code will display the current weather for specified city or lat, long
