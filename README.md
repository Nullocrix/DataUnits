
# **DataUnits**

A Python module for converting between SI and Binary units to bytes and vice-versa, with optional custom formatting for output.

## **Features**
- Convert between common units (e.g., KB, MB, GiB, TiB) and bytes.
- Support for both SI (base 10) and Binary (base 2) units.
- Customizable formatting with separators for better readability.
- Error handling for invalid input values.

---

## **Installation**
```bash
pip install DataUnits
```

---

## **Usage**
```python
from data_units import DataUnits

convert = DataUnits()

# Convert 1 GiB to Bytes
value = convert.to_bytes(gib=1)
print(value)  # Output: 1073741824

# Convert 1048576 Bytes to MiB with full precision
value = convert.from_bytes(mib=1048576)
print(value)  # Output: 1.0 MiB

# Using default separator
value = convert.to_bytes(mib=512, sep=False)
print(value)  # Output: 536,870,912

# Using custom separator example
value = convert.from_bytes(mib=536870912, sep='>')
print(value)  # Output: 1>024>512
```

---

## **Methods**

### **to_bytes()**
Convert a given value from SI or Binary units to bytes.

**Parameters:**
- `rounded` (bool, optional): Rounds the output to an integer. Default is `True`.
- `sep` (optional): Adds a separator for thousands formatting. Use `True` for commas or pass a custom separator.

**Example:**
```python
convert.to_bytes(gb=1024, sep=True)  # Output: 1,073,741,824
```

---

### **from_bytes()**
Convert a given byte value to the specified SI or Binary unit.

**Parameters:**
- `rounded` (bool, optional): Rounds the output to 6 decimal places. Default is `False`.
- `sep` (optional): Adds a separator for thousands formatting. Use `True` for commas or pass a custom separator.

**Example:**
```python
convert.from_bytes(bytes=536870912, rounded=True)  # Output: 0.5 GiB
```

---

## **Error Handling**
The module provides detailed error messages for invalid inputs, such as:
- Invalid unit types
- Non-numeric input values

---

## **License**
MIT License

---

## **Contributing**
Feel free to fork the project and submit pull requests for improvements or additional features.

---

## **Contact**
For questions or suggestions, contact [your_email@example.com].
