const puppeteer = require('puppeteer');

(async () => {
    const browser = await puppeteer.launch({
        headless: false, // Run in headful mode
        args: ['--no-sandbox', '--disable-setuid-sandbox']
    });
    const page = await browser.newPage();

    // Navigate to the weather page
    await page.goto('http://127.0.0.1:5000/weather');
    await new Promise(resolve => setTimeout(resolve, 500));

    // Wait for the input element to be present
    await page.waitForSelector('input[name="city"]');
    await new Promise(resolve => setTimeout(resolve, 500));

    // Test valid city input
    await page.type('input[name="city"]', 'London');
    await new Promise(resolve => setTimeout(resolve, 500));
    await page.click('button[type="submit"]');
    await new Promise(resolve => setTimeout(resolve, 500));
    // await page.waitForNavigation();
    await new Promise(resolve => setTimeout(resolve, 500));

    // Check if the weather information is displayed
    const weatherInfo = await page.$eval('.weather-box', el => el.textContent);
    await new Promise(resolve => setTimeout(resolve, 500));
    console.log('Weather Info for London:', weatherInfo);
    await new Promise(resolve => setTimeout(resolve, 500));

    // Navigate back to the weather page
    await page.goto('http://127.0.0.1:5000/weather');
    await new Promise(resolve => setTimeout(resolve, 500));

    // Wait for the input element to be present
    await page.waitForSelector('input[name="city"]');
    await new Promise(resolve => setTimeout(resolve, 500));

    // Test invalid city input
    await page.type('input[name="city"]', 'InvalidCity');
    await new Promise(resolve => setTimeout(resolve, 500));
    await page.click('button[type="submit"]');
    await new Promise(resolve => setTimeout(resolve, 500));

    // Check if the error message is displayed
    const errorMessage = await page.$eval('.error', el => el.textContent);
    await new Promise(resolve => setTimeout(resolve, 500));
    console.log('Error Message for InvalidCity:', errorMessage);
    await new Promise(resolve => setTimeout(resolve, 500));

    await browser.close();
})();