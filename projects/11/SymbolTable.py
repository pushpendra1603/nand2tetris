



class SymbolTable:

    def __init__(self):
        self.classSymbols = {}
        self.subroutineSymbols = {}
        self.symbols = {"static": self.classSymbols, "field": self.classSymbols,
                        "arg": self.subroutineSymbols, "var": self.subroutineSymbols}
        self.index = {"static": 0, "field": 0, "arg": 0, "var": 0}

    
    def startSubroutine(self):
        self.subroutineSymbols.clear()
        self.index["arg"] = self.index["var"] = 0


    def define(self, name, type, kind):
        self.symbols[kind][name] = (type, kind, self.index[kind])
        self.index[kind] += 1

    
    def VarCount(self, kind):
        return self.index[kind]


    def KindOf(self, name):
        (type, kind, index) = self.lookUp(name)
        return kind


    def TypeOf(self, name):
        (type, kind, index) = self.lookUp(name)
        return type


    def IndexOf(self, name):
        (type, kind, index) = self.lookUp(name)
        return index


    def lookUp(self, name):
        if name in self.subroutineSymbols:
            return self.subroutineSymbols[name]
        elif name in self.classSymbols:
            return self.subroutineSymbols[name]
        else:
            return (None, None, None)