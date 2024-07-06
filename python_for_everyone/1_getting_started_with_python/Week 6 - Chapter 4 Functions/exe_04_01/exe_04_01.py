hour = float(input('Enter Hours:'))
rate = float(input('Enter Rate: '))

def computepay (hour,rate):
	if hour > 40:
		overtime_hours = hour - 40
		overtime_rate = overtime_hours * rate * 1.5
		standard_rate = 40 * rate
		wages = standard_rate + overtime_rate
	else:
		wages = hour * rate
	return wages 

p = computepay(hour,rate)
print ('Pay',p)