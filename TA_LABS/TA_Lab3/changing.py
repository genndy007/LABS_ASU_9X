with open("words.txt") as f:
    old_data = f.read()

new_data = old_data.replace('eh;kO05^,w^Ir/[Oovfo', 'на_что_меняем')

with open ('words.txt', 'w') as f:
  f.write(new_data)