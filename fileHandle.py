import xlrd

# 读文本文件
def readTextFile(filePath):
    with open(filePath, "r", encoding='utf-8') as fh:
        content = fh.readlines()
        for index, line in enumerate(content):
            if "CRASH" in line:
                for dline in content[index:index+100:]:
                    if dline.startswith('//'):
                        print(dline.strip())

                break

# 读Excel文件
def readExceFile(filePath):
    data = xlrd.open_workbook(filePath)
    table = data.sheets()[0]
    for i in range(1,table.nrows):
        if "全球精选" in table.cell(i,14).value and table.cell(i,28).value == "是" and table.cell(i,29).value == "是" and table.cell(i,30).value =="有效":
            venderId = int(table.cell(i, 0).value)
            venderName = table.cell(i, 1).value
            storeId = int(table.cell(i, 5).value)
            storeName = table.cell(i, 6).value
            lng = table.cell(i, 12).value
            lag = table.cell(i, 13).value
            print(venderId, venderName, storeId, storeName, lng, lag)
            # break

# 读html文件
def readHtmlFile(filePath):
    # import pyquery
    pass
                

def writeTextFile(filePath):
    pass

def writeCsvFile(filePath):
    pass

def writeExcelFile(filePath):
    pass

if __name__ == "__main__":
    filePath = r'C:\Users\shoubo.wang\Desktop\tango_android_3.22.196195_20160227060335-4df109d22ae0af0b-O-staging2-201602280732.log'
    # filePath = r'C:\Users\shoubo.wang\Desktop\storeBaseInfo-20201022213400.xls'
    readTextFile(filePath)
    # readExceFile(filePath)