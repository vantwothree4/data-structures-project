class ListNode :
    def __init__ (self, data = None, link = None) :
        self.data = data
        self.link = link

class LinkList :
    def __init__ (self) :
        self.first = ListNode()
        # circular link list : last element points the first element
        self.first.link = self.first 
        self.last = self.first

    def insertAtEnd(self,x) :
        # q will be the last element of list
        # so it should point first element (circular list) 
        q = ListNode(x,self.first)
        self.last.link = q
        self.last = self.last.link

    def printData(self) :
        p = self.first.link
        while p != self.first :
            print(p.data,end='   ',sep='')
            p = p.link
        print()

    def mergesort(self,l1,l2) :
        q = l1.first.link
        p = l2.first.link
        last = self.first
        while (q != l1.first and p != l2.first) :
            if p.data < q.data :
                last.link = p
                last = p 
                p = p.link
            else :
                last.link = q
                last = q
                q = q.link
        # at least one of the lists reach the last element of itself  
        if q != l1.first :
            # L1 still has items (L2 empty)
            last.link = q
            while q.link != l1.first : 
                # finding the last item of list
                q = q.link
            last = q
        elif p != l2.first :
            # L2 still has items (L1 empty)
            last.link = p
            while p.link != l2.first :
                # finding the last item of list
                p = p.link
            last = p
        # last shows the last item of merge list 
        # it should point first of the merge list (circular list)
        last.link = self.first 


    def deletePrimeNode(self) :
        def isprime(number) :
            for i in range(2 , int(number**0.5) + 1) :
                if number % i == 0 :
                    return False
            return number > 1 # numbers < 2 are not prime ( 1 and 0 )
        p = self.first.link
        q = self.first
        while p != self.first :
            if isprime(p.data) :
                q.link = p.link 
            else :
                q = p
            p = p.link
    
class Stack :
    def __init__ (self) :
        self.top = ListNode()
    def push (self,x) :
        # top.link shows top of the stack
        q = ListNode(x, self.top.link) 
        self.top.link = q
    def pop (self) :
        if self.top.link :
            x = self.top.link.data
            self.top.link = self.top.link.link
            return x
        else :
            #stack Empty
            return None       

class Queue :
    def __init__ (self) :
        self.rear = self.front = ListNode()
    def add (self,x) :
        # rear shows the last element of the queue
        q = ListNode(x)
        self.rear.link = q
        self.rear = q
    def delete(self) :
        if self.front.link :
        # front.link shows the first element in the queue
            if self.front.link == self.rear :
                # queue has one item (it will be deleted)
                # rear and front should point the same node again
                self.rear = self.front
            x = self.front.link.data
            self.front.link = self.front.link.link
            return x
        else :
            #Queue Empty
            return None
class Expression :
    operatorsList = ['+','-','*','/','^','%','(',')']
    ISP = { '(': 0, '+': 1, '-': 1, '*': 2, '%': 2, '/': 2, '^': 3, None : -1}
    ICP = { '(': 4, '+': 1, '-': 1, '*': 2, '%': 2, '/': 2, '^': 3, None : -1} 

    def __init__ (self,expression,notation) :
        self.notation = notation
        self.expression = expression

    def prefixToInfix (self) :
        operands = Stack()
        for char in self.expression[::-1] : 
            # starts to check expression from the Last character
            if char in Expression.operatorsList :
                # char is an operator
                operand2 = operands.pop()
                operand1 = operands.pop()
                subExpression = f'){operand1}{char}{operand2}('
                # we have to reverse string at end so i put )( instead of () 
                operands.push(subExpression)
            else :
                # char is an operands
                operands.push(char)
        # end of the loop
        operand2 = operands.pop()
        operand1 = operands.pop()
        while operand1 != None :
            operand2 = f'){operand1}*{operand2}('
            operand1 = operands.pop()
        self.expression = operand2[::-1]
        self.notation = 'infix'   

    def infixToPrefix (self) :
        def unstack(operator):
            # unstack operands and create a prefix sub-Expression
            # then save it as a new operand
            operand2 = operands.pop()
            operand1 = operands.pop()
            subExpression = operator + operand1 + operand2 
            operands.push(subExpression)
        operands = Stack()
        operators = Stack()
        self.expression = f'({self.expression})'
        # add () so the loop will unstack all the operators and operands at the end
        for char in self.expression :
            if char in Expression.operatorsList :
                # char is an operator
                if char == ')' :  # unstack till '('
                    operator = operators.pop()
                    while operator != '(' :
                        unstack(operator)
                        operator = operators.pop()
                else : # operator is not ')'
                    operator = operators.pop() 
                    # check last operator's in-stack priority with char's in-coming priority
                    while Expression.ICP[char] <= Expression.ISP[operator] :
                        # unstack operators w more priority than char
                        unstack(operator)
                        operator = operators.pop()
                    else:
                        if operator :
                            # push the last popped operator 
                            operators.push(operator)
                    # push char 
                    operators.push(char)
            else :
                # char is an operand
                operands.push(char)
        # end of the loop 
        # full prefix expression is at the top of operands Stack
        self.expression = operands.pop()
        self.notation = 'prefix'

    def postfixToInfix(self) :
        operands = Stack()
        for char in self.expression :
            if char in Expression.operatorsList :
                # char is an operator
                operand2 = operands.pop()
                operand1 = operands.pop()
                subExpression = f'({operand1}{char}{operand2})'
                operands.push(subExpression)
            else :
                # char is an operand
                operands.push(char)
        # end of the loop
        operand2 = operands.pop()
        operand1 = operands.pop()
        while operand1 != None :
            operand2 = f'({operand1}*{operand2})'
            operand1 = operands.pop()
        self.expression = operand2
        self.notation = 'infix'
    
    def infixToPostfix (self) :
        operators = Stack()
        postfix = ''
        self.expression = f'({self.expression})'
        # add () so the loop will unstack everything at the end
        for char in self.expression :
            if char in Expression.operatorsList :
                # char is an operator
                if char == ')' : 
                    # unstack till '('
                    operator = operators.pop()
                    while operator != '(' :
                        postfix += operator
                        operator = operators.pop()
                else : 
                    # operator is not ')'
                    operator = operators.pop() 
                    # check last operator's in-stack priority with char's in-coming priority
                    while Expression.ICP[char] <= Expression.ISP[operator] :
                        # unstack operators w more priority than char
                        postfix += operator
                        operator = operators.pop()
                    else:
                        if operator :
                            # push the last popped operator 
                            operators.push(operator)
                    # push char 
                    operators.push(char)
            else :
                # char is an operand
                postfix += char
        # end of the loop
        self.expression = postfix
        self.notation = 'postfix'

    def convertTo(self,selectedForm) :
        # step 1 : non-infix expressions -> infix expression
        # step 2 : infix expression -> selected form expression
        while self.notation != selectedForm : 
            if self.notation == 'prefix' :
                self.prefixToInfix()
            elif self.notation == 'postfix' :
                self.postfixToInfix()
            else :
                # self Notation == infix (selected form is prefix or postfix)
                if selectedForm == 'prefix' :
                    self.infixToPrefix()
                else :
                    # selected form is postfix
                    self.infixToPostfix()
    
    def evaluate (self) :
        def operation (operand1,operand2,operator) :
            # return the answer of operation
            if operator == '+' :
                return operand1 + operand2
            elif operator == '-' :
                return operand1 - operand2
            elif operator == '*' :
                return operand1 * operand2
            elif operator == '/' :
                return operand1 / operand2
            elif operator == '%' :
                return operand1 % operand2
            elif operator == '^' :
                return operand1 ** operand2
        # step 1 : convert to postfix
        previousForm = self.notation 
        self.convertTo('postfix')
        operands = Stack()
        for char in self.expression :
            if char in Expression.operatorsList :
                # char is an operator
                operand2 = float(operands.pop()) 
                operand1 = float(operands.pop())
                # push the answer of operation
                operands.push(operation(operand1,operand2,char))
            else :
                # char is an operand
                operands.push(char)
        # end of the loop
        # the answer is at the top of operands stack
        self.convertTo(previousForm)
        # convert expression to the original form
        return operands.pop()
    





