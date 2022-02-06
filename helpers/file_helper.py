def getLines(file_path:str)->list[str]:
    file = open(file_path, encoding="utf-8")
    lines= file.readlines()
    file.close()
    return [line.strip() for line in lines]

def writeList(path:str, list:list[str])->list[str]:
    file = open(path, "w", encoding="utf-8")
    file.writelines("\n".join(list) )
    file.close()