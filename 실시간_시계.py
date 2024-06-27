import tkinter as tk
import time

def update_time():
    current_time = time.strftime('%Y-%m-%d\n%H:%M:%S') # 연-월-일 시-분-초 순으로 출력
    clock_label.config(text=current_time)
    clock_label.after(1000, update_time)  # 1초마다 업데이트

root = tk.Tk()
root.title("실시간 시계")

clock_label = tk.Label(root, font=('Arial', 48), bg='black', fg='white')
clock_label.pack(anchor='center')

update_time()  # 시간 업데이트 함수 호출

root.mainloop()
