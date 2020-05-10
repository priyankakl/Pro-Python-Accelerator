class First:
    def __init__(self):
        self.to_do = []
        self.done = []    


class ToDoList:

    def add(p1, task):
        p1.to_do.append(task)
        print("to_do", p1.to_do)
    

    def done(p1,task_done):
        p1.to_do.remove(task_done)
        p1.done.append(task_done)
        print("done", p1.done)
        


def main():
    p1 = First()
    list_name = input("Enter the To Do list name:\n")
    while True:
        option = input("Please select an option below:\n\t 1.add a task \t 2. done with a task \t 3. see tasks\n")
        if option == "1":
            task = input("Enter the task\n")
            ToDoList.add(p1,task)
        elif option == "2":
            task_done = input("Enter the task\n")
            ToDoList.done(p1,task_done)       
        elif option == "3":
            print("---------------" + list_name + "--------------")
            print("TO DO \t", p1.to_do)
            print("DONE \t", p1.done)
        else:
            break
    

if __name__=="__main__": 
    main()