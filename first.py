# ---------------------------- CLASS PURCHASE ----------------------------

class Purchase:  
    def __init__(self, customer_name, product, price, quantity):
        self.__customer_name = customer_name    # حفظ اسم الزبون بشكل private
        self.__product = product                # حفظ اسم المنتج
        self.__price = price                    # حفظ السعر
        self.__quantity = quantity              # حفظ الكمية

    # --------------------- Getters & Setters ---------------------

    def get_customer_name(self):
        return self.__customer_name             # ارجاع اسم الزبون

    def set_customer_name(self, name):
        self.__customer_name = name             # تعديل اسم الزبون

    def get_product(self):
        return self.__product                   # ارجاع اسم المنتج

    def set_product(self, product):
        self.__product = product                # تعديل اسم المنتج

    def get_price(self):
        return self.__price                     # ارجاع السعر

    def set_price(self, price):
        self.__price = price                    # تعديل السعر

    def get_quantity(self):
        return self.__quantity                  # ارجاع الكمية

    def set_quantity(self, quantity):
        self.__quantity = quantity              # تعديل الكمية

    # --------------------- Functional Methods ---------------------

    def get_total(self):
        return self.__price * self.__quantity   # حساب قيمة العملية: السعر × الكمية

    def __str__(self):
        # شكل الكتابة عند طباعة object من نوع Purchase
        return f"{self.__customer_name} bought {self.__quantity} x {self.__product} at ${self.__price} each"


# ---------------------------- READ PURCHASES ----------------------------

def read_purchases(filename):
    purchases = []                              # إنشاء قائمة فارغة لتخزين الكائنات

    with open(filename, 'r') as file:           # فتح ملف المشتريات للقراءة
        for line in file:                       # قراءة الملف سطر بسطر
            parts = line.strip().split(',')     # تقسيم السطر إلى أجزاء بناءً على الفاصلة

            if len(parts) == 4:                 # التأكد أن السطر يحتوي 4 قيم
                customer_name = parts[0]        # استخراج اسم الزبون
                product = parts[1]              # استخراج اسم المنتج
                price = float(parts[2])         # تحويل السعر إلى float
                quantity = int(parts[3])        # تحويل الكمية إلى int

                # إنشاء كائن Purchase
                purchase = Purchase(customer_name, product, price, quantity)

                purchases.append(purchase)      # إضافة الكائن للقائمة

    return purchases                            # إرجاع القائمة كاملة


# ---------------------------- TOTAL SALES ----------------------------

def compute_total_sales(purchases):
    total = 0                                   # متغير لجمع المبيعات
    for purchase in purchases:                  # المرور على كل عملية شراء
        total += purchase.get_total()           # إضافة إجمالي العملية إلى المجموع
    return total                                # إرجاع مجموع المبيعات


# ---------------------------- COUNT PRODUCTS ----------------------------

def count_products_sold(purchases):
    product_counts = {}                         # قاموس: المنتج → كمية البيع

    for purchase in purchases:                  # المرور على كل عملية شراء
        product = purchase.get_product()        # استخراج اسم المنتج
        quantity = purchase.get_quantity()      # استخراج الكمية

        if product in product_counts:           # إذا المنتج موجود في القاموس
            product_counts[product] += quantity # جمع الكمية
        else:
            product_counts[product] = quantity  # إضافة المنتج لأول مرة

    return product_counts                       # إرجاع القاموس


# ---------------------------- MARKETING QUESTIONS ----------------------------

def get_most_sold_product(purchases):
    products = count_products_sold(purchases)   # الحصول على عدد كل منتج
    
    most_product = None                         # اسم المنتج الأكثر بيعاً
    max_qty = -1                                # أعلى كمية بيع
    
    for product, qty in products.items():       # المرور على القاموس
        if qty > max_qty:                       # إيجاد أكبر كمية
            max_qty = qty
            most_product = product

    return most_product, max_qty                # إرجاع المنتج + الكمية


def get_top_customer_by_quantity(purchases):
    customer_counts = {}                        # قاموس: زبون → مجموع الكميات

    for purchase in purchases:
        name = purchase.get_customer_name()     # استخراج اسم الزبون
        qty = purchase.get_quantity()           # استخراج الكمية
        
        if name in customer_counts:
            customer_counts[name] += qty        # جمع الكمية
        else:
            customer_counts[name] = qty         # إضافة زبون جديد

    top_customer = None                         # اسم الزبون الأكثر شراء
    max_qty = -1                                # أعلى كمية

    for name, qty in customer_counts.items():   # المرور على القاموس
        if qty > max_qty:                       # إيجاد أعلى كمية
            max_qty = qty
            top_customer = name

    return top_customer, max_qty                # إرجاع الزبون والكمية


# ---------------------------- MAIN PROGRAM ----------------------------

def main():
    purchases = read_purchases("purchases.txt")   # قراءة ملف المشتريات

    print("\n--- All Purchases ---")
    for p in purchases:                            # طباعة كل عملية
        print(p)

    total_sales = compute_total_sales(purchases)   # حساب إجمالي المبيعات
    print(f"\nTotal Sales: ${total_sales:.2f}")

    products = count_products_sold(purchases)      # حساب الكميات لكل منتج
    print("\n--- Products Sold ---")
    for product, qty in products.items():
        print(f"{product}: {qty}")

    most_product, qty = get_most_sold_product(purchases)
    print(f"\nMost Sold Product: {most_product} ({qty} units)")

    top_customer, qty = get_top_customer_by_quantity(purchases)
    print(f"Top Customer by Quantity: {top_customer} ({qty} items)")


# ---------------------------- RUN MAIN ----------------------------

if __name__ == "__main__":
    main()    # تشغيل البرنامج
