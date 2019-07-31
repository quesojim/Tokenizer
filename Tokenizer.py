import re

SCANNER = re.compile(r'''
  (\s+) |                      # whitespace
  (/\*\*)  |                   #multilinestart
  (\*/)|                       #multilineend
  (//)[\n]* |                  # comments
  0[xX]([0-9A-Fa-f]+) |        # hexadecimal integer literals
  (\d+) |                      # integer literals
  (<<|>>) |                    # multi-char punctuation
  ([][(){}<>=,;:*+-/\"&]) |    # punctuation
  ([A-Za-z_][A-Za-z0-9_]*) |   # identifiers
  """(.*?)""" |                # multi-line string literal
  "((?:[^"\n\\]|\\.)*)" |      # regular string literal
  (.)                          # an error!

''', re.DOTALL | re.VERBOSE)



def load():
        filename = ("Main.jack")
        print("Processing...")
        infile = open(filename, 'r')
        line = infile.readline()
        filename = (filename.split('.', 1)[0].replace('.', '') + "T.xml")
        outfile = open(filename, 'w')
        outfile.write("<tokens>\n")
        inComment = False
        
        for line in infile:
            for match in re.finditer(SCANNER, line):
                space, mlinestart, mlineend, comment, hexint, integer, mpunct, \
                punct, word, mstringlit, stringlit, badchar = match.groups()
                if comment:
                    break
                if mlinestart:
                    inComment = True
                    print("Start Comment")
                if mlineend:
                    inComment = False
                    print("End Comment")
                if(inComment == False):
                    if word:
                        if (word == "class" or word == "constructor" or word == "method" or word == "function"
                            or word == "int" or word == "boolean" or word == "char" or word == "void" or
                            word == "var" or word == "static" or word == "field" or word == "let" or
                            word == "do" or word == "if" or word == "else" or word == "while" or word == "return"
                            or word == "true" or word == "false" or word == "null" or word == "this"):
                            outfile.write("<keyword> " + word + " </keyword>\n")
                        else:
                            outfile.write("<identifier> " + word + " </identifier>\n")
                    if integer:
                        outfile.write("<integerConstant> " + integer + " </integerConstant>\n")
                    if stringlit:
                        outfile.write("<stringConstant> " + stringlit + " </stringConstant>\n")
                    if punct:
                        if(punct == "<"):
                            outfile.write("<symbol> " + "&lt;" + " </symbol>\n")
                            print("SPECIAL CASE")
                        elif(punct == ">"):
                            outfile.write("<symbol> " + "&gt;" + " </symbol>\n")
                            print("SPECIAL CASE")
                        elif(punct == "\""):
                            outfile.write("<symbol> " + "&quot;" + " </symbol>\n")
                            print("SPECIAL CASE")
                        elif(punct == "&"):
                            outfile.write("<symbol> " + "&amp;" + " </symbol>\n")
                            print("SPECIAL CASE")
                        else:
                            outfile.write("<symbol> " + punct + " </symbol>\n")
                            print ("NORMAL SYMBOL PRINT")
                    
                
                
        outfile.write("</tokens>")
        outfile.close()

load()


