id_counter = 1 
id_map = {} 

def File_input(file):
    with open(file, 'r') as file:
        context = file.read()
    return context.split()

def token(Type):
    state = Type
    match state:
        case "ID":
            return "TK_ID"
        case "when":
            return "TK_when"
        case "loop-un":
            return "TK_loop-un"
        case "loop":
            return "TK_loop"
        case "make":
            return "TK_make"
        case "call":
            return "TK_call"
        case "Assign":
            return "TK_Assign"
        case "Float":
            return "TK_Float"
        case "nope":
            return "TK_nope"
        case "=":
            return "TK_="
        case "+":
            return "TK_+"
        case "-":
            return "TK_-"
        case "*":
            return "TK_*"
        case "%":
            return "TK_%"
        case "=":
            return "ALIGN_TK"
        case ">":
            return "TK_>"
        case "<":
            return "TK_<"
        case "INT":
            return "TK_INT"

def _while(lexeme):
    state = 1
    while 1:
        match state:
            case 1:
                if len(lexeme) == 10 :
                    state = 2
                else:
                    state = 13
            case 2:
                if lexeme[0] == 'l':
                    state = 3
                else:
                    state = 13
            case 3:
                if lexeme[1] == 'o':
                    state = 4
                else:
                    state = 13
            case 4:
                if lexeme[2] == 'o':
                    state = 5
                else:
                    state = 13
            case 5:
                if lexeme[3] == 'p':
                    state = 6
                else:
                    state = 13
            case 6:
                if lexeme[4] == '_':
                    state = 7
                else:
                    state = 13
            case 7:
                if lexeme[5] == 'u':
                    state = 8
                else:
                    state = 13
            case 8:
                if lexeme[6] == 'n':
                    state = 9
                else:
                    state = 13
            case 9:
                if lexeme[7] == 't':
                    state = 10
                else:
                    state = 13
            case 10:
                if lexeme[8] == 'i':
                    state = 11
                else:
                    state = 13
            case 11:
                if lexeme[9] == "l":
                    state = 12
                else:
                    state = 13
            case 12:
                if lexeme.endswith("l"):
                    return token("loop-un")
                else:
                    state = 13
            case 13:
                return False
            
def _if(lexeme):
    state = 1
    while 1:
        match state:
            case 1:
                if len(lexeme) == 4:
                    state = 2
                else:
                    state = 7
            case 2:
                if lexeme[0] == 'w':
                    state = 3
                else:
                    state = 7
            case 3:
                if lexeme[1] == 'h':
                    state = 4
                else:
                    state = 7
            case 4:
                if lexeme[2] == 'e':
                    state = 5
                else:
                    state = 7
            case 5:
                if lexeme[3] == 'n':
                    state = 6
                else:
                    state = 7
            case 6:
                if lexeme.endswith("n"):
                    return token("when")
                else:
                    state = 7
            case 7:
                return False
def Adad_ashari(lexeme):
    state = 1
    i = 0
    length = len(lexeme)

    while i < length:
        c = lexeme[i]
        match state:
            case 1:
                if c.isdigit():
                    state = 2
                else:
                    state = 5
            case 2:
                if c.isdigit():
                    state = 2
                elif c == '/':
                    state = 3
                else:
                    state = 5
            case 3:
                if c.isdigit():
                    state = 4
                else:
                    state = 5
            case 4:
                if c.isdigit():
                    state = 4
                else:
                    state = 5
            case 5:
                return False
        i += 1

    if state == 4:
        return token("Float")
    else:
        return False
            
def shenase(lexeme):
    state = 1
    i = 0
    l = len(lexeme)

    if len(lexeme) < 5:
        return False

    while i < l:
        c = lexeme[i]
        match state:
            case 1:
                if c == 'I':
                    state = 2
                else:
                    state = 6
            case 2:
                if c == '_':
                    state = 3
                else:
                    state = 6
            case 3:
                if c.isalnum():
                    state = 3
                elif c == '_':
                    state = 4
                else:
                    state = 6
            case 4:
                if c == 'I':
                    state = 5
                else:
                    state = 6
            case 5:
                return token_with_id(lexeme)
            case 6:
                return False
        i += 1

    if state == 5:
        return token_with_id(lexeme)
    else:
        return False

def integer(lexeme):
    state = 1
    i = 0
    l = len(lexeme)

    while i < l:
        c = lexeme[i]

        match state:
            case 1:
                if c.isdigit():
                    state = 2
                else:
                    state = 3  #Tale
            case 2:
                if not c.isdigit():  
                    state = 3
            case 3:
                return False
        i += 1

    if state == 2:  
        return token("INT")
    else:
        return False

def _nope(lexeme):
    state = 1
    while 1:
        match state:
            case 1:
                if len(lexeme) == 4:
                    state = 2
                else:
                    state = 7
            case 2:
                if lexeme[0] == 'n':
                    state = 3
                else:
                    state = 7
            case 3:
                if lexeme[1] == 'o':
                    state = 4
                else:
                    state = 7
            case 4:
                if lexeme[2] == 'p':
                    state = 5
                else:
                    state = 7
            case 5:
                if lexeme[3] == 'e':
                    state = 6
                else:
                    state = 7
            case 6:
                if lexeme.endswith("e"):
                    return token("nope")
                else:
                    state = 7
            case 7:
                return False

def _for(lexeme):
    state = 1
    while 1:
        match state:
            case 1:
                if len(lexeme) == 4:
                    state = 2
                else:
                    state = 7
            case 2:
                if lexeme[0] == 'l':
                    state = 3
                else:
                    state = 7
            case 3:
                if lexeme[1] == 'o':
                    state = 4
                else:
                    state = 7
            case 4:
                if lexeme[2] == 'o':
                    state = 5
                else:
                    state = 7
            case 5:
                if lexeme[3] == 'p':
                    state = 6
                else:
                    state = 7
            case 6:
                if lexeme.endswith("p"):
                    return token("loop")
                else:
                    state = 7
            case 7:
                return False
            
def _make(lexeme):
    state = 1
    while 1:
        match state:
            case 1:
                if len(lexeme) == 4:
                    state = 2
                else:
                    state = 7
            case 2:
                if lexeme[0] == 'm':
                    state = 3
                else:
                    state = 7
            case 3:
                if lexeme[1] == 'a':
                    state = 4
                else:
                    state = 7
            case 4:
                if lexeme[2] == 'k':
                    state = 5
                else:
                    state = 7
            case 5:
                if lexeme[3] == 'e':
                    state = 6
                else:
                    state = 7
            case 6:
                if lexeme.endswith("e"):
                    return token("make")
                else:
                    state = 7
            case 7:
                return False
            
def _call(lexeme):
    state = 1
    while 1:
        match state:
            case 1:
                if len(lexeme) == 4:
                    state = 2
                else:
                    state = 7
            case 2:
                if lexeme[0] == 'c':
                    state = 3
                else:
                    state = 7
            case 3:
                if lexeme[1] == 'a':
                    state = 4
                else:
                    state = 7
            case 4:
                if lexeme[2] == 'l':
                    state = 5
                else:
                    state = 7
            case 5:
                if lexeme[3] == 'l':
                    state = 6
                else:
                    state = 7
            case 6:
                if lexeme.endswith("l"):
                    return token("call")
                else:
                    state = 7
            case 7:
                return False


def _Assignment(lexeme):
    state = 1
    while 1:
        match state:
            case 1:
                if len(lexeme) == 2:
                    state = 2
                else:
                    state = 5
            case 2:
                if lexeme[0] == '-':
                    state = 3
                else:
                    state = 5
            case 3:
                if lexeme[1] == '>':
                    state = 4
                else:
                    state = 5
            case 4:
                if lexeme.endswith('>'):
                    return token("Assign")
                else:
                    state = 5
            case 5:
                return False
            

def mosavi(lexeme):
    if lexeme == '=':
        return token('=')
    return None

def add(lexeme):
    if lexeme == '+':
        return token('+')
    return None
            
def mines(lexeme):
    if lexeme == '-':
        return token('-')
    return None

    
def multi(lexeme):
    if lexeme == '*':
        return token('*')
    return None
            
def dev(lexeme):
    if lexeme == '%':
        return token('%')
    return None

def Bigger(lexeme):
    if lexeme == '>':
        return token('>')
    return None
            
def Smaller(lexeme):
    if lexeme == '<':
        return token('<')
    return None

def token_with_id(lexeme):
    global id_counter, id_map
    if lexeme not in id_map: 
        id_map[lexeme] = f"TK_ID, {id_counter}" 
        id_counter += 1 
    return id_map[lexeme] 

def chainfunctions(item, functions):
    for func in functions:
        result = func(item)
        if result:
            print(f"{item} ==> {result}")
            break
    else:
        print(f"This item ( {item} ) isn't Valid !!!.")

def main(file):
    functions = [_while, _for, _if, _make, _call, _Assignment, _nope, Adad_ashari, mosavi, add, mines, multi, dev, Bigger, Smaller, shenase, integer]
    context = File_input(file)
    for i in context:
        chainfunctions(i, functions)

main("G:\\Compiler\\Code\\input.txt")
