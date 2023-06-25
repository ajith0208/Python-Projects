import socket
from tkinter import *


# Functions
def send(msg_box, entry):
    msg = entry.get()
    msg_box.insert('end', f'Client : {msg}')
    entry.delete(0, END)
    s.send(bytes(msg, "utf-8"))


def receive(msg_box):
    msg = s.recv(100)
    msg_box.insert('end', f"Server : {msg.decode('utf-8')}")


# Main Content
root = Tk()
root.config(padx=10, pady=10)
root.title('Client')
# root.geometry('400x400')

entry = Entry(width=50)
entry.grid(row=2, columnspan=2)

msg_box = Listbox(root, width=50)
msg_box.grid(row=0, column=0, columnspan=2)

send_btn = Button(root, text='Send', command=lambda: send(msg_box, entry))
send_btn.grid(row=1, column=1)

rcv_btn = Button(root, text='Receive', command=lambda: receive(msg_box))
rcv_btn.grid(row=1, column=0)

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
HOST_NAME = socket.gethostname()
PORT = 12345
s.connect((HOST_NAME, PORT))

root.mainloop()

# while True:
#     msg = s.recv(100)
#     print('Server : '+msg.decode('utf-8'))
#     msg_to_server = input('Client : ')
#     s.send(bytes(msg_to_server, 'utf-8'))
