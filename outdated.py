list = [
    "January" ,
    "February" ,
    "March" ,
    "April" ,
    "May" ,
    "June" ,
    "July" ,
    "August" ,
    "September" ,
    "October" ,
    "November" ,
    "December"
]

while True:
    # get users input
    date = input("Date: ").strip()
    #first try xx/xx/xxxx
    try:
        month, day, year = date.split("/")

        #check 1<=month<=12 and 1<=day<=31
        if 1 <= int(month) <=12 and 1 <= int(day) <= 31:
            month = int(month)
            day = int(day)
            print(f"{year}-{month:02}-{day:02}")
            break
        else:
            pass

    except:
        #second try month day, year
        try:
            secmonth, secday, secyear = date.split(" ")
            secyear = int(secyear)
            if secmonth in list:
                #check if , in second str
                if ',' in secday:
                    secday = int(secday.replace(',', ''))
                    m = list.index(secmonth)
                    if 1 <= secday <= 31 and 0<=m<=11:

                        print(f"{secyear}-{m+1:02}-{secday:02}")
                        break

                    else:
                        pass
                else:
                    pass
            else:
                pass

        except:
            #neither of two format of input
            print("\n")
            pass




