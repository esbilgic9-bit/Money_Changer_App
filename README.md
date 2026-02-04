# Money Changer App 💸

A Python script that takes a total amount of money in MAD and breaks it down into the largest possible currency bills (200, 100, 50, and 20 MAD).

## 🚀 How it Works
The program calculates the number of bills required by using:
* **Floor Division (`//`)** to find the number of notes.
* **Modulo (`%`)** to track the remaining balance for the next denomination.

## 🛠️ Features
- Supports multiple denominations: 200, 100, 50, and 20 MAD.
- Professional output formatting using newline characters (`\n`) for better readability.
- Input validation (Integer based).

## 💻 Example Output
```text
Enter the total amount in MAD: 870
Results:
200 MAD bills: 4
100 MAD bills: 0
50 MAD bills: 1
20 MAD bills: 1
Remaining: 0 MAD
