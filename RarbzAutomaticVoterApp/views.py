from django.http import HttpResponse
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import time

def index(request):
  driver = webdriver.Chrome(ChromeDriverManager().install())
  driver.get("https://www.mtvema.com/vote/bestk-pop/")

  # roje_absolute_xpath = "//*[@id="root"]/div/section/div/div[4]/div/section[14]/div/div/div/div/div/div[2]/div/div/div/div[2]/div[5]/button"
  kpop_section_xpath = "/html/body[@class='loaded']/div[@id='root']/div[@class='containers-app-styles_app_3nv5w5mW0Zqzht93IcnLzd']/section[@class='containers-app-styles_content_oUqosZJpPrVx1TWUyP8se']/div[@class='sc-kEYyzF cRbcnB']/div[@class='containers-grid-styles_grid_1izqJEPBfNFaVhX79q0FfZ']/div/section[14]/div[@class='components-background-styles_background_1dQdg7G-QOKPvXGturlN_l components-element-layout-styles_element-layout_s9IkC0VuFEoAmUtKB0zS8 elements-accordion-components-root-styles_wrapper_2i2wyfdtpAAZL3KUu-Ttn7']/div[@class='components-background-styles_content_2m5Urr7WkuXg65_IDnMV5v']/div[@class='components-container-styles_container_PmYsVP5GHkqCkpDfs1B44']/div[@class='elements-accordion-components-root-styles_root_1SYNLaYUfgTyuCJGZZNAIP']/div[@class='components-container-styles_container_PmYsVP5GHkqCkpDfs1B44']/div[@class='rah-static rah-static--height-auto']/div/div/div[@class='elements-accordion-components-root-styles_content_lIYjt4MPfmHc7mdhAiIks']"
  kpop_title_xpath = "/html/body[@class='loaded']/div[@id='root']/div[@class='containers-app-styles_app_3nv5w5mW0Zqzht93IcnLzd']/section[@class='containers-app-styles_content_oUqosZJpPrVx1TWUyP8se']/div[@class='sc-kEYyzF cRbcnB']/div[@class='containers-grid-styles_grid_1izqJEPBfNFaVhX79q0FfZ']/div/section[14]/div[@class='components-background-styles_background_1dQdg7G-QOKPvXGturlN_l components-element-layout-styles_element-layout_s9IkC0VuFEoAmUtKB0zS8 elements-accordion-components-root-styles_wrapper_2i2wyfdtpAAZL3KUu-Ttn7']/div[@class='components-background-styles_content_2m5Urr7WkuXg65_IDnMV5v']/div[@class='components-container-styles_container_PmYsVP5GHkqCkpDfs1B44']/div[@class='elements-accordion-components-root-styles_root_1SYNLaYUfgTyuCJGZZNAIP']/div[@class='components-container-styles_container_PmYsVP5GHkqCkpDfs1B44']/div[@class='sc-bdVaJa eexeYn']/div[@class='components-accordion-styles_header_2l3Zp9YjD9kt-iXeNZ2xXZ components-accordion-styles_active_B4faHfTIlRRd82a20l5nQ']/div[@class='components-accordion-styles_headerInner_3LeVpkteqJ-y-IHwFLDsyS components-accordion-styles_active_B4faHfTIlRRd82a20l5nQ']/div[@class='elements-accordion-components-root-styles_header_9XhHLJ87pqTkfhqcrTAAU']"
  roje_xpath = "/html/body[@class='loaded']/div[@id='root']/div[@class='containers-app-styles_app_3nv5w5mW0Zqzht93IcnLzd']/section[@class='containers-app-styles_content_oUqosZJpPrVx1TWUyP8se']/div[@class='sc-kEYyzF cRbcnB']/div[@class='containers-grid-styles_grid_1izqJEPBfNFaVhX79q0FfZ']/div/section[14]/div[@class='components-background-styles_background_1dQdg7G-QOKPvXGturlN_l components-element-layout-styles_element-layout_s9IkC0VuFEoAmUtKB0zS8 elements-accordion-components-root-styles_wrapper_2i2wyfdtpAAZL3KUu-Ttn7']/div[@class='components-background-styles_content_2m5Urr7WkuXg65_IDnMV5v']/div[@class='components-container-styles_container_PmYsVP5GHkqCkpDfs1B44']/div[@class='elements-accordion-components-root-styles_root_1SYNLaYUfgTyuCJGZZNAIP']/div[@class='components-container-styles_container_PmYsVP5GHkqCkpDfs1B44']/div[@class='rah-static rah-static--height-auto']/div/div/div[@class='elements-accordion-components-root-styles_content_lIYjt4MPfmHc7mdhAiIks']/div[@class='elements-accordion-components-options-styles_root_11-2AMo7j83QpgPULj_x67']/div[@class='elements-accordion-components-item-styles_item_3UqYKLNwlTA3-XlJkgIjHA'][5]/button[@class='elements-accordion-components-item-styles_button_Nae_sr9iGBxv0mK2bG9iD sc-bZQynM hFZFVI']"
  # kpop_title = WebDriverWait(driver, 60).until(
  #   EC.presence_of_element_located((By.XPATH, kpop_title_xpath))
  # )  
  # kpop_section = WebDriverWait(driver, 60).until(
  #   EC.presence_of_element_located((By.XPATH, kpop_section_xpath))
  # )
  roje_voter = WebDriverWait(driver, 20).until(
    EC.presence_of_element_located((By.XPATH, roje_xpath))
  )
  print("found")
  # action_chains = ActionChains(driver)
  # action_chains.move_to_element(kpop_section).click(roje_voter).perform()
  # roje_voter.click()
  # print(len(rosie_voter))
  print("voted")
  time.sleep(20)
  print("done")
  driver.quit()
  return HttpResponse("Hello, world. You're at the polls index.")