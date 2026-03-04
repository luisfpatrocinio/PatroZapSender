# PatroZapSender

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
   ```bash
   pip install -r requirements.txt
   ```
