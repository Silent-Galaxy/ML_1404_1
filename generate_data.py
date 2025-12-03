import pandas as pd
import numpy as np

# تنظیمات تولید داده تصادفی (ولی منطقی)
np.random.seed(42)
n_samples = 500

# 1. تولید متراژ (بین ۵۰ تا ۴۰۰ متر)
area = np.random.randint(50, 400, n_samples)

# 2. تولید تعداد اتاق (بین ۱ تا ۶ خواب)
# منطق: خونه‌های بزرگتر معمولا اتاق بیشتر دارند
rooms = (area // 70) + np.random.randint(0, 2, n_samples) 

# 3. تولید سن بنا (بین ۰ تا ۳۰ سال)
age = np.random.randint(0, 30, n_samples)

# 4. فرمول سری قیمت (این فرمولیه که ماشین باید کشف کنه!)
# قیمت پایه + (متراژ * ۵۰) + (اتاق * ۳۰۰) - (سن * ۲۰) + کمی نویز بازار
base_price = 500 # قیمت پایه (مثلا ۵۰۰ میلیون)
price = base_price + (area * 0.08) + (rooms * 0.5) - (age * 0.1) + np.random.normal(0, 0.5, n_samples)

# ذخیره در فایل
df = pd.DataFrame({'Area': area, 'Rooms': rooms, 'Age': age, 'Price': price})
df.to_csv('house_data_500.csv', index=False)

print("✅ فایل house_data_500.csv با ۵۰۰ داده نمونه ساخته شد!")