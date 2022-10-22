import re
from symtable import hashTable

class Scanner:
    def __init__(self, reservedWords, operators, symTable):
        """
        initialize the scanner with the languages' reserved words, operators and a given symtable
        :param reservedWords: the reserved words of the language
        :param operators: the operators of the language
        :param symTable: a given symtable
        """
        self.reservedWords = reservedWords
        self.operators = operators
        self.symTable = symTable

    def scan(self):
        """
        scans the input program for identifiers and constants and adds them in the symtable
        :return:
        """
        f = open('input_problems.txt')
        for elem in re.split('\n|, | |\t', f.read().strip()):
            if elem not in self.operators:
                if elem not in self.reservedWords:
                    if elem != '':
                        if not self.symTable.contains(elem):
                            self.symTable.add(elem)
        print(self.symTable.toString())


reservedWords = ["numar", "af", "vector", "caracter", "sir", "daca", "daca_nu", "cat_timp",
                 "merge", "de_la", "pana_la", "cu_pasul", "citeste", "printeaza"]
operators = ["+", "-", "*", "/", ":=", "<", "<=", "=", ">", ">="]
symTbl = hashTable(15)
scanner = Scanner(reservedWords, operators, symTbl)
scanner.scan()

# TODO documentatie si link de github pe alexandru.craciun@ubbcluj.ro
