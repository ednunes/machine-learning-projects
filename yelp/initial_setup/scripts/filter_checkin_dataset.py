import json
from pprint import pprint

with open('../dataset/yelp_academic_dataset_checkin.json') as f:
    data = json.load(f)


with open('../dataset/yelp_academic_dataset_checkin.csv', 'w') as f:
    f.write('business_id,checkin_count\n')

    for i in range(0, len(data)):
        i_sum = 0
        
        for attr, value in data[i]['time'].items():
            i_sum += value

        f.write('{0},{1}\n'.format(data[i]['business_id'], i_sum))



