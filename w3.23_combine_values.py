item_list = [{'item': 'item1', 'amount': 400}, {'item': 'item2', 'amount': 300}, {'item': 'item1', 'amount': 750}]
result={}
sum=0
add=0
for x in item_list:
    if "item1" in x["item"]:
        sum+=x["amount"]
        result["item1"]=sum
    else:
        add+=x["amount"]
        result["item2"]=add
            
print(result)
