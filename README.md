# passwords_streanth

## Overview
**Password Analyzer** is a Python-based tool designed to evaluate the strength of a password by analyzing various characteristics. It scores passwords based on several factors, including length, repeated characters, sequential characters, and character composition (lowercase, uppercase, numbers, and special characters). 

The goal of this project is to provide a comprehensive analysis of password strength.

---

## Features
The Password Analyzer evaluates passwords based on the following criteria:
1. **Length**:
   - Non-linear penalty for shorter passwords.
   - Rewards passwords that meet or exceed a minimum recommended length.

2. **Repeated Characters**:
   - Identifies and penalizes consecutive repeating characters (e.g., "aaa" or "111").

3. **Sequential Characters**:
   - Checks for sequential characters in ascending or descending order (e.g., "123", "abc", or "zyx").

4. **Character Composition**:
   - Analyzes the types of characters used:
     - Lowercase letters
     - Uppercase letters
     - Numbers
     - Special characters
   - Includes both binary checks (e.g., at least one of each type) and percentage thresholds for diversity.

5. **Score System**:
   - Starts with a base score (e.g., 100) and applies reductions for "bad characteristics."
   - Final score provides a measure of password strength.

---

## Installation
To run the Password Analyzer, you need to have Python installed on your system.

1. **Clone the repository**:
   ```bash
   git clone https://github.com/poopick/passwords_streanth.git
   
