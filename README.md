
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
git clone https://github.com/Nullocrix/DataUnits.git && cd DataUnits; pip install .
```

---

## **Usage**
```python
from data_units import DataUnits

convert = DataUnits()

# Example 1: Convert 2 GiB to bytes, then back to GiB
value_in_bytes = convert.to_bytes(gib=2)
print(f"2 GiB in bytes: {value_in_bytes}")  # Output: 2147483648

value_in_gib = convert.from_bytes(gib=value_in_bytes)
print(f"2147483648 bytes in GiB: {value_in_gib}")  # Output: 2.0

# Example 2: Convert 500 MB (SI) to bytes, then back to MB with rounding
value_in_bytes = convert.to_bytes(mb=500)
print(f"500 MB in bytes: {value_in_bytes}")  # Output: 500000000

value_in_mb = convert.from_bytes(mb=value_in_bytes, rounded=True)
print(f"500000000 bytes in MB: {value_in_mb}")  # Output: 500.0

# Example 3: Convert 1.5 TiB to bytes, then back to TiB with a custom separator
value_in_bytes = convert.to_bytes(tib=1.5, sep="_")
print(f"1.5 TiB in bytes: {value_in_bytes}")  # Output: 1_649_267_441_664

value_in_tib = convert.from_bytes(tib=value_in_bytes, sep='_')
print(f"1,649,267,441,664 bytes in TiB: {value_in_tib}")  # Output: 1.5

# Example 4: Using a custom separator when converting both ways
value_in_bytes = convert.to_bytes(mib=1024, sep='_')
print(f"1024 MiB in bytes with custom separator: {value_in_bytes}")  # Output: 1_073_741_824

value_in_mib = convert.from_bytes(mib=1073741824, sep='.')
print(f"1073741824 bytes in MiB with custom separator: {value_in_mib}")  # Output: 1024.0
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
