import pandas as pd

df_review_las_vegas_restaurant = pd.read_json('../datasets/yelp_academic_dataset_review_las_vegas_restaurant.json', lines=True)
print('\nINFO\tShow df_review_las_vegas_restaurant\n')
print(df_review_las_vegas_restaurant.info())

drop_columns = ['useful', 'cool', 'funny', 'date']
df_review_las_vegas_restaurant.drop(drop_columns, axis=1, inplace=True)
print('\nINFO\tShow df_review_las_vegas_restaurant_reduce\n')
print(df_review_las_vegas_restaurant.info())

print('\nINFO\tGenerate review_las_vegas_restaurant_dataset.csv\n')
df_review_las_vegas_restaurant.to_csv('../datasets/review_las_vegas_restaurant_dataset.csv', index=False)