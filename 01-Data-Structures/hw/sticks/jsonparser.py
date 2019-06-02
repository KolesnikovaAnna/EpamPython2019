import numpy as np

def file_transformation(json_file):
    """Преобразование файла json в структуру"""
    struct = []
    json_file = str(json_file)
    json_file = json_file[2:len(json_file)-2]
    json_file = json_file.replace('\'', '')
    json_file = json_file.replace('[', '')
    json_file = json_file.replace(']', '') 
    json_file = json_file.replace('null', '0') 
    json_file = json_file.split('}, {')
    for i in range(0, len(json_file)):
        keys, values = [], []
        if json_file[i].count('{') > 0:
            json_file[i] = json_file[i].replace('{','')
        tmp = json_file[i].split(', "')
        for k in range(0, len(tmp)):
            tmp[k] = tmp[k].replace('"', '')
        for j in range(0, len(tmp)):
            t = tmp[j]
            t = t.split(': ')
            keys.append(t[0])
            values.append(t[1])
        struct.append(dict(zip(tuple(keys), tuple(values))))
    return struct

def sort_data(data):
    """Сортировка"""
    data_sorted = sorted(data, key = lambda k: int(k['price']) if int(k['price']) is not None else 0)
    return data_sorted

def merge(winedata_1, winedata_2):
    """Объединение двух структур в одну"""
    full_data = winedata_1
    for i in winedata_2:
        if i not in winedata_1:
            full_data.append(i)
    return sort_data(full_data)

def to_json(out_winedata_file, merged_winedata):
    """Преобразовываем данные для json"""
    out_winedata_file.write('[')
    index = 0
    for i in range(0, len(merged_winedata)):
        index_of_keys  = 0
        out_winedata_file.write('{')
        for key in merged_winedata[i].keys():
            if merged_winedata[i][key] is not None:
                value = str(merged_winedata[i][key]).replace("\\\\", "\\")
                out_winedata_file.write(f'"{key}": "{value}"')
            else:
                out_winedata_file.write(f'"{key}": null')
            if index_of_keys != (len(merged_winedata[i].keys()) - 1):
                out_winedata_file.write(', ')
            index_of_keys += 1
        if index != len(merged_winedata) - 1:
            out_winedata_file.write('}, ')
        else:
            out_winedata_file.write('}')
        index += 1
    out_winedata_file.write(']')

json_file =  open('winedata_1.json', 'r')
file1 = json_file.readlines()
json_file.close()
json_file =  open('winedata_2.json', 'r')
file2 = json_file.readlines()
json_file.close()

winedata_1 = file_transformation(file1)
winedata_2 = file_transformation(file2)
merged_winedata = merge(winedata_1, winedata_2)

out_winedata =  open('winedata_full.json', 'w')
to_json(out_winedata, merged_winedata)
out_winedata.close()