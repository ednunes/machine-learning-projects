import pandas as pd

df_business = pd.read_json('../yelp_dataset/yelp_academic_dataset_business.json', lines=True)
print('\nINFO\tShow df_business\n')
print(df_business.info())

df_business_las_vegas = df_business[df_business.city == 'Las Vegas']
print('\nINFO\tShow df_business_las_vegas info\n')
print(df_business_las_vegas.info())
del df_business

df_business_las_vegas_restaurant = df_business_las_vegas[df_business_las_vegas.categories.str.contains('Restaurant', na = False)]
print('\nINFO\tShow df_business_las_vegas_restaurant\n')
print(df_business_las_vegas_restaurant.info())
del df_business_las_vegas

drop_columns = ['attributes', 'categories', 'hours', 'address', 'city', 'state', 'neighborhood', 'name', 'state']
df_business_las_vegas_restaurant.drop(drop_columns, axis=1, inplace=True)
print('\nINFO\tShow df_business_las_vegas_restaurant_reduce\n')
print(df_business_las_vegas_restaurant.info())

print('\nINFO\tGenerate business_las_vegas_restaurant_dataset.csv\n')
df_business_las_vegas_restaurant.to_csv('../business_las_vegas_restaurant_dataset.csv', index=False)

business_id = list(df_business_las_vegas_restaurant['business_id'].values)
del df_business_las_vegas_restaurant

print('INFO\tGenerate business_id\n')
with open('business_id', 'w') as f:
    for item in business_id:
        f.write('%s\n' % item)

# df_reviews = pd.read_json('yelp_academic_dataset_review.json', lines=True)
# print(df_reviews.info())

# df_reviews_las_vegas = df_reviews[df_reviews.business_id.is_in(business_id)]
# print(df_reviews_las_vegas.info())

# df_reviews_las_vegas.to_csv('reviews_las_vegas_dataset.csv', index=False)
