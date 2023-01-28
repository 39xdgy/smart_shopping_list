from reader.amazon import amazon
from reader.walmart import walmart
import json

amazon_reader = amazon()
walmart_reader = walmart()
f = open('data.json')
data = json.load(f)
print(data)

while(True):
    print("What do you want to do.")
    num = input("1.add 2.remove 3.see list 4.see total 0.quit: ")
    

    if(num == "0"):
        json_object = json.dumps(data, indent=4)
        f.close()
        # Writing to sample.json
        with open("data.json", "w") as outfile:
            outfile.write(json_object)
        
        print("bye bitch")
        break
    if(num == "1"):
        print("please give the link below")
        link = input("link: ")
        response = ""
        print("amazon.com" in link)
        if("amazon.com" in link):
            response = amazon_reader.fetch(link)
            item_info = {
                "full name": amazon_reader.get_name(),
                "price": amazon_reader.get_price(),
                "link": link,
                "priority": int(input("From 1 to 5 how import this item is? "))
            }
            data[input("please give a name: ")] = item_info
        elif("walmart.com" in link):
            response = walmart_reader.fetch(link)
            item_info = {
                "full name": walmart_reader.get_name(),
                "price": walmart_reader.get_price(),
                "link": link,
                "priority": int(input("From 1 to 5 how import this item is? "))
            }
            data[input("please give a name: ")] = item_info
        else:
            print("ERROR: add failed due to amazon reader")
    if(num == "3"):
        print(data)
    if(num == "4"):
        total = 0
        for key in data:
            total += data[key]["price"]
        print(total)
    if(num == "9"):
        data = {}
            
