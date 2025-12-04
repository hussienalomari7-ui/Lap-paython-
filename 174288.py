import numpy as np  # استيراد مكتبة NumPy واختصار اسمها إلى np

# ==============================
# Part 1 — Store Inventory Data
# ==============================

# إنشاء مصفوفة ثنائية الأبعاد للمخزون (Inventory) كما في الجدول
inventory = np.array([  # إنشاء مصفوفة NumPy من قائمة قوائم
    [12, 10, 8],        # الصف الأول: المنتج P1 في الأقسام A,B,C
    [5, 7, 9],          # الصف الثاني: المنتج P2 في الأقسام A,B,C
    [14, 11, 6],        # الصف الثالث: المنتج P3 في الأقسام A,B,C
    [3, 4, 2],          # الصف الرابع: المنتج P4 في الأقسام A,B,C
    [20, 17, 15]        # الصف الخامس: المنتج P5 في الأقسام A,B,C
])                      # نهاية تعريف المصفوفة

print("=== Part 1: Inventory ===")  # طباعة عنوان جزء 1 للتوضيح

# طباعة عدد الأبعاد (ndim)
print("Dimensions:", inventory.ndim)  # طباعة عدد الأبعاد للمصفوفة (ثنائية = 2)

# طباعة الشكل (shape)
print("Shape:", inventory.shape)      # طباعة عدد الصفوف والأعمدة (5,3)

# طباعة عدد العناصر الكلي
print("Total elements:", inventory.size)  # طباعة عدد العناصر في المصفوفة (5*3 = 15)

# طباعة نوع البيانات
print("Data type:", inventory.dtype)      # طباعة نوع القيم المخزنة (int64 أو مشابه حسب الجهاز)

# طباعة عدد البايتات الكلي
print("Total bytes:", inventory.nbytes)   # طباعة الحجم بالبايت لجميع عناصر المصفوفة

# حساب عدد العناصر في القسم B (العمود الثاني)
section_b_total = inventory[:, 1].sum()   # اختيار العمود الثاني (B) وجمع قيمه
print("Total items in Section B:", section_b_total)  # طباعة مجموع القسم B

# إيجاد أكبر قيمة في القسم C (العمود الثالث)
section_c_max = inventory[:, 2].max()     # اختيار العمود الثالث (C) وأخذ أكبر قيمة
print("Max stock in Section C:", section_c_max)  # طباعة أكبر مخزون في القسم C

# استخراج المنتجات من 2 إلى 4 (الصفوف 1 إلى 3 بالـ index)
products_2_to_4 = inventory[1:4, :]       # اختيار الصفوف 1,2,3 وكل الأعمدة
print("Products 2–4 only:\n", products_2_to_4)  # طباعة المصفوفة الناتجة

# استخراج القسم A و C فقط لكل المنتجات (الأعمدة 0 و 2)
sections_a_c = inventory[:, [0, 2]]       # اختيار كل الصفوف والأعمدة 0 و 2 فقط
print("Sections A and C only:\n", sections_a_c)  # طباعة النتيجة


# ==============================
# Part 2 — Shipping Data
# ==============================

print("\n=== Part 2: Shipping ===")  # طباعة عنوان جزء 2 للتوضيح

# إنشاء مصفوفة الشحن خلال 4 أيام لـ 5 منتجات كما في الجدول
shipping = np.array([   # إنشاء مصفوفة للشحن
    [2, 1, 3, 0, 4],    # اليوم 1: الكميات لكل منتج P1..P5
    [3, 2, 1, 1, 2],    # اليوم 2
    [4, 0, 2, 1, 3],    # اليوم 3
    [1, 2, 3, 1, 4]     # اليوم 4
])                      # نهاية تعريف مصفوفة الشحن

# حساب مجموع الشحن لكل يوم (على مستوى الصفوف)
total_per_day = shipping.sum(axis=1)      # جمع القيم على المحور 1 (لكل صف = لكل يوم)
print("Total shipped per day:", total_per_day)  # طباعة مجموع الشحن لكل يوم

# حساب مجموع الشحن لكل منتج (على مستوى الأعمدة)
total_per_product = shipping.sum(axis=0)  # جمع القيم على المحور 0 (لكل عمود = لكل منتج)
print("Total shipped per product:", total_per_product)  # طباعة مجموع الشحن لكل منتج

# حساب مجموع الشحن الكلي
overall_total = shipping.sum()            # جمع كل عناصر المصفوفة
print("Overall total shipped:", overall_total)  # طباعة المجموع الكلي لكل الأيام والمنتجات

# تحديد اليوم ذو أعلى شحن
day_with_max = np.argmax(total_per_day) + 1  # إيجاد index أكبر قيمة ثم +1 لأن الأيام تبدأ من 1
print("Day with highest shipments:", day_with_max)  # طباعة رقم اليوم الأعلى شحناً

# تحديد المنتج ذو أقل شحن
product_with_min = np.argmin(total_per_product) + 1  # إيجاد index أقل قيمة ثم +1 لأن المنتجات تبدأ من 1
print("Product with lowest shipments: P", product_with_min)  # طباعة رقم المنتج الأقل شحناً

# أخذ جزء من مصفوفة الشحن للأيام من 2 إلى 4 والمنتجات 1 و 3 و 5
shipping_slice = shipping[1:4, [0, 2, 4]]  # اختيار الصفوف 1 إلى 3 والأعمدة 0 و 2 و 4
print("Shipping (days 2–4, products 1,3,5):\n", shipping_slice)  # طباعة الجزء المقتطع


# ==============================
# Part 3 — Data Cleaning
# ==============================

print("\n=== Part 3: Data Cleaning ===")  # طباعة عنوان جزء 3 للتوضيح

# إنشاء مصفوفة قراءات الحرارة مع وجود NaN وقيم سالبة
temps = np.array([4.0, 5.2, np.nan, 3.1, -1.0, 2.5, np.nan, 4.8])  # إنشاء مصفوفة temps بالقيم المعطاة

# حساب عدد قيم NaN في المصفوفة
nan_mask = np.isnan(temps)                # إنشاء مصفوفة منطقية تحدد أماكن الـ NaN
nan_count = nan_mask.sum()                # حساب عدد الـ True في الماسك (عدد الـ NaN)
print("Number of NaNs:", nan_count)       # طباعة عدد القيم المفقودة NaN

# حساب متوسط القيم غير NaN
mean_without_nan = np.nanmean(temps)      # حساب المتوسط مع تجاهل قيم NaN
print("Mean without NaNs:", mean_without_nan)  # طباعة المتوسط

# استبدال قيم NaN بالمتوسط المحسوب
temps[nan_mask] = mean_without_nan        # تعويض كل NaN بالمتوسط في نفس المصفوفة

# استبدال القيم السالبة بالصفر
negative_mask = temps < 0                 # إنشاء ماسك للقيم الأصغر من صفر
temps[negative_mask] = 0                  # تعيين القيم السالبة إلى 0

# حساب المتوسط والانحراف المعياري وأقصى قيمة بعد التنظيف
clean_mean = temps.mean()                 # حساب المتوسط للقيم بعد التنظيف
clean_std = temps.std()                   # حساب الانحراف المعياري للقيم بعد التنظيف
clean_max = temps.max()                   # إيجاد أكبر قيمة بعد التنظيف

print("Clean temps:", temps)              # طباعة المصفوفة بعد التنظيف
print("Mean:", clean_mean)                # طباعة المتوسط النهائي
print("Std:", clean_std)                  # طباعة الانحراف المعياري
print("Max:", clean_max)                  # طباعة أكبر قيمة


# ==========================================
# Part 5 — Customer Behavior & Fancy Indexing
# ==========================================

print("\n=== Part 5: Customer Behavior ===")  # طباعة عنوان جزء 5 للتوضيح

# إنشاء مصفوفة أنواع الزبائن
types = np.array(["VIP", "Regular", "Visitor", "VIP", "Visitor", "Regular", "Regular"])  # مصفوفة نوع الزبون لكل صف

# إنشاء مصفوفة spending عشوائية 7x4 بقيم بين 10 و 200
np.random.seed(0)                          # تثبيت seed لضمان نفس النتائج كل تشغيل (اختياري)
spending = np.random.randint(10, 201, (7, 4))  # إنشاء مصفوفة عشوائية 7x4 للأربعة منتجات

print("Customer types:", types)            # طباعة أنواع الزبائن
print("Spending matrix:\n", spending)      # طباعة مصفوفة الإنفاق

# إنشاء ماسك للزبائن من نوع VIP
vip_mask = (types == "VIP")               # مصفوفة منطقية True حيث النوع VIP
# إنشاء ماسك للزبائن غير VIP
non_vip_mask = (types != "VIP")           # مصفوفة منطقية True حيث النوع ليس VIP

# إظهار إنفاق الزبائن VIP فقط
vip_spending = spending[vip_mask]         # اختيار الصفوف التي نوعها VIP من مصفوفة الإنفاق
print("VIP spending:\n", vip_spending)    # طباعة إنفاق VIP

# إظهار إنفاق الزبائن غير VIP
non_vip_spending = spending[non_vip_mask] # اختيار الصفوف التي ليست VIP
print("Non-VIP spending:\n", non_vip_spending)  # طباعة إنفاق غير VIP

# استبدال القيم السالبة إن وُجدت في مصفوفة spending
negative_spending_mask = (spending < 0)   # مصفوفة منطقية تحدد أي عنصر أقل من صفر
spending[negative_spending_mask] = 0      # تعيين أي قيمة سالبة إلى 0
print("Spending after fixing negatives:\n", spending)  # طباعة المصفوفة بعد التصحيح


# ==========================================
# Part 6 — Reshaping, Views, Copies, Stacking
# ==========================================

print("\n=== Part 6: Reshaping & Stacking ===")  # طباعة عنوان جزء 6 للتوضيح

# إنشاء المصفوفة sales من 1 إلى 12
sales = np.arange(1, 13)                  # إنشاء مصفوفة 1D تحتوي الأعداد من 1 إلى 12
print("Original sales:", sales)           # طباعة المصفوفة الأصلية

# إعادة تشكيل المصفوفة إلى 3x4
sales_2d = sales.reshape(3, 4)            # تغيير شكل المصفوفة إلى 3 صفوف و 4 أعمدة
print("Sales 3x4:\n", sales_2d)           # طباعة المصفوفة بعد إعادة التشكيل

# إنشاء نسخة مسطحة باستخدام flatten (نسخة مستقلة)
sales_flatten = sales_2d.flatten()        # إنشاء نسخة 1D من المصفوفة (نسخة جديدة)
print("Flatten array:", sales_flatten)    # طباعة النسخة المسطحة

# إنشاء نسخة مسطحة باستخدام ravel (غالباً View)
sales_ravel = sales_2d.ravel()            # إنشاء مصفوفة 1D مرتبطة بالأصل إن أمكن
print("Ravel array:", sales_ravel)        # طباعة المصفوفة الناتجة من ravel

# تعديل أول عنصر في flatten (لن يؤثر على الأصل)
sales_flatten[0] = 999                    # تغيير أول عنصر في نسخة flatten إلى 999
print("After modifying flatten[0]:")      # توضيح ما حدث
print("sales:", sales)                    # طباعة المصفوفة الأصلية (لا تتغير)
print("sales_flatten:", sales_flatten)    # طباعة نسخة flatten بعد التعديل

# تعديل ثاني عنصر في ravel (سيؤثر على الأصل غالباً لأنه View)
sales_ravel[1] = 888                      # تغيير ثاني عنصر في ravel إلى 888
print("After modifying ravel[1]:")        # توضيح ما حدث
print("sales:", sales)                    # طباعة المصفوفة الأصلية (ستتأثر)
print("sales_ravel:", sales_ravel)        # طباعة ravel بعد التعديل

# توضيح في التعليق:
# flatten() ترجع نسخة جديدة مستقلة عن المصفوفة الأصلية
# ravel() ترجع View (نظرة) على نفس البيانات، لذلك التعديل عليها يغيّر الأصل إن أمكن

# -------- Stacking --------

# أخذ مخزون القسم A من مصفوفة inventory (العمود الأول)
section_a_inventory = inventory[:, 0]     # اختيار العمود 0 (قسم A) لكل المنتجات
print("Section A inventory:", section_a_inventory)  # طباعة المخزون في قسم A

# حساب مجموع الشحن لكل منتج من مصفوفة shipping
shipping_totals_per_product = shipping.sum(axis=0)  # جمع الشحن على الأيام لكل منتج
print("Shipping totals per product:", shipping_totals_per_product)  # طباعة مجموع الشحن لكل منتج

# إنشاء مصفوفة أسعار جديدة (افتراضية) لكل منتج من الخمسة
new_prices = np.array([50, 60, 70, 80, 90])  # أسعار جديدة لكل منتج P1..P5 (قيم مثال فقط)
print("New prices:", new_prices)             # طباعة الأسعار الجديدة

# تكديس (Stack) هذه البيانات أفقياً (كأعمدة) لكل منتج
combined = np.column_stack([section_a_inventory, shipping_totals_per_product, new_prices])  # دمج الأعمدة
print("Combined (Section A, shipping totals, new prices):\n", combined)  # طباعة المصفوفة المدمجة

# إضافة منتج جديد [6,5,4] إلى المخزون باستخدام vstack
new_product_row = np.array([[6, 5, 4]])  # إنشاء صف جديد يمثل مخزون المنتج الجديد في الأقسام A,B,C
inventory_with_new = np.vstack([inventory, new_product_row])  # إضافة الصف الجديد إلى أسفل المصفوفة
print("Inventory with new product:\n", inventory_with_new)  # طباعة المصفوفة بعد إضافة المنتج الجديد
