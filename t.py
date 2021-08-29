class GenerateVariableName:
    initial_index = 0
    last_index = 0
    variable_name = ""

    def validateInput(self, i) -> bool:
        if i is not "":
            return True
        else:
            return False


    def getInputVal(self):
        initial_index = input("Enter the first Index:")

        last_index = input("Index last Index:")

        variable_name = input("Name of Variable to generate:")

        self.initial_index = initial_index
        self.last_index = last_index
        self.variable_name = variable_name

        if (self.validateInput(i = self.initial_index) and self.validateInput(i = self.initial_index)):
            return self.generateVariables(initial_index = self.initial_index, last_index = self.last_index)
        else:
            print("You've succefully failed to supply either initial or final index")


    def generateVariables(self, initial_index, last_index) -> str:

        for x in range(int(initial_index),int(last_index)):
            print(self.variable_name.upper()+"_"+ str(x))


def main():
    generate = GenerateVariableName()
    generate.getInputVal()

if __name__ == "__main__":
    main()