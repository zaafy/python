def sanitize(text):
  return text.replace(' ', '').lower()

def objectCreator(text, size):
  dict = {}
  data = sanitize(text)
  for i in range(0, len(data) - size + 1):
    ngram = data[i:i+size]
    if ngram in dict:
      dict[ngram] += 1
    else:
      dict[ngram] = 1
    i += 1
  return dict

text = input("Write down the sequence of words delimited by space\n")
size = int(input("Write size of n-grams\n"))
print(objectCreator(text, size))

