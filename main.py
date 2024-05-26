with open('input.txt', 'r') as input_file, open('output.txt', 'w') as output_file:
    lines = input_file.readlines()

    math_sum = 0
    physics_sum = 0
    russian_sum = 0
    student_count = 0

    for line in lines:
        data = line.strip().split(';')
        math_score = int(data[1])
        physics_score = int(data[2])
        russian_score = int(data[3])

        average_score = (math_score + physics_score + russian_score) / 3
        output_file.write(f"{average_score:.9f}\n")

        math_sum += math_score
        physics_sum += physics_score
        russian_sum += russian_score
        student_count += 1

    math_average = math_sum / student_count
    physics_average = physics_sum / student_count
    russian_average = russian_sum / student_count

    output_file.write(f"{math_average:.9f} {physics_average:.9f} {russian_average:.9f}")