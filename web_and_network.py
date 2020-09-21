#xml作成
import xml.etree.ElementTree as ET

root = ET.Element('root')
tree = ET.ElementTree(element=root)

employee = ET.SubElement(root, 'employee')

employ =  ET.SubElement(employee, 'employ')
employ_id = ET.SubElement(employ, 'id')
employ_id.text = '111'
employ_id = ET.SubElement(employ, 'name')
employ_id.text = 'Mike'

tree.write('test.xml', encoding='utf-8',xml_declaration=True)

tree = ET.ElementTree(file='test.xml')
root = tree.getroot()

for employee in root:
    for employ in employee:
        for person in employ:
            print(person.tag, person.text)


#json作成
import json

j = {
    "employee": 
    [
        {"id": 111, "name": "Mike"},
        {"id": 222, "name": "Nancy"}
    ]
}

print(j)
print(type(j))#jsonはただのdict型
print("############")
print(json.dumps(j))
print(type(json.dumps(j)))#文字列になる
a = json.dumps(j)
print(json.loads(a))
print(type(json.loads(a)))


with open('test.json', 'w') as f:
    json.dump(j, f)

with open('test.json', 'r') as f:
    json.load(f)