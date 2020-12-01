#coding=utf-8
import xlrd

def readTextFile(filepath):
    #读取文本文件
    with open(filepath,'r')as fh:
        content = fh.readlines()
        for index,line in enumerate(content):
            if "CRASH" in line:
                for dline in content[index:index+100:]:
                    if dline.startswith("//"):
                        print(dline.strip())

                break


#读取excel文件

def readExcelFile(filepath):
    readbook = xlrd.open_workbook(filepath)
    sheet1 = readbook.sheets()[0]
    for i in range(1,sheet1.nrows):
        if "多点超市" in sheet1.cell(i,14).value and sheet1.cell(i,28).value == "是" and sheet1.cell(i,29).value == "是" and sheet1.cell(i,30).value =="有效":
            venderId = int(sheet1.cell(i,0).value)
            venderName = sheet1.cell(i,1).value
            stordId = sheet1.cell(i,5).value
            stordName = sheet1.cell(i,6).value

            print(venderId,venderName,stordId,stordName)



if __name__ == "__main__":
    # filepath = r"D:\stp\study\Coding\teacher\Python读文件1126\tango_android_3.22.196195_20160227060335-4df109d22ae0af0b-O-staging2-201602280732.log"
    # readTextFile(filepath)
    filepath = r"D:\stp\study\Coding\teacher\Python读文件1126\storeBaseInfo-20201022213400.xls"
    readExcelFile(filepath)


