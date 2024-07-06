try:
	hours = float(input('Enter your hours:'))
	rate = float (input('Enter your rate: '))
except:
	print ('Error: Please enter a Numeric Value')
	quit()
if hours > 40: 
	overtime_hours = hours - 40
	overtime_rate = overtime_hours * rate * 1.5
	regular_rate = 40 * rate
	wages = regular_rate + overtime_rate
else:
	wages = hours * rate 
print ('Wages:',wages )