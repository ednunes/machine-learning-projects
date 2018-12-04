import json
from pprint import pprint

with open('../dataset/yelp_academic_dataset_checkin.json') as f:
    data = json.load(f)

with open('business_id') as f:
    business_id = f.read().splitlines()

with open('../dataset/yelp_academic_dataset_checkin.csv', 'w') as f:
    f.write('business_id,checkin_count\n')

    j = 0

    for i in range(0, len(business_id)):
        j_sum = 0
        
        if data[j]['business_id'] != business_id[i]:
            f.write('{0},{1}\n'.format(business_id[i], 0))
            continue

        for attr, value in data[j]['time'].items():
            j_sum += value

        f.write('{0},{1}\n'.format(data[j]['business_id'], j_sum))
        j += 1

# with open('../dataset/yelp_academic_dataset_checkin.csv', 'w') as f1:
#     f.write('business_id,checkin_count\n')

#     for i in range(0, len(data)):
#         i_sum = 0
        
#         for attr, value in data[i]['time'].items():
#             i_sum += value

#         f.write('{0},{1}\n'.format(data[i]['business_id'], i_sum))



