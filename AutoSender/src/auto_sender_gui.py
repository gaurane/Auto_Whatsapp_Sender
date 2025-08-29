import csv
import time
import tkinter as tk
from tkinter import filedialog, messagebox
import importlib.util
import subprocess
import sys

# --------------------
# Auto-install pywhatkit if missing
# --------------------
def install_and_import(package):
    if importlib.util.find_spec(package) is None:
        subprocess.check_call([sys.executable, "-m", "pip", "install", package])
    globals()[package] = __import__(package)

install_and_import("pywhatkit")
import pywhatkit as kit


# --------------------
# Log helper for GUI
# --------------------
def log_message(msg):
    log_text.insert(tk.END, msg + "\n")
    log_text.see(tk.END)
    root.update_idletasks()


# --------------------
# Save Numbers (with names) to CSV
# --------------------
def save_numbers():
    raw_text = numbers_text.get("1.0", tk.END).strip()
    if not raw_text:
        messagebox.showerror("Error", "Please paste names and numbers first!")
        return

    lines = raw_text.splitlines()
    records = []
    serial_no = 1

    for line in lines:
        parts = line.strip().split()
        if len(parts) >= 3:  # First Last Phone
            first_name = parts[0]
            last_name = parts[1]
            phone = parts[-1]  # keep original (no +91 formatting)

            records.append((serial_no, first_name, last_name, phone))
            serial_no += 1

    if not records:
        messagebox.showerror("Error", "No valid entries found! (Format: First Last Phone)")
        return

    filename = filedialog.asksaveasfilename(
        title="Save CSV File",
        defaultextension=".csv",
        filetypes=[("CSV Files", "*.csv")]
    )

    if filename:
        with open(filename, "w", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(["S.No.", "First Name", "Last Name", "Phone"])
            for rec in records:
                writer.writerow(rec)

        messagebox.showinfo("Saved", f"Names & Numbers saved to {filename}")
        file_entry.delete(0, tk.END)
        file_entry.insert(0, filename)


# --------------------
# WhatsApp Invite Sender (pywhatkit version)
# --------------------
def send_invites(csv_file, invite_link):
    with open(csv_file, "r") as f:
        reader = csv.reader(f)
        next(reader)  # skip header
        records = [row for row in reader]

    for sno, first, last, number in records:
        log_message(f"➡️ Sending invite to {first} {last} ({number})...")

        number = number.strip()
        if not number.startswith("+"):  # ensure country code exists
            number = "+91" + number  # change this default country code if needed

        try:
            # instantly send (wait_time=15 sec for WhatsApp to load)
            kit.sendwhatmsg_instantly(
                phone_no=number,
                message=invite_link,
                wait_time=15,
                tab_close=True
            )
            log_message(f"✅ Sent to {first} {last} ({number})")
        except Exception as e:
            log_message(f"❌ Failed for {number}: {e}")

        time.sleep(5)  # small delay before next message

    messagebox.showinfo("Done", "All invites sent!")


# --------------------
# UI Functions
# --------------------
def browse_file():
    filename = filedialog.askopenfilename(
        title="Select CSV File",
        filetypes=(("CSV Files", "*.csv"), ("All Files", "*.*"))
    )
    file_entry.delete(0, tk.END)
    file_entry.insert(0, filename)


def start_sending():
    csv_file = file_entry.get()
    invite_link = invite_entry.get()
    if not csv_file or not invite_link:
        messagebox.showerror("Error", "Please select CSV file and enter invite link.")
        return
    send_invites(csv_file, invite_link)


# --------------------
# Tkinter GUI
# --------------------
root = tk.Tk()
root.title("WhatsApp AutoSender")
root.geometry("650x650")

tk.Label(root, text="Paste First Last Phone (one per line):").pack(pady=5)
numbers_text = tk.Text(root, height=10, width=70)
numbers_text.pack(pady=5)

save_btn = tk.Button(root, text="Save as CSV", command=save_numbers, bg="blue", fg="white")
save_btn.pack(pady=5)

tk.Label(root, text="CSV File with Names & Numbers:").pack(pady=5)
file_frame = tk.Frame(root)
file_frame.pack()
file_entry = tk.Entry(file_frame, width=50)
file_entry.pack(side=tk.LEFT, padx=5)
browse_btn = tk.Button(file_frame, text="Browse", command=browse_file)
browse_btn.pack(side=tk.LEFT)

tk.Label(root, text="WhatsApp Invite Link:").pack(pady=5)
invite_entry = tk.Entry(root, width=60)
invite_entry.pack(pady=5)

send_btn = tk.Button(root, text="Send Invites", command=start_sending,
                     bg="green", fg="white", height=2, width=25)
send_btn.pack(pady=20)

# Log window
tk.Label(root, text="Status Log:").pack(pady=5)
log_text = tk.Text(root, height=12, width=80, bg="black", fg="lime")
log_text.pack(pady=5)

root.mainloop()
