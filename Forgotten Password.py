# The program that checks if the password is different from the old one

old_password = "hello123"
new_password = "goodbye321"
compare_old_new = old_password != new_password
repeat_new_password = "goodbye321"
compare_new = new_password == repeat_new_password

print(f"Is new password different from old password? {compare_old_new}")
print(f"Has new password been introduced correctly? {compare_new}")