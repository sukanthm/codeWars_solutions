def decodeBits(a):
    return a.strip('0')[::min([len(x) for x in a.strip('0').split('0') if x!='']+[len(x) for x in a.strip('0').split('1') if x!=''])].replace('111', '-').replace('1','.').replace('0000000','   ').replace('000',' ').replace('0','')

def decodeMorse(morseCode):
    return ' '.join(''.join(MORSE_CODE[letter] for letter in word.split(' ')) for word in morseCode.strip().split('   '))
