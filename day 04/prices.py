prices = [105, 110, 108, 112, 115, 116, 114]

rolling_avg = []
window = 3

for i in range(len(prices) - window + 1):
    avg = sum(prices[i:i+window]) / window
    rolling_avg.append(round(avg, 2))

print(rolling_avg)