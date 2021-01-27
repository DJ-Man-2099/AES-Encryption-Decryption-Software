from copy import deepcopy

S_Box = [
    ['63', '7c', '77', '7b', 'f2', '6b', '6f', 'c5',
        '30', '01', '67', '2b', 'fe', 'd7', 'ab', '76'],
    ['CA', '82', 'C9', '7D', 'FA', '59', '47', 'F0',
        'AD', 'D4', 'A2', 'AF', '9C', 'A4', '72', 'C0', ],
    ['B7', 'FD', '93', '26', '36', '3F', 'F7', 'CC',
        '34', 'A5', 'E5', 'F1', '71', 'D8', '31', '15', ],
    ['04', 'C7', '23', 'C3', '18', '96', '05', '9A',
        '07', '12', '80', 'E2', 'EB', '27', 'B2', '75', ],
    ['09', '83', '2C', '1A', '1B', '6E', '5A', 'A0',
        '52', '3B', 'D6', 'B3', '29', 'E3', '2F', '84', ],
    ['53', 'D1', '00', 'ED', '20', 'FC', 'B1', '5B',
        '6A', 'CB', 'BE', '39', '4A', '4C', '58', 'CF', ],
    ['D0', 'EF', 'AA', 'FB', '43', '4D', '33', '85',
        '45', 'F9', '02', '7F', '50', '3C', '9F', 'A8', ],
    ['51', 'A3', '40', '8F', '92', '9D', '38', 'F5',
        'BC', 'B6', 'DA', '21', '10', 'FF', 'F3', 'D2', ],
    ['CD', '0C', '13', 'EC', '5F', '97', '44', '17',
        'C4', 'A7', '7E', '3D', '64', '5D', '19', '73', ],
    ['60', '81', '4F', 'DC', '22', '2A', '90', '88',
        '46', 'EE', 'B8', '14', 'DE', '5E', '0B', 'DB', ],
    ['E0', '32', '3A', '0A', '49', '06', '24', '5C',
        'C2', 'D3', 'AC', '62', '91', '95', 'E4', '79', ],
    ['E7', 'C8', '37', '6D', '8D', 'D5', '4E', 'A9',
        '6C', '56', 'F4', 'EA', '65', '7A', 'AE', '08', ],
    ['BA', '78', '25', '2E', '1C', 'A6', 'B4', 'C6',
        'E8', 'DD', '74', '1F', '4B', 'BD', '8B', '8A', ],
    ['70', '3E', 'B5', '66', '48', '03', 'F6', '0E',
        '61', '35', '57', 'B9', '86', 'C1', '1D', '9E', ],
    ['E1', 'F8', '98', '11', '69', 'D9', '8E', '94',
        '9B', '1E', '87', 'E9', 'CE', '55', '28', 'DF', ],
    ['8C', 'A1', '89', '0D', 'BF', 'E6', '42', '68',
        '41', '99', '2D', '0F', 'B0', '54', 'BB', '16'],
]

Inv_S_Box = [
    ['52', '09', '6A', 'D5', '30', '36', 'A5', '38',
        'BF', '40', 'A3', '9E', '81', 'F3', 'D7', 'FB', ],
    ['7C', 'E3', '39', '82', '9B', '2F', 'FF', '87',
        '34', '8E', '43', '44', 'C4', 'DE', 'E9', 'CB', ],
    ['54', '7B', '94', '32', 'A6', 'C2', '23', '3D',
        'EE', '4C', '95', '0B', '42', 'FA', 'C3', '4E', ],
    ['08', '2E', 'A1', '66', '28', 'D9', '24', 'B2',
        '76', '5B', 'A2', '49', '6D', '8B', 'D1', '25', ],
    ['72', 'F8', 'F6', '64', '86', '68', '98', '16',
        'D4', 'A4', '5C', 'CC', '5D', '65', 'B6', '92', ],
    ['6C', '70', '48', '50', 'FD', 'ED', 'B9', 'DA',
        '5E', '15', '46', '57', 'A7', '8D', '9D', '84', ],
    ['90', 'D8', 'AB', '00', '8C', 'BC', 'D3', '0A',
        'F7', 'E4', '58', '05', 'B8', 'B3', '45', '06', ],
    ['D0', '2C', '1E', '8F', 'CA', '3F', '0F', '02',
        'C1', 'AF', 'BD', '03', '01', '13', '8A', '6B', ],
    ['3A', '91', '11', '41', '4F', '67', 'DC', 'EA',
        '97', 'F2', 'CF', 'CE', 'F0', 'B4', 'E6', '73', ],
    ['96', 'AC', '74', '22', 'E7', 'AD', '35', '85',
        'E2', 'F9', '37', 'E8', '1C', '75', 'DF', '6E', ],
    ['47', 'F1', '1A', '71', '1D', '29', 'C5', '89',
        '6F', 'B7', '62', '0E', 'AA', '18', 'BE', '1B', ],
    ['FC', '56', '3E', '4B', 'C6', 'D2', '79', '20',
        '9A', 'DB', 'C0', 'FE', '78', 'CD', '5A', 'F4', ],
    ['1F', 'DD', 'A8', '33', '88', '07', 'C7', '31',
        'B1', '12', '10', '59', '27', '80', 'EC', '5F', ],
    ['60', '51', '7F', 'A9', '19', 'B5', '4A', '0D',
        '2D', 'E5', '7A', '9F', '93', 'C9', '9C', 'EF', ],
    ['A0', 'E0', '3B', '4D', 'AE', '2A', 'F5', 'B0',
        'C8', 'EB', 'BB', '3C', '83', '53', '99', '61', ],
    ['17', '2B', '04', '7E', 'BA', '77', 'D6', '26',
        'E1', '69', '14', '63', '55', '21', '0C', '7D'],
]

Mix_Column_Mat = [
    ['02', '03', '01', '01'],
    ['01', '02', '03', '01'],
    ['01', '01', '02', '03'],
    ['03', '01', '01', '02'],
]

Inv_Mix_Column_Mat = [
    ['0E', '0B', '0D', '09'],
    ['09', '0E', '0B', '0D'],
    ['0D', '09', '0E', '0B'],
    ['0B', '0D', '09', '0E'],
]

R_Const = ['01', '02', '04', '08', '10', '20', '40', '80', '1b', '36']

denom = [1, 0, 0, 0, 1, 1, 0, 1, 1]


def AES(basePlain, baseKey, mode=True):
    """
    This is the AES main Method
    """
    # preparing the plain text and the key, in Hex form
    plain = []
    key = []
    rounds = 10
    for j in range((len(basePlain))//8):
        plain.append([basePlain[j*8+i*2:j*8+i*2+2] for i in range(4)])
    for j in range((len(baseKey))//8):
        key.append([baseKey[j*8+i*2:j*8+i*2+2] for i in range(4)])
    key = KeyExpansion(key, rounds)
    if mode:  # encryption
        plain = AddRoundKey(plain, key[0])
        for r in range(rounds-1):
            plain = AESRound(plain, key[r+1])
        plain = FinalRound(plain, key[-1])
    else:  # decryption
        plain = AddRoundKey(plain, key[-1])
        for r in reversed(range(1,rounds)):
            plain = AESInvRound(plain, key[r])
        plain=InvFinalRound(plain,key[0])
    return ''.join([''.join(i) for i in plain])

def FinalRound(plain, key):
    for i in range(len(plain)):
        plain[i]=S_Box_F(plain[i])
    plain = ShiftRows(plain)
    plain = AddRoundKey(plain, key)
    return plain

def InvFinalRound(plain, key):
    plain = InvShiftRows(plain)
    for i in range(len(plain)):
        plain[i]=Inv_S_Box_F(plain[i])
    plain = AddRoundKey(plain, key)
    return plain


def S_Box_F(input):
    """
    This is the S-BOX method
    """
    temp = []
    for i in input:
        temp.append(S_Box[HextoDecimal(i[0])][HextoDecimal(i[1])])
    return temp


def Inv_S_Box_F(input):
    """
    This is the Inverse S-BOX method
    """
    temp = []
    for i in input:
        temp.append(Inv_S_Box[HextoDecimal(i[0])][HextoDecimal(i[1])])
    return temp


def Shift(input):
    """
    This is the row Shifting method
    """
    temp = input[0]
    for i in range(len(input)-1):
        input[i] = input[i+1]
    input[-1] = temp
    return input


def MixColumn(input):
    """
    This is the Mix Column method
    """
    temp = []
    for i in range(len(Mix_Column_Mat)):
        t2 = [0]*8
        for j in range(len(Mix_Column_Mat[i])):
            t3 = GFMultiplication(input[j], Mix_Column_Mat[i][j])
            t2 = GFAddition(t2, HextoBinary(t3))
        temp.append(BinarytoHex(t2))
    return temp


def InvMixColumn(input):
    """
    This is the Inverse Mix Column method
    """
    temp = []
    for i in range(len(Inv_Mix_Column_Mat)):
        t2 = [0]*8
        for j in range(len(Inv_Mix_Column_Mat[i])):
            t3 = GFMultiplication(input[j], Inv_Mix_Column_Mat[i][j])
            t2 = GFAddition(t2, HextoBinary(t3))
        temp.append(BinarytoHex(t2))
    return temp


def AddRoundKey(input, key):
    """
    This is the Adding Round Key method
    """
    temp = []
    for i in range(len(input)):
        temp.append(WordXOR(input[i], key[i]))
    return temp


def KeyExpansion(baseKey, rounds):
    """
    this is the Key Expansion method
    """
    # TODO: Test it
    temp = []
    temp.append(baseKey)
    for i in range(rounds):
        t2 = []
        # initial row, in new key
        t2.append(KeyExpansionRound(temp[i][-1], i, temp[i][0]))
        for j in range(1, 4):
            # the remaining rows
            t2.append(WordXOR(t2[j-1], temp[i][j]))
        temp.append(t2)
    return temp


def KeyExpansionRound(keyRow, index, firstRow):
    """
    this is the per interation Key Expansion method for first row
    """
    # TODO: Test it
    # Shift Round
    temp = deepcopy(keyRow)
    temp = Shift(temp)
    # S-Box Substitution
    temp = S_Box_F(temp)
    # XOR with key constant
    temp = WordXOR(temp, [R_Const[index]]+['00']*3)
    # XOR with original key
    temp = WordXOR(temp, firstRow)
    return temp


def WordXOR(in1, in2):
    """
    This is the XOR operation, done on a whole word (4 Bytes)
    """
    in1 = [HextoBinary(i) for i in in1]
    in2 = [HextoBinary(i) for i in in2]
    temp = []
    for i in range(len(in1)):
        temp.append(XOR(in1[i], in2[i]))
    return [BinarytoHex(i) for i in temp]


def XOR(in1, in2):
    """
    This is the XOR operation, done on a single Byte
    """
    return [in1[j] ^ in2[j] for j in range(len(in1))]


def HextoBinary(hex):
    """
    This Funcion converts the hex number to an array of binary numbers
    """
    temp = []
    for H in hex:
        temp += [int(i) for i in format(int(str(H), 16), '#06b')[2:]]
    return temp


def HextoDecimal(hex):
    """
    This Function returns the decimal value of the Hex input
    """
    return int(str(hex), 16)


def BinarytoDecimal(BinaryList):
    """
    This function converts the BinaryList to a decimal number
    """
    return int(''.join([str(i) for i in BinaryList]), 2)


def BinarytoHex(BinaryList):
    """
    This function converts a list of binary numbers into a hexadecimal number
    """
    return format(int(''.join([str(i) for i in BinaryList]), 2), '#04x')[2:].upper()


def AESRound(input, key):
    """
    This is the function of the nth round of the AES Encryption
    """
    # TODO: Test it
    temp = []
    for i in input:
        temp.append(S_Box_F(i))
    temp = ShiftRows(temp)
    for i in range(len(temp)):
        temp[i] = MixColumn(temp[i])
    temp = AddRoundKey(temp, key)
    return temp


def AESInvRound(input, key):
    """
    This is the function of the nth round of the AES Decryption
    """
    # TODO: Test it
    temp = InvShiftRows(input)
    for i in range(len(temp)):
        temp[i]=(Inv_S_Box_F(temp[i]))
    temp = AddRoundKey(temp, key)
    for i in range(len(temp)):
        temp[i] = InvMixColumn(temp[i])
    return temp


def GFMultiplication(in1, in2):
    """
    This Function multiplies 2 Bytes (Binary Arrays), in GF(2^8),

    with the Denom for XORing
    """
    in1 = HextoBinary(in1)
    in2 = HextoBinary(in2)
    temp = [0]*8
    for index in reversed(range(len(in2))):
        if in2[index] == 0:
            continue
        # Step1: Multiplying and XORing {if needed}
        result = Multi(in1, len(in2)-index-1, denom)
        # Step2: Adding (XORing)
        temp = GFAddition(temp, result)
        # Step3: Repeating Steps 1 to 3 (for 1's in in2 only)
    return BinarytoHex(temp)


def GFAddition(in1, in2):
    """
    This functions adds 2 Bytes (Binary Arrays), in GF(2^8)
    """
    return XOR(in1, in2)


def Multi(Binary, shifts, denom):
    """
    This Function Shifts, and XORs with Denomirator {GF Multiplication}
    """
    temp = deepcopy(Binary)
    for i in range(shifts):
        temp.append(0)
        if temp[0] == 1:
            temp = XOR(temp, denom)
        temp = temp[1:]
    return temp


def ShiftRows(Words):
    """
    This is the Shift Rows Function

    takes the whole 4 Words block
    """
    # TODO: Test it
    for i in range(len(Words)):
        for j in range(i):
            temp = Words[0][i]
            for k in range(len(Words[i])-1):
                Words[k][i] = Words[k+1][i]
            Words[-1][i] = temp
    return Words


def InvShiftRows(Words):
    """
    This is the Shift Rows Function

    takes the whole 4 Words block
    """
    # TODO: Test it
    for i in range(len(Words)):
        for j in range(i):
            temp = Words[-1][i]
            for k in reversed(range(len(Words[i])-1)):
                Words[k+1][i] = Words[k][i]
            Words[0][i] = temp
    return Words

request=''
print('This is the AES Encryption/Decryption Software')
while request != 'e':
    request=input('Please enter "s" to start, or "e" to exit: ')
    while request not in ['e','s']:
        print("invalid input, please try again")
        request=input('Please enter "s" to start, or "e" to exit: ')
    if request == 'e':
        break
    mode = input("Please enter 'e' for encryption, or 'd' for decryption: ")
    while mode not in ['e','d']:
        print("invalid input, please try again")
        mode = input("Please enter 'e' for encryption, or 'd' for decryption: ")
    Plain = input("Please enter Plain Text, in Hexadecimal form (must be of 32 characters): ")
    Key = input("Please enter the Key, in Hexadecimal form (must be of 32 characters): ")
    Cipher = AES(Plain,Key,mode=='e')
    print(f'The Result of your operation is {Cipher}')


