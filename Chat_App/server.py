import socket
from tkinter import *


# Functions
def send(msg_box, entry):
    msg = entry.get()
    msg_box.insert('end', f'Server : {msg}')
    entry.delete(0, END)
    client.send(bytes(msg, "utf-8"))


def receive(msg_box):
    msg_from_client = client.recv(100)
    msg_box.insert('end', f"Client : {msg_from_client.decode('utf-8')}")


# Main Content
root = Tk()
root.config(padx=10, pady=10)
root.title('Server')
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
s.bind((HOST_NAME, PORT))
s.listen(4)

client, address = s.accept()

root.mainloop()