print("Spark Mart")
print("-----------------------------------------------------------------","Welcome to Spark Mart","------------------------------------------------------------------------")
print("\n","Product Lists:")
print()
print("(1)Mobiles","(2)Mobile Chargers","(3)TV","(4)TV Remote",sep="\t")
print()
mobiles={"redmi":{"Brand name:":"Redmi","Model name:":"Note 10","Product ID:":"001","Actual Price:":"20000","Discount:":"5%"},"Vivo":{"Brand name:":"Vivo","Model name:":"V8","Product ID:":"002","Actual Price:":"20000","Discount:":"5%"},"Realme":{"Brand name:":"Realme","Model name:":"F3","Product ID:":"003","Actual Price:":"25000","Discount:":"5%"},"Poco":{"Brand name:":"Poco","Model name:":"X17 Pro","Product ID:":"004","Actual Price:":"25000","Discount:":"5%"},"Iphone":{"Brand name:":"Iphone","Model name:":"15 Pro","Product ID:":"005","Actual Price:":"80000","Discount:":"5%"}}
chargers={"redmi":{"Brand name:":"Redmi","Model name:":"10 Watts charger","Product ID:":"006","Actual Price:":500,"Discount:":"5%"},"Vivo":{"Brand name:":"Vivo","Model name:":"15 watts charger","Product ID:":"007","Actual Price:":1000,"Discount:":"5%"},"Realme":{"Brand name:":"Realme","Model name:":"20 watts charger","Product ID:":"008","Actual Price:":2000,"Discount:":"5%"},"Poco":{"Brand name:":"Poco","Model name:":"45 Watts charger","Product ID:":"009","Actual Price:":3000,"Discount:":"5%"},"Apple":{"Brand name:":"Apple","Model name:":"20 Watts charger","Product ID:":"010","Actual Price:":2000,"Discount:":"5%"}}
tv={"Sony":{"Brand name:":"Sony","Model name:":"42 Inches LED","Product ID:":"011","Actual Price:":50000,"Discount:":"5%"},"LG":{"Brand name:":"LG","Model name:":"54 Inches OLED","Product ID:":"012","Actual Price:":40000,"Discount:":"5%"},"Samsung":{"Brand name:":"Samsung","Model name:":"42 Inches QLED","Product ID:":"013","Actual Price:":80000,"Discount:":"5%"},"Oneplus":{"Brand name:":"Oneplus","Model name:":"42 Inches LED","Product ID:":"014","Actual Price:":45000,"Discount:":"5%"},"MI":{"Brand name:":"MI","Model name:":"43 Inch OLED","Product ID:":"015","Actual Price:":35000,"Discount:":"5%"}}
remote={"Sony":{"Brand name:":"Sony","Model name:":"Sony remote","Product ID:":"016","Actual Price:":3000,"Discount:":"5%"},"LG":{"Brand name:":"LG","Model name:":"LG remote","Product ID:":"017","Actual Price:":2000,"Discount:":"5%"},"Samsung":{"Brand name:":"Samsung","Model name:":"Samsung remote","Product ID:":"018","Actual Price:":4000,"Discount:":"5%"},"Oneplus":{"Brand name:":"Oneplus","Model name:":"Oneplus remote","Product ID:":"019","Actual Price:":1000,"Discount:":"5%"},"MI":{"Brand name:":"MI","Model name:":"MI remote","Product ID:":"020","Actual Price:":1000,"Discount:":"5%"}}
mobile1=20000
mobile2=20000
mobile3=20000
mobile4=25000
mobile5=80000
chargerprice=[500,1000,2000,3000,2000]
tvprice=[50000,40000,80000,45000,35000]
remoteprice=[3000,2000,4000,1000,1000]
print()
product=input("Pick any one:")
product=product.lower()

if product=="mobiles":
    print()
    print("------------------------------------------------------------------------","Mobiles","-------------------------------------------------------------------------------")
    print("(1)Redmi","\t","(2)Vivo","\t","(3)Realme","\t","(4)Poco","\t","(5)Iphone")
    print()
    mobile=input("Choose any one:")
    mobile=mobile.lower()
    print()
    if mobile=="redmi":
        print("---------Redmi---------")
        for a,b in mobiles.items():
            for c,d in b.items():
                if a!="redmi":
                    break
                print(c,d,sep="\t")
        discountprice=(mobile1*0.05)
        print("-----------------------")
        print("Disount price:",mobile1-discountprice)
        print()
        print("Buy now","\t","\t","\t","\t","Close")
        print()
        for i in range(0,100):
            mob1=input("Pick any one:")
            mob1=mob1.lower()
            if mob1=="buynow":
                print("--------------------------------------------------------------------------Buy now-------------------------------------------------------------------------------")
                print()
                fullname=input("Enter the Full name:")
                mobilenumber=input("Enter the mobile number:")
                address=input("Enter the address:")
                prodid="001"
                print("Product ID:",prodid)
                quantity=int(input("Enter quantity:"))
                print("--------------------------------------------------------------------------------Bill----------------------------------------------------------------------------")
                print("Full name:","Mobile number:","Address:","Product ID:","Quantity:","Price:",sep="              ",end="\n")
                print(fullname,mobilenumber,address,prodid,quantity,quantity*mobile1-quantity*discountprice,sep="                   ")
                break
            elif mob1=="close":
                print("Thank you for visiting!")
                exit()
            else:
                print("Invalid entry")
                continue
        
        
    if mobile=="vivo":
        print("----------Vivo---------")
        for a,b in mobiles.items():
            for c,d in b.items():
                if a!="Vivo":
                    continue
                print(c,d,sep="\t")
        discountprice=(mobile2*0.05)
        print("-----------------------")
        print("Disount amount:",mobile2-discountprice)
        print()
        print("Buy now","\t","\t","\t","\t","\t","Close")
        print()
        for i in range(0,100):
            mob1=input("Pick any one:")
            mob1=mob1.lower()
            if mob1=="buynow":
                print("--------------------------------------------------------------------------Buy now-------------------------------------------------------------------------------")
                print()
                fullname=input("Enter the Full name:")
                mobilenumber=input("Enter the mobile number:")
                address=input("Enter the address:")
                prodid="002"
                print("Product ID:",prodid)
                quantity=int(input("Enter quantity:"))
                print("--------------------------------------------------------------------------------Bill----------------------------------------------------------------------------")
                print("Full name:","Mobile number:","Address:","Product ID:","Quantity:","Price:",sep="              ",end="\n")
                print(fullname,mobilenumber,address,prodid,quantity,quantity*mobile2-quantity*discountprice,sep="                   ")
                break
            elif mob1=="close":
                print("Thank you for visiting!")
                exit()
            else:
                print("Invalid entry")
                continue
    if mobile=="realme":
        print("---------Realme--------")
        for a,b in mobiles.items():
            for c,d in b.items():
                if a!="Realme":
                    continue
                print(c,d,sep="\t")
        discountprice=(mobile3*0.05)
        print("-----------------------")
        print("Disount amount:",mobile3-discountprice)
        print()
        print("Buy now","\t","\t","\t","\t","\t","Close")
        print()
        for i in range(0,100):
            mob1=input("Pick any one:")
            mob1=mob1.lower()
            if mob1=="buynow":
                print("--------------------------------------------------------------------------Buy now-------------------------------------------------------------------------------")
                print()
                fullname=input("Enter the Full name:")
                mobilenumber=input("Enter the mobile number:")
                address=input("Enter the address:")
                prodid="003"
                print("Product ID:",prodid)
                quantity=int(input("Enter quantity:"))
                print("--------------------------------------------------------------------------------Bill----------------------------------------------------------------------------")
                print("Full name:","Mobile number:","Address:","Product ID:","Quantity:","Price:",sep="              ",end="\n")
                print(fullname,mobilenumber,address,prodid,quantity,quantity*mobile3-quantity*discountprice,sep="                   ")
                break
            elif mob1=="close":
                print("Thank you for visiting!")
                exit()
            else:
                print("Invalid entry")
                continue
    if mobile=="poco":
        print("----------Poco---------")
        for a,b in mobiles.items():
            for c,d in b.items():
                if a!="Poco":
                    continue
                print(c,d,sep="\t")
        discountprice=(mobile4*0.05)
        print("-----------------------")
        print("Disount amount:",mobile4-discountprice)
        print()
        print("Buy now","\t","\t","\t","\t","\t","Close")
        print()
        for i in range(0,100):
            mob1=input("Pick any one:")
            mob1=mob1.lower()
            if mob1=="buynow":
                print("--------------------------------------------------------------------------Buy now-------------------------------------------------------------------------------")
                print()
                fullname=input("Enter the Full name:")
                mobilenumber=input("Enter the mobile number:")
                address=input("Enter the address:")
                prodid="004"
                print("Product ID:",prodid)
                quantity=int(input("Enter quantity:"))
                print("--------------------------------------------------------------------------------Bill----------------------------------------------------------------------------")
                print("Full name:","Mobile number:","Address:","Product ID:","Quantity:","Price:",sep="              ",end="\n")
                print(fullname,mobilenumber,address,prodid,quantity,quantity*mobile4-quantity*discountprice,sep="                   ")
                break
            elif mob1=="close":
                print("Thank you for visiting!")
                exit()
            else:
                print("Invalid entry")
                continue
    if mobile=="iphone":
        print("----------Iphone---------")
        for a,b in mobiles.items():
            for c,d in b.items():
                if a!="Iphone":
                    continue
                print(c,d,sep="\t")
        discountprice=(mobile5*0.05)
        print("-----------------------")
        print("Disount amount:",mobile5-discountprice)
        print()
        print("Buy now","\t","\t","\t","\t","\t","Close")
        print()
        for i in range(0,100):
            mob1=input("Pick any one:")
            mob1=mob1.lower()
            if mob1=="buynow":
                print("--------------------------------------------------------------------------Buy now-------------------------------------------------------------------------------")
                print()
                fullname=input("Enter the Full name:")
                mobilenumber=input("Enter the mobile number:")
                address=input("Enter the address:")
                prodid="005"
                print("Product ID:",prodid)
                quantity=int(input("Enter quantity:"))
                print("--------------------------------------------------------------------------------Bill----------------------------------------------------------------------------")
                print("Full name:","Mobile number:","Address:","Product ID:","Quantity:","Price:",sep="              ",end="\n")
                print(fullname,mobilenumber,address,prodid,quantity,quantity*mobile5-quantity*discountprice,sep="                   ")
                break
            elif mob1=="close":
                print("Thank you for visiting!")
                exit()
            else:
                print("Invalid entry")
                continue

if product=="chargers":
    print()
    print("--------------------------------------------------------------------","Mobile chargers","---------------------------------------------------------------------------")
    print("(1)Redmi","\t","(2)Vivo","\t","(3)Realme","\t","(4)Poco","\t","(5)Apple")
    print()
    mobile=input("Choose any one:")
    mobile=mobile.lower()
    print()
    if mobile=="redmi":
        print("---------Redmi---------")
        for a,b in chargers.items():
            for c,d in b.items():
                if a!="redmi":
                    break
                print(c,d,sep="\t")
        discountprice=(chargerprice[0]*0.05)
        print("-----------------------")
        print("Disount amount:",chargerprice[0]-discountprice)
        print()
        print("Buy now","\t","\t","\t","\t","\t","Close")
        print("---------------------------------------")
        for i in range(0,100):
            mob1=input("Pick any one:")
            mob1=mob1.lower()
            if mob1=="buynow":
                print("--------------------------------------------------------------------------Buy now-------------------------------------------------------------------------------")
                print()
                fullname=input("Enter the Full name:")
                mobilenumber=input("Enter the mobile number:")
                address=input("Enter the address:")
                prodid="006"
                print("Product ID:",prodid)
                quantity=int(input("Enter quantity:"))
                print("--------------------------------------------------------------------------------Bill----------------------------------------------------------------------------")
                print("Full name:","Mobile number:","Address:","Product ID:","Quantity:","Price:",sep="              ",end="\n")
                print(fullname,mobilenumber,address,prodid,quantity,quantity*chargerprice[0]-quantity*discountprice,sep="                   ")
                break
            elif mob1=="close":
                print("Thank you for visiting!")
                exit()
            else:
                print("Invalid entry")
                continue
    if mobile=="vivo":
        print("----------Vivo---------")
        for a,b in chargers.items():
            for c,d in b.items():
                if a!="Vivo":
                    continue
                print(c,d,sep="\t")
        discountprice=(chargerprice[1]*0.05)
        print("-----------------------")
        print("Disount amount:",chargerprice[1]-discountprice)
        print()
        print("Buy now","\t","\t","\t","\t","\t","Close")
        print()
        for i in range(0,100):
            mob1=input("Pick any one:")
            mob1=mob1.lower()
            if mob1=="buynow":
                print("--------------------------------------------------------------------------Buy now-------------------------------------------------------------------------------")
                print()
                fullname=input("Enter the Full name:")
                mobilenumber=input("Enter the mobile number:")
                address=input("Enter the address:")
                prodid="007"
                print("Product ID:",prodid)
                quantity=int(input("Enter quantity:"))
                print("--------------------------------------------------------------------------------Bill----------------------------------------------------------------------------")
                print("Full name:","Mobile number:","Address:","Product ID:","Quantity:","Price:",sep="              ",end="\n")
                print(fullname,mobilenumber,address,prodid,quantity,quantity*chargerprice[1]-quantity*discountprice,sep="                   ")
                break
            elif mob1=="close":
                print("Thank you for visiting!")
                exit()
            else:
                print("Invalid entry")
                continue
    if mobile=="realme":
        print("---------Realme--------")
        for a,b in chargers.items():
            for c,d in b.items():
                if a!="Realme":
                    continue
                print(c,d,sep="\t")
        discountprice=(chargerprice[2]*0.05)
        print("-----------------------")
        print("Disount amount:",chargerprice[2]-discountprice)
        print()
        print("Buy now","\t","\t","\t","\t","\t","Close")
        print()
        for i in range(0,100):
            mob1=input("Pick any one:")
            mob1=mob1.lower()
            if mob1=="buynow":
                print("--------------------------------------------------------------------------Buy now-------------------------------------------------------------------------------")
                print()
                fullname=input("Enter the Full name:")
                mobilenumber=input("Enter the mobile number:")
                address=input("Enter the address:")
                prodid="008"
                print("Product ID:",prodid)
                quantity=int(input("Enter quantity:"))
                print("--------------------------------------------------------------------------------Bill----------------------------------------------------------------------------")
                print("Full name:","Mobile number:","Address:","Product ID:","Quantity:","Price:",sep="              ",end="\n")
                print(fullname,mobilenumber,address,prodid,quantity,quantity*chargerprice[2]-quantity*discountprice,sep="                   ")
                break
            elif mob1=="close":
                print("Thank you for visiting!")
                exit()
            else:
                print("Invalid entry")
                continue
    if mobile=="poco":
        print("----------Poco---------")
        for a,b in chargers.items():
            for c,d in b.items():
                if a!="Poco":
                    continue
                print(c,d,sep="\t")
        discountprice=(chargerprice[3]*0.05)
        print("-----------------------")
        print("Disount amount:",chargerprice[3]-discountprice)
        print()
        print("Buy now","\t","\t","\t","\t","\t","Close")
        print()
        for i in range(0,100):
            mob1=input("Pick any one:")
            mob1=mob1.lower()
            if mob1=="buynow":
                print("--------------------------------------------------------------------------Buy now-------------------------------------------------------------------------------")
                print()
                fullname=input("Enter the Full name:")
                mobilenumber=input("Enter the mobile number:")
                address=input("Enter the address:")
                prodid="009"
                print("Product ID:",prodid)
                quantity=int(input("Enter quantity:"))
                print("--------------------------------------------------------------------------------Bill----------------------------------------------------------------------------")
                print("Full name:","Mobile number:","Address:","Product ID:","Quantity:","Price:",sep="              ",end="\n")
                print(fullname,mobilenumber,address,prodid,quantity,quantity*chargerprice[3]-quantity*discountprice,sep="                   ")
                break
            elif mob1=="close":
                print("Thank you for visiting!")
                exit()
            else:
                print("Invalid entry")
                continue
    if mobile=="apple":
        print("----------Apple---------")
        for a,b in chargers.items():
            for c,d in b.items():
                if a!="Apple":
                    continue
                print(c,d,sep="\t")
        discountprice=(chargerprice[4]*0.05)
        print("-----------------------")
        print("Disount amount:",chargerprice[4]-discountprice)
        print()
        print("Buy now","\t","\t","\t","\t","\t","Close")
        print()
        for i in range(0,100):
            mob1=input("Pick any one:")
            mob1=mob1.lower()
            if mob1=="buynow":
                print("--------------------------------------------------------------------------Buy now-------------------------------------------------------------------------------")
                print()
                fullname=input("Enter the Full name:")
                mobilenumber=input("Enter the mobile number:")
                address=input("Enter the address:")
                prodid="010"
                print("Product ID:",prodid)
                quantity=int(input("Enter quantity:"))
                print("--------------------------------------------------------------------------------Bill----------------------------------------------------------------------------")
                print("Full name:","Mobile number:","Address:","Product ID:","Quantity:","Price:",sep="              ",end="\n")
                print(fullname,mobilenumber,address,prodid,quantity,quantity*chargerprice[4]-quantity*discountprice,sep="                   ")
                break
            elif mob1=="close":
                print("Thank you for visiting!")
                exit()
            else:
                print("Invalid entry")
                continue
if product=="tv":
    print()
    print("--------------------------------------------------------------------------","TV","---------------------------------------------------------------------------------")
    print("(1)Sony","\t","(2)LG","\t","(3)Samsung","\t","(4)Oneplus","\t","(5)MI")
    print()
    mobile=input("Choose any one:")
    mobile=mobile.lower()
    print()
    if mobile=="sony":
        print("----------Sony---------")
        for a,b in tv.items():
            for c,d in b.items():
                if a!="Sony":
                    break
                print(c,d,sep="\t")
        discountprice=(tvprice[0]*0.05)
        print("-----------------------")
        print("Disount amount:",tvprice[0]-discountprice)
        print()
        print("Buy now","\t","\t","\t","\t","\t","Close")
        print()
        for i in range(0,100):
            mob1=input("Pick any one:")
            mob1=mob1.lower()
            if mob1=="buynow":
                print("--------------------------------------------------------------------------Buy now-------------------------------------------------------------------------------")
                print()
                fullname=input("Enter the Full name:")
                mobilenumber=input("Enter the mobile number:")
                address=input("Enter the address:")
                prodid="011"
                print("Product ID:",prodid)
                quantity=int(input("Enter quantity:"))
                print("--------------------------------------------------------------------------------Bill----------------------------------------------------------------------------")
                print("Full name:","Mobile number:","Address:","Product ID:","Quantity:","Price:",sep="              ",end="\n")
                print(fullname,mobilenumber,address,prodid,quantity,quantity*tvprice[0]-quantity*discountprice,sep="                   ")
                break
            elif mob1=="close":
                print("Thank you for visiting!")
                exit()
            else:
                print("Invalid entry")
                continue
    if mobile=="lg":
        print("----------LG---------")
        for a,b in tv.items():
            for c,d in b.items():
                if a!="LG":
                    continue
                print(c,d,sep="\t")
        discountprice=(tvprice[1]*0.05)
        print("-----------------------")
        print("Disount amount:",tvprice[1]-discountprice)
        print()
        print("Buy now","\t","\t","\t","\t","\t","Close")
        print()
        for i in range(0,100):
            mob1=input("Pick any one:")
            mob1=mob1.lower()
            if mob1=="buynow":
                print("--------------------------------------------------------------------------Buy now-------------------------------------------------------------------------------")
                print()
                fullname=input("Enter the Full name:")
                mobilenumber=input("Enter the mobile number:")
                address=input("Enter the address:")
                prodid="012"
                print("Product ID:",prodid)
                quantity=int(input("Enter quantity:"))
                print("--------------------------------------------------------------------------------Bill----------------------------------------------------------------------------")
                print("Full name:","Mobile number:","Address:","Product ID:","Quantity:","Price:",sep="              ",end="\n")
                print(fullname,mobilenumber,address,prodid,quantity,quantity*tvprice[1]-quantity*discountprice,sep="                   ")
                break
            elif mob1=="close":
                print("Thank you for visiting!")
                exit()
            else:
                print("Invalid entry")
                continue
    if mobile=="samsung":
        print("--------Samsung-------")
        for a,b in tv.items():
            for c,d in b.items():
                if a!="Samsung":
                    continue
                print(c,d,sep="\t")
        discountprice=(tvprice[2]*0.05)
        print("-----------------------")
        print("Disount amount:",tvprice[2]-discountprice)
        print()
        print("Buy now","\t","\t","\t","\t","\t","Close")
        print()
        for i in range(0,100):
            mob1=input("Pick any one:")
            mob1=mob1.lower()
            if mob1=="buynow":
                print("--------------------------------------------------------------------------Buy now-------------------------------------------------------------------------------")
                print()
                fullname=input("Enter the Full name:")
                mobilenumber=input("Enter the mobile number:")
                address=input("Enter the address:")
                prodid="013"
                print("Product ID:",prodid)
                quantity=int(input("Enter quantity:"))
                print("--------------------------------------------------------------------------------Bill----------------------------------------------------------------------------")
                print("Full name:","Mobile number:","Address:","Product ID:","Quantity:","Price:",sep="              ",end="\n")
                print(fullname,mobilenumber,address,prodid,quantity,quantity*tvprice[2]-quantity*discountprice,sep="                   ")
                break
            elif mob1=="close":
                print("Thank you for visiting!")
                exit()
            else:
                print("Invalid entry")
                continue
    if mobile=="oneplus":
        print("--------Oneplus-------")
        for a,b in tv.items():
            for c,d in b.items():
                if a!="Oneplus":
                    continue
                print(c,d,sep="\t")
        discountprice=(tvprice[3]*0.05)
        print("-----------------------")
        print("Disount amount:",tvprice[3]-discountprice)
        print()
        print("Buy now","\t","\t","\t","\t","\t","Close")
        print()
        for i in range(0,100):
            mob1=input("Pick any one:")
            mob1=mob1.lower()
            if mob1=="buynow":
                print("--------------------------------------------------------------------------Buy now-------------------------------------------------------------------------------")
                print()
                fullname=input("Enter the Full name:")
                mobilenumber=input("Enter the mobile number:")
                address=input("Enter the address:")
                prodid="014"
                print("Product ID:",prodid)
                quantity=int(input("Enter quantity:"))
                print("--------------------------------------------------------------------------------Bill----------------------------------------------------------------------------")
                print("Full name:","Mobile number:","Address:","Product ID:","Quantity:","Price:",sep="              ",end="\n")
                print(fullname,mobilenumber,address,prodid,quantity,quantity*tvprice[3]-quantity*discountprice,sep="                   ")
                break
            elif mob1=="close":
                print("Thank you for visiting!")
                exit()
            else:
                print("Invalid entry")
                continue
    if mobile=="mi":
        print("---------MI---------")
        for a,b in tv.items():
            for c,d in b.items():
                if a!="MI":
                    continue
                print(c,d,sep="\t")
        discountprice=(tvprice[4]*0.05)
        print("-----------------------")
        print("Disount amount:",tvprice[4]-discountprice)
        print()
        print("Buy now","\t","\t","\t","\t","\t","Close")
        print()
        for i in range(0,100):
            mob1=input("Pick any one:")
            mob1=mob1.lower()
            if mob1=="buynow":
                print("--------------------------------------------------------------------------Buy now-------------------------------------------------------------------------------")
                print()
                fullname=input("Enter the Full name:")
                mobilenumber=input("Enter the mobile number:")
                address=input("Enter the address:")
                prodid="015"
                print("Product ID:",prodid)
                quantity=int(input("Enter quantity:"))
                print("--------------------------------------------------------------------------------Bill----------------------------------------------------------------------------")
                print("Full name:","Mobile number:","Address:","Product ID:","Quantity:","Price:",sep="              ",end="\n")
                print(fullname,mobilenumber,address,prodid,quantity,quantity*tvprice[4]-quantity*discountprice,sep="                   ")
                break
            elif mob1=="close":
                print("Thank you for visiting!")
                exit()
            else:
                print("Invalid entry")
                continue
if product=="remote":
    print()
    print("-----------------------------------------------------------------------","TV remote","------------------------------------------------------------------------------")
    print("(1)Sony","\t","(2)LG","\t","(3)Samsung","\t","(4)Oneplus","\t","(5)MI")
    print()
    mobile=input("Choose any one:")
    mobile=mobile.lower()
    print()
    if mobile=="sony":
        print("----------Sony---------")
        for a,b in remote.items():
            for c,d in b.items():
                if a!="Sony":
                    break
                print(c,d,sep="\t")
        discountprice=(remoteprice[0]*0.05)
        print("-----------------------")
        print("Disount amount:",remoteprice[0]-discountprice)
        print()
        print("Buy now","\t","\t","\t","\t","\t","Close")
        print()
        for i in range(0,100):
            mob1=input("Pick any one:")
            mob1=mob1.lower()
            if mob1=="buynow":
                print("--------------------------------------------------------------------------Buy now-------------------------------------------------------------------------------")
                print()
                fullname=input("Enter the Full name:")
                mobilenumber=input("Enter the mobile number:")
                address=input("Enter the address:")
                prodid="016"
                print("Product ID:",prodid)
                quantity=int(input("Enter quantity:"))
                print("--------------------------------------------------------------------------------Bill----------------------------------------------------------------------------")
                print("Full name:","Mobile number:","Address:","Product ID:","Quantity:","Price:",sep="              ",end="\n")
                print(fullname,mobilenumber,address,prodid,quantity,quantity*remoteprice[0]-quantity*discountprice,sep="                   ")
                break
            elif mob1=="close":
                print("Thank you for visiting!")
                exit()
            else:
                print("Invalid entry")
                continue
    if mobile=="lg":
        print("----------LG---------")
        for a,b in remote.items():
            for c,d in b.items():
                if a!="LG":
                    continue
                print(c,d,sep="\t")
        discountprice=(remoteprice[1]*0.05)
        print("-----------------------")
        print("Disount amount:",remoteprice[1]-discountprice)
        print()
        print("Buy now","\t","\t","\t","\t","\t","Close")
        print()
        for i in range(0,100):
            mob1=input("Pick any one:")
            mob1=mob1.lower()
            if mob1=="buynow":
                print("--------------------------------------------------------------------------Buy now-------------------------------------------------------------------------------")
                print()
                fullname=input("Enter the Full name:")
                mobilenumber=input("Enter the mobile number:")
                address=input("Enter the address:")
                prodid="017"
                print("Product ID:",prodid)
                quantity=int(input("Enter quantity:"))
                print("--------------------------------------------------------------------------------Bill----------------------------------------------------------------------------")
                print("Full name:","Mobile number:","Address:","Product ID:","Quantity:","Price:",sep="              ",end="\n")
                print(fullname,mobilenumber,address,prodid,quantity,quantity*remoteprice[1]-quantity*discountprice,sep="                   ")
                break
            elif mob1=="close":
                print("Thank you for visiting!")
                exit()
            else:
                print("Invalid entry")
                continue
    if mobile=="samsung":
        print("--------Samsung-------")
        for a,b in remote.items():
            for c,d in b.items():
                if a!="Samsung":
                    continue
                print(c,d,sep="\t")
        discountprice=(remoteprice[2]*0.05)
        print("-----------------------")
        print("Disount amount:",remoteprice[2]-discountprice)
        print()
        print("Buy now","\t","\t","\t","\t","\t","Close")
        print()
        for i in range(0,100):
            mob1=input("Pick any one:")
            mob1=mob1.lower()
            if mob1=="buynow":
                print("--------------------------------------------------------------------------Buy now-------------------------------------------------------------------------------")
                print()
                fullname=input("Enter the Full name:")
                mobilenumber=input("Enter the mobile number:")
                address=input("Enter the address:")
                prodid="018"
                print("Product ID:",prodid)
                quantity=int(input("Enter quantity:"))
                print("--------------------------------------------------------------------------------Bill----------------------------------------------------------------------------")
                print("Full name:","Mobile number:","Address:","Product ID:","Quantity:","Price:",sep="              ",end="\n")
                print(fullname,mobilenumber,address,prodid,quantity,quantity*remoteprice[2]-quantity*discountprice,sep="                   ")
                break
            elif mob1=="close":
                print("Thank you for visiting!")
                exit()
            else:
                print("Invalid entry")
                continue
    if mobile=="oneplus":
        print("--------Oneplus-------")
        for a,b in remote.items():
            for c,d in b.items():
                if a!="Oneplus":
                    continue
                print(c,d,sep="\t")
        discountprice=(remoteprice[3]*0.05)
        print("-----------------------")
        print("Disount amount:",remoteprice[3]-discountprice)
        print()
        print("Buy now","\t","\t","\t","\t","\t","Close")
        print()
        for i in range(0,100):
            mob1=input("Pick any one:")
            mob1=mob1.lower()
            if mob1=="buynow":
                print("--------------------------------------------------------------------------Buy now-------------------------------------------------------------------------------")
                print()
                fullname=input("Enter the Full name:")
                mobilenumber=input("Enter the mobile number:")
                address=input("Enter the address:")
                prodid="019"
                print("Product ID:",prodid)
                quantity=int(input("Enter quantity:"))
                print("--------------------------------------------------------------------------------Bill----------------------------------------------------------------------------")
                print("Full name:","Mobile number:","Address:","Product ID:","Quantity:","Price:",sep="              ",end="\n")
                print(fullname,mobilenumber,address,prodid,quantity,quantity*remoteprice[3]-quantity*discountprice,sep="                   ")
                break
            elif mob1=="close":
                print("Thank you for visiting!")
                exit()
            else:
                print("Invalid entry")
                continue
    if mobile=="mi":
        print("---------MI---------")
        for a,b in remote.items():
            for c,d in b.items():
                if a!="MI":
                    continue
                print(c,d,sep="\t")
        discountprice=(remoteprice[4]*0.05)
        print("-----------------------")
        print("Disount amount:",remoteprice[4]-discountprice)
        print()
        print("Buy now","\t","\t","\t","\t","\t","Close")
        print()
        for i in range(0,100):
            mob1=input("Pick any one:")
            mob1=mob1.lower()
            if mob1=="buynow":
                print("--------------------------------------------------------------------------Buy now-------------------------------------------------------------------------------")
                print()
                fullname=input("Enter the Full name:")
                mobilenumber=input("Enter the mobile number:")
                address=input("Enter the address:")
                prodid="020"
                print("Product ID:",prodid)
                quantity=int(input("Enter quantity:"))
                print("--------------------------------------------------------------------------------Bill----------------------------------------------------------------------------")
                print("Full name:","Mobile number:","Address:","Product ID:","Quantity:","Price:",sep="              ",end="\n")
                print(fullname,mobilenumber,address,prodid,quantity,quantity*remoteprice[4]-quantity*discountprice,sep="                   ")
                break
            elif mob1=="close":
                print("Thank you for visiting!")
                exit()
            else:
                print("Invalid entry")
                continue