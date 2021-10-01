import paho.mqtt.client as mqtt
import json
import time
import tkinter as tk

def send_new_data(client_id, token, secret, data, topic):
    client = mqtt.Client(client_id=client_id)
    client.username_pw_set(username=token, password=secret)
    client.connect(host="52.221.186.18", port=1883, keepalive=60)
    time.sleep(0.5)
    new_dict = dict()
    new_dict["data"] = data
    payload = json.dumps(new_dict)
    client.publish(topic, payload=payload)
    client.disconnect()

def set_error_log(msg):
    global app, error_log, reset_times
    error_log["text"] = msg
    reset_times += 1
    app.after(2000, reset_error_log)

def reset_error_log():
    global error_log, reset_times
    if reset_times > 0:
        reset_times -= 1
    if reset_times == 0:
        error_log["text"] = ""

def pack_and_send(user_id, temp, oxy, hr, ts):
    global DEFAULT_TIMESTAMP
    if ts.get() == "":
        ts.set(DEFAULT_TIMESTAMP)
    try:
        #print(user_id.get(), temp.get(), oxy.get(), hr.get())
        data = {
            "temperature": temp.get(),
            'o2': oxy.get(),
            "heartrate": hr.get(),
            "timestamp": ts.get(),
        }
        send_new_data(str(user_id.get()), "mqtt", "password", data, "homeIsolation")
        set_error_log("Success")
    except tk.TclError:
        set_error_log("Error")

PADDING_SIZE = 5
reset_times = 0
DEFAULT_TIMESTAMP = "CURRENT_TIME"

if __name__ == "__main__":
    app = tk.Tk()
    app.title("Housepital client (Mocked-up)")

    leftmaster = tk.Frame(app)
    leftmaster.pack(side=tk.LEFT, expand=True, padx=(PADDING_SIZE, PADDING_SIZE))

    tk.Label(leftmaster, text="User Id:").grid(row=0, column=0, sticky=tk.W)
    user_id_val = tk.IntVar(app, 1)
    tk.Entry(leftmaster, textvariable=user_id_val).grid(row=0, column=1)
    
    tk.Label(leftmaster, text="Temperature:").grid(row=1, column=0, sticky=tk.W)
    temp_val = tk.DoubleVar(app, 25)
    tk.Entry(leftmaster, textvariable=temp_val).grid(row=1, column=1)

    tk.Label(leftmaster, text="O2:", justify=tk.LEFT).grid(row=2, column=0, sticky=tk.W)
    oxy_val = tk.DoubleVar(app, 98)
    tk.Entry(leftmaster, textvariable=oxy_val).grid(row=2, column=1)

    tk.Label(leftmaster, text="Heart rate:").grid(row=3, column=0, sticky=tk.W)
    hr_val = tk.DoubleVar(app, 89)
    tk.Entry(leftmaster, textvariable=hr_val).grid(row=3, column=1)

    tk.Label(leftmaster, text="Timestamp:").grid(row=4, column=0, sticky=tk.W)
    ts_val = tk.StringVar(app, DEFAULT_TIMESTAMP)
    tk.Entry(leftmaster, textvariable=ts_val).grid(row=4, column=1)

    rightmaster = tk.Frame(app)
    rightmaster.pack(side=tk.RIGHT, expand=True, padx=(0, PADDING_SIZE))
    error_log = tk.Label(rightmaster)
    tk.Button(rightmaster, text='Send data', command=lambda: pack_and_send(user_id_val, temp_val, oxy_val, hr_val, ts_val)).pack(fill=tk.BOTH, expand=True)
    error_log.pack()
    
    app.resizable(width=False, height=False)
    app.mainloop()
