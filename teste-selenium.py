from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()

DEFAULT_PAGE = 'http://www.viva.ma.gov.br';

def access_default_page(fnc, route="/"):
    driver.get(DEFAULT_PAGE+route)

@access_default_page
def case_ct_001():
    # desenvolve aqui
    assert "Python" in driver.title

# chama aqui
case_ct_001()
driver.close()



    
"""
elem = driver.find_element_by_name("q")
elem.clear()
elem.send_keys("pycon")
elem.send_keys(Keys.RETURN)
assert "No results found." not in driver.page_source

"""