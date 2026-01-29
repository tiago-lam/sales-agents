docker run --rm --env-file .env sales-agent \
    --verbose False \
    --max_output_tokens 2048 \
    --query "Which product sold the most?"

# "Which product sold the most?" √
# "Which location had the highest sales volume?" √
# "What were the total sales for the period starting between 01/10/2012 and 01/11/2012? √"
# "What is the difference between planned quantity and actual quantity?" √
# "What is the impact of promotions in the price and selling volume?" √