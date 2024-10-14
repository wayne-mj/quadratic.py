import json
import math

def main() :
    discriminant = 0
    modified_data_set=[]

    with open('inputdata.json', 'r') as file:
        data = json.load(file)
    
    file.close()

    for obj in data:
        if obj.get('a') == None:
            obj['a'] = 0
        if obj.get('b') == None:
            obj['b'] = 0
        if obj.get('c') == None:
            obj['c'] = 0
        
        discriminant = obj['b']**2 - 4*obj['a']*obj['c']
        if discriminant < 0:
            obj['msg'] = "No real roots"
        else:
            obj['msg'] = "Real roots"
            obj['root1'] = (-obj['b'] + math.sqrt(discriminant)) / (2 * obj['a'])
            obj['root2'] = (-obj['b'] - math.sqrt(discriminant)) / (2 * obj['a'])

        modified_data_set.append(obj)

        with open('outputdata.json', 'w') as file:
            json.dump(modified_data_set, file, indent=4)
        file.close()

if __name__ == "__main__":
    main()