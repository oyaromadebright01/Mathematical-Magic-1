# import tkinter as tk
# from tkinter import messagebox

# def is_armstrong_number(num):
#     num_str = str(num)
#     num_len = len(num_str)
#     sum_of_powers = sum(int(digit) ** num_len for digit in num_str)
#     return sum_of_powers == num

# def check_number():
    
#     try:
#         num = int(entry.get())
#         if is_armstrong_number(num):
#             messagebox.showinfo("Result", f"{num} is an Armstrong number.")
#         else:
#             messagebox.showinfo("Result", f"{num} is not an Armstrong number.")
#     except ValueError:
#         messagebox.showerror("Error", "Please enter a valid integer.")

# def show_examples():
#     examples = [0, 1, 153, 370, 371, 407]
#     messagebox.showinfo("Examples", f"Examples of Armstrong numbers: {examples}")

# def check_range():
#     try:
#         start = int(start_entry.get())
#         end = int(end_entry.get())
#         armstrong_numbers = [num for num in range(start, end + 1) if is_armstrong_number(num)]
#         messagebox.showinfo("Result", f"Armstrong numbers in range {start} to {end}: {armstrong_numbers}")
#     except ValueError:
#         messagebox.showerror("Error", "Please enter valid integers for the range.")

# def calculate_factors():
#     try:
#         num = int(factor_entry.get())
#         factors = [i for i in range(1, num + 1) if num % i == 0]
#         messagebox.showinfo("Factors", f"Factors of {num}: {factors}")
#     except ValueError:
#         messagebox.showerror("Error", "Please enter a valid integer.")

# def roman_to_integer():
#     roman_numeral = roman_entry.get().upper()
#     roman_dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
#     integer_value = 0
#     prev_value = 0
#     for char in reversed(roman_numeral):
#         value = roman_dict.get(char, 0)
#         if value < prev_value:
#             integer_value -= value
#         else:
#             integer_value += value
#         prev_value = value
#     messagebox.showinfo("Result", f"The integer value of {roman_numeral} is {integer_value}")

# root = tk.Tk()
# root.title("Number Checker")
# root.geometry("400x500")
# root.configure(bg="#f0f0f0")

# # Create and place the widgets
# label = tk.Label(root, text="Enter a number:", font=("Helvetica", 14), bg="#f0f0f0")
# label.pack(pady=10)

# entry = tk.Entry(root, font=("Helvetica", 12))
# entry.pack(pady=5)

# check_button = tk.Button(root, text="Check Armstrong", command=check_number, font=("Helvetica", 12), bg="#4CAF50", fg="white")
# check_button.pack(pady=10)

# examples_button = tk.Button(root, text="Show Examples", command=show_examples, font=("Helvetica", 12), bg="#2196F3", fg="white")
# examples_button.pack(pady=10)

# range_label = tk.Label(root, text="Check range of numbers:", font=("Helvetica", 14), bg="#f0f0f0")
# range_label.pack(pady=10)

# start_label = tk.Label(root, text="Start:", font=("Helvetica", 12), bg="#f0f0f0")
# start_label.pack(pady=5)
# start_entry = tk.Entry(root, font=("Helvetica", 12))
# start_entry.pack(pady=5)

# end_label = tk.Label(root, text="End:", font=("Helvetica", 12), bg="#f0f0f0")
# end_label.pack(pady=5)
# end_entry = tk.Entry(root, font=("Helvetica", 12))
# end_entry.pack(pady=5)

# range_button = tk.Button(root, text="Check Range", command=check_range, font=("Helvetica", 12), bg="#FF5722", fg="white")
# range_button.pack(pady=10)

# factor_label = tk.Label(root, text="Calculate factors of a number:", font=("Helvetica", 14), bg="#f0f0f0")
# factor_label.pack(pady=10)

# factor_entry = tk.Entry(root, font=("Helvetica", 12))
# factor_entry.pack(pady=5)

# factor_button = tk.Button(root, text="Calculate Factors", command=calculate_factors, font=("Helvetica", 12), bg="#9C27B0", fg="white")
# factor_button.pack(pady=10)

# roman_label = tk.Label(root, text="Convert Roman numeral to integer:", font=("Helvetica", 14), bg="#f0f0f0")
# roman_label.pack(pady=10)

# roman_entry = tk.Entry(root, font=("Helvetica", 12))
# roman_entry.pack(pady=5)

# roman_button = tk.Button(root, text="Convert", command=roman_to_integer, font=("Helvetica", 12), bg="#FF9800", fg="white")
# roman_button.pack(pady=10)

# root.mainloop()


number = int(input("Enter the Number to check: "))
length = len(str(number))

result = 0
temp = number


while temp != 0:
    digit = temp % 10
    result += digit ** length
    temp = temp // 10 

if number == result:
    print("This is an Armstrong number.")
else:
    print("This is not an Armstrong number.")  
