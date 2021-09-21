import time
from selenium import webdriver
import unittest
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.action_chains import ActionChains

DEFAULT_PAGE = 'http://www.viva.ma.gov.br';

def access_default_page(route=''):
    def decorator(func): 
        def finterna(*args, **kwargs):
            args[0].driver.get(DEFAULT_PAGE+route)
            return func(*args, **kwargs)
    
        return finterna
    
    return decorator 
class VivaSeleniumTests(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())

    @access_default_page()
    def test_case_ct_017(self):
        # desenvolve aqui
        menuItem = self.driver.find_element_by_id('menu-item-2538')
        menuItem.click();

        assert "http://www.viva.ma.gov.br/secao/s7-noticias/" in self.driver.current_url

    @access_default_page()
    def test_case_ct_018(self):
        # desenvolve aqui
        menuItem = self.driver.find_element_by_id('menu-item-3503')
        
        hover = ActionChains(self.driver).move_to_element(menuItem)
        hover.perform()
        
        menuSubItem = self.driver.find_element_by_id('menu-item-5721')
        menuSubItem.click()

        assert "http://www.viva.ma.gov.br/cidadao-mirim/" in self.driver.current_url

    @access_default_page('/cidadao-mirim/')
    def test_case_ct_020(self):
        # desenvolve aqui
        logo = self.driver.find_element_by_id('topo-logo')
        
        logo.click();

        assert DEFAULT_PAGE in self.driver.current_url

    @access_default_page()
    def test_case_ct_021(self):
        # desenvolve aqui

        menuItem = self.driver.find_element_by_id('menu-item-2538')
        menuItem.click();

        noticiasByMenu = self.driver.current_url

        self.driver.get(DEFAULT_PAGE)

        maisNoticiasButton = self.driver.find_element_by_class_name('mais-noticias')
        maisNoticiasButton.click()

        print(noticiasByMenu, self.driver.current_url)

        assert noticiasByMenu in self.driver.current_url
    
    
    @access_default_page('/secao/s7-noticias/')
    def test_case_ct_022(self):
        # desenvolve aqui
        self.driver.maximize_window()
        noticias = self.driver.find_element_by_id('noticia-principal')
        links = noticias.find_elements_by_tag_name('a')
        def get_text(link):
            return link.text
        page1 = list(map(get_text, links))


        page2link = self.driver.find_element_by_link_text('2')
        page2link.click()

        noticiasPage2 = self.driver.find_element_by_id('noticia-principal')
        linksPage2 = noticiasPage2.find_elements_by_tag_name('a')
        def get_text(link):
            return link.text
        page2 = list(map(get_text, linksPage2))
        print(page1, page2)

        assert page1 != page2



    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()
