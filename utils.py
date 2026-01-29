def parse_and_print(data):
    full_text = ""
    for item in data:
        # If the item is a dictionary (structured data), extract the 'text' field
        if isinstance(item, dict) and 'text' in item:
            full_text += item['text']
        # If the item is a string (raw text), just append it
        elif isinstance(item, str):
            full_text += item
    return full_text