from selenium import webdriver
from selenium.webdriver.common.by import By
from mydp_app.models import *
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from django.urls import reverse
from selenium.webdriver.common.keys import Keys
import time

class TestProjectHomePage(StaticLiveServerTestCase):
    def setUp(self):
        self.browser = webdriver.Chrome()

    def tearDown(self):
        self.browser.close()

    def test_home_page_content(self):
        self.browser.get(self.live_server_url)
        intro = self.browser.find_element(By.CLASS_NAME, 'intro')
        self.assertEquals(intro.find_element(By.TAG_NAME, 'h2').text, 'Get Your DP Banner')

    def test_click_banner_redirect_to_view_page(self):
        self.browser.get(self.live_server_url)
        view_banner_url = self.live_server_url + reverse('view-banner', kwargs={'slug': 'testing-banner'})
        banner = self.browser.find_element(By.CLASS_NAME, 'banner-grid')
        banner.find_element(By.CLASS_NAME, 'banner-link').click()
        self.assertEquals(self.browser.current_url, view_banner_url)


    
