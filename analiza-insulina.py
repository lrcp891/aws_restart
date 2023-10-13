f = open('./preproinsulin-seq.txt','r')
a = [' ','0','1','2','3','4','5','6','7','8','9','/','ORIGIN','\n']
lst = []
for line in f:
    for word in a:
        if word in line:
            line = line.replace(word,'')
    lst.append(line)
f.close()
f = open('./preproinsulin-seq-clean.txt','w')
for line in lst:
    f.write(line)
f.close()

# open and read file, and save content as a variable to know string length 
with open('./preproinsulin-seq-clean.txt','r') as f:
    content=f.read()
print("El largo de preproinsulina es {}. La cadena es: {}".format(len(content),content))

#lsinsulin-seq-clean.txt -----------------------------------------
with open('./lsinsulin-seq-clean.txt','w') as f:
    f.write(content[0:24])
with open('./lsinsulin-seq-clean.txt','r') as f:
    contentL=f.read()
print("El largo de linsulina es {}. La cadena es: {}".format(len(contentL),contentL))


#binsulin-seq-clean.txt -------------------------------------------
with open('./binsulin-seq-clean.txt','w') as f:
    f.write(content[24:54])
with open('./binsulin-seq-clean.txt','r') as f:
    contentB=f.read()
print("El largo de binsulina es {}. La cadena es: {}".format(len(contentB),contentB))

#cinsulin-seq-clean.txt --------------------------------------------
with open('./cinsulin-seq-clean.txt','w') as f:
    f.write(content[54:89])
with open('./cinsulin-seq-clean.txt','r') as f:
    contentC=f.read()
print("El largo de cinsulina es {}. La cadena es: {}".format(len(contentC),contentC))

#ainsulin-seq-clean.txt --------------------------------------------
with open('./ainsulin-seq-clean.txt','w') as f:
    f.write(content[89:110])
with open('./ainsulin-seq-clean.txt','r') as f:
    contentA=f.read()
print("El largo de ainsulina es {} La cadena es: {}".format(len(contentA),contentA))

f.close()

