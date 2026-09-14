# 🏦 CLI Bank Management System (Pure Python)

[![Python Version](https://img.shields.io/badge/python-3.8%2B-blue.svg)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](http://makeapullrequest.com)

A feature-packed, lightweight **Command Line Interface (CLI) Banking System** built entirely with pure Python. This application demonstrates core **Object-Oriented Programming (OOP)** principles, data persistence using JSON file handling, dynamic account number generation, and input validation.

---

## ✨ Features

- 🆕 **Account Creation**:
  - Automatically generates unique 7-character alphanumeric Account Numbers (e.g., `ABC1234`).
  - Age validation (Strictly 18+ requirement).
  - 4-digit numeric PIN verification.
- 🔐 **Secure Authentication**:
  - Requires Account Number and PIN validation before granting access to operations.
- 💰 **Financial Transactions**:
  - **Deposit Money**: Add funds with validation against negative values.
  - **Withdraw Money**: Withdraw funds with real-time balance validation (prevents overdraft).
- 📊 **Account Inquiries**:
  - **Check Balance**: Instant real-time balance lookup.
  - **Account Details**: View complete profile information securely.
- ⚙️ **Account Management**:
  - **Update Profile**: Modify registered details like Name, Age, Email, Phone Number, or PIN.
  - **Delete Account**: Permanent account deletion with user confirmation prompt.
- 💾 **Data Persistence**:
  - Uses `json` for auto-saving and loading account records (`data.json`).

---

## 🛠️ Concepts & Technologies Used

- **Language**: Python 3
- **Core Concepts**:
  - **Object-Oriented Programming (OOP)**: Class abstraction, encapsulation, static methods (`@staticmethod`).
  - **Data Handling**: JSON serialization and deserialization for data persistence.
  - **Module Integration**: `json`, `random`, `string`, `pathlib`.
  - **Input Validation**: Handling edge cases (minor age restrictions, PIN length/type constraints, balance limits).

---

## 📂 Project Structure

```text
banksystem-pure-python/
│
├── main.py          # Primary entry point containing Bank class and CLI interface
├── data.json        # Local database storing active account records
└── README.md        # Project documentation & setup instructions
```

---

## 🚀 Getting Started

### Prerequisites
Make sure you have **Python 3.8+** installed on your system. You can verify your installation by running:
```bash
python --version
```

### Installation & Execution

1. **Clone the Repository**
   ```bash
   git clone https://github.com/heerp5/banksystem-pure-python.git
   cd banksystem-pure-python
   ```

2. **Run the Application**
   ```bash
   python main.py
   ```

---

## 💡 Usage Example

When you run `main.py`, you will be greeted with an interactive numeric menu:

```text
Press 1 for Creating your account
Press 2 to withdraw money from your account
Press 3 check balance of your account
Press 4 for Updating details of your account
Press 5 for Delete your account
Press 6 to Deposit money 
Press 7 for details of your account
Your response: 
```

### Sample Workflow
1. Select `1` to create a new account, enter your personal details, and set a 4-digit PIN.
2. Note down your auto-generated **Account Number** (e.g., `XYZ9876`).
3. Select `6` to deposit initial funds into your newly created account.
4. Select `3` to verify your updated balance or `7` for complete account details.

---

## 🛣️ Future Roadmap

- [ ] Add a continuous execution loop with an **Exit** option.
- [ ] Implement inter-account funds transfer.
- [ ] Password/PIN hashing using `hashlib` for enhanced security.
- [ ] Mini-statement / Transaction history logging.

---

## 🤝 Contributing

Contributions, issues, and feature requests are welcome!  
Feel free to check the [issues page](https://github.com/heerp5/banksystem-pure-python/issues) if you want to contribute.

---

## 📜 License

Distributed under the **MIT License**. See `LICENSE` for more information.
