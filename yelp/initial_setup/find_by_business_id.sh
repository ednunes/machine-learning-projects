while read id; do
  echo $id
  grep -e "$id" yelp_academic_dataset_review.json >> yelp_academic_dataset_review_las_vegas.json
done <business_id
