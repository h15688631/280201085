books = ["ULYSSES","ANIMAL FARM","BRAVE NEW WORLD","ENDER'S GAME"]
book_dict = {}
for i in books:
  book_dict[i] = 'value'
  value = len(i)
  unique_ch = len(set(i))
  book_dict[i] = (value,unique_ch)
print(book_dict)