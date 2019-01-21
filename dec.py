nos = "jgjemnijkn"
nos = list(nos)
string = ""
for i in range (len(nos)):
    string += str(ord(nos[i]) - 97 - i)
print(string,nos)
