import tkinter as tk
window = tk.Tk()
window.geometry('800x600')
var1=[]
var2=[]
var3=[]
var4=[]
def next_to():
    global var1
    global var2
    global var3
    global var4
    var1.append(t1.get())
    var2.append(t2.get())
    var3.append(t3.get())
    var4.append(t4.get())
    tx.insert('end',r"订单{0}：数量为：{1}   起条码为：{2}   终条码为：{3}\n".format(var1[-1],var4[-1],var2[-1],var3[-1]))
    t1.delete(0,50)
    t2.delete(0,50)
    t3.delete(0,50)
    t4.delete(0,50)
    
def start_calc():
    tx.insert('insert',r'有  ')
    
tk.Label(window, text=r"订单号：").place(x=20, y=10)
t1=tk.Entry(window,show=None,width=23)
t1.place(x=80,y=10)
tk.Label(window, text=r"起条码：").place(x=20, y=40)
t2=tk.Entry(window,show=None,width=23)
t2.place(x=80,y=40)
tk.Label(window, text=r"终条码：").place(x=20, y=70)
t3=tk.Entry(window,show=None,width=23)
t3.place(x=80,y=70)
tk.Label(window, text=r"订单数量：").place(x=20, y=100)
t4=tk.Entry(window,show=None,width=23)
t4.place(x=80,y=100)
tk.Button(window,text=r"下一个订单信息",command=next_to).place(x=20,y=130)
tk.Button(window,text=r"结束输入",command=start_calc).place(x=200,y=130)
tx=tk.Text(window,width=500)
tx.place(x=20,y=200)

