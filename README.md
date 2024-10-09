# Welcome to the class API!
We will be using this repo to create an API for our entire class. We will use Flask for this application and each member of the class will work within this single repo.

## Commit instructions for developers
A GitHub action has been created for automatic semantic version tagging using this repository: [Github tag with sematic versioning](https://github.com/marketplace/actions/github-tag-with-semantic-versioning). It uses [Angular Commit Message Conventions](https://github.com/angular/angular.js/blob/master/DEVELOPERS.md#-git-commit-guidelines) as commit message guidelines.

Here is an example of the release type that will be done based on a commit messages:

| Commit message                                                                                                                                                                                   | Release type  |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------- |
| `fix(pencil): stop graphite breaking when too much pressure applied`                                                                                                                             | Patch Release |
| `feat(pencil): add 'graphiteWidth' option`                                                                                                                                                       | Minor Release |
| `perf(pencil): remove graphiteWidth option`<br><br>`BREAKING CHANGE: The graphiteWidth option has been removed.`<br>`The default graphite width of 10mm is always used for performance reasons.` | Major Release |

If no commit message contains any information, then **default_bump** (currently set to minor) will be used.

## How to install pip requirements

Make sure to run these commands before you run the Flask app. It will install all the requirements

```
pip install -r requirements.txt
```

## Testing
### To run all the tests at once:
Run 
```
pytest
``` 
or

```
ptw .
```
### To run a test on a specific endpoint:
```
python3 -m pytest ./test/test_nameoffile.py
``` 

## API Endpoint Information
### How to run and get to your endpoint
To get to your endpoint go to the folder the app is in in a terminal (EX. class-api-IT4200-2024-fall) and run the following command:
```
python3 -m flask run
``` 
This will start the server. From there navigate to the url and your desired endpoint “http://127.0.0.1:5000/calc” for calculator for example. 

## Factorial Endpoint
Go to http://127.0.0.1:5000/factorial?n=5
But replace the value of n with whatever number you want to see the factorial of.

## Power Endpoint
Go to http://127.0.0.1:5000/power?base=2&exp=4
But replace the values of base and exp with whatever numbers you want.

## How to use fruit_info Endpoint
Navigate to http://127.0.0.1:5000/fruitInfo?fruit=apple
Replace "apple" from the end of the url with the fruit of your choice.
If the fruit isn't available an error message will come up and you will be given a list of options.
Choose a fruit from the options given.

## How to Use the Calculator Endpoint

Use the following template to add, subtract, multiply, or divide two numbers: 
`http://127.0.0.1:5000/calc?x=<number>&y=<number>&op=<operator>`
- Replace `<number>` with the numbers you want to use.
- Replace `<operator>` with one of the following operations: `add`, `subtract`, `multiply`, `divide`.

### Important Notes:
- The operators must be spelled exactly as shown above, or you will receive an error.
- If any of the variables (`x`, `y`, or `op`) are missing, you will receive an error.

## How to use the motivation Endpoint
The /motivation endpoint provides a random motivational quote whenever accessed via a GET request. When a user sends a request to this endpoint, the app responds with one of five pre-defined motivational quotes, returned in JSON format. This allows users to easily retrieve an encouraging message with every request, making it useful for applications or websites where inspiration or daily motivation is desired. Each request will randomly select and serve one quote from the list.

## how to use get motivation
The /motivation endpoint provides a random motivational quote whenever accessed via a GET request. When a user sends a request to this endpoint, the app responds with one of five pre-defined motivational quotes, returned in JSON format. This allows users to easily retrieve an encouraging message with every request, making it useful for applications or websites where inspiration or daily motivation is desired. Each request will randomly select and serve one quote from the list.

## How to use twoManaCombo Endpoint
Go to http://127.0.0.1:5000/twoManaCombos?color=your_color. Specifiy which color you want included in your deck by replacing it with your_color. If you don't want to specify, you can leave it blank. Then, get the combo name, and start building your next MTG deck! ⚪🔵⚫🔴🟢

## How to get to the stoic quotes Endpoint
Go to http://127.0.0.1:5000/quotes for a good random stoic quotes from Plato and others.

to test python3 -m unittest test_quotes.py 

## How to use pizzaToppings Endpoint
Go to http://127.0.0.1:5000/pizzaToppings to finally decide what sauce and toppings to put on your pizza 🍕!
To test if the code is working properly run:
"python -m pytest ./test/test_toppings.py"

## How to use Dad Jokes Endpoint
Go to http://127.0.0.1:5000/dadjoke to laugh so hard you throw up! Now with even more hilarious Dad jokes!
To run tests to verify functionality of the dadjokes endpoint enter "python -m pytest ./test/test_dadjoke.py".

## How to use the Travel Randomizer Endpoint
Go to http://127.0.0.1:5000/travel to be given a randomly chosen travel destination! 
This app will output a popular travel destination in "city, country" JSON format.
To test functionality, run this script:
python3 -m pytest ./test/test_travel.py

## Facts API
This Flask-based API provides random facts about swimming and wrestling.

Endpoints
Swimming Fact: GET /swimming_fact
Returns a random swimming fact.
Wrestling Fact: GET /wrestling_fact
Returns a random wrestling fact.



## How to use Marathon Facts Endpoint
Go to http://127.0.0.1:5000/marathonFacts to learn a random fact about marathons! 
Use the template to return a hex code of the color you want "http://127.0.0.1:5000/color?color=blue"
Replace the "blue" at the end with any color of your choosing.
If the color doesn't exist in the library, you will get an error.

### /greet
- **Method:** GET
- **Description:** Returns a welcome message.
- **Example Response:**
  ```json
  {
    "message": "Hello, Welcome to the API!"
  }

## How to use the Quotes Endpoint

Open up the url to http://127.0.0.1:5000/quotes
Start reading people's favorite quotes!

## How to Use the Favorite Quote Endpoint
=======
### Available Endpoints

- **Basketball Facts Endpoint**
  - **Endpoint**: `GET /basketballFacts`
  - **Description**: Provides random basketball facts through a simple GET endpoint, returning a JSON response with each request. It includes unit tests to ensure the endpoint functions correctly, providing a reliable source of basketball trivia.
  - **Test File**: test_basketball_fact.py

- **Brainrot Endpoint**
  - **Endpoint**: `GET /brainrot`
  - **Description**: Add a new word to your vocabulary!
  - **Test File**: test_brainrot.py

- **Calculator Endpoint**
  - **Endpoint**: `GET /calc?x=<number>&y=<number>&op=<operator>`
  - **Description**: Use the following template to add, subtract, multiply, or divide two numbers: `http://127.0.0.1:5000/calc?x=<number>&y=<number>&op=<operator>`. Replace `<number>` with the numbers you want to use, and replace `<operator>` with one of the following operations: `add`, `subtract`, `multiply`, `divide`.
    
    For square or square root operations, use the following template: `http://127.0.0.1:5000/calc?x=<number>&op=<operator>`. Replace `<number>` with the number you want to use, and replace `<operator>` with either `square` or `sqrt`.
  - **Important Notes**: 
    - The operators must be spelled exactly as shown above, or you will receive an error.
    - If any of the variables (`x`, `y`, or `op`) are missing (Unless specified), you will receive an error.
    - You can also use an HTML form to interact with the calculator endpoint. The form allows you to input values and select operations, then submit the form to see the result. 
  - **Test File**: test_calc.py


- **Color Hexifier Endpoint**
  - **Endpoint**: `GET /color?color=blue`
  - **Description**: Use the template to return a hex code of the color you want "http://127.0.0.1:5000/color?color=blue". Replace the "blue" at the end with any color of your choosing. If the color doesn't exist in the library, you will get an error.
  - **Test File**: test_color_hexifier.py

- **Convert To Binary Endpoint**
  - **Endpoint**: `GET /convertToBinary?num=#`
  - **Description**: Go to http://127.0.0.1:5000/convertToBinary?num=# and replace the # with any non-negative whole number! Don't even think about putting in floats, strings, or blanks. I have tested all of those cases and you will get appropriate responses for each!
  - **Test File**: test_binaryconvert.py

- **Dad Jokes Endpoint**
  - **Endpoint**: `GET /dadjoke`
  - **Description**: Go to this endpoint to laugh so hard you throw up! Now with even more hilarious Dad jokes!
  - **Test File**: test_dadjoke.py

- **Factorial Endpoint**
  - **Endpoint**: `GET /factorial?n=<value>`
  - **Description**: Go to http://127.0.0.1:5000/factorial?n=5. Replace the value of `n` with whatever number you want to see the factorial of. You can also add more factorials by doing `?n=5&n=4&n=3` and so on.
  - **Test File**: test_factorial.py

- **Favorite Quote Endpoint**
  - **Endpoint**: `GET /favoritequote`
  - **Description**: Retrieve a favorite quote. Update: You can add your own favorite quote now too!!
  - **Test File**: test_favorite_quote.py

- **AnimalEndpoint**
  - **Endpoint**: `GET /animalGuesser`
  - **Description**: The Animal Guesser API provides a simple way to randomly guess an animal from a predefined list. 
  - **Test File**: test_animal.py

- **Fortune Cookie Endpoint**
  - **Endpoint**: `GET /fortune`
  - **Description**: Returns a random fortune in JSON format.
  - **Test File**: test_fortune.py

- **Fruit Info Endpoint**
  - **Endpoint**: `GET /fruitInfo?fruit=<fruit_name>`
  - **Description**: Navigate to `http://127.0.0.1:5000/fruitInfo?fruit=<fruit_name>`. Replace `<fruit_name>` with the name of the fruit you want information about. If the fruit isn't available, an error message will appear, and you will be given a list of available options. Choose a fruit from the options provided.
  - **Important Notes**:
    - Ensure the fruit name is spelled correctly to avoid errors.
    - If the fruit is not available, you will need to select from the provided options.

- **Generate Name Endpoint**
  - **Endpoint**: `GET /randomName`
  - **Description**: Get a randomly generated name.
  - **Test File**: test_generate_name.py

- **Get Items Endpoint**
  - **Endpoint**: `GET /items`
  - **Description**: Returns a list of items. Optionally filter items by a minimum price. Query parameter `min_price` filters items that have a price greater than or equal to the specified value (default is 0).
  - **Test File**: test_get_items.py

- **Greeting Endpoint**
  - **Endpoint**: `GET /greet`
  - **Description**: Returns a welcome message.
  - **Example Response:**
  ```json
    {
      "message": "Hello, Welcome to the API!"
    }
  ```
  - **Test File**: test_greet.py

- **Live Weather Endpoint**
  - **Endpoint**: `GET /weather/city_name`
  - **Description**: Pick a city you want live weather in and put it after /weather/ in the URL. Example: http://127.0.0.1:5000/weather/Seattle. It should list the current weather conditions of the selected city.
  - **Test File**: test_weather.py

- **Make an Endpoint**
  - **Endpoint**: `GET /howToMakeEndpoint`
  - **Description**: Learn how to make an endpoint.
  - **Test File**: test_howtomakeendpoint.py

- **Marathon Facts Endpoint**
  - **Endpoint**: `GET /marathonFacts`
  - **Description**: Learn a random fact about marathons!
  - **Test File**: test_marathonfacts.py

- **MTG Mana Endpoint**
  - **Endpoint**: `GET /MTGmana`
  - **Description**: Learn about what each mana color is known for! 🕊️🌊⚰️🔥🌿
  - **Test File**: test_onemana.py

- **Motivation Endpoint**
  - **Endpoint**: `GET /motivation`
  - **Description**: The /motivation endpoint provides a random motivational quote whenever accessed via a GET request. When a user sends a request to this endpoint, the app responds with one of five pre-defined motivational quotes, returned in JSON format.
  - **Test File**: test_motivation.py

- **Pizza Toppings Endpoint**
  - **Endpoint**: `GET /pizzaToppings`
  - **Description**: Too lazy to think of what pizza to order? Get your crust, sauce and toppings randomly chosen. 
  - **Test File**: test_toppings.py

- **Pokefishing Endpoint**
  - **Endpoint**: `GET /pokefishing`
  - **Description**: Catch a Magikarp!
  - **Test File**: test_pokefishing.py

- **Power Endpoint**
  - **Endpoint**: `GET /power?base=<value>&exp=<value>`
  - **Description**: Go to http://127.0.0.1:5000/power?base=2&exp=4. Replace the values of `base` and `exp` with whatever numbers you want.
- **Test File**: test_power.py

- **Random Fact Endpoint**
  - **Endpoint**: `GET /randomFact`
  - **Description**: Retrieve a random fact!
  - **Test File**: test_randomFact.py

- **Sports Facts Endpoint**
  - **Endpoint**: `GET /sports_fact`
  - **Description**: Learn fun facts about various sports! Use the 'category' parameter to filter the facts! 🏅
  - **Test File**: test_sportsfacts.py

- **Stoic Quotes Endpoint**
  - **Endpoint**: `GET /quotes`
  - **Description**: Get a good random stoic quote from Plato and others.
  - **Test File**: test_quotes.py

- **Tennis Facts Endpoint**
  - **Endpoint**: `GET /tennisFacts`
  - **Description**: 🎾 Learn fun facts about tennis!
  - **Test File**: test_tennisfacts_.py

- **Travel Randomizer Endpoint**
  - **Endpoint**: `GET /travel`
  - **Description**: Be given a randomly chosen travel destination! This app will output a popular travel destination in "city, country" JSON format.
  - **Test File**: test_travel.py

- **Two Mana Combo Endpoint**
  - **Endpoint**: `GET /twoManaCombos?color=your_color`
  - **Description**: Go to http://127.0.0.1:5000/twoManaCombos?color=your_color. Specify which color you want included in your deck by replacing it with your_color. ⚪🔵⚫🔴🟢
  - **Test File**: test_twomana.py


## Contributors

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

## About The Contributors


## how to use basketball facts
This Flask-based API provides random basketball facts through a simple GET endpoint, returning a JSON response with each request. It includes unit tests to ensure the endpoint functions correctly, providing a reliable source of basketball trivia.

## How to use the Pokefishing Endpoint
Go to http://127.0.0.1:5000/pokefishing to catch a Magikarp!


```bash
#Soren Bybee: 
  Interests: Hiking, Rock Climbing, Mountain Biking, and Playing Video Games.
    - Add me up on Discord(sorenbybee) if your looking to play Rainbow Six Siege on PC.
    - If you need someone to approve your pull requests here is my number: (530-363-6531)
```


## Welcome to The IT4200 Art Gallery!


*Only KOOL Kids Will Get This Reference....

![alt text](https://github.com/UTT-Connole/class-api-IT4200-2024-fall/blob/main/images/git%20hw%20edited.png)


```bash
⬛⬛⬛⬛⬛🟩🟩⬛🟩🟩⬛⬛⬛
⬛⬛⬛⬛🟩🟩🟩🟩🟩🟩🟩⬛⬛ 
⬛⬛⬛🟩🟩⬜⬛⬜⬜⬛🟩⬛⬛ 
⬛⬛⬛🟩🟩🟩🟩🟩🟩🟩⬛⬛⬛
⬛⬛🟩🟩🟩🟩🟫🟫🟫🟫⬛⬛⬛
⬛⬛🟩🟩🟩🟩🟩🟩🟩⬛⬛⬛⬛
Pepe after forcing to main....


Go Trailblazers! 🦬
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
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
(;-;) lifu

```