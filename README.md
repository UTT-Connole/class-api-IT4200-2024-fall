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

If no commit message contains any information, then **default_bump** (currently set to minor) will be used. For major changes, using the exact given format including the line spacing is required. All others do not require any extra lines.

### Other commit options

* **feat**: A new feature
* **fix**: A bug fix
* **docs**: Documentation only changes
* **style**: Changes that do not affect the meaning of the code (white-space, formatting, missing
  semi-colons, etc)
* **refactor**: A code change that neither fixes a bug nor adds a feature
* **perf**: A code change that improves performance
* **test**: Adding missing or correcting existing tests
* **chore**: Changes to the build process or auxiliary tools and libraries such as documentation
  generation

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

### Available Endpoints
[**All Facts Endpoint**](#AllFacts) | [**Animal Endpoint**](#Animal) | [**Brainrot Endpoint**](#Brainrot) | [**Calculator Endpoint**](#Calculator) | [**Color Hexifier Endpoint**](#Hexifier) | [**Convert To Binary Endpoint**](#Binary) | [**Convert To Decimal Endpoint**](#Decimal) | [**Dad Jokes Endpoint**](#Dad) | [**Factorial Endpoint**](#Factorial) | [**Favorite Quote Endpoint**](#Favorite) | [**Fortune Cookie Endpoint**](#Fortune) | [**Fruit Info Endpoint**](#Fruit) | [**Generate Name Endpoint**](#Name) | [**Get Items Endpoint**](#Items) | [**Greeting Endpoint**](#Greeting) | [**Live Weather Endpoint**](#Weather) | [**Make an Endpoint**](#Make) | [**Marathon Facts Endpoint**](#Marathon) | [**MTG Mana Endpoint**](#MTG) | [**Motivation Endpoint**](#Motivation) | [**Netflix Show Endpoint**](#Netflix) | [**Photo Gallery Endpoint**](#Photo) | [**Pizza Toppings Endpoint**](#Pizza) | [**Pokefishing Endpoint**](#Pokefishing) | [**Power Endpoint**](#Power) | [**Random Fact Endpoint**](#Random) | [**Sports Facts Endpoint**](#Sports) | [**Study Fact Endpoint**](#Study) | [**Stoic Quotes Endpoint**](#Stoic) | [**Tennis Facts Endpoint**](#Tennis) | [**Travel Randomizer Endpoint**](#Travel) | [**Two Mana Combo Endpoint**](#Combo) | [**Version Endpoints**](#Version) 

- <a name="AllFacts">**All Facts Endpoint**</a>
  - **Endpoint**: 'GET /allFacts'
  - **Description**: The All Facts endpoint is a consolidated endpoint of facts about various topics. Just going to the /allFacts endpoint will return a random fact from any category. But specifying a category, like random, swimming, basketball, and wrestling will return a random fact about that category. EX: /allFacts?category=swimming
  - **Test File**: test_allfacts.py

- <a name="Animal">**Animal Endpoint**</a>
  - **Endpoint**: `GET /animalGuesser`
  - **Description**: The Animal Guesser will randomly guess an animal from a predefined list. If the user makes a guess, it checks the guess against the selected animal. If the guess is correct, it returns a success message. If the guess is incorrect, it returns a message with a hint that reveals the first letter of the animal. EX: /animalGuesser?guess=lion
  - **Test File**: test_animal.py

- <a name="Brainrot">**Brainrot Endpoint**</a>
  - **Endpoint**: `GET /brainrot`
  - **Description**: Add a new word to your vocabulary!
  - **Test File**: test_brainrot.py

- <a name="Calculator">**Calculator Endpoint**</a>
  - **Endpoint**: `GET /calc?x=<number>&y=<number>&op=<operator>` or `POST /calc`
  - **Description**: Use the following template to add, subtract, multiply, divide, or find the modulus of two numbers: `http://127.0.0.1:5000/calc?x=<number>&y=<number>&op=<operator>`. Replace `<number>` with the numbers you want to use, and replace `<operator>` with one of the following operations: `add`, `subtract`, `multiply`, `divide`, `mod`, `power`.
    
    For square, square root, or cube operations, use the following template: `http://127.0.0.1:5000/calc?x=<number>&op=<operator>`. Replace `<number>` with the number you want to use, and replace `<operator>` with either `square`, `sqrt`, or `cube`.

    For binary and decimal conversions, use the following template: `http://127.0.0.1:5000/calc?x=<number>&op=<operator>`. Replace `<number>` with the number you want to convert to binary or decimal with either `decimal` or `binary` respectively.

    You can also use an HTML form to interact with the calculator endpoint. The form allows you to input values and select operations, then submit the form to see the result.
  - **Important Notes**: 
    - The operators must be spelled exactly as shown above, or you will receive an error.
    - If any of the variables (`x`, `y`, or `op`) are missing (unless specified), you will receive an error.
    - If no parameters are provided, the endpoint will render an HTML form for input.
  - **Test File**: `test_calc.py`

- <a name="Hexifier">**Color Hexifier Endpoint**</a>
  - **Endpoint**: `GET /color?color=blue`
  - **Description**: Use the template to return a hex code of the color you want "http://127.0.0.1:5000/color?color=blue". Replace the "blue" at the end with any color of your choosing. If the color doesn't exist in the library, you will get an error.
  - **Test File**: test_color_hexifier.py

- <a name="Binary">**Convert To Binary Endpoint**</a>
  - **Endpoint**: `GET /convertToBinary?num=#&type=decimal`
  - **Description**: Go to http://127.0.0.1:5000/convertToBinary?num=#&type=decimal to get the binary convertion of any non-negative whole number!
   Don't even think about putting in floats, strings, or blanks. I have tested all of those cases and you will get appropriate responses for each!
  - **Test File**: test_binaryconvert.py

- <a name="Decimal">**Convert To Decimal Endpoint**</a>
  - **Endpoint**: `GET /convertToBinary?num=#&type=binary`
  - **Description**: Go to http://127.0.0.1:5000/convertToBinary?num=#&type=binary to get the decimal number of any binary number!
   Don't even think about putting in floats, strings, or blanks. I have tested all of those cases and you will get appropriate responses for each!
  - **Test File**: test_binaryconvert.py

- <a name="Dad">**Dad Jokes Endpoint**</a>
  - **Endpoint**: `GET /dadjoke`
  - **Description**: Go to this endpoint to laugh so hard you throw up! Now with even more hilarious Dad jokes!
  - **Test File**: test_dadjoke.py

- <a name="Factorial">**Factorial Endpoint**</a>
  - **Endpoint**: `GET /factorial?n=<value>`
  - **Description**: Go to http://127.0.0.1:5000/factorial?n=5. Replace the value of `n` with whatever number you want to see the factorial of. You can also add more factorials by doing `?n=5&n=4&n=3` and so on. Try larger numers as well!
  - **Test File**: test_factorial.py

- <a name="Favorite">**Favorite Quote Endpoint**</a>
  - **Endpoint**: `GET /favoritequote`
  - **Description**: Retrieve a favorite quote. Update: You can add your own favorite quote now too!!
  - **Test File**: test_favorite_quote.py

- <a name="Fortune">**Fortune Cookie Endpoint**</a>
  - **Endpoint**: `GET /fortune`
  - **Description**: Returns a random fortune in JSON format. You can specify the count parameter to request multiple fortunes.
  - **Test File**: test_getfortune.py

- <a name="Fruit">**Fruit Info Endpoint**</a>
  - **Endpoint**: `GET /fruitInfo?fruit=<fruit_name>`
  - **Description**: Navigate to `http://127.0.0.1:5000/fruitInfo?fruit=<fruit_name>`. Replace `<fruit_name>` with the name of the fruit you want information about. If the fruit isn't available, an error message will appear, and you will be given a list of available options. Choose a fruit from the options provided.
  - **Important Notes**:
    - Ensure the fruit name is spelled correctly to avoid errors.
    - If the fruit is not available, you will need to select from the provided options.

- <a name="Name">**Generate Name Endpoint**</a>
  - **Endpoint**: `GET /generateName`
  - **Description**: Get a randomly generated name. You can specify the length parameter to filter names by a specific length.
  - **Test File**: test_generate_name.py

- <a name="Items">**Get Items Endpoint**</a>
  - **Endpoint**: `GET /items/(integer)`
  - **Description**: Returns a list of items from items.json. Add an integer value (eg: /items/2) and it will only return a list of items where the price is greater than the value.
  - **Test File**: test_get_items.py test_items.py

- <a name="Greeting">**Greeting Endpoint**</a>
  - **Endpoint**: `GET /greet`
  - **Description**: Returns a welcome message with a name now!.
  - **Example Response:**
  ```json
    {
      "message": "Hello, Welcome to the API!"
    }
  ```
  - **Test File**: test_greet.py

- <a name="Weather">**Live Weather Endpoint**</a>
  - **Endpoint**: `GET /weather/city_name`
  - **Description**: Pick a city you want live weather in and put it after /weather/ in the URL. Example: http://127.0.0.1:5000/weather/Seattle. It should list the current weather conditions of the selected city.
  - **Test File**: test_weather.py

- <a name="Make">**Make an Endpoint**</a>
  - **Endpoint**: `GET /howToMakeEndpoint`
  - **Description**: Learn how to make an endpoint step by step!
  - **Test File**: test_howtomakeendpoint.py

- <a name="Marathon">**Marathon Facts Endpoint**</a>
  - **Endpoint**: `GET /marathonFacts`
  - **Description**: Learn a random fact about marathons! Now returns in plain text!
  - **Test File**: test_marathonfacts.py

- <a name="MTG">**MTG Mana Endpoint**</a>
  - **Endpoint**: `GET /MTGmana`
  - **Description**: Learn about what each mana color is known for! 🕊️🌊⚰️🔥🌿
  - **Test File**: test_onemana.py

- <a name="Motivation">**Motivation Endpoint**</a>
  - **Endpoint**: `GET /motivation`
  - **Description**: The /motivation endpoint provides a random motivational quote whenever accessed via a GET request. When a user sends a request to this endpoint, the app responds with one of five pre-defined motivational quotes, returned in JSON format.
  - **Test File**: test_motivation.py test_get_motivation.py

- <a name="Netflix">**Netflix Shows Endpoint**</a>
  - **Endpoint**: `GET /netflix-shows`
  - **Description**: Get a random fun fact about your favorite Netflix shows! Add your own shows and facts to the source code to see them on the endpoint! !NO Adult Content allowed!
  - **Test File**: `test_netflix_shows.py`

- <a name="Photo">**Photo Gallery Endpoint**</a>
  - **Endpoint**: `GET /photogallery`
  - **Description**: Go checkout the art gallery complied by yours truly. !Add your own images to the images folder to see them on the endpoint! !NO Adult Content allowed! 
  - **Test File**: test_photogallery.py

- <a name="Pizza">**Pizza Endpoint**</a>
  - **Endpoint**: `GET /pizza`
  - **Description**: This endpoint randomly generates a pizza, but sometimes you may get two pizzas instead of one! You can customize the cheese level by putting in a cheese query. Added the option to request a half-and-half pizza where each half of the pizza has a different set of toppings. The cheese level options are: Light Cheese, Regular Cheese, and Extra Cheese. Also recently added a new half half toppings feature.🍕🍕🍕
  - **Example request**: http://127.0.0.1:5000/pizza?cheese=Extra%20Cheese
  - **Test File**: test_pizza.py

- <a name="Soda">**Soda Endpoint**</a>
  - **Endpoint**: `GET /soda`
  - **Description**: This endpoint is used to choose a soda to go with your meal. 🥤🥤🥤
  - **Test File**: test_soda.py

- <a name="Pokefishing">**Pokefishing Endpoint**</a>
  - **Endpoint**: `GET /pokefishing`
  - **Description**: Catch a Magikarp! Refresh the page to cast your line again. Don't forget to reel it in!
  - **Test File**: test_pokefishing.py

- <a name="Power">**Power Endpoint**</a>
  - **Endpoint**: `GET /power?base=<value>&exp=<value>`
  - **Description**: Go to http://127.0.0.1:5000/power?base=2&exp=4. Replace the values of `base` and `exp` with whatever numbers you want.
- **Test File**: test_power.py

- <a name="Stoic">**Stoic Quotes Endpoint**</a>
  - **Endpoint**: `GET /quotes`
  - **Description**: Get a good random stoic quote from Plato and others.
  - **Test File**: test_quotes.py

- <a name="Study">**Study Facts Endpoint**</a>
  - **Endpoint**: `GET /study-facts`
  - **Description**: Retrieve random study tips and facts to enhance your learning experience! Add your own tips to the source code to see them on the endpoint! !NO Adult Content allowed!
  - **Test File**: `test_study_facts.py`

- <a name="Tennis">**Tennis Facts Endpoint**</a>
  - **Endpoint**: `GET /tennis_fact`
  - **Description**: 🎾 Learn fun facts about tennis!
  - **Test File**: test_tennisfacts_.py

- <a name="Travel">**Travel Randomizer Endpoint**</a>
  - **Endpoint**: `GET /travel`
  - **Description**: Be given a randomly chosen travel destination! This app will output a popular travel destination in "city, country" JSON format.
  - **Test File**: test_travel.py

- <a name="Combo">**Two Mana Combo Endpoint**</a>
  - **Endpoint**: `GET /twoManaCombos?color=your_color`
  - **Description**: Go to http://127.0.0.1:5000/twoManaCombos?color=your_color. Specify which color you want included in your deck by replacing it with your_color. ⚪🔵⚫🔴🟢
  - **Test File**: test_twomana.py
    
- <a name="Version">**Version Endpoints**</a>
  - **Endpoint**: `GET /version`
  - **Description**: Returns the latest version of the repository based on the latest tag.
  - **Test File**: test_version.py

  - **Endpoint**: `GET /current-version`
  - **Description**: Returns the current working version of the application based on the current commit.
  - **Test File**: test_version.py

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

```bash
#Soren Bybee: 
  Interests: Hiking, Rock Climbing, Mountain Biking, and Playing Video Games.
    - Add me up on Discord(sorenbybee) if your looking to play Rainbow Six Siege on PC.
    - If you need someone to approve your pull requests here is my number: (530-363-6531)
```

## Welcome to The IT4200 Art Gallery!


*Only KOOL Kids Will Get This Reference....

![alt text](https://github.com/UTT-Connole/class-api-IT4200-2024-fall/blob/main/images/gojo.jpg)


```bash
⬛⬛⬛⬛⬛🟩🟩⬛🟩🟩⬛⬛⬛
⬛⬛⬛⬛🟩🟩🟩🟩🟩🟩🟩⬛⬛ 
⬛⬛⬛🟩🟩⬜⬛⬜⬜⬛🟩⬛⬛ 
⬛⬛⬛🟩🟩🟩🟩🟩🟩🟩⬛⬛⬛
⬛⬛🟩🟩🟩🟩🟫🟫🟫🟫⬛⬛⬛
⬛⬛🟩🟩🟩🟩🟩🟩🟩⬛⬛⬛⬛
Pepe after forcing to main....

⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣠⠤⠤⠤⠤⠤⣄⣀⠀⠀⠀⠀⠀⢀⣀⡤⠤⠖⠒⠲⠦⠤⣄⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣤⡖⠒⠒⠶⢿⣤⣀⠀⠀⠀⠀⠀⠉⠙⠒⢦⣤⠖⠋⠁⠀⠀⠀⠀⠀⠀⠀⠀⠉⠓⢦⣄⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⣀⡴⠖⠛⠉⢉⣉⣉⠉⠓⠶⢤⣀⠉⠁⠀⠀⣀⣀⣤⣤⡤⠤⠤⣤⣤⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⢷⣄⠀⠀⠀⠀
⠀⠀⢠⣾⡵⠶⠛⠉⠉⠉⠉⠉⠉⠙⠳⢦⡈⠙⢶⣴⢋⣉⣠⠴⠶⠖⠚⠛⠓⠶⠦⣍⡙⠲⣦⣀⠀⠀⠀⠀⠀⠀⠀⠘⣿⣧⡀⠀⠀
⠀⣠⠟⢁⣤⣶⣶⣤⣀⠀⠀⠀⠀⠀⠀⠀⠙⢦⣠⣟⣋⣡⣤⣀⡀⠀⠀⠀⠀⠀⠀⠀⠙⠳⣄⠙⠳⣄⠀⠀⠀⠀⠀⠀⢿⣿⣷⡀⠀
⣼⠋⢰⣿⡿⠿⣿⠟⣿⡆⠀⠀⠀⠀⠀⠀⢀⡾⢹⣿⣿⣿⣿⣿⣿⣦⠀⠀⠀⠀⠀⠀⠀⠀⠈⠳⢤⣈⣀⠀⠀⠀⠀⠀⠘⣿⣿⣧⠀
⣧⠀⠸⣿⣧⣠⣾⢿⣿⡇⠀⠀⠀⠀⠀⠀⢸⠀⢸⣿⡋⠉⢹⣧⣨⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⣷⠀⠀⠀⠀⠀⣿⣿⣿⡇
⠘⢷⡀⠙⠻⠿⠿⠿⠋⠀⠀⠀⠀⠀⠀⣠⣾⡄⠘⣿⣷⣶⣾⣛⣿⣿⠁⠀⠀⠀⠀⠀⠀⠀⠀⣠⡶⠚⠋⠁⠀⠀⠀⠀⠀⢹⣿⣿⣷
⠀⠀⣽⠶⠦⣄⣀⣀⣀⣀⣀⣀⡴⠶⠛⠁⠀⠻⣆⡈⠛⠿⠿⠿⠛⠁⠀⠀⠀⠀⠀⠀⢀⣠⠞⠁⣠⡄⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⣿
⠀⠀⠈⠓⠦⢤⡤⣤⡤⠤⠤⠤⠶⠞⠀⠀⠀⠀⢻⣝⠶⢤⣄⣀⣀⣀⣀⣀⣀⣠⠤⠖⢋⣁⡴⠞⠉⠀⠀⠀⠀⠀⠀⠀⠀⠘⣿⣿⣿
⠀⠀⢠⡴⠖⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⠲⣤⣄⣉⣉⣉⣉⣭⣥⡤⠴⠒⠋⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿
⠀⠀⡇⣠⣤⡤⠤⠤⠦⠦⠴⠶⠶⣤⣤⣤⣤⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣿⣿⣿
⠀⢰⡟⠉⠀⠀⣀⣀⣤⣤⣤⣀⣀⣀⠀⠀⠀⠈⠉⠉⠛⠲⠶⢤⣄⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⣿
⠀⠀⠙⢧⡀⠸⣏⠀⠀⠀⠈⣿⣿⣿⣿⣿⣿⣿⣶⣦⣤⣤⣀⣀⠀⠈⠙⠳⠦⢤⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣸⣿⣿⣿
⠀⠀⠀⠀⢻⡄⠙⡇⠀⠀⠀⠸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣤⣀⠀⠈⠙⢳⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿
⠀⠀⠀⠀⠀⡇⠀⣧⠀⠀⠀⠀⠹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣄⠀⣸⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣿⣿⣿⣿
⠀⠀⠀⠀⢠⡇⠀⣧⠀⠀⠀⠀⠀⠻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⢀⡟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣾⣿⣿⣿⡏
⠀⠀⠀⠀⢸⡇⠀⡏⠀⠀⠀⠀⠀⠀⢻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠋⢁⣾⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢰⣿⣿⣿⡿⠁
⠀⠀⠀⠀⢸⠀⢰⡇⠀⠀⠀⠀⠀⠀⠈⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠋⠀⣠⡞⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣿⣿⣿⣿⠃⠀
⠀⠀⠀⠀⢸⠀⢸⠁⠀⠀⠀⠀⠀⠀⠀⠘⣿⣿⣿⣿⣿⣿⣿⣿⣿⠟⠁⢀⡼⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣿⣿⣿⣿⠃⠀⠀
⠀⠀⠀⠀⣿⠀⠸⣧⡀⠀⠀⠀⠀⠀⠀⠀⠸⣿⣿⣿⣿⣿⠟⠋⠀⢀⡴⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣼⣿⣿⣿⠟⠁⠀⠀⠀
⠀⠀⠀⠀⠹⡆⠀⠈⠙⠶⠶⢤⣄⣀⣀⣀⣤⡽⠿⠛⠉⠀⢀⣤⠞⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣴⣿⣿⣿⠟⠃⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠻⣷⢦⣤⣀⣀⣀⡀⠀⠀⢀⣀⣀⣀⡤⠶⠞⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣴⣾⣿⣿⡿⠟⠁⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠈⠳⣄⣀⠀⠈⠉⠉⠉⠉⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣠⣴⣾⣿⠿⠿⠛⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠙⠒⠒⠲⠦⠤⠤⠤⠤⠤⠤⠤⠤⠤⠤⠤⠶⠒⠒⠚⠛⠉⠉⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
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