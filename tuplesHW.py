def record_group_details():
    group_details = []

    print("Enter details for the five groups:\n")

    for i in range(1, 6):
        print(f"Group {i}:")
        groupname = input("Enter the group name: ")
        sizeofthegroup = int(input("Enter the size of the group: "))
        dateofthecompetition = input("Enter the date of the competition (YYYY-MM-DD): ")
        venue = input("Enter the venue: ")
        typeofthemedal = input("Enter the type of medal (Gold/Silver/Bronze): ")

        group_tuple = (groupname, sizeofthegroup, dateofthecompetition, venue, typeofthemedal)
        group_details.append(group_tuple)
        print()

    print("\nRecorded Details:")
    group_number = 1
    for details in group_details:
        print(f"Group {group_number}: {details}")
        group_number += 1

record_group_details()