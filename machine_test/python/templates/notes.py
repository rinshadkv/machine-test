x=[500,100,50,10,5,2,1]
y=int(input("e4nter"))
i=0
while y>0:
  if y>x[i]:
    count=y//x[i]
    # print(
    #     "tortel number of notes",
    #     "5oo",count, "notes of", x[i],
    #     "100",count, "notes of", x[i],
    #     "50",count, "notes of", x[i],
    #     "20",count, "notes of", x[i],
    #     "10",count, "notes of", x[i],
    #     "5",count, "notes of", x[i],
    #     "2",count, "notes of", x[i],
    #     "1",count, "notes of", x[i]

    # )
    print(y, "requires", count, "notes of", x[i] )
  y=y%x[i]
  i+=1