#----Q.No.10 WAP to calculate the frequency of each characters in a string
# s=input("Enter a string:")
# result={}

# for char in s:
#     if char in result.keys():
#         result[char]=result[char]+1
#     else:
#         result[char]=1



# for key,value in result.items():
#     # key, value =x
#     print(f"{key}:{value}")

# ----Q.No.11 WaP to generate percentage of each students

grades_dict={
    "Alice":{"Math":90,"Science":85,"Literature":88},
    "BOB":{"Math":78,"Science":82,"Literature":94},
    "Charlie":{"Math":92,"Science":91,"Literature":94}
}


for x in grades_dict.items():
    k,v=x
    sum=0
    i=0
    for y in v.items():
        k1,v1=y
        sum=sum+v1
        i=i+1
    per=sum/i
        
    print(per)




        