def CharFrequency(string):
    freqMap = {}
    for c in string:
        freqMap[c] = freqMap.get(c, 0) + 1
    return freqMap

print(CharFrequency("hello World"))



nums = [10, 15, 20, 25, 30]
filtered_nums = [num*2 for num in nums if num%2==0]
print(filtered_nums)

def convertRawData(data):
    converted_data = []
    for d in data:
        try:
            converted_data.append(int(d))
        except ValueError as e:
            print(f'{d}, {e}')
    return converted_data


api_data = ["123", "45a", "90", "fail"]
processedData = convertRawData(api_data)
print(processedData)

