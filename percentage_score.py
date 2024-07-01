num_courses = int(input('Enter your number of courses '))

total_score = 0

for i in range(num_courses):
    course_name = input(f'Enter course {i+1} name: ')
    # score = float(input(f'Enter score for {course_name}: '))

    while True:
      score = float(input(f'Enter score for {course_name}: '))
      
      if score <=100:
            total_score += score    
            break
      else:
          print('Invalid Score')
    if 70<= score <= 100:
          print(f'Your grade score for {course_name} is A')
    elif 60<= score <= 69:
          print(f'Your grade score for {course_name} is B')
    elif 50<= score <= 59:
          print(f'Your grade score for {course_name} is C')
    elif 45<= score <= 49:
          print(f'Your grade score for {course_name} is D')  
    elif 40<= score <= 44:
          print(f'Your grade score for {course_name} is E')
    else :
          print(f'Your grade score for {course_name} is F')

percentage_score = (total_score/(num_courses * 100)) * 100

print(f'Percentage score: {percentage_score:.2f}%')