import csv

responseFromClient = "20158511"

with open('data.csv', 'r') as csvFile:
    reader = csv.reader(csvFile)
    rows = []
    flag = 0
    for row in reader:
         # print(row)
         rows.append(row)
        # print(col[0]
    # print(rows)
    for i in range (len(rows)):
        # k = i
        for j in range(0,3):
            m = j
            print(rows[i][j])
    #         if(rows[i][j] == responseFromClient):
    #             print(rows[i][m + 1])
    #             flag = 1
    # if(flag == 0):
    #     print("arey pp roll number chusko sarigga")
csvFile.close()
