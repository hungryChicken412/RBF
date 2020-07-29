from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from selenium import webdriver
from selenium.webdriver.firefox.options import Options


from datetime import datetime

startTime = datetime.now()
print()

options = Options()
options.headless = True;
driver = webdriver.Firefox(options = options, executable_path= "geckodriver.exe")

##driver = webdriver.PhantomJS("PhantomJS.exe")

driver.get("http://mpresults.nic.in/mpbse/XIIHSSC-2020/HSSC_2020-XII.htm")

rn = "203241852"
rollno = driver.find_element_by_name('rollno')
rollno.clear();
rollno.send_keys(rn)
appno = driver.find_element_by_name('appno')
found = False;

anRange = [23212555, 23212570]

currentAN = anRange[0];
print("Testing For: " + rn);

while (found == False or currentAN > anRange[1]):
	driver.get("http://mpresults.nic.in/mpbse/XIIHSSC-2020/HSSC_2020-XII.htm")
	rollno = driver.find_element_by_name('rollno')
	rollno.clear();
	rollno.send_keys(rn)
	appno = driver.find_element_by_name('appno')

	appno.clear()
	an = str(currentAN)
	print("Currently Testing: " + an)
	appno.send_keys(an)

	submit = driver.find_element_by_xpath("/html/body/table[2]/tbody/tr/td[2]/div/center/table/tbody/tr/td/form/div/table/tbody/tr[3]/td[2]/p/input[1]")
	submit.click()

	try:
		element = WebDriverWait(driver, 10).until(
		        lambda driver: driver.current_url == "http://mpresults.nic.in/mpbse/XIIHSSC-2020/XII_2020-HSSC.asp"
		    )

		if ("Please enter valid Roll No. and Application No.") in driver.page_source:
			currentAN += 1;
			
		else:
			print("correct Roll no");
			found = True;
			driver.save_screenshot('screen.png')

		
	except:
		print("Time-out!");
		driver.quit();

endtime = datetime.now();
if (found == True):
	print("Correct Application Number is: " + str(currentAN));
else:
	print("Sorry Application Number Not Found In The Given Range");
print(endtime - startTime);
driver.quit();