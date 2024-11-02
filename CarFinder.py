AllowedVehicleList=["Ford F-150" , "Chevrolet Silverado" , "Tesla CyberTruck" , "Toyota Tundra" , "Nissan Titan"]
def menu():
    print("*" * 32)
    print("Auto Country Vehicle Finder v0.2")
    print("*" * 32)
    print("Please Enter the following number below from the following menu:")
    print()

    print("1.PRINT all Authorized Vehicles")
    print("2.SEARCH for Authorized Vehicles")
    print("3.Exit")
menu()
choice=int(input())

if choice==1:
    print("The AutoCountry sales manager has authorized the purchase and sale of the following vehicles:")
    for v in AllowedVehicleList:
        print(v)
    
elif(choice==2):
    print('\033[1m' +"Please enter the full vehicle name."+'\033[0m')
    vname=input()
    if vname in AllowedVehicleList:
        print(f'{vname} is an authorized vehicle')
        menu()
        choice=int(input())
    else:
        print(f'{vname} is not an authorized vehicle, if you received this in error please check the spelling and try again')
        menu()
        choice=int(input())
else:
    print("Thank you for using the AutoCountry Vehicle Finder,goodbye!") 
