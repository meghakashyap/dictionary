datas=[{"name":"komal","score":40,"school":"pyds"},{"name":"koma","score":40,"school":"pyd"},{"name":"jaya","score":60,"school":"pyds"},{"name":"Sonam","score":60,"school":"Union"},{"name":"Akshit","score":50,"school":"Sumer Field school"}]
dic={}
i=0
while i<len(datas):
    dic[i]=datas[i]
    if datas[i]["school"]=="pyds" and datas[i]["score"]>=50:
        print(datas[i])
    i+=1