# secret code language
import random
s = {"ksj","wgg","jsa","sis","coz","woa","poz","mil","yao","wkq"
    ,"lko","ert","apo","bla","csk","csk","out","ews","iuy","bdt",
     "bng","vcy","poi","vfg","olk","gdd","jhu","lkm","uio"}
a = list(s)

print("\nWelcome to Secret Code Language 🔐")

input("Press Enter to continue... ")
while True:
  errors=[]
  l = input("\n  Encode/ Decode/ Exit \n  Enter C/D/E : ")
  ask = l.upper()
  if ask =="C":
     print("\n🔐 Encoding Mode Selected\n")
     c = input("Enter Your Sentence: ")
     word = c.split()
     print("--- Encoded Sentence ---\n", end=" ")
     for m in word:
         if len(m) < 3:
             print(m[-1] + m[0:-1], end=" ")
         elif len(m) >= 3:
             code = f"{random.choice(a)}{m[1:]}{m[0]}{random.choice(a)}"
             print(code, end=" ")
     print()
     while True:
         choice = input("\nContinue? (Y/N): ").upper()
         if choice == "Y":
             break
         elif choice == "N":
             print("Goodbye 👋")
             exit()
         else:
             print("Invalid input, try again")
  elif ask=="D":
     print("\n📥 Decoding Mode Selected\n")
     d = input("Enter Your Encoded Sentence: ")
     z = d.split()
     print("--- Decoded Sentence ---\n", end=" ")
     for p in z:
         if len(p) < 3:
             print(p[-1] + p[0:-1], end=" ")
         elif len(p) >=8:
             # remove prefix and suffix
             temp = p[3:-3]
             decoded = temp[-1] + temp[0:-1]
             print(decoded, end=" ")
         else:
             errors.append(p)
     print()
     if errors:
         print("\nErrors:", " ".join(errors))
     else:
         print("\nNo errors found")
     while True:
         choice = input("\nContinue? (Y/N): ").upper()
         if choice == "Y":
             break
         elif choice == "N":
             print("Goodbye 👋")
             exit()
  elif ask =="E":
     print("Have a Good Day, Thank You🙏")
     break
  else:
     print("Invalid Input. Please enter C / D / E")
print("\nDone ✅")
