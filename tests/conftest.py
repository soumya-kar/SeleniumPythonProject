"""
This module contains shared fixtures.
"""
import pytest
import selenium.webdriver
import json

@pytest.fixture
def config(scope='session'):

  # Read the file
  with open('config.json') as config_file:
    config = json.load(config_file)
  
  # Assert values are acceptable
  #assert config['browser'] in ['Firefox', 'Chrome', 'Headless Chrome']
  assert isinstance(config['implicit_wait'], int)
  assert config['implicit_wait'] > 0

  # Return config so it can be used
  return config


@pytest.fixture
def browser(config):
  # Initialize the driver instance
  if config['browser'].upper() == 'CHROME':
    b=selenium.webdriver.Chrome()
  elif config['browser'].upper() == 'FIREFOX':
    b=selenium.webdriver.Firefox()
  elif config['browser'].upper() == 'HEADLESS CHROME':
    opts = selenium.webdriver.ChromeOptions()
    opts.add_argument('headless')
    b = selenium.webdriver.Chrome(options=opts)
  else:
    raise Exception(f'Browser "{config["browser"]}" is not supported')

  #Maximize the window
  b.maximize_window()

  # Make its calls wait up to 10 seconds for elements to appear
  b.implicitly_wait(config['implicit_wait'])

  # Return the WebDriver instance for the setup
  yield b

  # Quit the WebDriver instance for the cleanup
  b.quit()
