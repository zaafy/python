def word_extraction(sentence):
  words = sentence.split()
  cleaned_text =  [w.lower() for w in words]
  return cleaned_text

def objectCreator(text):
  dict = {}
  cleaned_text = word_extraction(text)
  for word in cleaned_text:
    if word in dict:
      dict[word] += 1
    else:
      dict[word] = 1
  return dict

text = input("Write down the sequence of words delimited by space\n")
print(objectCreator(text))

