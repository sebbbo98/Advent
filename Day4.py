f=open(r"/content/Day4.txt", 'r', encoding='utf-8')
passport=f.read()

passport=passport.split("\n\n")
Noofvalidpw=0
for i in range(len(passport)):

  if "eyr:" in passport[i]:
    if "iyr:" in passport[i]:
      if "byr:" in passport[i]:
        if "ecl:" in passport[i]:
          if "pid:" in passport[i]:
            if "hcl:" in passport[i]:
              if "hgt" in passport[i]:
                Noofvalidpw+=1 



print(passport)
print(Noofvalidpw)
