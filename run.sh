#!/bin/bash
python3 run.py \
    --data_path ./dataset/sales.csv \
    --model models/gemini-2.5-flash \
    "$@"

# Document queries
# "Which product sold the most?" √
# "Which location had the highest sales volume?" √
# "What were the total sales for the period starting between 01/10/2012 and 01/11/2012? √"
# "What is the difference between planned quantity and actual quantity?" √
# "What is the impact of promotions in the price and selling volume?" √

# Testing queries
# "What is the first and last date, in cronological order, in this sales dataset?" √