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
        """Convert SI or Binary units to bytes with optional float output."""
        try:
            # Normalize input keys to lowercase
            operation_type = {key.lower(): value for key, value in operation_type.items()}

            # Ensure only one unit is provided
            if len(operation_type) > 2:  # One unit + optional `sep`
                raise ValueError("Provide only one unit at a time.")

            for unit, power in {**self.BINARY, **self.SI}.items():
                if unit in operation_type:
                    value = operation_type[unit]

                    # Ensure input is numeric
                    if not isinstance(value, (int, float, str)) or isinstance(value, bool):
                        raise TypeError(f"Invalid value type for {unit}: {type(value)}")

                    # Convert string numbers
                    try:
                        value = float(value)
                    except ValueError:
                        raise ValueError(f"Cannot convert '{value}' to a number.")

                    base = 1024 if unit in self.BINARY else 1000  # Detect base
                    output = value * (base ** power)  # Convert to bytes

                    # Apply rounding
                    output = int(output) if rounded else output

                    # Handle separator formatting
                    sep = operation_type.get('sep', False)
                    if sep:
                        output = f"{output:,}".replace(',', str(sep)) if sep is not True else f"{output:,}"

                    return output  # Return the processed output

            return None  # No valid unit found

        except (ValueError, TypeError) as e:
            return f"Error: {e}"  # Return error messages instead of breaking execution

    def from_bytes(self, rounded=False, **operation_type):
        """Convert bytes to SI or Binary units (Full Precision or Rounded)."""
        try:
            # Normalize input keys to lowercase
            operation_type = {key.lower(): value for key, value in operation_type.items()}

            # Ensure only one unit is provided
            if len(operation_type) > 2:  # One unit + optional `sep`
                raise ValueError("Provide only one unit at a time.")

            for unit, power in {**self.BINARY, **self.SI}.items():
                if unit in operation_type:
                    byte_value = operation_type[unit]

                    # Ensure input is numeric
                    if not isinstance(byte_value, (int, float, str)) or isinstance(byte_value, bool):
                        raise TypeError(f"Invalid value type for {unit}: {type(byte_value)}")

                    # Convert string numbers
                    try:
                        byte_value = float(byte_value)
                    except ValueError:
                        raise ValueError(f"Cannot convert '{byte_value}' to a number.")

                    base = 1024 if unit in self.BINARY else 1000  # Detect base
                    output = byte_value / (base ** power)  # Convert bytes to the specified unit

                    # Apply rounding only if requested
                    if rounded:
                        output = round(output, 6)  # Round to 6 decimal places
                    else:
                        output = f"{output:.15f}".rstrip('0').rstrip('.')  # Keep full precision

                    # Handle separator formatting
                    sep = operation_type.get("sep", False)
                    if sep:
                        output = f"{float(output):,}".replace(',', str(sep)) if sep is not True else f"{float(output):,}"

                    return output

            return None  # No valid unit found

        except (ValueError, TypeError) as e:
            return f"Error: {e}"  # Return error messages instead of breaking execution
