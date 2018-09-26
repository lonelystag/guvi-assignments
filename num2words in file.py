import num2word
file=open("sample.txt","r")
lines=file.readlines()
file.close()
file=open("sample.txt","w")
file.write(num2words(lines))
f.close
