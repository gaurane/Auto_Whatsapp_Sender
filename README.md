
# WhatsApp Invitation Sender

### Project Description

This is a simple yet powerful automation script designed to streamline the process of sending personalized invitations via WhatsApp. Instead of manually typing each message, this tool automates the entire workflow from data entry to message delivery, using your laptop's default web browser.

It's the perfect solution for sending event invites, promotional messages, or personalized notifications to a small list of contacts efficiently.

-----

## Getting Started

### Prerequisites

Before you run the script, make sure you have the following installed:

  * **Python:** Version 3.6 or higher. You can download it from [python.org](https://www.python.org/downloads/).
  * **Web Browser:** Chrome, Firefox, or Edge. You'll also need the corresponding `webdriver` for your browser. The script will automatically try to find and manage it, but manual installation may be necessary.

### Installation

1.  **Clone the repository** (if you're using Git) or download the script files directly.
2.  **Install the required Python libraries** by running this command in your terminal:
    ```bash
    pip install pandas selenium
    ```
3.  **Ensure a `webdriver` is installed.** The `selenium` library can often handle this automatically. However, if you run into errors, you may need to manually download the driver for your browser and place it in your system's PATH.

-----

## How to Use

Follow these simple steps to send your invitations:

1.  **Run the script:** Open your terminal or command prompt, navigate to the project directory, and run the script:

    ```bash
    python your_script_name.py
    ```

2.  **Enter Contact Details:** The script will prompt you to enter the `Name`, `Phone Number`, and any `Details` for each contact. When you are finished adding contacts, simply type `done` and press Enter.

3.  **Provide the Invite Link:** Next, the script will ask you to paste the **invitation link** you want to send.

4.  **Log in to WhatsApp Web:** A new browser window will open. You must **manually scan the QR code** to log in to WhatsApp Web. The script will wait until you are logged in.

5.  **Send Invitations:** Once you are logged in, the script will automatically begin the process. It will open a new chat for each contact from your list, type the personalized message, and send it. **Do not close the browser window or interact with the keyboard/mouse** while the script is running to avoid any errors.

-----

## Features

  * **Automated Data Capture:** Easily enter contact information directly into the command line.
  * **CSV File Generation:** Automatically saves all entered data to a `contacts.csv` file for future use.
  * **Personalized Messages:** Uses a customizable template to include each contact's name and specific details.
  * **Browser-Based Sending:** Leverages WhatsApp Web to send messages directly from your personal account.
  * **Built-in Delays:** Includes programmed delays to mimic human behavior and reduce the risk of account flagging.

-----

## Customization

You can easily modify the message template within the script to change the wording of your invitations. Look for the message string in the code and adjust it as needed.

*Example template:*
`Hello {{Name}}! You are cordially invited to our event. Here is the link: {{InviteLink}}. {{Details}}`

-----
