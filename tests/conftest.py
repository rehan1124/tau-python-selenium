"""
Contains shared fixtures
"""
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.edge.service import Service
from webdriver_manager.microsoft import EdgeChromiumDriverManager
import json
import os

os.environ['WDM_SSL_VERIFY'] = '0'


@pytest.fixture()
def config():
    # Read the config file
    with open("config.json") as config_file:
        config = json.load(config_file)

    # Make necessary assertions for values in config file
    assert config["browser"] in ("Chrome", "Edge", "Headless Chrome")
    assert config["implicit_wait"] > 0
    assert isinstance(config["implicit_wait"], int)

    return config


@pytest.fixture()
def open_browser(config):
    print(f'''\n\n*** Browser type: {config["browser"]} ***\n\n''')

    # Initialize chrome driver instance
    if config["browser"] == "Edge":
        driver = webdriver.Edge(service=Service(EdgeChromiumDriverManager().install()))
    elif config["browser"] == "Chrome":
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    elif config["browser"] == "Headless Chrome":
        opts = webdriver.ChromeOptions()
        opts.add_argument("headless")
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=opts)
    else:
        raise Exception(f'''*** Browser {config["browser"]} is not supported ***''')

    # Add implicit wait of 30 seconds
    driver.implicitly_wait(config["implicit_wait"])
    driver.maximize_window()

    # Open application url
    driver.get(config["app_url"])

    # Yield driver instance
    # Generator
    yield driver

    # Quit driver once test is over
    driver.quit()
