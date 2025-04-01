def temp_conversion():
    print(f"celsius | farrenheit")
    celsius:int = 0
    while celsius <30:
        

        for celsius in range (10,31,5):
            farenheit = celsius*(9/5)+32
            print (str(celsius), str(farenheit))
     
temp_conversion()