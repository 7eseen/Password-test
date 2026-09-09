import tkinter as tk
from tkinter import messagebox
import secrets
import string


def generate_password():
    # أخذ طول كلمة المرور من المستخدم
    try:
        length = int(length_entry.get())

        if length < 4:
            messagebox.showwarning("خطأ", "أقل عدد حروف هو 4")
            return

        # دمج الحروف والأرقام والرموز
        alphabet = string.ascii_letters + string.digits + string.punctuation

        # توليد كلمة مرور باستخدام مكتبة secrets
        password = ''.join(secrets.choice(alphabet) for _ in range(length))

        # عرض كلمة المرور في الواجهة
        password_var.set(password)

        # فحص القوة تلقائيًا بعد التوليد
        check_strength(password)

    except ValueError:
        messagebox.showerror("خطأ", "الرجاء إدخال رقم صحيح للطول")


def check_strength(password=None):
    # إذا لم يتم تمرير كلمة مرور خذها من الحقل النصي
    if password is None:
        password = password_var.get()

    if not password:
        strength_var.set("لم يتم إدخال كلمة مرور")
        return

    # فحص شروط القوة
    length = len(password)
    has_upper = any(c.isupper() for c in password)
    has_lower = any(c.islower() for c in password)
    has_digit = any(c.isdigit() for c in password)
    has_special = any(c in string.punctuation for c in password)

    # حساب النقاط
    score = sum([
        has_upper,
        has_lower,
        has_digit,
        has_special,
        length >= 12
    ])

    # تحديد مستوى القوة
    if score <= 2:
        strength_var.set("القوة: ضعيفة")
    elif score <= 4:
        strength_var.set("القوة: متوسطة")
    else:
        strength_var.set("القوة: قوية")


# إعداد واجهة المستخدم
root = tk.Tk()
root.title("أداة كلمات المرور")
root.geometry("400x300")

# المتغيرات
password_var = tk.StringVar()
strength_var = tk.StringVar(value="القوة غير محددة")

# العناصر
tk.Label(root, text="طول كلمة المرور", font=("Arial", 12)).pack(pady=5)

length_entry = tk.Entry(root, font=("Arial", 12), justify="center")
length_entry.insert(0, "12")
length_entry.pack(pady=5)

tk.Button(
    root,
    text="توليد كلمة مرور",
    command=generate_password,
    font=("Arial", 12)
).pack(pady=5)

tk.Entry(
    root,
    textvariable=password_var,
    font=("Arial", 14),
    justify="center",
    width=25
).pack(pady=10)

tk.Button(
    root,
    text="فحص كلمة المرور المكتوبة",
    command=check_strength,
    font=("Arial", 10)
).pack(pady=5)

tk.Label(
    root,
    textvariable=strength_var,
    font=("Arial", 14, "bold")
).pack(pady=10)

root.mainloop()