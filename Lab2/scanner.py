import re
from symtable import hashTable

"""

Scanning
Definition = treats the source program as a sequence of characters,
detect lexical tokens, classify and codify them

INPUT: source program
OUTPUT: PIF + ST

    Algorithm Scanning v1
    While (not(eof)) do
        detect(token);
        classify(token);
        codify(token);
    End_while
"""


class Scanner:
    def __init__(self, reservedWords, operators, separators, symTable, pif, tokenFileName):
        """
        initialize the scanner with the languages' reserved words, operators and a given symtable
        :param reservedWords: the reserved words of the language
        :param operators: the operators of the language
        :param symTable: a given symtable
        """
        self.reservedWords = reservedWords
        self.operators = operators
        self.separators = separators
        self.symTable = symTable
        self.pif = pif
        self.counter = 1
        self.tokenFileName = tokenFileName
        self.tokenTable = []

        self.generateTokenTable()

    def scan(self):
        """
        scans the input program for identifiers and constants and adds them in the symtable
        :return:
        """
        f = open('pb1.txt')
        lineCount = 0
        lexicalError = False
        lexicalErrorLine = -1
        lexicalErrorToken = -1
        for line in f.readlines():
            lineCount += 1
            for elem in re.split('\n|, | |\t', line.strip()):
                if elem in self.reservedWords or elem in self.operators or elem in self.separators:
                    self.pif.append((elem, self.getTokenCode(elem), 0))
                elif elem == '':
                    pass
                elif self.isIdentifier(elem):
                    self.symTable.add(elem)
                    self.pif.append((elem, 1, self.getSymTableCode(elem)))
                elif self.isConstant(elem):
                    self.symTable.add(elem)
                    self.pif.append((elem, 0, self.getSymTableCode(elem)))
                else:
                    lexicalError = True
                    lexicalErrorLine = lineCount
                    lexicalErrorToken = elem

        if lexicalError:
            print("Lexical Error at line ", lexicalErrorLine, " token ", lexicalErrorToken)
        else:
            print("Lexically Correct")

        print("\nSymTable:")
        print(self.symTable.toString())
        print("\nPIF:")
        for pif_pair in self.pif:
            print(pif_pair)
        print("\nToken Table: ")
        print(scanner.tokenTable)

    def getSymTableCode(self, elem):
        symTableItems = self.symTable.getItems()
        positionInHashTable, positionInInnerList = self.symTable.getPosition(elem)
        codePair = symTableItems[positionInHashTable][positionInInnerList]
        if codePair[1] == elem:
            return codePair[0]

    def getTokenCode(self, elem):
        for tkn in self.tokenTable:
            if elem in tkn:
                return tkn[1]
        return False

    def isIdentifier(self, elem):
        return bool(re.search("^[a-zA-Z_][a-zA-Z_0-9]*$", elem))

    def isConstant(self, elem):
        return bool(re.search("^[0-9]+$", elem))

    def generateTokenTable(self,):
        f = open(self.tokenFileName, 'r')
        counter = 2
        self.tokenTable.append(("CONST", 0))
        self.tokenTable.append(("IDENT", 1))
        for line in f.readlines():
            self.tokenTable.append((line.strip(), counter))
            counter += 1


reservedWords = ["int", "bool", "array", "char", "string", "if", "else", "while", "for", "read", "print"]
operators = ["+", "-", "*", "/", "%", ":=", ">", "<", "<=", "=", ">="]
separators = ["(", ")", "[", "]", "{", "}", ":", ";"]
symTbl = hashTable(15)
pif = []
scanner = Scanner(reservedWords, operators, separators, symTbl, pif, "token.in.txt")
scanner.scan()



"""
reservedWords = ["numar", "af", "vector", "caracter", "sir", "daca", "daca_nu", "cat_timp",
                 "merge", "de_la", "pana_la", "cu_pasul", "citeste", "printeaza"]
operators = ["+", "-", "*", "/", ":=", "<", "<=", "=", ">", ">="]
"""
