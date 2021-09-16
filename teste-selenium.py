from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()

DEFAULT_PAGE = 'http://www.viva.ma.gov.br';

def access_default_page(route=''):
    def decorator(func): 
        def finterna(*args, **kwargs):
            driver.get(DEFAULT_PAGE+route)
            return func(*args, **kwargs)
    
        return finterna
    
    return decorator 

@access_default_page()
def case_ct_017():
    # desenvolve aqui
    menuItem = driver.find_element_by_id('menu-item-2538')
    menuItem.click();

    assert "http://www.viva.ma.gov.br/secao/s7-noticias/" in driver.current_url

# chama aqui
case_ct_017()
driver.close()



    
"""
elem = driver.find_element_by_name("q")
elem.clear()
elem.send_keys("pycon")
elem.send_keys(Keys.RETURN)
assert "No results found." not in driver.page_source

"""