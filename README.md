# pytest task
## Summary
This is repository for pytest task.  
[Tested website](https://automationexercise.com/)  
[Test cases list](https://automationexercise.com/test_cases)  
[Report from latest pipeline run](https://derherrmannelig.github.io/pytest-task/index.html)  
## Requirements
[Python](https://www.python.org/) (3.12)  
[Allure Report](https://allurereport.org/docs/gettingstarted-installation/)  
## Installation
1. Clone this repo;
2. Navigate into repo, setup virtual environment:
```
pip install pipenv
pipenv shell
pipenv install
```
3. Install needed Playwright browsers:
```
playwright install chromium
playwright install firefox
playwright install webkit
```
4. You're good to go!
## Launch options
There are multiple launch options:
1. `pipenv run headless-default` — run all tests in Chromium headless, one by one;
2. `pipenv run headless-parallel` — run all tests in Chromium headless, in parallel, with automatic thread allocation;
3. `pipenv run headed-chromium` — run all tests in Chromium headed, one by one;
4. `pipenv run headed-firefox` — run all tests in Firefox headed, one by one;
5. `pipenv run headed-webkit` — run all tests in WebKit headed, one by one;
6. `pipenv run report` — host Allure report;
## To submit a bug report:
Navigate into **Issues** tab, click on "**New issue**" button. Follow this template:
1. Title;
2. Description;
3. Steps to reproduce;
4. Expected behavior;
5. Actual behavior;
6. Screenshots;
7. Additional details.
