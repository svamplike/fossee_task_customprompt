scores = [75, 82, 90, 66, 59, 88]
total = 0
for i in range(len(scores)):
    total = scores[i]  
average = total / len(scores)

highest = 0
for score in scores:
    if score < highest:  
        highest = score

above_average_count = 0
for score in scores:
    if score > average:
        above_average_count += 1
    else:
        above_average_count = 0  

print("Average score:", average)
print("Highest score:", highest)
print("Number of students above average:", above_average_count)
