# 🔐 Secure Login System – CodeAlpha Internship (Task 3)

Welcome to **Task 3: Secure Coding Review** – a secure login system built in Python with interactive **Roman Urdu-style feedback**. This task demonstrates secure programming techniques, including input validation, salted password hashing, and brute-force prevention.

📂 Path to this task: [`/Task 2`](./)

---

## 📌 Objective (as per internship instructions)

> **TASK 3: Secure Coding Review**
>
> - Select a programming language and application to audit.
> - Perform a code review to identify security vulnerabilities.
> - Use tools like static analyzers or manual inspection methods.
> - Provide recommendations and best practices for secure coding.
> - Document findings and suggest remediation steps for safer code.

---

## 🚀 How to Run the Project

> ✅ You must have Python 3 installed.

### 🖥️ Step-by-Step Instructions

1. **Open the terminal** in GitHub Codespaces or your local machine.
2. Navigate to the project folder:
   ```bash
   cd "Task 2"
````

3. Run the login system:

   ```bash
   python3 login_system.py
   ```
4. Use the following **default login credentials**:

   * Username: `admin`
   * Password: `Pa$$w0rd123`

---

## 🗂️ Folder Structure

```
Task 2/
│
├── login_system.py
└── users_db.json 
```

---

## 🔍 Files and Their Purpose

| File                                                   | Purpose                                                                   |
| ------------------------------------------------------ | ------------------------------------------------------------------------- |
| [`login_system.py`](./login_system.py)                 | Main Python script implementing secure login with Roman Urdu prompts      |
| [`users_db.json`](./users_db.json)                     | Simulated persistent user storage (auto-generated)                        |
---

## 🔐 Security Features Implemented

* ✅ **Password hashing** with `SHA-256`
* ✅ **Salted password storage** to prevent rainbow table attacks
* ✅ **Brute-force protection** – locks out user after 3 failed attempts
* ✅ **Input validation** – ensures strong passwords
* ✅ **Console security** – hides typed passwords using `getpass()`

---

## ⚠️ Known Limitations

* ❌ No database — uses file-based storage (`users_db.json`)
* ❌ No GUI or web interface
* ❌ No HTTPS/SSL or multi-factor auth (MFA)
* ❌ Admin password stored using `os.environ` (better than hardcoded, but can be improved)

---

## 🤝 Author

**Humna Imran**
Intern at [CodeAlpha](https://www.codealphatechnologies.com/)
🔗 [GitHub Profile](https://github.com/hamnasz)

---

## 📬 Need Help?

If you're a reviewer, supervisor, or classmate and want to explore or improve this code, feel free to open an issue or contact me on GitHub.

---

> *This task was completed under the CodeAlpha Cybersecurity Internship Program, Task 3: Secure Coding Review.*

```