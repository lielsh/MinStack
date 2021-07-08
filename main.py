class MinStack:
    
    def __init__(self, maxLen=15):  # Default maximum length of a MinStack is set to 15
        self.__mainArr = []
        self.__minArr = []
        self.__maxLen = maxLen
    
    def __len__(self):
        return len(self.__minArr)

    def __str__(self):
        return str(self.__mainArr)
    
    def push(self, num):
        if not self.isFull():
            if type(num) == int or type(num) == float:
                
                self.__mainArr.append(num)
                
                if self.__len__() == 0 or (self.__len__() > 0 and num <= self.__minArr[self.__len__()-1]):
                    self.__minArr.append(num)
               
                elif self.__len__() > 0 and num > self.__minArr[self.__len__()-1]:
                    self.__minArr.append(self.__minArr[self.__len__()-1])
                
                print("The number {} has been successfully added".format(num))
                
            else:
                print("{} ({}) is an invalid input - numbers only (skipped)".format(num, type(num)))
        
        else:
            print("The stack is already full ({})".format(self.__maxLen))
    
    def pop(self):
        if self.isEmpty():
            print("The stack is empty")

        else:
             pop = self.__mainArr.pop()
             self.__minArr.pop()
             print("The number {} has been successfully removed".format(pop))
 
    def isEmpty(self):
        return True if self.__len__() == 0 else False
    
    def isFull(self):
        return True if self.__len__() == self.__maxLen else False
    
    def getMinimum(self):
        return self.__minArr[self.__len__()-1] if not self.isEmpty() else None
        
if __name__ == "__main__":
    
    # Test No.1
    print("\n###### Test No.1 ######")
    input1 = [1,2,6,0,8]
    stack1 = MinStack()
    for num in input1: stack1.push(num)
    for i in range(10): stack1.pop()   
    print(stack1.getMinimum())
    
    # Test No.2
    print("\n###### Test No.2 ######")
    input2 = [8,8,3,3,3,9,9]
    stack2 = MinStack()
    for num in input2: stack2.push(num)
    for i in range(5): stack2.pop()
    print(stack2.getMinimum())

    # Test No.3
    print("\n###### Test No.3 ######")
    input3 = [1, True, '3', None, [], {}]
    stack3 = MinStack()
    for num in input3: stack3.push(num)  
    print(stack3.getMinimum())

    # Test No.4
    print("\n###### Test No.4 ######")
    input4 = [1, 3, 1, 54]
    stack4 = MinStack(2)
    for num in input4: stack4.push(num)  
    print(stack3.getMinimum())