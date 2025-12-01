# ============================================
# 1) الاستيراد و فحص الإصدار
# ============================================

import pandas as pd  # استيراد مكتبة pandas و تسميتها بالاختصار القياسي pd
import numpy as np   # استيراد مكتبة NumPy لاستخدام المصفوفات و الدوال الرياضية

print(pd.__version__)  # طباعة إصدار pandas للتأكد من التوافق مع الأمثلة

# ============================================
# 2) Series basics  (سيريس – شبيه بالعمود)
# ============================================

obj = pd.Series([4, 7, -5, 3])  # إنشاء Series بدون تسميات مخصصة (index افتراضي 0..n-1)
print(obj)                      # عرض عناصر الـSeries مع الـindex و نوع البيانات

print(obj.values)               # إظهار القيم كـnumpy array
print(obj.index)                # إظهار كائن الـIndex (يمثّل التسميات 0..3)

# Series مع index مخصّص
obj2 = pd.Series([4, 7, -5, 3], index=['d', 'b', 'a', 'c'])  # إنشاء Series مع تسميات مخصّصة
print(obj2)                                                  # طباعة الـSeries مع الـindex المخصّص
print(obj2.index)                                            # إظهار الـIndex (يتكوّن من strings)

# الوصول إلى عنصر باستخدام label
print(obj2['a'])        # طباعة القيمة عند label 'a'
obj2['d'] = 6           # تعديل القيمة عند label 'd' لتصبح 6
print(obj2[['c', 'a', 'd']])  # اختيار أكثر من label بتمرير قائمة من labels

# Boolean filtering على Series
print(obj2[obj2 > 0])   # اختيار العناصر التي قيمتها > 0 فقط
print(obj2 * 2)         # ضرب جميع القيم في 2 (عملية عنصر بعنصر)
print(np.exp(obj2))     # تطبيق دالة الأس الأسية من NumPy على كل عنصر

# مثال Series بسيط لاستخدام mean / min / max
ages = pd.Series([4, 7, 5, 3])  # إنشاء Series تمثل أعمارًا
print(ages.mean())              # حساب المتوسط الحسابي للقيم
print(ages.min())               # القيمة الصغرى في الـSeries
print(ages.max())               # القيمة الكبرى في الـSeries

# ============================================
# 3) Series كأنها dict + إنشاء من قواميس + isnull/notnull
# ============================================

# Series تشبه القاموس: الفحص باستخدام 'in' يتحقق من وجود label في الـindex فقط
print('b' in obj2.index)  # التحقق هل label 'b' موجود في index
print('e' in obj2.index)  # التحقق هل label 'e' موجود في index
print(4 in obj2.values)   # التحقق هل القيمة 4 موجودة ضمن القيم (نستخدم .values هنا)

# إنشاء Series من dict: المفاتيح تصبح labels
sdata = {'Ohio': 35000, 'Texas': 71000, 'Oregon': 16000, 'Utah': 5000}  # قاموس يمثل بيانات ولايات
obj3 = pd.Series(sdata)                                                # تحويل القاموس إلى Series
print(obj3)                                                            # ترتيب المفاتيح يكون غالبًا أبجديًا

# إنشاء Series أخرى مع index معيّن يختلف عن مفاتيح القاموس
states = ['California', 'Ohio', 'Oregon', 'Texas']  # قائمة بالـlabels المرغوبة
obj4 = pd.Series(sdata, index=states)               # إنشاء Series بحيث يُعاد ترتيب و إضافة NaN عند الغائب
print(obj4)                                         # ملاحظة ظهور NaN لـ California

# الكشف عن القيم المفقودة NaN
print(pd.isnull(obj4))  # إرجاع Series من قيم منطقية True/False لوجود NaN
print(pd.notnull(obj4)) # العكس: True للقيم غير المفقودة
print(obj4.isnull())    # استدعاء isnull مباشرة من الـSeries

# محاذاة تلقائية بالـindex في العمليات الحسابية
print(obj3)          # عرض Series الأولى
print(obj4)          # عرض Series الثانية
print(obj3 + obj4)   # جمع السلسلتين؛ تُجمع القيم ذات نفس الـlabel و تُنتج NaN عند عدم وجود label في أحدهما

# تسمية Series و تسمية الـindex
obj4.name = 'population'   # إعطاء اسم للسلسلة (مثلاً population)
obj4.index.name = 'state'  # إعطاء اسم لمحور الـindex (مثلاً state)
print(obj4)                # طباعة Series بعد التسمية

# تغيير index بالكامل دفعة واحدة
obj_tmp = pd.Series([4, 7, -5, 3])           # إنشاء Series جديدة مع index افتراضي
obj_tmp.index = ['Bob', 'Steve', 'Jeff', 'Ryan']  # تعيين index جديد كقائمة أسماء
print(obj_tmp)                               # عرض الـSeries بالـindex الجديد

# ============================================
# 4) DataFrame basics – إنشاء من dict و التعامل مع الأعمدة و الصفوف
# ============================================

# إنشاء DataFrame من dict قوائم (كل قائمة تمثل عمودًا)
data = {                       # قاموس يحتوي على 3 أعمدة: state, year, pop
    'state': ['Ohio', 'Ohio', 'Ohio', 'Nevada', 'Nevada', 'Nevada'],  # قائمة قيم عمود state
    'year':  [2000, 2001, 2002, 2001, 2002, 2003],                    # قائمة قيم عمود year
    'pop':   [1.5,  1.7,  3.6,  2.4,  2.9,  3.2]                      # قائمة قيم عمود pop
}
frame = pd.DataFrame(data)      # إنشاء DataFrame من القاموس
print(frame)                    # طباعة DataFrame؛ index افتراضي 0..5 و الأعمدة بترتيب القاموس

print(frame.head())            # عرض أول 5 صفوف (هنا الجدول صغير لكن هذا هو الاستخدام القياسي)
print(frame.head(3))           # عرض أول 3 صفوف فقط

# تحديد ترتيب الأعمدة عند الإنشاء
frame_reordered = pd.DataFrame(data, columns=['pop', 'state', 'year'])  # إعادة ترتيب الأعمدة
print(frame_reordered)                                                 # عرض DataFrame بالأعمدة بالترتيب الجديد

# إنشاء DataFrame مع index مخصص و إضافة عمود غير موجود (debt سيصبح كله NaN)
frame2 = pd.DataFrame(                     # إنشاء DataFrame جديد
    data,
    columns=['year', 'state', 'pop', 'debt'],                 # ترتيب الأعمدة مع عمود debt الجديد
    index=['one', 'two', 'three', 'four', 'five', 'six']      # index مخصّص ككلمات
)
print(frame2)                          # عرض frame2
print(frame2.columns)                  # إظهار أسماء الأعمدة كـIndex object

# الوصول إلى عمود بطريقتين: dict-like و attribute-like
print(frame2['state'])  # الوصول لعمود state باستخدام []
print(frame2.year)      # الوصول لعمود year باستخدام النقطة (فقط إذا الاسم صالح كمتغير)

# الوصول إلى صف باستخدام loc مع label من الـindex
print(frame2.loc['three'])  # إرجاع صف label='three' كسلسلة Series

# تعديل عمود كامل بتعيين قيمة ثابتة (سكALAR)
frame2['debt'] = 16.5       # تعيين القيمة 16.5 لكل الصفوف في عمود debt
print(frame2)               # عرض DataFrame بعد التعديل

# تعديل عمود بتعيين مصفوفة NumPy بنفس طول الـindex
frame2['debt'] = np.arange(6.)  # تعيين القيم 0..5 على صفوف عمود debt
print(frame2)                   # عرض DataFrame بعد التعديل

# مثال توضيحي (فقط تعليق): لو استخدمنا np.arange(5) هنا سيسبب ValueError لاختلاف الطول

# تعيين Series إلى عمود مع محاذاة حسب index
val = pd.Series([-1.2, -1.5, -1.7], index=['two', 'four', 'five'])  # Series مع بعض labels المتطابقة مع index
frame2['debt'] = val                                               # محاذاة Series مع index frame2
print(frame2)                                                      # تظهر NaN في الصفوف الأخرى

# إنشاء عمود جديد من شرط منطقي
frame2['eastern'] = frame2.state == 'Ohio'  # إنشاء عمود boolean يساوي True إذا state='Ohio'
print(frame2)                               # عرض DataFrame مع العمود الجديد

# حذف عمود باستخدام del
del frame2['eastern']  # حذف العمود eastern من DataFrame
print(frame2.columns)  # عرض الأعمدة المتبقية بعد الحذف

# ملاحظة: لا يمكن إنشاء عمود جديد باستخدام frame2.eastern = ... (تعمل لكن مع تحذيرات؛ الأفضل استخدام الأقواس)

# ============================================
# 5) View vs Copy في الأعمدة
# ============================================

cl_view = frame2['debt']   # أخذ عمود debt (غالبًا view على البيانات الأصلية)
cl_view.iloc[0] = 1.0      # تعديل أول عنصر في view – قد يعدّل DataFrame الأصلي أيضًا
print(frame2['debt'])      # نلاحظ أن أول قيمة أصبحت 1.0

cl_copy = frame2['debt'].copy()  # إنشاء نسخة مستقلة من العمود
cl_copy.iloc[0] = 10.0           # تعديل النسخة فقط
print(cl_copy)                   # طباعة النسخة المعدّلة (أول قيمة 10)
print(frame2['debt'])            # التأكد أن العمود الأصلي لم يتغير (ما زال 1.0 في أول عنصر)

# ============================================
# 6) DataFrame من dict متداخل + transpose + dict of Series
# ============================================

pop = {                                # قاموس من قواميس (nested dict)
    'Nevada': {2001: 2.4, 2002: 2.9},  # قاموس فرعي لقيم Nevada حسب السنة
    'Ohio':   {2000: 1.5, 2001: 1.7, 2002: 3.6}  # قاموس فرعي لقيم Ohio
}
frame3 = pd.DataFrame(pop)   # إنشاء DataFrame؛ الأعمدة = أسماء الولايات، الـindex = السنوات
print(frame3)                # عرض frame3

print(frame3.T)              # .T لعمل transpose (تبديل الصفوف بالأعمدة)

# تحديد index عند الإنشاء من dict متداخل
frame3_with_index = pd.DataFrame(pop, index=[2001, 2002, 2003])  # تحديد السنوات كـindex
print(frame3_with_index)                                         # تظهر NaN للسنة 2003

# dict of Series (قواميس أعمدتها Series)
pdata = {                            # قاموس يحتوي على Series لكل ولاية
    'Ohio': frame3['Ohio'][:-1],     # أخذ كل السنوات ما عدا الأخيرة لـOhio
    'Nevada': frame3['Nevada'][:2]   # أخذ أول قيمتين لـNevada
}
frame_from_pdata = pd.DataFrame(pdata)  # إنشاء DataFrame من dict of Series
print(frame_from_pdata)                 # عرض النتيجة

# أسماء للـindex و الأعمدة و values
frame3.index.name = 'year'   # تسمية محور الصفوف بـyear
frame3.columns.name = 'state' # تسمية محور الأعمدة بـstate
print(frame3)                 # عرض DataFrame مع التسميات

print(frame3.values)          # الحصول على القيم كمصفوفة ثنائية الأبعاد NumPy
print(frame2.values)          # الحصول على قيم frame2 كمصفوفة (قد تحتوي أنواعا مختلفة => dtype=object)

# ============================================
# 7) Index objects – خصائص و عمليات شبيهة بالمجموعة
# ============================================

obj_for_index = pd.Series(range(3), index=['a', 'b', 'c'])  # Series بقيم 0..2 و index 'a','b','c'
idx = obj_for_index.index                                   # الحصول على كائن Index
print(idx)                                                  # طباعة الـIndex
print(idx[1:])                                              # تقطيع Index من الموضع 1 حتى النهاية

# Index غير قابل للتعديل (immutable)، السطر التالي سيولد خطأ لو أزلنا الـtry/except
try:
    idx[1] = 'd'    # محاولة تغيير عنصر داخل Index (غير مسموح)
except TypeError as e:
    print("Index is immutable:", e)  # طباعة رسالة توضيحية عن الخطأ

# مشاركة Index بين أكثر من Series
labels = pd.Index(["Sam", "Zac", "Al"])             # إنشاء Index يدويًا
obj_shared = pd.Series([1.5, -2.5, 0], index=labels)  # Series تستخدم نفس الـIndex
print(obj_shared)                                   # طباعة Series
print(obj_shared.index is labels)                  # التحقق أن index هو نفسه الكائن labels (نفس الهوية)

# خصائص شبيهة بالمجموعة (membership)
print(frame3.columns)                # عرض أسماء الأعمدة كـIndex
print('Ohio' in frame3.columns)      # فحص وجود 'Ohio' كعمود
print(2003 in frame3.index)          # فحص وجود 2003 كصف في الـindex

# Index يمكن أن يحتوي على قيم مكررة
dup_labels = pd.Index(['foo', 'foo', 'bar', 'bar'])  # إنشاء Index بقيم مكررة
print(dup_labels)                                    # طباعة الـIndex ذو التكرار

# بعض عمليات المجموعات بين indexات
print(frame2.index.union(frame3.index))         # اتحاد index بين frame2 و frame3
print(frame2.index.intersection(frame3.index))  # تقاطع index بينهما
print(frame2.index.difference(frame3.index))    # الفرق: العناصر الموجودة في frame2.index فقط

# بعض الدوال الشائعة على Index
print(frame2.index.delete(0))           # إرجاع Index جديد بعد حذف العنصر عند الموضع 0
print(frame2.index.drop('one', errors='ignore'))  # حذف label معين من الـIndex (مع تجاهل الخطأ إن لم يوجد)
print(frame2.index.is_monotonic_increasing)       # هل index متزايد (مرتب)؟
print(frame2.index.is_unique)                     # هل كل القيم في index فريدة؟
print(frame2.index.unique())                      # إرجاع Index بالقيم الفريدة فقط

# مثال على Index مكرر والـloc يرجع أكثر من صف
frame2_dup = frame2.copy()                  # عمل نسخة من frame2
frame2_dup.index = ['one', 'one', 'three', 'four', 'five', 'six']  # جعل أول صفين بنفس label 'one'
print(frame2_dup.loc['one'])               # loc على label مكرر يرجّع صفين

# ============================================
# 8) Selection / Indexing مع DataFrame و Series بما فيها loc و iloc
# ============================================

# إنشاء DataFrame بسيط لمثال الفهرسة
data_idx = pd.DataFrame(                      # إنشاء DataFrame من مصفوفة أعداد
    np.arange(16).reshape((4, 4)),           # مصفوفة 4x4 بالأرقام 0..15
    index=['Ohio', 'Colorado', 'Utah', 'New York'],  # index أسماء ولايات
    columns=['one', 'two', 'three', 'four']          # أسماء الأعمدة
)
print(data_idx)                               # عرض DataFrame

# اختيار عمود واحد أو أكثر بـ[]
print(data_idx['two'])                        # اختيار عمود واحد، النتيجة Series
print(data_idx[['three', 'one']])             # اختيار عدة أعمدة بإعطاء قائمة أسماء

# تقطيع الصفوف مثل NumPy باستخدام slice
print(data_idx[:2])                           # اختيار أول صفين (Ohio و Colorado)

# Boolean indexing (تحديد الصفوف بشرط على عمود)
print(data_idx[data_idx['three'] > 5])        # اختيار الصفوف التي قيمة عمود three فيها أكبر من 5

# مقارنة كاملة مع عدد يعيد DataFrame منطقي
bool_df = data_idx < 5                        # مقارنة كل القيم مع 5 تعيد True/False
print(bool_df)                                # طباعة DataFrame المنطقي

# استخدام DataFrame المنطقي لتعيين قيم
data_tmp = data_idx.copy()                    # إنشاء نسخة للعمل عليها
data_tmp[data_tmp < 5] = 0                    # استبدال كل القيم <5 بـ0
print(data_tmp)                               # عرض DataFrame بعد الاستبدال

# ========= loc (label-based) =========
print(data_idx.loc['Colorado', ['two', 'three']])  # اختيار صف label='Colorado' وعمودين بالـlabels

# تقطيع بالـlabels – النهاية شاملة في loc
print(data_idx.loc[:'Utah', 'two'])           # اختيار الصفوف حتى 'Utah' وعمود 'two' فقط

# ========= iloc (position-based) =========
print(data_idx.iloc[2, [3, 0, 1]])            # اختيار صف رقم 2 و الأعمدة 3,0,1 (بالترتيب الجديد)
print(data_idx.iloc[2])                       # اختيار صف رقم 2 بالكامل كـSeries
print(data_idx.iloc[[1, 2], [3, 0, 1]])       # اختيار صفين (1 و2) وأعمدة متعددة

# iloc مع تقطيع الصفوف و الأعمدة ثم فلترة بشرط
print(data_idx.iloc[:, :3][data_idx['three'] > 5])  # أخذ أول 3 أعمدة ثم اختيار الصفوف بشرط على three

# ========= at / iat للوصول إلى قيمة واحدة =========
print(data_idx.at['Ohio', 'one'])   # at للوصول إلى قيمة scalar باستخدام labels
print(data_idx.iat[0, 0])           # iat للوصول إلى قيمة scalar باستخدام أرقام المواضع

# ============================================
# 9) Integer index semantics مع Series + loc/iloc
# ============================================

ser = pd.Series(np.arange(3.))  # Series بقيم 0.0,1.0,2.0 و index افتراضي 0,1,2 (أعداد صحيحة)
print(ser)                      # طباعة Series

# محاولة استخدام ser[-1] غير مفضلة لأنه غامض؛ في بعض الإصدارات قد تعطي خطأ
try:
    print(ser[-1])              # محاولة الوصول باستخدام index سالب (قد تثير خطأ)
except Exception as e:
    print("Direct ser[-1] is ambiguous / may fail:", e)  # توضيح أن الاستخدام غير آمن

ser2 = pd.Series(np.arange(3.), index=['a', 'b', 'c'])  # Series مع index نصي
print(ser2[-1])                                         # هنا -1 يُفسّر كفهرسة مكانية (آخر عنصر)

# استخدام loc و iloc لحسم الالتباس
print(ser[:1])                 # تقطيع عادي – يستخدم أرقام المواضع مثل NumPy (حتى قبل الموضع 1)
print(ser.loc[:1])             # loc بالـlabels – النهاية شاملة (labels 0 و1)
print(ser.iloc[:1])            # iloc بالأرقام – يأخذ أول عنصر فقط (الموضع 0)

# ============================================
# 10) Arithmetic alignment بين Series و DataFrame
# ============================================

s1 = pd.Series([7.3, -2.5, 3.4, 1.5], index=['a', 'c', 'd', 'e'])  # Series أولى مع index معين
s2 = pd.Series([-2.1, 3.6, -1.5, 4, 3.1], index=['a', 'c', 'e', 'f', 'g'])  # Series ثانية
print(s1)                      # عرض السلسلة الأولى
print(s2)                      # عرض السلسلة الثانية
print(s1 + s2)                 # جمع مع محاذاة labels؛ ينتج NaN عندما لا يوجد label في أحدهما

df1 = pd.DataFrame(                 # DataFrame أول
    np.arange(9.).reshape((3, 3)),  # مصفوفة 3x3 بالقيم 0..8
    columns=list('bcd'),            # الأعمدة b,c,d
    index=['Ohio', 'Texas', 'Colorado']  # index الولايات
)
df2 = pd.DataFrame(                 # DataFrame ثانٍ
    np.arange(12.).reshape((4, 3)), # مصفوفة 4x3 بالقيم 0..11
    columns=list('bde'),            # الأعمدة b,d,e
    index=['Utah', 'Ohio', 'Texas', 'Oregon']  # index مختلف جزئيًا
)
print(df1)                    # عرض DataFrame الأول
print(df2)                    # عرض DataFrame الثاني
print(df1 + df2)              # جمع مع محاذاة الصفوف و الأعمدة؛ القيم غير المشتركة تصبح NaN

df3 = pd.DataFrame({'A': [1, 2]})  # DataFrame بعمود A فقط
df4 = pd.DataFrame({'B': [3, 4]})  # DataFrame بعمود B فقط
print(df3 + df4)                   # لا يوجد صفوف/أعمدة مشتركة؛ النتيجة كلها NaN

# ============================================
# 11) مثال عملي: تنظيف و استكشاف بيانات طلاب (student_data)
# ============================================

# بدلاً من القراءة من CSV، ننشئ نفس البيانات هنا كقائمة قواميس
student_data = [  # كل dict يمثل صف طالب
    {"ID": 1, "Age": 18, "StudyHours": 12, "Absences": 3,  "Assignments": 8,  "Test1": 75, "Test2": 80, "Projects": 90, "Participation": 10, "FinalGrade": 85, "Class": "Pass"},
    {"ID": 2, "Age": 19, "StudyHours": np.nan, "Absences": 0,  "Assignments": 10, "Test1": 88, "Test2": 82, "Projects": 85, "Participation": 9,  "FinalGrade": 87, "Class": "Pass"},
    {"ID": 3, "Age": 18, "StudyHours": 5,  "Absences": -1, "Assignments": 6,  "Test1": 40, "Test2": 45, "Projects": 50, "Participation": 2,  "FinalGrade": 48, "Class": "Fail"},
    {"ID": 4, "Age": 20, "StudyHours": 8,  "Absences": 2,  "Assignments": 9,  "Test1": 55, "Test2": 60, "Projects": 70, "Participation": 8,  "FinalGrade": 65, "Class": "Pass"},
    {"ID": 5, "Age": 21, "StudyHours": 15, "Absences": 4,  "Assignments": 10, "Test1": np.nan, "Test2": 85, "Projects": 80, "Participation": 10, "FinalGrade": 88, "Class": "Pass"},
    {"ID": 6, "Age": 17, "StudyHours": 3,  "Absences": 7,  "Assignments": 5,  "Test1": 30, "Test2": 35, "Projects": 40, "Participation": 3,  "FinalGrade": 38, "Class": "Fail"},
    {"ID": 7, "Age": 18, "StudyHours": 10, "Absences": 1,  "Assignments": np.nan, "Test1": 65, "Test2": 70, "Projects": 75, "Participation": 7,  "FinalGrade": 72, "Class": "Pass"},
    {"ID": 8, "Age": 19, "StudyHours": 7,  "Absences": 2,  "Assignments": 8,  "Test1": 60, "Test2": 62, "Projects": 65, "Participation": 6,  "FinalGrade": 66, "Class": "Pass"},
    {"ID": 9, "Age": 20, "StudyHours": 4,  "Absences": 3,  "Assignments": 4,  "Test1": 35, "Test2": 40, "Projects": 42, "Participation": 2,  "FinalGrade": 44, "Class": "Fail"},
    {"ID": 10, "Age": 21, "StudyHours": 13, "Absences": 0,  "Assignments": 10, "Test1": 90, "Test2": 92, "Projects": 95, "Participation": 10, "FinalGrade": 94, "Class": "Pass"},
]

df = pd.DataFrame(student_data)  # تحويل قائمة القواميس إلى DataFrame
print("Original student DataFrame:")  # طباعة عنوان توضيحي
print(df)                           # عرض الجدول الأصلي

print(df.tail())                    # عرض آخر 5 صفوف (هنا نفس الجدول تقريبًا)
print(df.isnull())                  # جدول منطقي يوضّح أماكن القيم المفقودة
print(df.columns)                   # عرض أسماء الأعمدة
print(df.index)                     # عرض الـindex
print(df.info())                    # معلومات عن الأعمدة وأنواع البيانات وعدد القيم غير المفقودة

# مثال: الحصول على عمر أول طالب
print(df.loc[0, 'Age'])             # استخدام loc للوصول لعمر الطالب في الصف 0

# ---------- 2) Data Cleaning ----------
# استبدال NaN في الأعمدة الرقمية بالـmedian لكل عمود
medians = df.median(numeric_only=True)  # حساب median لكل الأعمدة الرقمية
df.fillna(value=medians, inplace=True)  # استبدال NaN بالـmedian في نفس DataFrame

# بديل آخر مكافئ (تعليمي فقط – لا حاجة لتنفيذه مرتين عادة)
numeric_cols = df.select_dtypes(include=[np.number]).columns  # اختيار أسماء الأعمدة الرقمية فقط
for col in numeric_cols:                                      # تكرار على الأعمدة الرقمية
    median_val = df[col].median()                             # حساب median للعمود الحالي
    df[col] = df[col].fillna(median_val)                      # ملء قيم NaN في هذا العمود بالـmedian

# استبدال القيم السالبة (مثل Absences < 0) بـ 0 باستخدام where
df['Absences'] = df['Absences'].where(df['Absences'] >= 0, 0)  # إبقاء القيم >=0 كما هي و جعل الباقي 0

# مثال عام على جميع الأعمدة الرقمية: جعل أي قيمة سالبة =0
for col in numeric_cols:                       # لكل عمود رقمي
    df[col] = df[col].where(df[col] >= 0, 0)   # شرط where لإرجاع 0 بدلاً من القيم السالبة

# تحويل عمود Class إلى lowercase لتوحيد الشكل
df['Class'] = df['Class'].str.lower()          # تحويل نصوص العمود إلى حروف صغيرة

# حذف الصفوف المكررة (إن وجدت)
df.drop_duplicates(inplace=True)               # حذف أي صف مكرر تمامًا

# ---------- 3) Exploratory Data Analysis ----------
print(df.describe())                           # عرض إحصاءات وصفية للأعمدة الرقمية (count, mean, std, ...)

correlations = df.corr(numeric_only=True)      # حساب مصفوفة الارتباط بين الأعمدة الرقمية
print("Correlation with FinalGrade:")          # طباعة عنوان
print(correlations['FinalGrade'])              # عرض عمود ارتباط كل ميزة مع FinalGrade

covariances = df.cov(numeric_only=True)        # حساب مصفوفة التباين بين الأعمدة الرقمية
print("Covariance matrix:")                    # عنوان توضيحي
print(covariances)                             # عرض مصفوفة التباين

# مثال على قراءة قيمة ارتباط محددة بين Test1 و Test2
if 'Test1' in correlations.index and 'Test2' in correlations.columns:  # التأكد من وجود الأعمدة في مصفوفة الارتباط
    print("Correlation between Test1 and Test2:", correlations.loc['Test1', 'Test2'])  # طباعة قيمة الارتباط

# ---------- 4) Feature Reduction ----------
# نفترض أن Test1 و Test2 مرتبطان بقوة؛ يمكن حذف واحد لتقليل التكرار
if 'Test1' in df.columns:              # التأكد من وجود العمود
    df.drop(columns=['Test1'], inplace=True)  # حذف عمود Test1 من DataFrame
    print("Dropped Test1 column for feature reduction.")  # رسالة توضيحية

# ---------- 5) Label Encoding للعمود Class ----------
df['Class'] = df['Class'].map({'pass': 1, 'fail': 0})  # تحويل 'pass' إلى 1 و 'fail' إلى 0

print(df.head())                     # طباعة أول صفوف بعد التنظيف و الترميز

# ---------- 6) حفظ البيانات المنظّفة في ملف CSV ----------
df.to_csv("cleaned_student_data.csv", index=False)  # حفظ DataFrame المنظّف في ملف CSV بدون index
print("Saved cleaned_student_data.csv")             # رسالة تأكيد الحفظ
