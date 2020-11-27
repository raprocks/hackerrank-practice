num = int(input())
room_numbers = input()

room_number = [int(number) for number in room_numbers.split(" ")]

room_set = set(room_number)

print(int(((num * sum(room_set))-sum(room_number))/(num -1)))
