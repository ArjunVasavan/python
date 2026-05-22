emojy = {
        ":)" : "😀",
        ":(" : "😔",
        ":()": "🫨",
        ":/": "😕"
        }

message = input("-> ")

words = message.split(" ")  #  it goes through string and whenevr it finds " " it will seperate it

print(words)

output = ""

for key in words:
   output+=emojy.get(key,key) + " "

print(output)

