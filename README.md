html

<div align="center">
  <img src="assets/icon.png" alt="PatroZapSender Icon" width="200" style="border-radius: 20px;"/>
  <h1>PatroZapSender</h1>
  <p><em>A lightweight Python automation tool to send bulk personalized WhatsApp messages from CSV data.</em></p>
</div>

<br>

A modular, user-friendly Python automation tool designed to send bulk personalized WhatsApp Web messages using customer data parsed from a CSV file.

This tool is designed so that end-users do not need to modify any Python code. All messages and contacts are managed through simple external files.

## Features

- Parses detailed address and customer data from CSV files using `pandas`.
- Uses dynamic `.txt` templates for personalized messages (supports `{Nome}` and `{Endereco}` tags).
- Automates browser interaction with WhatsApp Web using `pyautogui`.
- Safe for version control: ignores real data files by default to protect user privacy.

## Prerequisites

- Python 3.x
- A default web browser logged into WhatsApp Web.

## Installation

1. Clone this repository.
2. Install the required dependencies:
   ````bash
   pip install -r requirements.txt```
   ````

## Configuration

Before running the script, you need to set up your data files:

1. Navigate to the `data/` folder.
2. Duplicate `contacts_sample.csv` and rename the copy to `contacts.csv`. Fill it with your actual customer data.
3. Duplicate `message_template_sample.txt` and rename the copy to `message_template.txt`.
4. Edit `message_template.txt` with your custom message. You can use the following dynamic tags that will be automatically replaced by the script:

- `{Nome}`: Replaced by the first name of the customer.
- `{Endereco}`: Replaced by the formatted full address of the customer.

## Usage

1. Open WhatsApp Web in your default browser and verify your session is active.
2. Run the main script from the root directory:

```bash
python src/Main.py
```

_Note: Do not use your mouse or keyboard while the automation is running to prevent interrupting the script._
