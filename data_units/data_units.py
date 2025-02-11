# Version 1.0.0
class DataUnits:
    BINARY = {
        'kib': 1, 'mib': 2, 'gib': 3, 'tib': 4,
        'pib': 5, 'eib': 6, 'zib': 7, 'yib': 8
    }

    SI = {
        'kb': 1, 'mb': 2, 'gb': 3, 'tb': 4,
        'pb': 5, 'eb': 6, 'zb': 7, 'yb': 8
    }

    def to_bytes(self, rounded=True, **operation_type):
        try:
            operation_type = {key.lower(): value for key, value in operation_type.items()}

            if len(operation_type) > 2:
                raise ValueError("Provide only one unit at a time.")

            for unit, power in {**self.BINARY, **self.SI}.items():
                if unit in operation_type:
                    value = operation_type[unit]

                    if not isinstance(value, (int, float, str)) or isinstance(value, bool):
                        raise TypeError(f"Invalid value type for {unit}: {type(value)}")
                        
                    try:
                        value = float(value)
                    except ValueError:
                        raise ValueError(f"Cannot convert '{value}' to a number.")

                    base = 1024 if unit in self.BINARY else 1000
                    output = value * (base ** power)
                    output = int(output) if rounded else output
                    
                    sep = operation_type.get('sep', False)
                    if sep:
                        output = f"{output:,}".replace(',', str(sep)) if sep is not True else f"{output:,}"

                    return output

            return None

        except (ValueError, TypeError) as e:
            return f"Error: {e}"

    def from_bytes(self, rounded=False, **operation_type):
        try:
            operation_type = {key.lower(): value for key, value in operation_type.items()}
            
            if len(operation_type) > 2:
                raise ValueError("Provide only one unit at a time.")

            for unit, power in {**self.BINARY, **self.SI}.items():
                if unit in operation_type:
                    byte_value = operation_type[unit]

                    if not isinstance(byte_value, (int, float, str)) or isinstance(byte_value, bool):
                        raise TypeError(f"Invalid value type for {unit}: {type(byte_value)}")
                        
                    try:
                        byte_value = float(byte_value)
                    except ValueError:
                        raise ValueError(f"Cannot convert '{byte_value}' to a number.")

                    base = 1024 if unit in self.BINARY else 1000
                    output = byte_value / (base ** power)
                    
                    if rounded:
                        output = round(output, 6)
                    else:
                        output = f"{output:.15f}".rstrip('0').rstrip('.')

                    sep = operation_type.get("sep", False)
                    if sep:
                        output = f"{float(output):,}".replace(',', str(sep)) if sep is not True else f"{float(output):,}"

                    return output

            return None

        except (ValueError, TypeError) as e:
            return f"Error: {e}"
