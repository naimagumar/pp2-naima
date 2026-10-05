import re
import json

with open("/Users/naimagumargmail.com/Desktop/PP2_Practices/practice 5/raw.txt", "r", encoding="utf-8") as file:
    text = file.read()


# 1. Extract prices
prices = re.findall(r'\d[\d\s]*,\d{2}', text)


# 2. Find product names
product_pattern = r'\d+\.\n\s*(.+?)\n\s*\d+,\d+\s*x'
product_names = re.findall(product_pattern, text)


# 3. Calculate total amount
total_amount = sum(
    float(price.replace(" ", "").replace(",", "."))
    for price in re.findall(r'\n\s*([\d\s]+,\d{2})\n\s*Стоимость', text)
)


# 4. Extract date and time
date_time = re.search(
    r'Время:\s*(\d{2}\.\d{2}\.\d{4})\s*(\d{2}:\d{2}:\d{2})',
    text
)

date = date_time.group(1)
time = date_time.group(2)


# 5. Find payment method
if "Банковская карта" in text:
    payment_method = "Банковская карта"
else:
    payment_method = "Unknown"


# 6. Create structured JSON
result = {
    "prices": prices,
    "product_names": product_names,
    "total_amount": total_amount,
    "date": date,
    "time": time,
    "payment_method": payment_method
}


print(json.dumps(result, ensure_ascii=False, indent=4))