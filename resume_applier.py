import urllib
import BeautifulSoup
import urlparse
import mechanize
import subprocess

def main():

	url = 'https://www.roboform.com/filling-test-all-fields'

	br = mechanize.Browser()
	br.open(url)
	br.set_handle_robots(False)

	'''for link in br.links():
		print "The base url is: " + link.base_url
		print "The url is: " + link.url + '\n'

		new_url = urlparse.urljoin(link.base_url, link.url)

		b1 = urlparse.urlparse(new_url).hostname
		b2 = urlparse.urlparse(new_url).path

		print "http://", b1, b2
		print "-" * 50'''

	for form in br.forms():
		print "Form name: ", form.name
		print form

		print "-" * 50

	select = raw_input("Form to select: ")

	try:
		br.select_form(select)
	except:
		print "No form with that name exists. Selecting default."
		br.form = list(br.forms())[0]
		#print "ERROR: Form does not exist"

	for control in br.form.controls:
		#print control
		try:
			print "=" * 50
			print "Type: {}, Name: {}, value: {}".format(control.type, control.name, br[control.name])
		except:
			print "ERROR: Moving on."

		if control.type == "select":
			print control.items
			valid_input = []
			for item in control.items:
				print "Name:", item.name
				print "Values:", str([label.text for label in item.get_labels()])

				valid_input.append(item.name)

				print "-" * 50

			select = raw_input("Select ItemName: ")

			while select not in valid_input:
				print "Invalid. Try again."
				select = raw_input("Select ItemName: ")	#Try again if improper input

			control.value = [select]

		if control.type == "text":
			control.value = "Placeholder text" #Here is where you set what you want to enter

		if control.type == "text":
			control.value = "Placeholder text" #Here is where you set what you want to enter

		try:
			print "=" * 50
			print "Type: {}, Name: {}, value: {}".format(control.type, control.name, br[control.name])
		except:
			print "ERROR: Moving on."

	response = br.submit()
	with open('test.html', 'w') as test:
		test.write(response.read())

	subprocess.call(['google-chrome', 'test.html'])
	br.back() #Go back


if __name__ == '__main__':
	main()