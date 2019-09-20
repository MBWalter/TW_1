def list_item():
    to_do_file =open("To_do_list.txt", "r")
    print("\nYou saved the following to do intems: ")
    print(to_do_file.read())
    to_do_file.close()

def add_item():
    with open("To_do_list.txt", "r+") as to_do_file:
        x = len(to_do_file.readlines())
        y = input("Add a task: ")
        to_do_file.write(str(x+1) + ".[ ]" + y + "\n")
        print("Item added! ")
        to_do_file.close()

def mark_item():
    with open("To_do_list.txt", "r+") as to_do_file:
        line = to_do_file.readlines()
        y = int(input("Which task did you completed? "))
        l = open("To_do_list.txt", "w")
        r = int(len(str(y)))
        for i in range(len(line)):
            if i == y-1:
                l.write(str(y) + ".[X]" + line[i][(r+4):])
            else:
                l.write(line[i])

def archive_item():
     with open("To_do_list.txt", "r+") as l:
        line = l.readlines()
        l = open("To_do_list.txt", "w+")
        x = 0
        for lines in line:
            if "[X]" in lines:
                pass
            else:
                x += 1
                l.write(str(x) + lines[1:])
print("Your completed tasks have been archived! ")

while True:
    cmd = input("Please specify a command [list, add, mark, archive]: ")
    if cmd == 'list':
        list_item()
    elif cmd == 'add':
        add_item()
    elif cmd == 'mark':
        mark_item()
        list_item()
    elif cmd == 'archive':
        archive_item()
        list_item()
