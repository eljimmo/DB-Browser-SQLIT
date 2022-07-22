

txt = "we will use this to help us parse data"

x = txt.split()

print(x)


txt = "we#will#be#using#this#to parse data"

x = txt.split("#",1)

print(x)

txt = "we, will be using python, to parse data, first insert a txt file"

x = txt.split(", ")

print(x)
