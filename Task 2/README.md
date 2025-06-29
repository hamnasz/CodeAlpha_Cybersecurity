# 🔐 Secure Login System – CodeAlpha Internship (Task 3)

Welcome to **Task 3: Secure Coding Review** – a professional-grade, secure login system built in Python featuring interactive **Roman Urdu-style feedback**. This project demonstrates modern secure programming practices, including input validation, salted password hashing, and brute-force attack prevention.

📂 **Location:** [`/Task 2`](./)

---

## 📌 Objective

> **TASK 3: Secure Coding Review**
>
> - Select a programming language and application to audit.
> - Perform a code review to identify security vulnerabilities.
> - Utilize tools such as static analyzers or manual inspection methods.
> - Provide recommendations and best practices for secure coding.
> - Document findings and suggest remediation steps for safer code.

---

## 🚀 Getting Started

> **Prerequisite:** Python 3 must be installed.

### 🖥️ Quick Start Guide

1. **Open your terminal** (GitHub Codespaces or local machine).
2. Navigate to the project directory:
   ```bash
   cd "Task 2"
   ```
3. Launch the login system:
   ```bash
   python3 login_system.py
   ```
4. Use the following **default login credentials**:
   - **Username:** `admin`
   - **Password:** `Pa$$w0rd123`

---

## 🗂️ Project Structure

```
Task 2/
│
├── login_system.py
└── users_db.json
```

---

## 🔍 File Overview

| File                                    | Description                                               |
| ---------------------------------------- | --------------------------------------------------------- |
| [`login_system.py`](./login_system.py)   | Main script implementing secure login with Roman Urdu UI  |
| [`users_db.json`](./users_db.json)       | Simulated persistent user storage (auto-generated)        |

---

## 🔐 Security Highlights

- **Password Hashing:** Utilizes `SHA-256` for secure password storage
- **Salted Passwords:** Protects against rainbow table attacks
- **Brute-force Protection:** Locks account after 3 failed attempts
- **Input Validation:** Enforces strong password requirements
- **Console Security:** Hides passwords in the terminal using `getpass()`

---

## ⚠️ Known Limitations

- **No database integration:** Uses simple file-based storage (`users_db.json`)
- **No graphical/web interface**
- **No HTTPS/SSL or Multi-Factor Authentication (MFA)**
- **Admin password is set via `os.environ`:** More secure than hardcoding, but further improvements are possible

---

## 👤 Author

**Humna Imran**  
Intern, [CodeAlpha](https://www.codealphatechnologies.com/)  
[GitHub: hamnasz](https://github.com/hamnasz)

---

## 📬 Support & Contribution

If you are a reviewer, supervisor, or fellow intern interested in reviewing or enhancing this code, please feel free to open an issue or contact me through GitHub.

---

> _This project was developed for the CodeAlpha Cybersecurity Internship, Task 3: Secure Coding Review._