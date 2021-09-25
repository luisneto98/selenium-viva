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
    def test_case_ct_016(self):
        # desenvolve aqui
        constrat = self.driver.find_element_by_id('is_normal_contrast')
        constrat.click()
        
        fontSize = self.driver.find_element_by_id('is_normal_fontsize')
        fontSize.click()

        carousel = self.driver.find_element_by_class_name('carousel-inner')
        carousel.click()

        highConstrat = self.driver.find_element_by_id('is_high_contrast')
        
        largeFontSize = self.driver.find_element_by_id('is_large_fontsize')

        time.sleep(1)

        assert highConstrat
        assert largeFontSize

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

    @access_default_page('/secao/s7-noticias/')
    def test_case_ct_019(self):
        # desenvolve aqui
        blockNotice = self.driver.find_element_by_id('noticia-principal')
        links = blockNotice.find_elements_by_tag_name('div')
        firstNotice = links[0]
        firstNotice.click()
        notice = self.driver.find_element_by_id('noticia-principal')
        image = notice.find_element_by_tag_name('img')
        url = self.driver.current_url
        image.click()

        assert url != self.driver.current_url

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


    @access_default_page()
    def test_case_ct_023(self):
        # desenvolve aqui
        button = self.driver.find_element_by_class_name('wp-image-1965')
        button.click();

        assert "https://seati.segov.ma.gov.br/procon/agendamento/" in self.driver.current_url

    @access_default_page()
    def test_case_ct_024(self):
        # desenvolve aqui
        self.driver.implicitly_wait(100)
        socialLi = self.driver.find_element_by_class_name('Facebook')
        facebookLink = socialLi.find_element_by_tag_name('a')
        ActionChains(self.driver).move_to_element(facebookLink).perform()
        facebookLink.click()
        time.sleep(5)
        self.driver.switch_to.window(self.driver.window_handles[1])
        assert "facebook" in self.driver.current_url

    @access_default_page('/secao/s7-noticias/')
    def test_case_ct_025(self):
        # desenvolve aqui
        self.driver.maximize_window()
        blockNotice = self.driver.find_element_by_id('noticia-principal')
        links = blockNotice.find_elements_by_tag_name('div')
        firstNotice = links[0]
        dateExternal = firstNotice.text.split('\n')[0]

        firstNotice.click()

        dateInternal = self.driver.find_element_by_class_name('tarja-data').text
        assert dateExternal in dateInternal

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()
