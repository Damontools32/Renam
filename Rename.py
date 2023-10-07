import os

# مسیر فولدر اصلی
base_dir = '/content/downloads'

# تابع برای تغییر نام فایل‌ها و فولدرها و اضافه کردن نام مورد نظر به ابتدا و محدودیت تعداد کاراکتر به ۳۰
def rename_files_and_folders(folder_path):
    items = os.listdir(folder_path)
    for item in items:
        item_path = os.path.join(folder_path, item)
        current_name, ext = os.path.splitext(item)
        new_name = '@vstpluginsample_' + current_name[:30]  # اضافه کردن @vstpluginsample به ابتدا و محدودیت تعداد کاراکتر
        new_name_with_ext = new_name + ext  # اضافه کردن پسوند به نام جدید
        os.rename(item_path, os.path.join(folder_path, new_name_with_ext))

# تغییر نام فایل‌ها و فولدرها و اضافه کردن نام مورد نظر به ابتدا و محدودیت تعداد کاراکتر برای همه فولدرها و زیرفولدرها
for root, dirs, files in os.walk(base_dir):
    for dir in dirs:
        folder_path = os.path.join(root, dir)
        rename_files_and_folders(folder_path)
    rename_files_and_folders(root)
