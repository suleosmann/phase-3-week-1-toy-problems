def convert_to_24_hour(hour, minute, period):
    if period == "pm" and hour != 12:
        hour += 12
    elif period == "am" and hour == 12:
        hour = 0
    
    # Format the hour and minute to ensure they're two digits
    hour_str = str(hour).zfill(2)
    minute_str = str(minute).zfill(2)
    
    return hour_str + minute_str

# Test cases
print(convert_to_24_hour(12, 30, "am"))  # Output: 0830
print(convert_to_24_hour(8, 30, "pm"))  # Output: 2030
