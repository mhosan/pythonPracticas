import buscar
import driver
import time

driver = driver.seteoDriver()

urls = ['https://web.arba.gov.ar/atencion']


for url in urls:
    buscar.buscar(url, driver, "Drupal")
    time.sleep(5)
# driver.quit()


