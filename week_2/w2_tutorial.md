# Movie Theater Admission System

## Scenario

A movie theater has the following admission policy:

A person is allowed to enter if:

- The user is **13 years old or older**, OR  
- The user is **under 13 AND accompanied by an adult**,  
- AND the user must have a **valid ticket**

---

## Boolean Expression

\[
(A \lor (\neg A \land B)) \land C
\]

Where:

- **A** = Age ≥ 13  
- **B** = Accompanied by Adult (only valid if age < 13)  
- **C** = Valid Ticket  

---

# 1. Identify the Components

## 1.1 Inputs

The system requires:

1. User's Age  
2. Accompanied by Adult (Yes/No)  
3. Valid Ticket (Yes/No)  

---

## 1.2 Process

The system evaluates:

- If age ≥ 13 → user qualifies based on age  
- If age < 13 → check adult accompaniment  
- Ticket must always be valid  
- Final decision depends on combined conditions  

---

## 1.3 Output

- Allow Entry  
- Deny Entry  

---

# 2. Design the Algorithm

## 2.1 Canva Flowchart 
![Movie Theater Admission Flowchart](https://github.com/SuYeeMyatMoe/SuYeeMyatMoe_202505010331_python-programming/blob/main/week_2/diagram.png)
---

# 2.2 Truth Table

Expression:

\[
(A \lor (\neg A \land B)) \land C
\]

| A (≥13) | B (Adult if <13) | C (Ticket) | Result |
|--------|------------------|------------|--------|
| F | F | F | Deny Entry |
| F | F | T | Deny Entry |
| F | T | F | Deny Entry |
| F | T | T | Allow Entry |
| T | F | F | Deny Entry |
| T | F | T | Allow Entry |
| T | T | F | Deny Entry |
| T | T | T | Allow Entry |

---

# 2.3 Algorithm (Step-by-Step Solution)

1. Start  
2. Input age  
3. Input accompanied by adult status  
4. Input valid ticket status  
5. IF age ≥ 13 THEN  
   - IF ticket is valid → Allow Entry  
   - ELSE → Deny Entry  
6. ELSE (age < 13) THEN  
   - IF accompanied by adult AND ticket is valid → Allow Entry  
   - ELSE → Deny Entry  
7. End  

---

# 2.4 Pseudocode

```
START

INPUT age
INPUT accompaniedByAdult
INPUT validTicket

IF age >= 13 THEN
    IF validTicket = TRUE THEN
        DISPLAY "Allow Entry"
    ELSE
        DISPLAY "Deny Entry"
    ENDIF

ELSE
    IF accompaniedByAdult = TRUE AND validTicket = TRUE THEN
        DISPLAY "Allow Entry"
    ELSE
        DISPLAY "Deny Entry"
    ENDIF
ENDIF

END
```

---

# 3. Evaluate Expression

---

### Test Case 1

| Variable | Value |
|-----------|--------|
| Age | 15 |
| Accompanied by Adult | No |
| Valid Ticket | Yes |

**Evaluation**

```
(True OR False) AND True
True AND True
True
```

**Output**
```
Allow Entry
```

---

### Test Case 2

| Variable | Value |
|-----------|--------|
| Age | 10 |
| Accompanied by Adult | Yes |
| Valid Ticket | Yes |

**Evaluation**

```
(False OR True) AND True
True AND True
True
```

**Output**
```
Allow Entry
```

---

### Test Case 3

| Variable | Value |
|-----------|--------|
| Age | 10 |
| Accompanied by Adult | No |
| Valid Ticket | Yes |

**Evaluation**

```
(False OR False) AND True
False AND True
False
```

**Output**
```
Deny Entry
```

---

### Test Case 4

| Variable | Value |
|-----------|--------|
| Age | 16 |
| Accompanied by Adult | No |
| Valid Ticket | No |

**Evaluation**

```
(True OR False) AND False
True AND False
False
```

**Output**
```
Deny Entry
```

---

- **A** = Age ≥ 13  
- **B** = Accompanied by Adult  
- **C** = Valid Ticket  

A user is allowed to enter the movie theater only if they satisfy the age/adult requirement and possess a valid ticket.
