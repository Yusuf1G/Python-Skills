text = "X-DSPAM-Confidence:    0.8475"
one = text.find('0')
two = text.find('5')
result = text[one:two+1]
results = float(result)
print(results)
#print(one)
#print(two)
#result = text[]