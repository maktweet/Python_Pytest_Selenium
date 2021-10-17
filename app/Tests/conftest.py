import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from app.Configs.Config import TestData


@pytest.fixture(params=[TestData.BROWSER], scope="class")
def driver_init(request):
    if request.param == "remote":
        driver = webdriver.Remote(
            command_executor='http://selenium-hub:4444/wd/hub',
            desired_capabilities={'browserName': 'chrome', 'javascriptEnabled': True})
    elif request.param == "chrome":
        s = Service(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=s)

    driver.get(TestData.BASEURL)
    request.cls.driver = driver
    yield
    driver.close()
