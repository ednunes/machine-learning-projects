#!/bin/bash

while read id; do
  echo $id
  grep -e "$id" ../yelp_dataset/yelp_academic_dataset_review.json >> ../dataset/yelp_academic_dataset_review_las_vegas_restaurant.json
done <business_id

while read id; do
  echo $id
  grep -e "$id" ../yelp_dataset/yelp_academic_dataset_checkin.json >> ../dataset/yelp_academic_dataset_checkin.json
done <business_id
