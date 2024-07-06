try:
	score = float(input('Enter a score between 0.0 - 1.0:'))
except:
	print('Enter a valid number between 0.0 - 1.0')
	quit()	
if score <0.0 or score >1.0:
	print('Please enter a score between 0.0-1.0')
elif score >= 0.9:
	print('A')
elif score >= 0.8:
	print ('B')
elif score >= 0.7: 
	print('C')
elif score >= 0.6:
	print('D')
elif score < 0.6:
	print('F')