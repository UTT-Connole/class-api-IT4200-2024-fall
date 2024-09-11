# Welcome to the class API!
We will be using this repo to create an API for our entire class. We will use Flask for this application and each member of the class will work within this single repo.

## How to install pip requirements

Make sure to run these commands before you run the Flask app. It will install all the requirements

```
pip install -r requirements.txt
```

## How to Test

Run 
```
pytest
``` 
or

```
ptw .
```

## How to run and get to your endpoint
To get to your endpoint go to the folder the app is in in a terminal (EX. class-api-IT4200-2024-fall) and run the command “python3 -m flask run”, this will start the server. From there navigate to the url and your desired endpoint “http://127.0.0.1:5000/calc” for calculator for example. 

## How to use Calculator Endpoint
Use this template to add or subtract two numbers together "http://127.0.0.1:5000/calc?x=#&y=#&op=#"
Replace the first two #'s with what ever numbers you would like! The last # is your operator
Current Operators: add, subtract, multiply, divide
If you leave one of the variables empty, you will get an error.

## How to use twoManaCombo Endpoint
Go to http://127.0.0.1:5000/twoManaCombos, get the combo name, and start building your next MTG deck!

## How to get to the stoic quotes Endpoint
Go to http://127.0.0.1:5000/quotes for a good random stoic quotes from Plato and others.

## How to use pizzaToppings Endpoint
Go to http://127.0.0.1:5000/pizzaToppings to finally decide what to put on your pizza!

## How to use Dad Jokes Endpoint
Go to http://127.0.0.1:5000/dadjoke to laugh so hard you throw up! Now with even more hilarious Dad jokes!
To run tests to verify functionality of the dadjokes endpoint enter "python -m pytest ./test/test_dadjoke.py".

## How to use the Travel Randomizer Endpoint
Go to http://127.0.0.1:5000/travel to be given a randomly chosen travel destination!

## How to use Marathon Facts Endpoint
Go to http://127.0.0.1:5000/marathonFacts to learn a random fact about marathons! 
Use the template to return a hex code of the color you want "http://127.0.0.1:5000/color?color=blue"
Replace the "blue" at the end with any color of your choosing.
If the color doesn't exist in the library, you will get an error.

## How to use the Quotes Endpoint

Open up the url to http://127.0.0.1:5000/quotes
Start reading people's favorite quotes!

## How to Use the Favorite Quote Endpoint

To retrieve a favorite quote, navigate to:

http://127.0.0.1:5000/favoritequote

## How to use Color Hexifier endpoint

Use the template to return a hex code of the color you want "http://127.0.0.1:5000/color?color=blue"
Replace the "blue" at the end with any color of your choosing.
If the color doesn't exist in the library, you will get an error.

## How to use Fortune Cookie Endpoint

This API has a `/fortune` endpoint that returns a random fortune in JSON format. 
# How to make an Endpoint
Go to http://127.0.0.1:5000/howToMakeEndpoint to learn how to make an endpoint.

## How to use the Random Fact Endpoint

To retrieve a random fact, navigate to http://127.0.0.1:5000/randomFact

## How to use the tennisFacts Endpoint

🎾 Go to http://127.0.0.1:5000/tennisFacts to learn fun facts about tennis!

## How to use the Pokefishing Endpoint
Go to http://127.0.0.1:5000/pokefishing to catch a Magikarp!

## How to use the randomWord Endpoint
Go to http://127.0.0.1:5000/randomWord to add a new word to your vocabulary!

## How to Rebase
 * step 1: STOP, just use merge thingy....

## Contributors:

* Laura Coulome
* Riker Evans
* Jace Barrett
* Donavan Franco
* Christian Bassilios
* Soren Bybee
* Keaton Hall
* Josh Beckstrand
* Dallin Hougaard
* Andres
* Travis Gunter
* Morgan Andrus
* Yomi Odubiyi
* Brayden Connole

## Add some Text art to make the repo more welcoming!
* ⬛⬛⬛⬛⬛🟩🟩⬛🟩🟩⬛⬛⬛
* ⬛⬛⬛⬛🟩🟩🟩🟩🟩🟩🟩⬛⬛ 
* ⬛⬛⬛🟩🟩⬜⬛⬜⬜⬛🟩⬛⬛ 
* ⬛⬛⬛🟩🟩🟩🟩🟩🟩🟩⬛⬛⬛
* ⬛⬛🟩🟩🟩🟩🟫🟫🟫🟫⬛⬛⬛
* ⬛⬛🟩🟩🟩🟩🟩🟩🟩⬛⬛⬛⬛
* Pepe after forcing to main....


Go Trailblazers! 🦬


⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣀⡀⠤⠤⢠⣄⣀⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠄⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⢀⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⡤⠖⠋⠉⠁⢀⣀⠀⠀⠀⠉⠙⠓⠶⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢻⣶⠀⠀⠀⠀⠀⠀
⠀⠀⠀⢀⣾⣿⣿⣷⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⡾⠋⠤⠤⠤⠤⠖⠛⠙⢿⣅⡀⠀⠀⠀⠀⠀⠙⠦⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡄⠀⠀⣿⡇⠀⠀⠀⠀⢀
⠀⠀⠀⣿⣿⣿⣿⣿⠀⠂⠀⠀⠀⠀⠀⢀⣾⣭⣤⣤⣤⣤⣄⣀⠀⣀⣀⢀⡟⢹⣶⣤⣀⡀⢀⣀⣠⣼⣳⣄⠀⠀⠀⠀⠀⠀⠀⣼⢻⣷⣦⣾⠀⠀⡄⠀⣠⠟
⠀⠀⠀⠀⠉⠛⠿⢿⣿⣷⣄⠀⠀⠀⢠⣾⠿⠛⠉⠙⠛⠻⠿⣿⠿⢟⣡⣾⡁⠀⣿⠻⠿⣿⠿⠿⣿⣿⠟⠻⣆⠀⠀⠀⠀⠀⣸⣿⣮⣿⣿⣿⡇⠘⢀⡼⠋⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠉⠻⣿⣶⣤⡴⣿⣿⡆⢚⣻⣿⣿⣟⡿⠛⠺⠟⠉⠈⠀⠘⠛⠀⠀⠰⢾⣿⣿⣿⣷⣦⡌⠷⣄⠀⢀⣼⣿⡿⠛⠛⠉⠉⣷⣴⠋⠁⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⣿⠀⢰⣿⣿⠱⣿⣋⣽⣿⣿⣝⣿⣾⣆⣠⡴⠶⠞⠷⣾⣆⣶⠾⣿⣶⡶⢮⣝⢿⡀⠘⢾⣿⠟⠁⠀⠀⠀⠀⠀⠸⣿⡄⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣽⠇⠀⠀⠉⠛⠿⣿⣿⡿⠿⠟⠛⠉⣩⡥⠤⠄⠀⠀⠈⠙⠻⢾⣿⣿⣟⣒⠋⠀⠁⠀⢸⡏⠀⠀⠀⠀⠀⠀⠀⠀⢿⣿⡄⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⡏⠀⠀⠀⠀⠀⠀⠀⢀⣴⠆⠀⢠⠞⠁⠀⠀⠀⢶⣆⡀⠀⠀⠀⠐⣬⡉⠉⠁⠀⠀⠀⠈⣷⡀⠀⠀⠀⠀⠀⠀⠀⠘⣧⠱⡄⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⠀⠀⠀⠀⠀⠀⠀⣠⣾⣿⣤⣶⣶⣤⣤⣀⡀⠀⠈⢻⣧⣄⣀⣤⣤⢸⣿⢶⣤⡀⠀⠀⠀⠘⣇⠀⠀⠀⠀⠀⠀⠀⠀⠹⡆⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⡇⠀⠀⠀⢀⣤⣶⠿⠟⠉⠀⠉⠉⠙⠿⠿⣿⣿⣿⣿⣾⣿⠿⠛⠋⠙⠻⣿⣷⣿⣿⣶⣄⡀⠀⢹⣆⠀⠀⣀⣀⠤⠞⠋⠀⣠⣴⠆
⠀⠀⠀⠀⠀⠀⠀⠀⠀⣼⠀⠀⠀⢰⣿⠋⣡⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠐⠋⠉⠙⢿⡀⠀⠀⠀⠀⠀⠛⢿⣿⣿⣽⣿⡆⠀⢹⡆⠉⠉⣀⣤⠴⠚⠋⠉⠀⠀
⠀⠀⠀⠀⠀⠀⠀⢀⣼⠏⠀⠀⠀⠘⠏⣸⣿⣴⣦⣤⣤⣤⣤⣤⣀⣷⣀⠀⠀⠀⠀⣘⣃⣀⣀⣀⣀⣀⣀⣈⣿⡏⢿⡇⠿⠀⣸⡷⠚⠋⠉⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⢀⡴⠛⣡⡆⠀⠀⠀⠀⠀⠈⢹⣿⣿⣿⣿⢻⣿⠉⢻⡿⠛⠿⣿⠿⠿⠿⣿⡟⠻⡿⢿⣿⣿⣿⡟⠷⢸⡇⠀⠀⣿⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⢀⣴⠋⣠⠾⠙⣷⠀⠀⠀⠀⠀⠀⠀⠘⢻⣿⣿⣿⣿⣶⣾⣇⣀⣀⣿⣄⣀⢀⣿⣅⣠⣧⣼⣿⠿⠙⠀⠀⠈⠇⠀⠀⣏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⡾⠉⡟⠁⠀⠀⠹⣦⠀⠀⠀⠀⠀⠀⠀⠀⠁⢹⣟⣿⣿⣿⣿⠹⣿⡝⢿⡟⠻⣿⣿⠻⡟⠛⠁⠀⠀⠀⠀⠀⠀⠀⢸⡏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⢸⡇⢰⠁⠀⠀⠀⠀⠙⣧⡀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠙⠻⠶⠶⢶⣶⣦⣤⣶⣶⣾⣶⣶⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣾⠇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⢸⠂⡿⠀⠀⠀⠀⠀⠀⠘⣷⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠻⣧⠀⠀⠀⠀⠀⠀⠀⠀⢀⡿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⣿⢸⠁⠀⠀⠀⠀⠀⠀⠀⠘⣿⣦⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠻⡆⠀⠀⠀⠀⠀⠀⢀⣼⠇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⢠⡇⡜⠀⠀⠀⠀⠀⠀⠀⠀⠀⢈⣧⠹⣦⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣦⣼⠇⠀⠀⠀⠀⠀⠀⠀⣠⠞⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⣿⡇⢁⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⠛⠀⢸⠙⠷⣦⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⣿⡄⠀⠀⠀⣀⣠⠴⠟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⢠⣿⠀⢸⡀⠀⠀⠀⠀⠀⠀⠀⠀⣾⠀⢠⡟⠀⠀⠀⠉⠛⠷⠦⣤⣤⣀⣀⣀⣀⣀⣀⣀⣈⠛⣦⣴⠞⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⢸⣿⠀⣼⣷⠀⠀⠀⠀⠀⠀⠀⢠⡇⠀⡾⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⠉⠉⠉⠉⠉⠉⢻⡁⠀⢧⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⢸⣿⠀⠈⣿⡀⠀⠀⠀⠀⠀⠀⣸⠇⢠⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢧⠀⢸⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠈⣿⣧⠀⠻⡇⠀⠀⠀⠀⠀⠀⢸⡀⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⡆⢸⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠘⣿⣧⡀⠀⠀⠀⠀⠀⠀⠐⢺⡿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⡞⢡⡟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠈⠻⠿⠁⠀⠀⠀⠀⠀⠀⢸⡇⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⠏⢠⠏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⡇⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣰⠋⢠⠏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣸⡿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣰⠋⢠⠏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⢀⠀⠀⠀⠀⢠⡤⠛⠛⠀⠈⣆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⡾⠁⠀⣏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠐⠿⢦⣤⣤⣤⣼⣀⣀⣤⣤⠴⠛⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣴⠋⠀⠀⠀⠉⠙⠒⠦⠤⠀⠀⠀⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⠛⠳⠶⠦⠤⣤⣄⣀⣀⠀⠠⠀⠀⢻⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⠉⠙⠛⠛⠛⠛⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
        *
       /O\
      /_O_\
     /O/_\O\
    /_O_|_O_\
   /O/_O_|_O_\
  /_O_|_O_|_O_\
 /O/_O_|_O_|_O_\
/_O_|_O_|_O_|_O_\
       |||
       |||
       |||
