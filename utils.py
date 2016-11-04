def sma(data, n):
	averages = []
	if len(data) >= n:
		rolling_average = sum(data[0:n]) / float(n)
		averages.append(rolling_average)
		for i in range(n, len(data)):
			rolling_average += (data[i] - data[i-n]) / float(n)
			averages.append(rolling_average)
	return averages

def itunes_duration_to_minutes(duration):
	numerals = [int(x) for x in duration.split(":")]
	numerals.reverse()
	multiplier = 1.0 / 60
	cumulant = 0
	for num in numerals:
		cumulant += multiplier * num
		multiplier *= 60
	return cumulant
