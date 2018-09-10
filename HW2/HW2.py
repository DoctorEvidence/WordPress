#caluclates the n grams of input with given n value

def ngrams(input, n):
  input = input.split(' ')
  output = {}
  for i in range(len(input)-n+1):
    g = ' '.join(input[i:i+n])
    output.setdefault(g, 0)
    output[g] += 1
  return output

num = input("enter the 'n' gram \n")

filename = raw_input("please enter the file you wish to encrypt \n")

with open(filename, 'r') as myFile:
    data = myFile.read().replace('\n', '')
    print(data)

print(ngrams(data, num))

#prints the frequency of individual chatacters within the given string

def char_frequency(str1):
    dict = {}
    for n in str1:
        keys = dict.keys()
        if n in keys:
            dict[n] += 1
        else:
            dict[n] = 1
    return dict
    
print(char_frequency(data))