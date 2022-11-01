AWS_ID = "arn:aws:iam:123456789012:user/Development/product_1234/*\n\n"
account_id = (AWS_ID.split(":")[3])
print(f"This is my account id:{account_id}")