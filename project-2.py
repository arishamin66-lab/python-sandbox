def analyze_number(numbers):
    top = numbers[0]
    low = numbers[0]
    sum = 0
    even = 0
    odd = 0
    for num in numbers:
        sum += num
        if num > top:
            top = num
        if num < low:
            low = num
        if num % 2 == 0:
            even += 1 
        else:
            odd += 1
    return even,odd,sum,top,low
    
a = [10,20,30,43]

print(analyze_number(a))
    