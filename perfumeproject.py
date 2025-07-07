import tkinter as tk
from tkinter import messagebox
import customtkinter
from PIL import Image, ImageTk
import sqlite3
conn = sqlite3.connect(r"D:\pj\admin.db")
cursor = conn.cursor()

def connect_db():
    conn = sqlite3.connect(r"D:\pj\admin.db")
    cursor = conn.cursor()
    return conn, cursor

def login():
    username = Entry_username.get()
    password = Entry_password.get()
    if check_login(username, password):
        messagebox.showinfo("Login", "Login Successful!")
        open_shop_window()  # เปิดหน้าต่างร้านค้าหลังจากล็อกอินสำเร็จ
    else:
        messagebox.showerror("Login", "Invalid username or password.")

def check_login(username, password):
    conn, cursor = connect_db()
    cursor.execute("SELECT * FROM users WHERE Username = ? AND Password = ?", (username, password))
    result = cursor.fetchone()
    conn.close()
    return result is not None

def register_user(Name, Birthday, Username, Password):
    try:
        conn, cursor = connect_db()
        cursor.execute("INSERT INTO users (Name, Birthday, Username, Password) VALUES (?, ?, ?, ?)", 
                       (Name, Birthday, Username, Password))
        conn.commit()
        messagebox.showinfo("Registration", "Registration Successful!")
    except sqlite3.Error as e:
        messagebox.showerror("Error", f"An error occurred: {e}")
    finally:
        conn.close()

def submit_registration():
    Name = Entry_Name.get()
    Birthday = Entry_Birthday.get()
    Username = Entry_Username.get()
    Password = Entry_Password.get()

    if Name and Birthday and Username and Password:
        register_user(Name, Birthday, Username, Password)
        window2.withdraw()
        window.deiconify()
    else:
        messagebox.showerror("Error", "Please fill in all fields.")

def open_window2():
    window.withdraw()
    window2.deiconify()

def open_window3():
    window.withdraw()
    window3.deiconify()

def toggle_password():
    if Entry_password.cget('show') == '*':
        Entry_password.configure(show="") 
        img_eye.config(image=photo_eye_open)  
    else:
        Entry_password.configure(show='*')
        img_eye.config(image=photo_eye_closed) 

window = tk.Tk()
window.title("My Perfume")
window.geometry("1920x1080")

image_path = r"log in.png"
image = Image.open(image_path)
image = image.resize((1600,700))
photo = ImageTk.PhotoImage(image)

label_image = tk.Label(master=window, image=photo, bg="#fffff1")
label_image.place(x=5, y=12)

Button1 = customtkinter.CTkButton(
    master=window, text="Log in",
    font=("Georgia", 14),
    command=login
)
Button1.place(x=1130, y=390)

Button2 = customtkinter.CTkButton(
    master=window, text="register",
    font=("Georgia", 14),
    command=open_window2
)
Button2.place(x=1130, y=440)

Button3 = customtkinter.CTkButton(
    master=window, text="admin",
    font=("Georgia", 14),
    command=open_window3
)
Button3.place(x=50, y=25)

Entry_username = customtkinter.CTkEntry(
    master=window,
    placeholder_text="Username",
    font=("Georgia", 14),
    height=30,
    width=195
)
Entry_username.place(x=1100, y=290)

Entry_password = customtkinter.CTkEntry(
    master=window,
    placeholder_text="Password",
    show="*",  
    font=("Georgia", 14),
    height=30,
    width=195
)
Entry_password.place(x=1100, y=340)

photo_eye_closed = ImageTk.PhotoImage(Image.open(r"eye_closed.jpg").resize((18, 18)))
photo_eye_open = ImageTk.PhotoImage(Image.open(r"eye_open.jpg").resize((18, 18)))
img_eye = tk.Button(master=window, image=photo_eye_closed, command=toggle_password, borderwidth=0, bg="#fffff1")
img_eye.place(x=1272, y=344)


window2 = tk.Toplevel()
window2.title("My Perfume")
window2.geometry("1920x1080")
window2.configure(bg="#FFFFFF")
window2.withdraw()

image_path2 = r"sign up.png"
image2 = Image.open(r"sign up.png")
image2 = image2.resize((1600, 700))  
photo2 = ImageTk.PhotoImage(image2)

label_image2 = tk.Label(master=window2, image=photo2, bg="#44312B")
label_image2.place(x=5, y=12)

Entry_Name = customtkinter.CTkEntry(master=window2, placeholder_text="Name", font=("Arial", 14))
Entry_Name.place(x=250, y=300)

Entry_Birthday = customtkinter.CTkEntry(master=window2, placeholder_text="Birthday", font=("Arial", 14))
Entry_Birthday.place(x=450, y=300)

Entry_Username = customtkinter.CTkEntry(master=window2, placeholder_text="Username", font=("Arial", 14))
Entry_Username.place(x=250, y=350)

Entry_Password = customtkinter.CTkEntry(master=window2, placeholder_text="Password", show="*", font=("Arial", 14))
Entry_Password.place(x=450, y=350)

Button_sign_up = customtkinter.CTkButton(
    master=window2, text="Sign in", font=("Arial", 14), command=submit_registration
)
Button_sign_up.place(x=345, y=450)

Checkbox_id5 = customtkinter.CTkCheckBox(
    master=window2,
    text="Consent to Disclosure of Personal Information"
)
Checkbox_id5.place(x=270, y=400)

def open_shop_window():
    window.withdraw() 
    shop_window = tk.Toplevel()
    shop_window.title("Shop - My Perfume")
    shop_window.geometry("1920x1080")
    shop_window.configure(bg="#44312B")
    
    bg_image = Image.open(r"product.png")
    bg_image = bg_image.resize((1400, 800)) 
    bg_photo = ImageTk.PhotoImage(bg_image)
    
    bg_label = tk.Label(shop_window, image=bg_photo)
    bg_label.image = bg_photo  
    bg_label.place(x=0, y=0, relwidth=1, relheight=1) 

    button_frame = tk.Frame(shop_window)
    button_frame.pack(pady=90)
    button_frame.place(x=65, y=600)

    customtkinter.CTkButton(button_frame, text="Floral",font=("Arial", 30), command=lambda: display_products(shop_window, "Floral")).pack(side=tk.LEFT, padx=110,pady=30)
    customtkinter.CTkButton(button_frame,text="Fruity",font=("Arial", 30), command=lambda: display_products(shop_window, "Fruity")).pack(side=tk.LEFT, padx=110,pady=30)
    customtkinter.CTkButton(button_frame,text="Woody",font=("Arial", 30), command=lambda: display_products(shop_window, "Woody")).pack(side=tk.LEFT, padx=110,pady=30)
    customtkinter.CTkButton(button_frame, text="Oriental",font=("Arial", 30), command=lambda: display_products(shop_window, "Oriental")).pack(side=tk.LEFT, padx=110,pady=30)
    
    
    # สร้างปุ่มกลับไปหน้า login
    Button_back = customtkinter.CTkButton(
        master=shop_window, 
        text="Exits", 
        font=("Arial", 14), 
        command=lambda: [shop_window.destroy(), window.deiconify()] 
    )
    Button_back.place(x=40, y=10)

    # จัดการการปิดหน้าต่าง
    shop_window.protocol("WM_DELETE_WINDOW", lambda: [shop_window.destroy(), window.deiconify()])

def display_products(shop_window, category):
    # ลบ widget เก่าทั้งหมดในหน้าต่าง
    for widget in shop_window.winfo_children():
        widget.destroy()
     
    # สร้าง label สำหรับหัวข้อ
    title_label = tk.Label(shop_window, text=f"{category} Perfumes", font=("Arial", 50), bg="#44312B", fg="#F2E6DC")
    title_label.pack(pady=20)

    # ดึงข้อมูลสินค้าจากฐานข้อมูล
    conn, cursor = connect_db()
    cursor.execute("SELECT name, price, image_path FROM products WHERE category = ?", (category,))
    products = cursor.fetchall()
    conn.close()

    # สร้าง canvas และ scrollbar สำหรับการเลื่อน
    canvas = tk.Canvas(shop_window, bg="#44312B")
    scrollbar = tk.Scrollbar(shop_window, orient="vertical", command=canvas.yview)
    canvas.configure(yscrollcommand=scrollbar.set)

    # สร้าง frame สำหรับแสดงสินค้าใน canvas
    products_frame = tk.Frame(canvas, bg="#44312B")
    canvas.create_window((0, 0), window=products_frame, anchor="nw")

    canvas.pack(side="left", fill="both", expand=True)
    scrollbar.pack(side="right", fill="y")

    # แสดงสินค้าในกรอบ frame
    for i, (name, price, img_path) in enumerate(products):
        display_product(products_frame, name, price, img_path, i // 4, i % 4)

    products_frame.update_idletasks()


    # อัปเดต scroll region ของ canvas
    canvas.config(scrollregion=canvas.bbox("all"))

    # ปุ่ม "View Cart" และ "Checkout"
    Button_view_cart = customtkinter.CTkButton(
        master=shop_window, text="View Cart", font=("Arial", 14), command=lambda: view_cart(shop_window)
    )
    Button_view_cart.place(x=1300, y=10)

    Button_checkout = customtkinter.CTkButton(
        master=shop_window, text="Checkout", font=("Arial", 14), command=lambda: checkout(shop_window)
    )
    Button_checkout.place(x=1300, y=50)

    # ปุ่ม "Back to Categories"
    Button_back = customtkinter.CTkButton(
        master=shop_window, text="Back to Categories", font=("Arial", 14), command=lambda: display_categories(shop_window)
    )
    Button_back.place(x=40, y=10)

    # สร้างปุ่ม "About Us"
    Button_About_Us = customtkinter.CTkButton(
        master=shop_window, text="About Us", font=("Arial", 14), command=lambda: About_Us(shop_window)
    )
    Button_About_Us.place(x=40, y=50)

    
    # สร้างปุ่มกลับไปหน้า login
    Button_back = customtkinter.CTkButton(
        master=shop_window, 
        text="Exits", 
        font=("Arial", 14), 
        command=lambda: [shop_window.destroy(), window.deiconify()] 
    )
    Button_back.place(x=40, y=90)

    # จัดการการปิดหน้าต่าง
    shop_window.protocol("WM_DELETE_WINDOW", lambda: [shop_window.destroy(), window.deiconify()])

def display_product(products_frame, perfume_name, perfume_price, perfume_image_path, row, column):
    product_frame = tk.Frame(products_frame, bg="#DABA9D")
    product_frame.grid(row=row, column=column, padx=10, pady=10)

    try:
        # ตรวจสอบว่า image_path เป็นไฟล์ที่มีอยู่จริง
        if not os.path.exists(perfume_image_path):
            raise FileNotFoundError(f"Image file not found: {perfume_image_path}")

        # เปิดรูปภาพและปรับขนาด
        perfume_image = Image.open(perfume_image_path)
        perfume_image = perfume_image.resize((350, 350))
        perfume_photo = ImageTk.PhotoImage(perfume_image)

        # แสดงรูปภาพใน Label
        image_label = tk.Label(product_frame, image=perfume_photo, bg="#44312B")
        image_label.image = perfume_photo  # เก็บอ้างอิงไว้เพื่อไม่ให้ถูก garbage-collected
        image_label.pack()

        
        # ลบ "฿" และ "," ออกจากราคา ก่อนแปลงเป็น float
        try:
            perfume_price = perfume_price.replace("฿", "").replace(",", "")
            perfume_price = float(perfume_price)  # แปลงเป็น float
        except ValueError:
            perfume_price = 0.0  # หากแปลงไม่ได้ ให้ตั้งค่าเป็น 0.0

        # ฟอร์แมตราคาใหม่
        formatted_price = f"฿{perfume_price:,.0f}" 

        # แสดงชื่อและราคา
        name_label = tk.Label(product_frame, text=perfume_name, font=("Arial", 16), bg="#F2E6DC")
        name_label.pack(pady=5)

        price_label = tk.Label(product_frame, text=formatted_price, font=("Arial", 16), fg="black", bg="#FFFFFF")
        price_label.pack()

        # ปุ่ม Add to Cart
        add_to_cart_button = customtkinter.CTkButton(
            master=product_frame, text="Add to Cart", font=("Arial", 12),
            command=lambda: add_to_cart(perfume_name, perfume_price)
        )
        add_to_cart_button.pack(pady=5)

    except Exception as e:
        # ถ้ามีปัญหาในการโหลดรูปภาพหรือไฟล์ไม่พบ ให้แสดงข้อผิดพลาด
        messagebox.showerror("Error", f"Could not load image: {e}")

def About_Us(shop_window):
    for widget in shop_window.winfo_children():
        widget.destroy()
        
    bg_image = Image.open(r"about.png")
    bg_image = bg_image.resize((1400, 800))
    bg_photo = ImageTk.PhotoImage(bg_image)
    
    bg_label = tk.Label(shop_window, image=bg_photo)
    bg_label.image = bg_photo  
    bg_label.place(x=0, y=0, relwidth=1, relheight=1) 

    button_frame = tk.Frame(shop_window)
    button_frame.pack(pady=90)
    button_frame.place(x=65, y=600)

    # สร้างปุ่ม "Back to Categories"
    Button_back = customtkinter.CTkButton(
        master=shop_window, text="Back to Categories", font=("Arial", 14), command=lambda: display_categories(shop_window)
    )
    Button_back.place(x=40, y=10)


def display_categories(shop_window):
    for widget in shop_window.winfo_children():
        widget.destroy()
    
    bg_image = Image.open(r"product.png")
    bg_image = bg_image.resize((1400, 800)) 
    bg_photo = ImageTk.PhotoImage(bg_image)
    
    bg_label = tk.Label(shop_window, image=bg_photo)
    bg_label.image = bg_photo  
    bg_label.place(x=0, y=0, relwidth=1, relheight=1) 

    button_frame = tk.Frame(shop_window)
    button_frame.pack(pady=90)
    button_frame.place(x=65, y=600)

    customtkinter.CTkButton(button_frame, text="Floral",font=("Arial", 30), command=lambda: display_products(shop_window, "Floral")).pack(side=tk.LEFT, padx=110,pady=30)
    customtkinter.CTkButton(button_frame,text="Fruity",font=("Arial", 30), command=lambda: display_products(shop_window, "Fruity")).pack(side=tk.LEFT, padx=110,pady=30)
    customtkinter.CTkButton(button_frame,text="Woody",font=("Arial", 30), command=lambda: display_products(shop_window, "Woody")).pack(side=tk.LEFT, padx=110,pady=30)
    customtkinter.CTkButton(button_frame, text="Oriental",font=("Arial", 30), command=lambda: display_products(shop_window, "Oriental")).pack(side=tk.LEFT, padx=110,pady=30)

shopping_cart=[]

global name
global quantity
# ฟังก์ชันดึงจำนวนสินค้าคงเหลือในฐานข้อมูล
def get_stock_quantity_from_db(name):
    conn, cursor = connect_db()
    cursor.execute("SELECT quantity FROM products WHERE name=?", (name,))
    result = cursor.fetchone()
    return result[0] if result else 0

def add_to_cart(name, price):
    # ตรวจสอบว่าในตะกร้ามีสินค้านี้อยู่แล้วหรือไม่
    for item in shopping_cart:
        if item[0] == name:  # ถ้ามีสินค้าอยู่แล้ว
            available_stock = get_stock_quantity_from_db(name)  
            if item[2] < available_stock:  # หากในตะกร้ายังมีจำนวนไม่เกินสต๊อก
                item[2] += 1  # เพิ่มจำนวน
            else:
                messagebox.showwarning("Stock Limit", "Cannot add more items, stock is limited.")
            return 
    # ถ้าไม่มีสินค้านี้ในตะกร้า ให้เพิ่มสินค้าลงไปใหม่
    available_stock = get_stock_quantity_from_db(name)
    if available_stock > 0:
        shopping_cart.append([name, price, 1])
    else:
        messagebox.showwarning("Out of Stock", "This item is out of stock.")
    get_stock_quantity_from_db(name)

# ฟังก์ชันในการแสดงผลตะกร้า
def view_cart(shop_window):
    cart_window = tk.Toplevel(shop_window)
    cart_window.title("Shopping Cart")
    cart_window.geometry("800x600") 
    cart_window.configure(bg="#f0f0f2")

    def increase_quantity(idx):
    # ใช้ idx เพื่อเข้าถึงข้อมูลสินค้าในตะกร้า
        name, price, quantity = shopping_cart[idx]
        
        # ตรวจสอบจำนวนสินค้าที่มีในฐานข้อมูล
        available_stock = get_stock_quantity_from_db(name)
        
        if quantity < available_stock:  # ตรวจสอบจำนวนสินค้าในตะกร้าไม่เกินจำนวนในฐานข้อมูล
            shopping_cart[idx][2] += 1  # เพิ่มจำนวนในตะกร้า
            update_cart(cart_window)
        else:
            messagebox.showwarning("Stock Limit", "Cannot add more items, stock is limited.")

    def decrease_quantity(idx):
        if shopping_cart[idx][2] > 1:
            shopping_cart[idx][2] -= 1  
            update_cart(cart_window)
        else:
            messagebox.showwarning("Warning", "Cannot decrease quantity below 1.")

    def remove_item(idx):
        del shopping_cart[idx]  
        update_cart(cart_window)
        
    def update_cart(cart_window):
    # ลบ widget เก่าทั้งหมดจาก cart_window
        for widget in cart_window.winfo_children():
            widget.destroy()

        # สร้าง Canvas และ Scrollbar
        canvas = tk.Canvas(cart_window, bg="#ffffff") 
        scrollbar = tk.Scrollbar(cart_window, orient="vertical", command=canvas.yview)
        canvas.configure(yscrollcommand=scrollbar.set)

        canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")

        # สร้าง content_frame เพื่อใส่ข้อมูลสินค้าทั้งหมด
        content_frame = tk.Frame(canvas, bg="#ffffff") 
        canvas.create_window((0, 0), window=content_frame, anchor="nw")

        content_frame.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))

        # สร้าง header ของตารางสินค้า
        header = tk.Frame(content_frame, bg="#ffffff")
        header.grid(row=0, column=0, sticky="w", padx=40, pady=10)
        tk.Label(header, text="Item", font=("Georgia", 14), bg="#ffffff").grid(row=0, column=0, padx=70)
        tk.Label(header, text="Price", font=("Georgia", 14), bg="#ffffff").grid(row=0, column=1, padx=10)
        tk.Label(header, text="Quantity", font=("Georgia", 14), bg="#ffffff").grid(row=0, column=2, padx=10)
        tk.Label(header, text="Total", font=("Georgia", 14), bg="#ffffff").grid(row=0, column=3, padx=10)
        tk.Label(header, text="Actions", font=("Georgia", 14), bg="#ffffff").grid(row=0, column=4, padx=30)

        # ถ้าตะกร้าสินค้าเป็นศูนย์
        if not shopping_cart:
            label = tk.Label(cart_window, text="Your cart is empty.", font=("Georgia", 16), bg="#ffffff")
            label.pack(pady=50)
        else:
            total_price = 0  # เริ่มคำนวณราคาทั้งหมด
            for idx, item in enumerate(shopping_cart):
                name, price, quantity = item
                price_formatted = f"฿{price:,.0f}"
                total_item_price = price * quantity
                total_item_price_formatted = f"฿{total_item_price:,.0f}" 

                row = tk.Frame(content_frame, bg="#ffffff")
                row.grid(row=idx+1, column=0, sticky="w", padx=10, pady=5)

                # แสดงรายละเอียดสินค้าในแถว
                tk.Label(row, text=name, font=("Georgia", 14), bg="#ffffff", width=20).grid(row=0, column=0, padx=10)
                tk.Label(row, text=price_formatted, font=("Georgia", 14), bg="#ffffff").grid(row=0, column=1, padx=10)
                tk.Label(row, text=quantity, font=("Georgia", 14), bg="#ffffff").grid(row=0, column=2, padx=10)
                tk.Label(row, text=total_item_price_formatted, font=("Georgia", 14), bg="#ffffff").grid(row=0, column=3, padx=10)

                # สร้างปุ่มเพิ่ม ลด และลบสินค้า
                action_frame = tk.Frame(row, bg="#ffffff")
                action_frame.grid(row=0, column=4, padx=20)
                
                button_increase = tk.Button(action_frame, text="+", font=("Georgia", 14), command=lambda idx=idx: increase_quantity(idx), width=3, bg="#56b4d3", fg="white", relief="flat")
                button_increase.grid(row=0, column=0, padx=10)

                button_decrease = tk.Button(action_frame, text="-", font=("Georgia", 14), command=lambda idx=idx: decrease_quantity(idx), width=3, bg="#56b4d3", fg="white", relief="flat")
                button_decrease.grid(row=0, column=1, padx=5)

                button_remove = tk.Button(action_frame, text="Remove", font=("Georgia", 14), command=lambda idx=idx: remove_item(idx), width=8, bg="#d9534f", fg="white", relief="flat")
                button_remove.grid(row=0, column=2, padx=5)

                total_price += total_item_price  # คำนวณราคาทั้งหมด

            # แสดงยอดรวม
            label_total = tk.Label(content_frame, text=f"Total: ฿{total_price:,.0f}", font=("Georgia", 18), bg="#ffffff")
            label_total.grid(row=len(shopping_cart)+1, column=0, columnspan=5, pady=20) 

    update_cart(cart_window)

def checkout(shop_window):
    global checkout_window
    global entry_name, entry_phone, entry_address  
    
    checkout_window = tk.Toplevel(shop_window)
    checkout_window.title("Checkout")
    checkout_window.geometry("900x600")
    checkout_window.configure(bg="#44312B")

    label_title = tk.Label(checkout_window, text="Please fill in your details", font=("Georgia", 36), bg="#F2E6DC")
    label_title.pack(pady=20)

    label_name = tk.Label(checkout_window, text="Name:", font=("Georgia", 24), bg="#F2E6DC")
    label_name.pack(pady=5)
    entry_name = customtkinter.CTkEntry(checkout_window, font=("Georgia", 20), width=500,height=80)
    entry_name.pack(pady=5)

    label_phone = tk.Label(checkout_window, text="Phone Number:", font=("Georgia", 24), bg="#F2E6DC")
    label_phone.pack(pady=5)
    entry_phone = customtkinter.CTkEntry(checkout_window, font=("Georgia", 20), width=500,height=80)
    entry_phone.pack(pady=5)

    label_address = tk.Label(checkout_window, text="Address:", font=("Georgia", 24), bg="#F2E6DC")
    label_address.pack(pady=5)
    entry_address = customtkinter.CTkEntry(checkout_window, font=("Georgia", 20), width=500, height=80)
    entry_address.pack(pady=5)

    button_finalize = customtkinter.CTkButton(
        master=checkout_window, text="Complete Order", font=("Arial", 24), command=finalize_checkout
    )
    button_finalize.pack(pady=20)

def finalize_checkout():
    global order_id
    name = entry_name.get()
    phone = entry_phone.get()
    address = entry_address.get()

    if not name or not phone or not address:
        messagebox.showerror("Error", "Please fill in all details!")
    else:
        total_price = 0
        for item in shopping_cart:
            price = item[1] 
            price = f"฿{price:,.0f}"
            price = price.replace('฿', '').replace(',', '')
            total_price += float(price) * item[2] 
            
        # บันทึกข้อมูลการสั่งซื้อไปยังฐานข้อมูล และได้รับ order_id
        order_id = save_to_database(name, phone, address, total_price, shopping_cart)
        # แสดงหน้าต่างสรุปคำสั่งซื้อพร้อม QR
        show_order_summary_with_qr(name, phone, address, total_price, shopping_cart, order_id)  # ส่ง order_id ด้วย
        # show_receipt_pdf(order_id, shopping_cart)
        show_receipt_pdf(order_id, shopping_cart)
        update_stock_after_checkout(shopping_cart)
        shopping_cart.clear()  # ล้างตะกร้าสินค้า


def save_to_database(name, phone, address, total_price, shopping_cart):
    from datetime import datetime  # นำเข้า datetime ถ้ายังไม่มี
    
    # ปรับให้ items มีราคาต่อหน่วยที่เป็น "บาท" และมีคอมม่า
    items = "\n".join([
        f"{item[0]} - ฿{float(item[1]):,.0f} x {item[2]}" 
        for item in shopping_cart
    ])
    
    # ดึงวันที่ปัจจุบัน
    order_date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')  # รูปแบบ YYYY-MM-DD HH:MM:SS

    # แปลงราคาสุทธิให้อยู่ในรูปแบบ "บาท" พร้อมคอมม่า
    total_price_formatted = f"฿{total_price:,.0f}"
    
    # เพิ่ม order_date ในคำสั่ง INSERT
    cursor.execute("""
        INSERT INTO orders (name, phone, address, total_price, items, order_date) 
        VALUES (?, ?, ?, ?, ?, ?)
    """, (name, phone, address, total_price_formatted, items, order_date))

    # ดึง order_id ที่ถูกสร้างขึ้น
    order_id = cursor.lastrowid  # ได้ค่า id ล่าสุดที่ถูกสร้างจากคำสั่ง INSERT
    conn.commit()
    return order_id


def show_order_summary_with_qr(name, phone, address, total_price, shopping_cart, order_id):
    qr_image_path = r"qr_code.jpg"
    try:
        qr_image = Image.open(qr_image_path)
        qr_image = qr_image.resize((250, 300))  
        qr_image_tk = ImageTk.PhotoImage(qr_image)
    except FileNotFoundError:
        print("QR Code image file not found.")
        return

    global order_window
    order_window = tk.Toplevel()
    order_window.title("Order Summary and Payment")
    order_window.geometry("400x800")
    order_window.configure(bg="#44312B")
    checkout_window.withdraw()
    order_window.deiconify()
    
    canvas = tk.Canvas(order_window, bg="#44312B") 
    scrollbar = tk.Scrollbar(order_window, orient="vertical", command=canvas.yview)
    canvas.configure(yscrollcommand=scrollbar.set)

    canvas.pack(side="left", fill="both", expand=True)
    scrollbar.pack(side="right", fill="y")

    frame = tk.Frame(canvas, bg="#44312B") 
    canvas.create_window((0, 0), window=frame, anchor="nw")
    frame.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))

    title_label = tk.Label(frame, text="Your Order Summary", font=("Georgia", 20, "bold"), bg="#F2E6DC", fg="#44312B")
    title_label.pack(pady=10, padx=50)

    info_frame = tk.Frame(frame, bg="#44312B")
    info_frame.pack(pady=20, padx=50)

    info_labels = [
        f"Name: {name}",
        f"Phone: {phone}",
        f"Address: {address}",
        f"Total Price: ฿{total_price:,.0f}",  
        f"Items Ordered:"
    ]
    
    for text in info_labels:
        label = tk.Label(info_frame, text=text, font=("Georgia", 18), bg="#44312B", fg="#F2E6DC", anchor="center")
        label.pack(pady=5, padx=50)

    for item in shopping_cart:
        name, price, quantity = item
        price_str = f"{price:,.0f}"  # ฟอร์แมตราคาให้เป็นข้อความ
        item_label = tk.Label(frame, text=f"{name} - ฿{price_str} x {quantity}", font=("Georgia", 12), anchor="w")
        item_label.pack()

    qr_label = tk.Label(frame, text="Scan this QR Code to pay", font=("Georgia", 18, "bold"), bg="#F2E6DC", fg="#44312B")
    qr_label.pack(pady=20)

    qr_img_label = tk.Label(frame, image=qr_image_tk)
    qr_img_label.image = qr_image_tk
    qr_img_label.pack(pady=10, padx=50)

    confirm_button = tk.Button (frame, text="Confirm Order", font=("Georgia", 20), bg="#F2E6DC", fg="#44312B", command=lambda: [
        messagebox.showinfo( "Thank You", "ขอบคุณที่เลือกใช้บริการของเรา!"),
        order_window.destroy()  # ปิดหน้าต่างสรุปคำสั่งซื้อ
    ])
    confirm_button.pack(pady=20)

import os
from datetime import datetime
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfbase import pdfmetrics


def show_receipt_pdf(order_id, shopping_cart):
    conn, cursor = connect_db()
    
    # ดึงข้อมูลจากฐานข้อมูล (ชื่อ, เบอร์โทร, ที่อยู่) ตาม order_id
    cursor.execute("SELECT name, phone, address, total_price FROM orders WHERE id = ?", (order_id,))
    customer_data = cursor.fetchone()
    
    if not customer_data:
        print(f"No order found with ID {order_id}")
        return
    
    name, phone, address, total_price = customer_data
    
    # ลงทะเบียนฟอนต์ภาษาไทย
    try:
        pdfmetrics.registerFont(TTFont('THSarabun', 'D:/pj/THSarabunNew.ttf'))
    except Exception as e:
        print(f"Error registering font: {e}")
        return
    
    # สร้างชื่อไฟล์ PDF โดยใช้เวลาปัจจุบัน
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    pdf_filename = f"receipt_{timestamp}.pdf"
    
    # สร้าง PDF
    c = canvas.Canvas(pdf_filename, pagesize=letter)
    
    # ใช้ฟอนต์ที่ลงทะเบียนไว้
    c.setFont("THSarabun", 14)

    # พิมพ์หัวข้อใบเสร็จ
    c.setFont("THSarabun", 18)
    c.drawString(70, 750, "ใบเสร็จสำหรับคำสั่งซื้อ")
    c.setFont("THSarabun", 14)
    c.drawString(70, 730, f"วันที่: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    c.drawString(70, 710, f"ชื่อลูกค้า: {name}")  # ใช้ชื่อที่ดึงมาจากฐานข้อมูล
    c.drawString(70, 690, f"เบอร์โทรศัพท์: {phone}")
    c.drawString(70, 670, f"ที่อยู่: {address}")

    # เส้นแบ่ง
    c.setStrokeColorRGB(0, 0, 0)
    c.setLineWidth(1)
    c.line(70, 650, 550, 650)

    # สรุปรายการสินค้า
    c.setFont("THSarabun", 14)
    y_position = 630
    c.drawString(70, y_position, "Item Description")
    c.drawString(300, y_position, "Unit Price")
    c.drawString(400, y_position, "Quantity")
    c.drawString(500, y_position, "Total")
    
    # เส้นแบ่งรายการสินค้า
    y_position -= 20
    c.line(70, y_position, 550, y_position)
    
    total = 0
    for item in shopping_cart:
            item_name, price, quantity = item
            if isinstance(price, str):
                price = float(price.replace('฿', '').replace(',', '').strip())
            item_total = price * quantity
            total += item_total
        
            # พิมพ์ข้อมูลรายการสินค้า
            c.drawString(70, y_position - 20, item_name)
            c.drawString(300, y_position - 20, f"฿{int(price):,}")  # ใส่คอมม่าที่ราคาต่อหน่วย
            c.drawString(400, y_position - 20, f"{quantity}")
            c.drawString(480, y_position - 20, f"฿{item_total:,.0f}")  
            # ปรับตำแหน่ง y สำหรับรายการถัดไป
            y_position -= 30
            
            if y_position < 100:
                c.showPage() 
                y_position = 750 
        
    # เส้นแบ่งสุดท้าย
    c.line(70, y_position, 550, y_position)

    # พิมพ์ราคาสุทธิ
    y_position -= 20
    c.setFont("THSarabun", 16)
    c.drawString(70, y_position, f"Total Amount: ฿{total:,.0f}")  # ใส่คอมม่าที่ราคารวม
    
    # เส้นแบ่งก่อนส่วนข้อความ
    y_position -= 40
    c.line(70, y_position, 550, y_position)

    # บันทึกไฟล์ PDF
    c.save()

    # เปิดไฟล์ PDF อัตโนมัติ
    try:
        if os.name == 'posix': 
            os.system(f'open {pdf_filename}')
        elif os.name == 'nt':  # สำหรับ Windows
            os.system(f'start {pdf_filename}')
    except Exception as e:
        print(f"Error opening PDF: {e}")
    
    conn.close()

def update_stock_quantity_in_db(product_name, new_quantity):
    """อัพเดทจำนวนสินค้าคงเหลือในฐานข้อมูล"""
    conn, cursor = connect_db()  # เชื่อมต่อกับฐานข้อมูล
    query = "UPDATE products SET quantity = ? WHERE name = ?"
    cursor.execute(query, (new_quantity, product_name))  # อัพเดทจำนวนสต็อก
    conn.commit() 
    cursor.close() 
    conn.close() 
    
def update_stock_after_checkout(cart_items):
    """อัพเดทจำนวนสต็อกสินค้าหลังจากการชำระเงิน"""
    conn, cursor = connect_db()  # เชื่อมต่อกับฐานข้อมูล
    try:
        for item in cart_items:
            product_name, price, quantity = item  # แยกข้อมูลของสินค้า
            available_stock = get_stock_quantity_from_db(product_name)  # ดึงจำนวนสต็อกจากฐานข้อมูล
            
            if available_stock >= quantity:
                new_quantity = available_stock - quantity  # คำนวณจำนวนสินค้าหลังจากการขาย
                update_stock_quantity_in_db(product_name, new_quantity)  # อัพเดทสต็อกในฐานข้อมูล
            else:
                print(f"Not enough stock for {product_name}. Available stock: {available_stock}, requested quantity: {quantity}")
                
    except sqlite3.Error as e:
        print(f"Error while updating stock: {e}")
    finally:
        cursor.close()  # ปิด cursor
        conn.close()  

import os

def connect_admin():
        conn, cursor = connect_db() 
        cursor = conn.cursor()
        return conn,cursor

def check_users():
    conn, cursor = connect_admin()
    if conn and cursor:
        cursor.execute("SELECT * FROM admin_users")
        users = cursor.fetchall()
        print("Users in the database:")
        for user in users:
            print(user)  
        conn.close()
    else:
        print("Failed to connect to the database.")

def check_login1(username, password):
    conn, cursor = connect_admin()
    if conn and cursor:
        cursor.execute("SELECT * FROM admin_users WHERE Username = ? AND Password = ?", (username, password))
        result = cursor.fetchone()
        conn.close()
        return result is not None
    else:
        return False

def register_user1(Name, Role, Username, Password):
    try:
        conn, cursor = connect_admin()
        if conn and cursor:
            # เพิ่มข้อมูลผู้ใช้ใหม่
            cursor.execute("INSERT INTO admin_users (Name, Role, Username, Password) VALUES (?, ?, ?, ?)", 
                           (Name, Role, Username, Password))
            conn.commit()
            print(f"User {Username} added successfully.")  
            messagebox.showinfo("Registration", "Registration Successful!")
        else:
            messagebox.showerror("Error", "Failed to connect to database.")
    except sqlite3.Error as e:
        messagebox.showerror("Error", f"An error occurred: {e}")
    finally:
        if conn:
            conn.close()


def login1():
    username = Entry_username3.get()
    password = Entry_password3.get()
    if username and password:
        if check_login1(username, password):
            messagebox.showinfo("Login", "Login Successful!")
            open_window5()  # เปิดหลังจากล็อกอินสำเร็จ
        else:
            messagebox.showerror("Login", "Invalid username or password.")
    else:
        messagebox.showerror("Login", "Please fill in both username and password.")

def submit_registration1():
    Name = Entry_Name4.get()
    Role = Entry_Role.get()
    Username = Entry_Username4.get()
    Password = Entry_Password4.get()

    print(f"Name: {Name}, Role: {Role}, Username: {Username}, Password: {Password}") 

    if Name and Role and Username and Password:
        register_user1(Name, Role, Username, Password)
        window4.withdraw()
        window3.deiconify()
    else:
        messagebox.showerror("Error", "Please fill in all fields.")

def toggle_password1():
    if Entry_password3.cget('show') == '*':
        Entry_password3.configure(show="") 
        img_eye3.config(image=photo_eye_open3)  
    else:
        Entry_password3.configure(show='*')
        img_eye3.config(image=photo_eye_closed3) 

def open_window4():
    window3.withdraw()
    window4.deiconify()

window3 = tk.Toplevel()
window3.title("admin")
window3.geometry("1500x750")
window3.configure(bg="#fbdae4")
window3.withdraw()

image_path3 = r"C:\Users\HP\Downloads\login.jpg"
image3= Image.open(image_path3)
image3 = image3.resize((1920,1080))
photo3 = ImageTk.PhotoImage(image3)

label_image3 = tk.Label(master=window3, image=photo3, bg="#fffff1")
label_image3.place(x=5, y=12)

Button13 = customtkinter.CTkButton(
    master=window3, text="Log in",
    font=("Georgia", 14),
    command=login1  # ใช้ฟังก์ชัน login1
)
Button13.place(x=235, y=600)

Button23 = customtkinter.CTkButton(
    master=window3, text="register",
    font=("Georgia", 14),
    command=open_window4
)
Button23.place(x=400, y=600)

Entry_username3 = customtkinter.CTkEntry(
    master=window3,
    placeholder_text="Username",
    font=("Georgia", 14),
    height=30,
    width=195
)
Entry_username3.place(x=300, y=450)

Entry_password3 = customtkinter.CTkEntry(
    master=window3,
    placeholder_text="Password",
    show="*",  
    font=("Georgia", 14),
    height=30,
    width=195
)
Entry_password3.place(x=300, y=500)

photo_eye_closed3 = ImageTk.PhotoImage(Image.open(r"eye_closed.jpg").resize((18, 18)))
photo_eye_open3 = ImageTk.PhotoImage(Image.open(r"eye_open.jpg").resize((18, 18)))
img_eye3 = tk.Button(master=window3, image=photo_eye_closed3,command=toggle_password1, borderwidth=0, bg="#fffff1")
img_eye3.place(x=470, y=505)

window4 = tk.Toplevel()
window4.title("My Perfume")
window4.geometry("1500x750")
window4.configure(bg="#fbdae4")
window4.withdraw()

image_path4 = r"C:\Users\HP\Downloads\singin.jpg"
image4 = Image.open(r"C:\Users\HP\Downloads\singin.jpg")
image4 = image4.resize((1920, 1080))  
photo4 = ImageTk.PhotoImage(image4)

label_image4 = tk.Label(master=window4, image=photo4, bg="#fbdae4")
label_image4.place(x=5, y=12)

Entry_Name4 = customtkinter.CTkEntry(master=window4, placeholder_text="Name", font=("Georgia", 14),width=300)
Entry_Name4.place(x=790, y=310)

Entry_Role = customtkinter.CTkEntry(master=window4, placeholder_text="Role", font=("Georgia", 14),width=300)
Entry_Role.place(x=1170, y=310)

Entry_Username4 = customtkinter.CTkEntry(master=window4, placeholder_text="Username", font=("Georgia", 14),width=300)
Entry_Username4.place(x=790, y=360)

Entry_Password4 = customtkinter.CTkEntry(master=window4, placeholder_text="Password", show="*", font=("Georgia", 14),width=300)
Entry_Password4.place(x=1170, y=360)

Button_sign_up4 = customtkinter.CTkButton(
    master=window4, text="Sign in", font=("Georgia", 14), command=submit_registration1
)
Button_sign_up4.place(x=1070, y=480)

Checkbox_id55 = customtkinter.CTkCheckBox(
    master=window4,
    text="Consent to Disclosure of Personal Information"
)
Checkbox_id55.place(x=1000, y=420)

import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import sqlite3

def create_table_ad():
    try:
        conn, cursor = connect_db()
        # สร้างตาราง products ถ้ายังไม่มี
        cursor.execute('''CREATE TABLE IF NOT EXISTS products (
                            product_id INTEGER PRIMARY KEY AUTOINCREMENT,
                            name TEXT,
                            price REAL,
                            quantity INTEGER,
                            image_path TEXT,
                            category TEXT)''') 
        conn.commit()
    except Exception as e:
        print(f"Error creating table: {e}")
    finally:
        if conn:
            conn.close()

from tkinter import filedialog
def upload_image():
    global image_entry  
    file_path = filedialog.askopenfilename(
        title="Select image file",
        filetypes=[("Image files", "*.png;*.jpg;*.jpeg")]
    )

    if file_path:
        file_name = os.path.basename(file_path)
        image_entry.delete(0, tk.END)
        image_entry.insert(0, file_name)  # ใส่ชื่อไฟล์เข้าไปในช่องกรอก
    else:
        messagebox.showwarning("No file selected", "Please select an image file.")  # แจ้งเตือนหากไม่มีการเลือกไฟล์

# ฟังก์ชันแสดงรายการสินค้าใน GUI
def open_window5():
    global window5, image_entry  # เพิ่ม global เพื่อให้ใช้ได้ในฟังก์ชันต่างๆ
    window5 = tk.Tk()
    window5.title("Product List")
    window5.geometry("1500x750")
    window5.configure(bg="#fe3ab8")
    window3.withdraw()

    # Treeview สำหรับแสดงสินค้าผลลัพธ์
    tree = ttk.Treeview(window5, columns=("Product Name", "Price", "Image_path", "Quantity", "Category"), show="headings")
    tree.heading("Product Name", text="Product Name")
    tree.heading("Price", text="Price")
    tree.heading("Image_path", text="Image_path")
    tree.heading("Quantity", text="Quantity")
    tree.heading("Category", text="Category")

    conn, cursor = connect_db()
    cursor.execute("SELECT product_id, name, price,image_path,quantity,category FROM products ")
    products = cursor.fetchall()
    conn.close()

    # เพิ่มข้อมูลสินค้าใน Treeview
    for product in products:
        product_id, name, price,image_path ,quantity,category = product 
        tree.insert("", tk.END, values=(name, price, image_path,quantity,category))

    # จัดเรียงและกำหนดขนาดของคอลัมน์
    tree.column("Product Name", width=250)
    tree.column("Price", width=100)
    tree.column("Image_path",width=100)
    tree.column("Quantity", width=100)
    
    # แสดงข้อมูลใน Treeview
    tree.pack(padx=20, pady=20)

    # ช่องกรอกข้อมูลสินค้า
    name_label1 = tk.Label(window5, text="Product Name", font=("Georgia", 14), bg="#fbdae4")
    name_label1.place(x=500, y=300)
    name_entry1 = customtkinter.CTkEntry(master=window5, placeholder_text="Product Name", font=("Georgia", 14), width=300)
    name_entry1.place(x=700, y=300)

    price_label = tk.Label(window5, text="Price (฿)", font=("Georgia", 14), bg="#fbdae4")
    price_label.place(x=500, y=350)
    price_entry = customtkinter.CTkEntry(master=window5, placeholder_text="Price", font=("Georgia", 14), width=300)
    price_entry.place(x=700, y=350)

    image_label = tk.Label(window5, text="Image_path", font=("Georgia", 14), bg="#fbdae4")
    image_label.place(x=500, y=400)
    image_entry = customtkinter.CTkEntry(master=window5, placeholder_text="Image_path", font=("Georgia", 14), width=300)
    image_entry.place(x=700, y=400)
    button_select_image = customtkinter.CTkButton(
        master=window5, text="Select Image", font=("Georgia", 14), command=upload_image
    )
    button_select_image.place(x=860, y=400)

    # ปรับตำแหน่งช่องกรอกจำนวนและหมวดหมู่ให้ไม่ทับกัน
    quantity_label = tk.Label(window5, text="Quantity", font=("Georgia", 14), bg="#fbdae4")
    quantity_label.place(x=500, y=450)
    quantity_entry = customtkinter.CTkEntry(master=window5, placeholder_text="Quantity", font=("Georgia", 14), width=300)
    quantity_entry.place(x=700, y=450)

    category_label = tk.Label(window5, text="Category", font=("Georgia", 14), bg="#fbdae4")
    category_label.place(x=500, y=500)
    category_entry = customtkinter.CTkEntry(master=window5, placeholder_text="Category", font=("Georgia", 14), width=300)
    category_entry.place(x=700, y=500)

    # ฟังก์ชันเพิ่มสินค้า
    def add_new_product():
        name = name_entry1.get()
        price = price_entry.get()
        quantity = quantity_entry.get()
        image = image_entry.get()
        category = category_entry.get()

        if not name or not price or not quantity or not category:
            messagebox.showerror("Input Error", "All fields are required.")
            return

        try:
            # ลบคอมมาออกจากราคาก่อนแปลงเป็น float
            price = price.replace(",", "")  # ลบคอมม่า
            price = float(price.replace('฿', '').strip())  # แปลงเป็น float
            quantity = int(quantity)
        except ValueError:
            messagebox.showerror("Input Error", "Invalid price or quantity.")
            return

        # เชื่อมต่อกับฐานข้อมูล และเพิ่มข้อมูลใหม่
        conn, cursor = connect_db()
        cursor.execute("SELECT * FROM products WHERE name = ?", (name,))
        existing_product = cursor.fetchone()

        if existing_product:
            messagebox.showerror("Product Exists", "This product already exists in the database.")
            conn.close()
            return
        formatted_price = f"฿{price:,.0f}"
        cursor.execute("INSERT INTO products (name, price, image_path, quantity, category) VALUES (?, ?, ?, ?, ?)",
                    (name, formatted_price, image, quantity, category))
        conn.commit()
        conn.close()

        # เพิ่มข้อมูลใน Treeview
        tree.insert("", tk.END, values=(name, f"฿{price:,.0f}", image, quantity, category))
        name_entry1.delete(0, tk.END)
        price_entry.delete(0, tk.END)
        image_entry.delete(0, tk.END)
        quantity_entry.delete(0, tk.END)
        category_entry.delete(0, tk.END)

    # ฟังก์ชันลบสินค้า
    def delete_selected_product():
        selected_item = tree.selection()
        if not selected_item:
            messagebox.showerror("Selection Error", "Please select a product to delete.")
            return

        item_values = tree.item(selected_item)["values"]
        product_name = item_values[0]

        conn, cursor = connect_db()
        cursor.execute("DELETE FROM products WHERE name = ?", (product_name,))
        conn.commit()
        conn.close()

        # ลบรายการจาก Treeview
        tree.delete(selected_item)

    # ฟังก์ชันออก
    def close_window():
        window5.quit()

    # เพิ่มปุ่ม
    button_Add_Product = customtkinter.CTkButton(
        master=window5, text="Add Product", font=("Georgia", 14), command=add_new_product
    )
    button_Add_Product.place(x=470, y=600)

    button_Delete_Selected = customtkinter.CTkButton(
        master=window5, text="Delete Selected Product", font=("Georgia", 14), command=delete_selected_product
    )
    button_Delete_Selected.place(x=670, y=600)

    button_exit = customtkinter.CTkButton(
        master=window5, text="Exit", font=("Georgia", 14), command=close_window
    )
    button_exit.place(x=900, y=600)

    button_order_history = customtkinter.CTkButton(
    master=window5, text="order history", font=("Georgia", 14), command=open_window6
    )
    button_order_history.place(x=40, y=10)

    window5.mainloop()
    
def open_window6():
    global window6
    window6 = tk.Tk()  # สร้างหน้าต่าง Tk
    window6.title("order history")
    window6.geometry("1500x750")
    window6.configure(bg="#fe3ab8")
    window5.withdraw()

    columns = ("id", "name", "phone", "address", "total_price", "items")
    
    # สร้าง Treeview สำหรับแสดงรายการคำสั่งซื้อ
    orders = ttk.Treeview(window6, columns=columns, show="headings", height=12)
    for col in columns:
        orders.heading(col, text=col)  # กำหนดหัวข้อคอลัมน์
        orders.column(col, width=150)  # กำหนดความกว้างของคอลัมน์

    # วาง Treeview ในตำแหน่งที่ต้องการ
    orders.place(x=270, y=90, width=900, height=400)

    # เชื่อมต่อฐานข้อมูลและดึงข้อมูลคำสั่งซื้อ
    conn, cursor = connect_db()
    cursor.execute("SELECT id, name, phone, address, total_price, items FROM orders")
    rows = cursor.fetchall()

    # เพิ่มข้อมูลจากฐานข้อมูลลงใน Treeview
    for row in rows:
        orders.insert("", "end", values=row)
    
    conn.close()  
    
    # ปรับขนาดของแต่ละเซลล์ให้สามารถแสดงข้อความที่ยาวเกินหนึ่งบรรทัดได้
    for child in orders.get_children():
        for col in columns:
            text = orders.item(child, 'values')[columns.index(col)]
            orders.set(child, col, text)

    # เพิ่มการแสดงผลแบบ multiline สำหรับแต่ละเซลล์
    for child in orders.get_children():
        for col in columns:
            text = orders.item(child, 'values')[columns.index(col)]
            orders.set(child, col, text.replace('\n', ' '))  # แทนที่ newline ด้วย space

    button_back_produce = customtkinter.CTkButton(
    master=window6, text="back to produce list", font=("Georgia", 14), command=close_window6
    )
    button_back_produce.place(x=40, y=10)

    detailed_report = customtkinter.CTkButton(
    master=window6, text="detailed report page", font=("Georgia", 14), command=open_window7
    )
    detailed_report.place(x=1250, y=10)

def close_window6():
    window6.withdraw()
    window5.deiconify()

def open_window7():
    global window7
    window7 = tk.Tk()  # สร้างหน้าต่าง Tk
    window7.title("Detailed Report Page")
    window7.geometry("1500x750")  # ตั้งขนาดของหน้าต่างให้เหมือนกับ window6
    window7.configure(bg="#fe3ab8")
    window6.withdraw()  # ซ่อนหน้าต่างเดิม

    # สร้างกรอบการกรองข้อมูล
    filter_frame = tk.Frame(window7, bg="#fe3ab8")
    filter_frame.pack(pady=20)

    # วันที่ (วัน/เดือน/ปี)
    tk.Label(filter_frame, text="วัน:", font=("Georgia", 14), bg="#fe3ab8").grid(row=0, column=0, padx=10)
    day_combo = ttk.Combobox(filter_frame, values=[str(i) for i in range(1, 32)] + ["ทุกวัน"], state="readonly", font=("Georgia", 14))
    day_combo.grid(row=0, column=1, padx=10)

    tk.Label(filter_frame, text="เดือน:", font=("Georgia", 14), bg="#fe3ab8").grid(row=0, column=2, padx=10)
    month_combo = ttk.Combobox(filter_frame, values=[str(i) for i in range(1, 13)] + ["ทุกเดือน"], state="readonly", font=("Georgia", 14))
    month_combo.current(datetime.now().month - 1)
    month_combo.grid(row=0, column=3, padx=10)

    tk.Label(filter_frame, text="ปี:", font=("Georgia", 14), bg="#fe3ab8").grid(row=0, column=4, padx=10)
    current_year = datetime.now().year
    year_combo = ttk.Combobox(filter_frame, values=[str(year) for year in range(current_year - 10, current_year + 1)] + ["ทุกปี"], state="readonly", font=("Georgia", 14))
    year_combo.current(10)
    year_combo.grid(row=0, column=5, padx=10)

    # ฟังก์ชันกรองข้อมูล
    def apply_filter():
        conn, cursor = connect_db()  # เปิดการเชื่อมต่อฐานข้อมูลใหม่
        selected_day = day_combo.get()
        selected_month = month_combo.get()
        selected_year = year_combo.get()

        # เช็คการเลือกค่ากรอง
        if selected_day == "ทุกวัน" and selected_month == "ทุกเดือน" and selected_year == "ทุกปี":
            messagebox.showwarning("กรองข้อมูล", "กรุณาเลือกอย่างน้อยหนึ่งตัวกรอง")
            return

        query = "SELECT order_date, name, items, total_price FROM orders WHERE 1=1"

        # กรองตามวัน
        if selected_day != "ทุกวัน":
            selected_day = selected_day.zfill(2)
            query += f" AND strftime('%d', order_date) = '{selected_day}'"
        
        # กรองตามเดือน
        if selected_month != "ทุกเดือน":
            selected_month = selected_month.zfill(2)
            query += f" AND strftime('%m', order_date) = '{selected_month}'"
        
        # กรองตามปี
        if selected_year != "ทุกปี":
            query += f" AND strftime('%Y', order_date) = '{selected_year}'"

        cursor.execute(query)
        orders = cursor.fetchall()

        # ลบข้อมูลเก่าใน treeview
        for row in treeview.get_children():
            treeview.delete(row)

        total_revenue = 0
        for order in orders:
            # แทนที่ \n ด้วย space สำหรับข้อมูลที่มีหลายบรรทัด
            order_data = [
                str(order[0]),  
                order[1].replace('\n', ' '),  # แทนที่ \n ในชื่อ
                order[2].replace('\n', ' '),  # แทนที่ \n ในรายการ
                str(order[3])  # ราคา
            ]

            # แปลงราคาจาก string เป็น float หากมีสัญลักษณ์ ฿ หรือคอมมา
            try:
                numeric_price = float(str(order[3]).replace(",", "").replace("฿", "").strip())
            except ValueError:
                numeric_price = 0  # ตั้งค่าเริ่มต้นหากแปลงไม่ได้

            treeview.insert('', 'end', values=order_data)  # เพิ่มข้อมูลใน Treeview
            total_revenue += numeric_price  # คำนวณรายได้รวม

        # อัปเดตข้อความรายได้รวม
        total_label.config(text=f"รายได้รวม: ฿{total_revenue:,.0f}")

        conn.close()  

 
    filter_button = tk.Button(filter_frame, text="ยืนยัน", command=apply_filter, font=("Georgia", 16), bg="#f0b7c5")
    filter_button.grid(row=0, column=6, padx=20)


    scrollbar = tk.Scrollbar(window7, orient="horizontal")
    scrollbar.pack(side="bottom", fill="x")

    columns = ["order date", "name", "items", "total_price"]
    
    treeview = ttk.Treeview(window7, columns=columns, show="headings", height=12, xscrollcommand=scrollbar.set)
    
    # ตั้งชื่อหัวข้อคอลัมน์
    for col in columns:
        treeview.heading(col, text=col)
        treeview.column(col, width=200)
    
    # วาง Treeview ในตำแหน่งที่ต้องการ
    treeview.place(x=270, y=90, width=900, height=400)
    
    # เชื่อมต่อฐานข้อมูลและดึงข้อมูล
    conn, cursor = connect_db()
    cursor.execute("SELECT order_date, name, items, total_price FROM orders")  # ดึงข้อมูลจากตาราง orders
    orders_data = cursor.fetchall()

    # เพิ่มข้อมูลลงใน Treeview
    for order in orders_data:
        order_data = [str(order[0]),  
                      order[1].replace('\n', ' '),  # แทนที่ \n ในชื่อ
                      order[2].replace('\n', ' '),  # แทนที่ \n ในรายการ
                      str(order[3])]  # ราคา
        
        treeview.insert('', 'end', values=order_data)

    # ปิดการเชื่อมต่อฐานข้อมูล
    conn.close()
    
    # ป้ายแสดงรายได้รวม
    total_label = tk.Label(window7, text="รายได้รวม: 0 บาท", font=("Georgia", 16), bg="#fe3ab8")
    total_label.place(x=400, y=530)

    # ปุ่มย้อนกลับ
    Back_order_history = customtkinter.CTkButton(
        master=window7, text="Back to Order History", font=("Georgia", 14), command=close_window7
    )
    Back_order_history.place(x=40, y=10)
    
def close_window7():
    window7.withdraw()
    window6.deiconify() 

create_table_ad()  
window.mainloop()