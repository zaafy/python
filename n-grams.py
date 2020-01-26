def sanitize(text):
  return text.replace(' ', '').lower()

def objectCreator(text):
  dict = {}
  data = sanitize(text)
  for i in range(0, len(data) - 2):
    ngram = data[i:i+3]
    if ngram in dict:
      dict[ngram] += 1
    else:
      dict[ngram] = 1
    i += 1
  return dict

text = input("Write down the sequence of words delimited by space\n")
print(objectCreator(text))

