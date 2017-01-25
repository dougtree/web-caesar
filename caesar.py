def encrypt(text,rot):
  enc =''
  for i in text:
    enc = enc + rotate_character(i,rot)
  return enc

alphabet = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'

def alphabet_position(char):
  for i in range(len(alphabet)):
    if char==alphabet[i]:
      return i
  else:
      return char

def rotate_character(char, n):
  pos = alphabet_position(char)
  index =0
  posit = n%26
  if char.isalpha():
    if (pos>25 and pos+posit>51):
      newLocation = alphabet[(pos+posit)%26+ 26]
    elif(pos>25 and pos+posit<=51):
      newLocation = alphabet[pos+posit]
    elif (pos+posit > 25):
      newLocation = alphabet[(pos+posit)%26]
    else:
        newLocation = alphabet[pos+posit]
    return newLocation
  else:
    return char
