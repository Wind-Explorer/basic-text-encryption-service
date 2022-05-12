versionNumber='1.0'

def main():

    architecture=8
    openTeskey=open('data.teskey', 'r')
    rawTeskey=openTeskey.read()
    teskey=[rawTeskey[i:i+architecture] for i in range(0, len(rawTeskey), architecture)]
    binary_1=teskey[1]
    binary_2=teskey[2]
    binary_3=teskey[3]
    binary_4=teskey[4]
    binary_5=teskey[5]
    binary_6=teskey[6]
    binary_7=teskey[7]
    binary_8=teskey[8]
    binary_9=teskey[9]
    binary_0=teskey[10]
    binary_A=teskey[11]
    binary_B=teskey[12]
    binary_C=teskey[13]
    binary_D=teskey[14]
    binary_E=teskey[15]
    binary_F=teskey[16]
    binary_G=teskey[17]
    binary_H=teskey[18]
    binary_I=teskey[19]
    binary_J=teskey[20]
    binary_K=teskey[21]
    binary_L=teskey[22]
    binary_M=teskey[23]
    binary_N=teskey[24]
    binary_O=teskey[25]
    binary_P=teskey[26]
    binary_Q=teskey[27]
    binary_R=teskey[28]
    binary_S=teskey[29]
    binary_T=teskey[30]
    binary_U=teskey[31]
    binary_V=teskey[32]
    binary_W=teskey[33]
    binary_X=teskey[34]
    binary_Y=teskey[35]
    binary_Z=teskey[36]
    binary_a=teskey[37]
    binary_b=teskey[38]
    binary_c=teskey[39]
    binary_d=teskey[40]
    binary_e=teskey[41]
    binary_f=teskey[42]
    binary_g=teskey[43]
    binary_h=teskey[44]
    binary_i=teskey[45]
    binary_j=teskey[46]
    binary_k=teskey[47]
    binary_l=teskey[48]
    binary_m=teskey[49]
    binary_n=teskey[50]
    binary_o=teskey[51]
    binary_p=teskey[52]
    binary_q=teskey[53]
    binary_r=teskey[54]
    binary_s=teskey[55]
    binary_t=teskey[56]
    binary_u=teskey[57]
    binary_v=teskey[58]
    binary_w=teskey[59]
    binary_x=teskey[60]
    binary_y=teskey[61]
    binary_z=teskey[62]
    binary_GRAVE=teskey[63]
    binary_TILDE=teskey[64]
    binary_EXCLAMATION=teskey[65]
    binary_AT=teskey[66]
    binary_TAG=teskey[67]
    binary_DOLLAR=teskey[68]
    binary_PERCENTAGE=teskey[69]
    binary_CARET=teskey[70]
    binary_AMPERSAND=teskey[71]
    binary_ASTERISK=teskey[72]
    binary_LBRAKET=teskey[73]
    binary_RBRAKET=teskey[74]
    binary_HYPHEN=teskey[75]
    binary_UNDERSCORE=teskey[76]
    binary_EQUAL=teskey[77]
    binary_PLUS=teskey[78]
    binary_LSQUAREBRAKET=teskey[79]
    binary_LCURLYBRAKET=teskey[80]
    binary_RSQUAREBRAKET=teskey[81]
    binary_RCURLYBRAKET=teskey[82]
    binary_VERTICALBAR=teskey[84]
    binary_SEMICOLON=teskey[85]
    binary_COLON=teskey[86]
    binary_APOSTROPHE=teskey[87]
    binary_QUOTATION=teskey[88]
    binary_COMMA=teskey[89]
    binary_LESSTHAN=teskey[90]
    binary_FULLSTOP=teskey[91]
    binary_MORETHAN=teskey[92]
    binary_SLASH=teskey[93]
    binary_QUESTION=teskey[94]
    binary_SPACE=teskey[0]

    def endProcess():
        openTeskey.close()
        print('\n' * 200)
        exit()

    def chooseAction1():
        print('\n' * 200)
        print('Text Encryption Service Version {}'.format(versionNumber))
        encryptOrDecrypt=input('Do you want to encrypt or decrypt data?\n\n1. Decrypt something\n\n2. Encrypt something\n\n3. Exit\n\nEnter an option: ')
        if encryptOrDecrypt=='1':
            chooseDataDecrypt()
        elif encryptOrDecrypt=='2':
            chooseDataEncrypt()
        elif encryptOrDecrypt=='3':
            endProcess()
        else:
            print('\nThat is not an option!\n')
            chooseAction1()

    def whatToDoNext():
        whatNextUserOption=input('What next?\n\n1. Encrypt something\n\n2. Decrypt something\n\n3. Exit\n\nEnter an option: ')
        if whatNextUserOption=='1':
            chooseDataEncrypt()
        elif whatNextUserOption=='2':
            chooseDataDecrypt()
        elif whatNextUserOption=='3':
            endProcess()
        else:
            print('\nInvalid option!\n\n')
            whatToDoNext()

    def chooseDataEncrypt():
        print('\n' * 200)
        userInputEncrypt=input('Enter the data you wish to encrypt: ')
        def decode(data):
            return list(data)
        encodedData=(decode(userInputEncrypt))
        encodedData=[binary_SPACE if i==' '
        else binary_1 if i=='1'
        else binary_2 if i=='2'
        else binary_3 if i=='3'
        else binary_4 if i=='4'
        else binary_5 if i=='5'
        else binary_6 if i=='6'
        else binary_7 if i=='7'
        else binary_8 if i=='8'
        else binary_9 if i=='9'
        else binary_0 if i=='0'
        else binary_A if i=='A'
        else binary_B if i=='B'
        else binary_C if i=='C'
        else binary_D if i=='D' 
        else binary_E if i=='E'
        else binary_F if i=='F' 
        else binary_G if i=='G'
        else binary_H if i=='H' 
        else binary_I if i=='I' 
        else binary_J if i=='J' 
        else binary_K if i=='K' 
        else binary_L if i=='L'
        else binary_M if i=='M' 
        else binary_N if i=='N'
        else binary_O if i=='O'
        else binary_P if i=='P'
        else binary_Q if i=='Q'
        else binary_R if i=='R'
        else binary_S if i=='S'
        else binary_T if i=='T'
        else binary_U if i=='U'
        else binary_V if i=='V'
        else binary_W if i=='W'
        else binary_X if i=='X'
        else binary_Y if i=='Y'
        else binary_Z if i=='Z'
        else binary_a if i=='a'
        else binary_b if i=='b'
        else binary_c if i=='c'
        else binary_d if i=='d'
        else binary_e if i=='e'
        else binary_f if i=='f'
        else binary_g if i=='g'
        else binary_h if i=='h'
        else binary_i if i=='i'
        else binary_j if i=='j'
        else binary_k if i=='k'
        else binary_l if i=='l'
        else binary_m if i=='m'
        else binary_n if i=='n'
        else binary_o if i=='o'
        else binary_p if i=='p'
        else binary_q if i=='q'
        else binary_r if i=='r'
        else binary_s if i=='s'
        else binary_t if i=='t'
        else binary_u if i=='u'
        else binary_v if i=='v'
        else binary_w if i=='w'
        else binary_x if i=='x'
        else binary_y if i=='y'
        else binary_z if i=='z'
        else binary_GRAVE if i=='`'
        else binary_TILDE if i=='~'
        else binary_EXCLAMATION if i=='!'
        else binary_AT if i=='@'
        else binary_TAG if i=='#'
        else binary_DOLLAR if i=='$'
        else binary_PERCENTAGE if i=='%'
        else binary_CARET if i=='^'
        else binary_AMPERSAND if i=='&'
        else binary_ASTERISK if i=='*'
        else binary_LBRAKET if i=='('
        else binary_RBRAKET if i==')'
        else binary_HYPHEN if i=='-'
        else binary_UNDERSCORE if i=='_'
        else binary_EQUAL if i=='='
        else binary_PLUS if i=='+'
        else binary_LSQUAREBRAKET if i=='['
        else binary_LCURLYBRAKET if i=='{'
        else binary_RSQUAREBRAKET if i==']'
        else binary_RCURLYBRAKET if i=='}'
        else binary_VERTICALBAR if i=='|'
        else binary_SEMICOLON if i==';'
        else binary_COLON if i==':'
        else binary_APOSTROPHE if i=="'"
        else binary_QUOTATION if i=='"'
        else binary_COMMA if i==','
        else binary_LESSTHAN if i=='<'
        else binary_FULLSTOP if i=='.'
        else binary_MORETHAN if i=='>'
        else binary_SLASH if i=='/'
        else binary_QUESTION if i=='?'
        else i for i in encodedData]
        print('\n' * 200)
        print('Data encoded:\n\n{}\n'.format(''.join(encodedData)))
        whatToDoNext()

    def chooseDataDecrypt():
        print('\n' * 200)
        userInputDecrypt=input('Enter the data you wish to decrypt: ')
        decodedData=[userInputDecrypt[i:i+architecture] for i in range(0, len(userInputDecrypt), architecture)]
        decodedData=[' ' if i==binary_SPACE
        else '1' if i==binary_1
        else '2' if i==binary_2
        else '3' if i==binary_3
        else '4' if i==binary_4
        else '5' if i==binary_5
        else '6' if i==binary_6
        else '7' if i==binary_7
        else '8' if i==binary_8
        else '9' if i==binary_9
        else '0' if i==binary_0
        else 'A' if i==binary_A
        else 'B' if i==binary_B
        else 'C' if i==binary_C
        else 'D' if i==binary_D
        else 'E' if i==binary_E
        else 'F' if i==binary_F 
        else 'G' if i==binary_G
        else 'H' if i==binary_H 
        else 'I' if i==binary_I 
        else 'J' if i==binary_J 
        else 'K' if i==binary_K 
        else 'L' if i==binary_L
        else 'M' if i==binary_M 
        else 'N' if i==binary_N
        else 'O' if i==binary_O
        else 'P' if i==binary_P
        else 'Q' if i==binary_Q
        else 'R' if i==binary_R
        else 'S' if i==binary_S
        else 'T' if i==binary_T
        else 'U' if i==binary_U
        else 'V' if i==binary_V
        else 'W' if i==binary_W
        else 'X' if i==binary_X
        else 'Y' if i==binary_Y
        else 'Z' if i==binary_Z
        else 'a' if i==binary_a
        else 'b' if i==binary_b
        else 'c' if i==binary_c
        else 'd' if i==binary_d
        else 'e' if i==binary_e
        else 'f' if i==binary_f
        else 'g' if i==binary_g
        else 'h' if i==binary_h
        else 'i' if i==binary_i
        else 'j' if i==binary_j
        else 'k' if i==binary_k
        else 'l' if i==binary_l
        else 'm' if i==binary_m
        else 'n' if i==binary_n
        else 'o' if i==binary_o
        else 'p' if i==binary_p
        else 'q' if i==binary_q
        else 'r' if i==binary_r
        else 's' if i==binary_s
        else 't' if i==binary_t
        else 'u' if i==binary_u
        else 'v' if i==binary_v
        else 'w' if i==binary_w
        else 'x' if i==binary_x
        else 'y' if i==binary_y
        else 'z' if i==binary_z
        else '`' if i==binary_GRAVE
        else '~' if i==binary_TILDE
        else '!' if i==binary_EXCLAMATION
        else '@' if i==binary_AT
        else '#' if i==binary_TAG
        else '$' if i==binary_DOLLAR
        else '%' if i==binary_PERCENTAGE
        else '^' if i==binary_CARET
        else '&' if i==binary_AMPERSAND
        else '*' if i==binary_ASTERISK
        else '(' if i==binary_LBRAKET
        else ')' if i==binary_RBRAKET
        else '-' if i==binary_HYPHEN
        else '_' if i==binary_UNDERSCORE
        else '=' if i==binary_EQUAL
        else '+' if i==binary_PLUS
        else '[' if i==binary_LSQUAREBRAKET
        else '{' if i==binary_LCURLYBRAKET
        else ']' if i==binary_RSQUAREBRAKET
        else '}' if i==binary_RCURLYBRAKET
        else '|' if i==binary_VERTICALBAR
        else ';' if i==binary_SEMICOLON
        else ':' if i==binary_COLON
        else "'" if i==binary_APOSTROPHE
        else '"' if i==binary_QUOTATION
        else ',' if i==binary_COMMA
        else '<' if i==binary_LESSTHAN
        else '.' if i==binary_FULLSTOP
        else '>' if i==binary_MORETHAN
        else '/' if i==binary_SLASH
        else '?' if i==binary_QUESTION
        else i for i in decodedData]
        print('\n' * 200)
        print('Data decoded:\n\n{}\n'.format(''.join(decodedData)))
        whatToDoNext()

    chooseAction1()

main()
