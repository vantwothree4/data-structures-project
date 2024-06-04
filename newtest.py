import vansProject
def testLinklists() :
    while 1 :
        print('\n    you can create linklists, print them and delete prime nodes from it.')
        print('    you can also merge two sorted lists')
        print('\n    1)create list\n    2)merge-sort lists\n    3)exit')
        selection = input("    choose an option: ")
        if selection == '1' :
            test = vansProject.LinkList()
            print("\n    enter some integer values (seperate them with space):")
            items = input('    ')
            for item in items.split() :
                test.insertAtEnd(int(item)) 
            print('\n    list created. what do you want to do with it?')
            while selection != '3':
                print('\n    1)print the list\n    2)delete prime nodes\n    3)go back to previous menu')
                selection = input("    choose an option: ")
                if selection == '1' :
                    print("\n    list:\n    ",end='')
                    test.printData()
                elif selection == '2' :
                    test.deletePrimeNode()
                    print("\n    done\n    list:\n    ",end='')
                    test.printData()
        elif selection == '2' :
            test = vansProject.LinkList()
            l1 = vansProject.LinkList()
            l2 = vansProject.LinkList()
            print("\n    enter sorted integer values for first list (seperate them with space):")
            items = input('    ')
            for item in items.split() :
                l1.insertAtEnd(int(item)) 
            print("    enter sorted integer values for second list (seperate them with space):")
            items = input('    ')
            for item in items.split() :
                l2.insertAtEnd(int(item)) 
            test.mergesort(l1,l2)
            print("    merge-sorted list:\n    ",end='')
            test.printData()
        elif selection == '3' :
            return  
        
def testStack() :
    test = vansProject.Stack()
    while 1 :
        print ('\n    you can create stacks, push items and pop them.')
        print('\n    1)push item\n    2)pop item\n    3)exit')
        selection = input("    choose an option: ")
        if selection == '1' :
            item = input('\n    enter the data: ')
            test.push(item)
            print('    done.')
        elif selection == '2' :
            print('\n    popped item: ',test.pop())
        elif selection == '3' :
            return

def testQueue() :
    test = vansProject.Queue()
    while 1 :
        print ('\n    you can create Queues, add items and delete them.')
        print('\n    1)add item\n    2)delete item\n    3)exit')
        selection = input("    choose an option: ")
        if selection == '1' :
            item = input('\n    enter the data: ')
            test.add(item)
            print('    done.')
        elif selection == '2' :
            print('\n    deleted item: ',test.delete())
        elif selection == '3' :
            return

def testExpressions() :
    print('\n    you can convert infix, prefix and postfix expressions and evaluate the answer')
    notation = input("\n    enter the notation of the expression: ")
    exp = input("\n    enter the expression(don't use space): ")
    test = vansProject.Expression(exp, notation.lower())
    while 1 :
        print('\n    1)convert expression\n    2)evaluate answer(for one-digit ints)\n    3)exit ')
        selection = input("    choose an option: ")
        if selection == '1' :
            selectedForm = input("\n    select a form to convert expression: ")
            test.convertTo(selectedForm.lower())
            print(f"\n    the {selectedForm} of the expression is:   ",test.expression)
        elif selection == '2' :
            print("    the evaluated value is:  ",test.evaluate())
        elif selection == '3' :
            return
    

continueTask = ''
intro = '''
    what can this program do?\n
    1) create Linkedlists and work with them
    2) create Stacks and work with them
    3) create Queues and work with them
    4) convert Prefix, Infix and Postfix expressions and evaluate the answer''' 
while continueTask.lower() != 'exit':
    print(intro)
    selection = input("\n    choose an option: ")
    if selection == '1' :
        testLinklists()
    elif selection == '2' :
        testStack()
    elif selection == '3' :
        testQueue()
    elif selection == '4' :
        testExpressions()
    
    continueTask = input('\n    press enter to continue or type "exit" to exit\n    ')

