# Welcome to the class API!
We will be using this repo to create an API for our entire class. We will use Flask for this application and each member of the class will work within this single repo.

## Commit instructions for developers
A GitHub action has been created for automatic semantic version tagging using this repository: [Github tag with semantic versioning](https://github.com/marketplace/actions/github-tag-with-semantic-versioning). It uses [semantic-release](https://github.com/semantic-release/semantic-release)  as commit message guidelines.

Here is an example of the release type that will be done based on a commit messages:

| Commit message                                                                                                                                                                                   | Release type                                                                                                    |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | --------------------------------------------------------------------------------------------------------------- |
| `fix(pencil): stop graphite breaking when too much pressure applied`                                                                                                                             | Patch Release                                                                                           |
| `feat(pencil): add 'graphiteWidth' option`                                                                                                                                                       | Minor Release                                                                                       |
| `perf(pencil): remove graphiteWidth option`<br><br>`BREAKING CHANGE: The graphiteWidth option has been removed.`<br>`The default graphite width of 10mm is always used for performance reasons.` | Major Release <br /> (Note that the `BREAKING CHANGE: ` token must be in the footer of the commit) |

If no commit message contains any information, then **default_bump** (currently set to minor) will be used. 

## How to install pip requirements

Make sure to run these commands before you run the Flask app. It will install all the requirements

```
pip install -r requirements.txt
```

## Running the DB Locally

Run:

```
docker-compose up
```


### Seeding the Database

First, ensure you have the aws cli installed:

```
aws --version
```

If you don't have it installed: [AWS CLI Installation Guide](https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html#getting-started-install-instructions)


Run the seed bash script

```
bash dynamo/seed.bash
```
If you have issues running the bash script try the python script

```
python dynamo/seed.py
```

If everythin ran correctly, you should be able to go to the `/db_test` endpoint and see the seed data returned there.



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
[**All Facts Endpoint**](#AllFacts) | [**Animal Endpoint**](#Animal) | [**Automobiles Endpoint**] | (#Automobiles) [**Brainrot Endpoint**](#Brainrot) | [**Calculator Endpoint**](#Calculator) | [**Color Hexifier Endpoint**](#Hexifier) | [**Continents Endpoint**](#Continents) | [**Convert To Binary Endpoint**](#Binary) | [**Convert To Decimal Endpoint**](#Decimal) | [**Dad Jokes Endpoint**](#Dad) | [**Factorial Endpoint**](#Factorial) | [**Favorite Quote Endpoint**](#Favorite) | [**Fortune Cookie Endpoint**](#Fortune) | [**Fruit Info Endpoint**](#Fruit) | [**Generate Name Endpoint**](#Name) | [**Get Items Endpoint**](#Items) | [**Greeting Endpoint**](#Greeting) | [**Live Weather Endpoint**](#Weather) | [**Make an Endpoint**](#Make) | [**Marathon Facts Endpoint**](#Marathon) | [**MTG Mana Endpoint**](#MTG) | [**Motivation Endpoint**](#Motivation) | [**Multiply Endpoint**](#multiply) | [**Netflix Show Endpoint**](#Netflix) | [**Photo Gallery Endpoint**](#Photo) | [**Pizza Toppings Endpoint**](#Pizza) | [**Pokefishing Endpoint**](#Pokefishing) | [**Power Endpoint**](#Power) | [**Random Fact Endpoint**](#Random) | [**Sports Facts Endpoint**](#Sports) | [**Study Fact Endpoint**](#Study) | [**Stoic Quotes Endpoint**](#Stoic) | [**Tennis Facts Endpoint**](#Tennis) | [**Travel Randomizer Endpoint**](#Travel) | [**Two Mana Combo Endpoint**](#Combo) | [**Version Endpoints**](#Version) | [**Readme Endpoint**](#Readme) 

- <a name="AllFacts">**All Facts Endpoint**</a>
  - **Endpoint**: 'GET /allFacts'
  - **Description**: The All Facts endpoint is a consolidated endpoint of facts about various topics. Going to the /allFacts endpoint will show you which categories you can specify. Specifying a category (i.e random, tennis, swimming, basketball, popularity, studying or wrestling) will return a random fact about that category. EX: /allFacts?category=swimming 🌈🎾🏊🏀💅📚🤼. Add your own favorite facts/tips to the source code to see them on the endpoint! !NO Adult Content allowed! 
  - **Test File**: test_allfacts.py

- <a name="Animal">**Animal Endpoint**</a>
  - **Endpoint**: `GET /animalGuesser`
  - **Description**: The Animal Guesser will randomly guess an animal from a predefined list. If the user makes a guess, it checks the guess against the selected animal. If the guess is correct, it returns a success message. If the guess is incorrect, it returns a message with a hint that reveals the first letter of the animal. You will only get 5 guesses and it will be game over! This endpoint now returns an html page.
  - **Test File**: test_animal.py

- <a name="Automobiles">**Automobiles Endpoint**</a>
- **Endpoint**: `GET /automobiles`
- **Description**: Returns a list of automobiles in JSON format. You can filter the results using query parameters like `make`, `model`, or `year`.
- **Test File**: `test_handle_automobiles.py`


- <a name="Brainrot">**Brainrot Endpoint**</a>
  - **Endpoint**: `GET /brainrot`
  - **Description**: Add a new word to your vocabulary!
  - **Test File**: test_brainrot.py

- <a name="Calculator">**Calculator Endpoint**</a>
  - **Endpoint**: `GET /calc?x=<number>&y=<number>&op=<operator>` or `POST /calc`
  - **Description**: Use the following template to add, subtract, multiply, divide, or find the modulus of two numbers: `http://127.0.0.1:5000/calc?x=<number>&y=<number>&op=<operator>`. Replace `<number>` with the numbers you want to use, and replace `<operator>` with one of the following operations: `add`, `subtract`, `multiply`, `divide`, `mod`, `power`, `exp`.
    
    For square, square root, or cube operations, use the following template: `http://127.0.0.1:5000/calc?x=<number>&op=<operator>`. Replace `<number>` with the number you want to use, and replace `<operator>` with either `square`, `sqrt`, or `cube`.

    For binary and decimal conversions, use the following template: `http://127.0.0.1:5000/calc?x=<number>&op=<operator>`. Replace `<number>` with the number you want to convert to binary or decimal with either `decimal` or `binary` respectively.

    You can also use an HTML form to interact with the calculator endpoint. The form allows you to input values and select operations, then submit the form to see the result.
  - **Important Notes**: 
    - The operators must be spelled exactly as shown above, or you will receive an error.
    - If any of the variables (`x`, `y`, or `op`) are missing (unless specified), you will receive an error.
    - If no parameters are provided, the endpoint will render an HTML form for input.
  - **Test File**: `test_calc.py` `puppeteer_test_calc.js`
  - **Running Puppeteer Tests**:
    To run the Puppeteer tests for the calculator, follow these steps:
    1. Install Puppeteer using npm:
        ```sh
        npm install puppeteer
        ```
    2. Run the Puppeteer test script:
        ```sh
        node test/puppeteer_test_calc.js

  - <a name="Crypto">**Crypto prices Endpoint**</a>
  - **Endpoint**: `GET /bitcoin_price`, `GET /ethereum_price`
  - **Description**: Check what the price for crypto is!
  - **Test File**: test_crypto.py

- <a name="Hexifier">**Color Hexifier Endpoint**</a>
  - **Endpoint**: `GET /color?color=blue`
  - **Description**: Use the template to return a hex code of the color you want "http://127.0.0.1:5000/color". Type in the color of your choice into the text box on the page then press the "Get Hex Code" button to find out the hex code of the color. If the color doesn't exist in the library of colors saved, then you will return an error.
  - **Test File**: test_color_hexifier.py

- <a name="Binary">**Convert To Binary Endpoint**</a>
  - **Endpoint**: `GET /convertToBinary?num=#&type=decimal`
  - **Description**: Go to http://127.0.0.1:5000/convertToBinary?num=#&type=decimal to get the binary convertion of any non-negative whole number!
   Don't even think about putting in floats, strings, or blanks. I have tested all of those cases and you will get appropriate responses for each!
  - **Test File**: test_binaryconvert.py

-<a name="Continents">**Continents Endpoint**</a>
  - **Endpoint**: `GET /continents`
  - **Description**: Returns a list of continents in JSON format. You can retrieve specific continents using their unique ID.
  - **Test File**: `test_getcontinents.py`

- <a name="SingleContinent">**Single Continent Endpoint**</a>
  - **Endpoint**: `GET /continents/<int:continent_id>`
  - **Description**: Returns details of a single continent based on the provided ID. If the continent ID does not exist, a 404 error will be returned.
  - **Test File**: `test_get_single_continent.py`

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
  - Implemented PATCH functionality to allow updating favorite quotes based on author.
  - Added tests for successful updates, handling non-existent quotes, and input validation.
  - **Test File**: test_favorite_quote.py

- <a name="Fortune">**Fortune Cookie Endpoint**</a>
  - **Endpoint**: `GET /fortune`
  - **Description**: Returns a random fortune in JSON format. You can specify the count parameter to request multiple fortunes.
  - **Test File**: test_getfortune.py

- <a name="Fruit">**Fruit Info Endpoint**</a>
  - **Endpoint**: `GET /fruitInfo?fruit=<fruit_name>`
  - **Description**: Navigate to `http://127.0.0.1:5000/fruitInfo?fruit=<fruit_name>`. Replace `<fruit_name>` with the name of the fruit you want information about. If the fruit isn't available, an error message will appear, and you will be given a list of available options. Choose a fruit from the options provided. To add a new fruit, use Postman with the POST method, then navigate to `http://127.0.0.1:5000/fruitInfo?fruit=<fruit_name>&color=<fruit_color>&taste=<fruit_taste>`, Replace `<fruit_name>`, `<fruit_color>`, and `<fruit_taste>` with the desired fruit name, color, and taste, respectively. If the fruit is added successfully, a confirmation message will be returned. If any required data is missing, an error message will prompt you to provide the necessary information.
  - **Important Notes**:
    - Ensure the fruit name is spelled correctly to avoid errors.
    - If the fruit is not available, you will need to select from the provided options.

- <a name="Name">**Generate Name Endpoint**</a>
  - **Endpoint**: `GET /generateName` or `GET /generateName?gender=male` or `GET /generateName?length=3&gender=female`
  - **Description**: Get a randomly generated name. You can specify the `length` parameter to filter names by a specific length, and the `gender` parameter to filter names by gender (`male` or `female`), but both of these parameters are optional.
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
  - **Puppeteer Test File**: puppeteer_test_weather.js

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
  - **Description**: The /motivation endpoint provides a random motivational quote whenever accessed via a GET request. When a user sends a request to this endpoint, the app responds with one of five pre-defined motivational quotes, returned in JSON format. Additionally, users can retrieve the full list of motivational quotes by using the query parameter `all=true`. This returns all available quotes.
  - **Test File**: test_motivation.py test_get_motivation.py

- <a name="multiply">**Multiply Endpoint**</a>
  - **Endpoint**: `GET /multiply`
  - **Description**: Multiply two numbers provided as query parameters. This endpoint now also supports multiplying multiple numbers by providing a comma-separated list in the `numbers` parameter.
  - **Parameters**: 
    - `a`: The first number to multiply (required).
    - `b`: The second number to multiply (required).
    - `numbers`: A comma-separated list of numbers to multiply (optional).
  - **Response**:
    - Success: Returns a JSON object with the multiplication result.
    - Error: Returns an error message if inputs are missing or invalid.
  - **Test File**: `test_multiply.py`

- <a name="Netflix">**Netflix Shows Endpoint**</a>
  - **Endpoint**: `GET /netflix-shows`
  - **Description**: Get a random fun fact about your favorite Netflix shows! Add your own shows and facts to the source code to see them on the endpoint! !NO Adult Content allowed!
  - Fixed `get_netflix_shows` function to ensure it gracefully handles cases where a title filter does not match any shows, returning a 404 error with a clear message.
  - Corrected response structure for title filter to prevent errors when no shows are found.
  - Added test cases for base random selection, title filter match, and non-matching filter.
  - **Test File**: `test_netflix_shows.py`

- <a name="Photo">**Photo Gallery Endpoint**</a>
  - **Endpoint**: `GET /photogallery`
  - **Description**: Go checkout the art gallery complied by yours truly. !Add your own images to the images folder to see them on the endpoint! !NO Adult Content allowed! 
  - **Test File**: test_photogallery.py
 
- <a name="PizzaMeal">Pizza Meal Endpoint</a>
  - **Endpoint**: `GET /pizza_meal`
  - **Description**: This endpoint generates a complete meal, now has both a randomly selected pizza and soda combo. Customize your pizza by selecting a cheese level (Light, Regular, or Extra Cheese) or opt for a half-and-half pizza with unique toppings on each side. Some pizzas may come with a special type designation like Gluten-Free, Vegan, or Keto for dietary preferences. The meal includes a soda with a random brand, bottle size (Personal or 2 Liter), and ice preference (With Ice or No Ice). Use the `soda=all` query parameter to view the full list of soda brands. 🍕🥤
  - **Test File**: test_pizza_meal.py

- <a name="Pokefishing">**Pokefishing Endpoint**</a>
  - **Endpoint**: `GET /pokefishing`
  - **Description**: Catch a Magikarp! Refresh the page to cast your line again. Don't forget to reel it in!
  - **Test File**: test_pokefishing.py

- <a name="Power">**Power Endpoint**</a>
  - **Endpoint**: `GET /power?base=<value>&exp=<value>`
  - **Description**: Go to http://127.0.0.1:5000/power?base=2&exp=4. Replace the values of `base` and `exp` with whatever numbers you want.
- **Test File**: test_power.py

- <a name="Restaurants">**Restaurants Endpoint**</a>
  - **Endpoint**: `GET /restaurant`
  - **Description**: Go to http://127.0.0.1:5000/restaurant. See the list of restaurants and their menus and then place your order.
  - **Test File**: test_restaurants.py

- <a name="Stoic">**Stoic Quotes Endpoint**</a>
  - **Endpoint**: `GET /quotes`
  - **Description**: Get a good random stoic quote from Plato and others.
  - **Test File**: test_quotes.py

- <a name="Travel">**Travel Randomizer Endpoint**</a>
  - **Endpoint**: `GET /travel`
  - **Description**: Be given a randomly chosen travel destination! This app will output a popular travel destination in "city, country" JSON format. The app now allows users to specify a maximum flight duration, returning a travel destination that fits within the provided time limit.
  - **Test File**: test_travel.py

- <a name="Combo">**Two Mana Combo Endpoint**</a>
  - **Endpoint**: `GET /twoManaCombos?color=your_color`
  - **Description**: Go to http://127.0.0.1:5000/twoManaCombos?color=your_color. Specify which color you want included in your deck by replacing it with your_color. ⚪🔵⚫🔴🟢
  - **Test File**: test_twomana.py

- <a name="XKCD Comic">**XKCD Comics Endpoint**</a>
  - **Endpoint**: `GET /xkcd-comic`
  - **Description**: Go to http://127.0.0.1:5000/xkcd-comic. Refresh the page to enjoy many comics!
  - **Test File**: test_xkcd.py

- <a name="Books">**Books Endpoint**</a>
  - **Endpoint**: `GET /books`
  - **Description**: Just a endpoint about books.
  - **Test File**: test_books.py
    
- <a name="Version">**Version Endpoint**</a>
  - **Endpoint**: `GET /version`
  - **Description**: Returns the latest version of the repository based on the `VERSION` environment variable.
  - **Test File**: test_version.py

- <a name="Readme">**Readme Endpoint**</a>
  - **Endpoint**: `GET /readme`
  - **Description**: view the README.
  - **Test File**: test_readme.py

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

## Welcome to The IT4200 Art Gallery!


*Only KOOL Kids Will Get This Reference....

![alt text](https://github.com/UTT-Connole/class-api-IT4200-2024-fall/blob/main/images/gojo.jpg)
```

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
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠙⠒⠒⠲⠦⠤⠤⠤⠤⠤⠤⠤⠤⠤⠤⠤⠶⠒⠒⠚⠛⠉⠉⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢶⡿⣿⣿⣿⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⡿⢿⣿⣿⣿⢿⣾⣿⡵⡟⡮⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡻⡍⠄⠘⠫⢶⣹⡿⡷⡿⣵⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣷⠈⡀⠉⢳⣿⣽⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡔⠀⠠⡟⡽⡟⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣾⣟⡧⣰⣣⣋⡭⣝⣿⣿⣻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣯⣿⣿⣿⣗⢿⣶⣿⣿⣿⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡽⡛⣯⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡟⠛⠱⠛⠛⠿⣿⣿⣿⣿⣿⣿⣿⡟⢻⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣆⠂⠂⠀⠀⠀⠙⢿⣿⣿⣿⣽⣜⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣀⡢⠀⠀⠀⠀⠀⠹⣿⣿⣯⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡟⣿⣿⣟⢿⣿⣿⣿⣿⣿⣿⣿⣿⣟⢻⣿⣿⠲⡂⡀⠀⠀⡄⠀⢹⣿⣿⣻⣿⣿⣿⣿⠻⣿⣿⢻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⣿⣿⠁⢻⣿⡿⣸⣿⣿⣿⣿⣿⣿⣿⣿⠓⠿⠾⣿⠧⠀⠰⢚⠷⠄⠀⢸⣿⣿⣿⣿⣿⣿⣿⠁⢸⣷⠎⣿⣟⢿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⡌⣽⣷⣭⣟⣁⣻⣿⡿⣿⣿⣿⣿⣿⣿⣿⡟⢹⣿⣦⠀⠐⢶⡄⠀⠀⠘⣿⣿⣿⣿⠟⠻⣿⡖⠀⠿⠹⣿⠛⣼⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡟⠟⠳⣶⠹⣷⣶⣿⡟⣡⣿⣿⣿⣿⣿⣿⣿⢡⣿⣿⣯⣥⣄⠘⣿⡀⠀⠀⣼⣿⣿⣿⣷⡄⠀⠉⣵⣿⣏⢆⢺⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣯⣤⣶⣶⢞⣻⣿⠛⣼⣿⣿⣿⣿⣿⣿⣿⡯⢼⣿⣿⣿⣿⣿⣢⣿⠇⡄⢠⣿⣿⣿⣿⣿⣿⣷⣔⠸⣿⣿⣿⣷⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣏⣑⣶⠘⣿⣿⣿⣿⣿⣿⣿⣿⠆⣿⢿⠟⣿⣿⣿⡟⢸⣠⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⠇⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣵⣴⣿⢁⠘⢿⣿⣿⣿⣿⣿⣿⣇⣿⡁⠰⣾⣿⣹⡏⢠⣏⣻⡿⢿⠿⢿⣿⣿⣿⣟⠿⠂⢠⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡕⢖⠀⠙⡻⢿⣿⣿⣿⣿⣿⣿⣶⡿⠃⠘⣱⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣟⢎⢄⠀⢠⡹⣿⣿⣿⣿⣿⣿⣽⣓⢐⡴⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⣿⠏⠀⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠽⣦⡄⢯⣻⡿⣿⡿⢝⡛⠙⠉⠀⢹⡠⠯⡿⣿⣿⣿⣿⣿⡿⢟⣥⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣧⣿⣿⣿⣽⣿⣿⣿⣼⡿⢂⡤⣍⡁⢀⡶⡆⡽⠙⣻⣫⣷⣿⣿⣿⣿⣿⣿⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣾⣿⣮⣞⣻⣿⠀⡁⠀⠃⠀⣼⣿⣿⣿⣿⣿⣿⣿⣿⣶⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣅⢉⢉⡿⢥⡁⠶⠒⠨⠴⠀⢭⡛⢻⣿⣿⣿⣿⣿⣿⡟⠝⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⣿⣟⣟⣿⣷⣌⣽⣿⡵⣿⣿⣌⠞⣭⡑⠠⠠⣰⠎⢠⡙⡆⠙⣿⡿⢿⡿⠿⣷⢠⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢿⢽⣿⣟⣻⣿⣿⡞⠽⢍⡷⣟⢿⢿⣶⠕⠶⡷⣄⣴⡧⢋⣋⠁⠀⠺⣷⡈⠈⣆⡩⡄⠈⡿⣿⡿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢿⣿⣿⣿⣿⣷⣿⣿⣟⣖⣫⡿⣿⣶⣘⠜⣻⣧⣷⣿⡍⣖⣈⢘⣙⡛⢷⣨⢽⣤⣤⡏⠈⡹⠴⠄⠼⢾⣷⣾⣷⣆⠿⡟⢿⣿⠿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣿⣿⡟⣻⣿⠷⣟⣯⣽⣿⣿⣷⠙⠿⡦⣿⣙⣾⣷⣮⡥⣱⡶⠊⡑⠞⡿⣙⠒⣦⣆⣼⣿⣯⢶⠻⣶⠘⢮⣙⡙⢉⣻⣷⣝⡦⡀⢭⠂
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⢱⣼⣿⣥⣯⢻⣷⣿⣧⣽⡛⣦⢼⠙⣿⣏⣹⣿⣟⢚⡺⢳⡷⡦⡺⢛⣹⢚⢿⡿⣿⣿⣫⣓⡀⠜⢿⣟⢹⣎⣨⣗⠸⣴⢂⡝⢿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣽⣿⢿⣿⣿⡿⢿⣿⠿⡟⣿⣭⣉⢍⣼⢿⣼⣥⡩⠽⣷⠾⢿⣪⣇⣾⣿⠰⣻⣿⣿⠁⣼⣇⡝⣿⢮⣿⡿⣀⠦⢹⢒⢥⠿⣿⡟⢂⠀⡳⣼
⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
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