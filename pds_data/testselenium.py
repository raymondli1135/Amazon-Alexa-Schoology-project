from selenium import webdriver
from selenium.webdriver.common.keys import Keys 
import time
import boto3
from selenium.webdriver.firefox.options import Options
#import sys 
#import codecs
#sys.stdout=codecs.getwriter('utf-8')(sys.stdout)

driver = webdriver.Firefox()
# options = Options()
# options.add_argument("--headless")
# driver = webdriver.Firefox(firefox_options=options)

driver.get("http://lms.pds.org")
element = driver.find_element_by_id("edit-mail")
element.send_keys("XXXXX")
element = driver.find_element_by_id("edit-pass")
element.send_keys("XXXXX")
element.send_keys(Keys.RETURN)
time.sleep(5)

s3 = boto3.resource('s3')

bucket = s3.Bucket('pds-assignments')
for key in bucket.objects.all():
	key.delete()
#bucket.delete()

def save_to_s3(day, value):
	print "Day=", day
	#val1 = '\n'.join(value)
	val1 = '. '.join(value)
	print "value=", val1 
	s3.Object('pds-assignments', day).put(Body = val1)


s3.create_bucket(Bucket = 'pds-assignments')
  
sentence = []
assignments = driver.find_elements_by_css_selector(".upcoming-list > *")
prev_day = ''
for assignment in assignments:
	description = assignment.text
	description = description.replace('\n', ' ')
	day = description.split(",")[0]
	if day in ['MONDAY', 'TUESDAY', 'WEDNESDAY', 'THURSDAY', 'FRIDAY', 'SATURDAY', 'SUNDAY']:
		if len(sentence)>0:
			save_to_s3(prev_day, sentence)
			sentence = []
		prev_day = day
	else:
		sentence.append(description)

if sentence is not '':
	save_to_s3(prev_day, sentence)

for key in bucket.objects.all():
	print key











