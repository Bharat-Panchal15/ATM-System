# ATM System (CLI App)

A simple command-line based ATM system simulation built in Python using Object-Oriented Programming (OOP). The system allows users to register accounts, login, deposit, withdraw money, view balance, change PINs, and logout — all via a terminal interface.

---

## 🚀 Features

- Register a new bank account
- Login and logout from account
- View account balance
- Deposit money (min ₹2000)
- Withdraw money (min ₹3000, maintain ₹2500 minimum balance)
- Change account PIN
- Session-based account management (no file/database storage yet)

---

## 🛠️ Tech Stack

- **Language:** Python  
- **Concepts Used:**
  - OOP (Classes for Account and ATMSystem)
  - Conditional access (requires login for operations)
  - CLI interaction via `match-case`
  - Planned upgrade: JSON/file-based storage

---

## 📂 Files

- `main.py` – Main script containing the entire ATM system logic

---

## 👤 Author

- Bharat Panchal  
- [GitHub Profile](https://github.com/Bharat-Panchal15)

## ▶️ How to Run

```bash
python main.py
