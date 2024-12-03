const puppeteer = require('puppeteer');

(async () => {
    const browser = await puppeteer.launch({
        headless: false, // Run in headful mode
        args: ['--no-sandbox', '--disable-setuid-sandbox']
    });
    const page = await browser.newPage();

    // Define for flask app
    const baseUrl = 'http://127.0.0.1:5001/';

    await page.goto(`${baseUrl}/calc`);

    // Function to perform a calculation using the UI
    async function performCalculation(x, y, operation, expectedResult) {
        await page.type('#x', x.toString());
        // Replace page.waitForTimeout(500); with the promise-based delay
        await new Promise(resolve => setTimeout(resolve, 500)); // Wait for 500ms

        if (!['square', 'sqrt', 'binary', 'decimal', 'cube'].includes(operation)) {
            await page.type('#y', y.toString());
            await new Promise(resolve => setTimeout(resolve, 500)); // Wait for 500ms
        }

        await page.select('#op', operation);
        await new Promise(resolve => setTimeout(resolve, 500)); // Wait for 500ms

        await page.click('button[type="submit"]');
        await new Promise(resolve => setTimeout(resolve, 500)); // Wait for 500ms

        // Wait for the result to be updated
        await page.waitForFunction(
            () => document.getElementById('result').textContent.trim() !== '',
            { timeout: 5000 }
        );

        // Result
        const result = await page.$eval('#result', el => el.textContent.trim());
        console.log(`${operation} operation result:`, result);

        // Verify the result
        if (result !== expectedResult.toString()) {
            throw new Error(`Expected ${expectedResult} but got ${result}`);
        }

        // Clear input fields and result for the next test
        await page.evaluate(() => {
            document.getElementById('x').value = '';
            const yField = document.getElementById('y');
            if (yField) {
                yField.value = '';
            }
            document.getElementById('result').textContent = '';
        });
        // Replace page.waitForTimeout(500); with the promise-based delay
        await new Promise(resolve => setTimeout(resolve, 500)); // Wait for 500ms
    }

    // Test cases
    await performCalculation(10, 312, 'add', 322);
    await performCalculation(10, 5, 'subtract', 5);
    await performCalculation(10, 2, 'multiply', 20);
    await performCalculation(10, 5, 'divide', 2);
    await performCalculation(10, 0, 'divide', 'You cannot divide by 0'); // Adjust expected result if necessary

    await browser.close();
})();