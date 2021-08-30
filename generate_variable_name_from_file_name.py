import json
class GenerateVariableName:
    variable_name = ""
    uuidList = []
    def validateInput(self, i) -> bool:
        if i != "":
            return True
        else:
            return False

    def loadListData(self, file_location):
        with open(file_location) as f:
            data = json.load(f)
        return data

    def getInputVal(self):
        variable_name = input("Name of Variable to generate:")
        file_location = input("Enter File Location:")
        self.variable_name = variable_name
        if self.validateInput(i = self.variable_name):
            lists = self.loadListData(file_location = file_location)
            self.uuidList = lists
            return self.getListAndGenarateConstVarables()
        else:
            print("You've succefully failed to supply variable name")

    def generateVariables(self, initial_index, last_index) -> str:
        for x in range(int(initial_index),int(last_index)):
            print(self.variable_name.upper()+"_"+ str(x))

    def getListAndGenarateConstVarables(self):
        for idx, val in enumerate(self.uuidList):
            print(f"public static final String {self.variable_name}_{idx} =  \"{val}\";")



def main():
    generate = GenerateVariableName()
    generate.getInputVal()


if __name__ == "__main__":
    main()