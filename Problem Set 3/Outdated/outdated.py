months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]

def meth_one(date):
    try:
        # Clean the input and split by "/"
        date = date.strip().split('/')
        if len(date) != 3:
            return False  # Invalid format
        
        month = int(date[0])
        day = int(date[1])
        year = int(date[2])
        
        # Check for valid month and day ranges
        if not (1 <= month <= 12 and 1 <= day <= 31):
            return False
        
        # Format day and month as two digits
        day = f"{day:02}"
        month = f"{month:02}"
        
        # Return formatted date
        return f"{year}-{month}-{day}"
    except (ValueError, IndexError):
        return False

def meth_two(date):
    try:
        # Clean the input and split by spaces
        date = date.strip().split()
        if len(date) != 3:
            return False  # Invalid format
        
        year = int(date[2])
        month_name = date[0]
        day = int(date[1].strip(','))
        
        # Convert month name to number
        if month_name not in months:
            return False
        
        month = months.index(month_name) + 1
        
        # Check for valid day range
        if not (1 <= month <= 12 and 1 <= day <= 31):
            return False
        
        # Format day and month as two digits
        day = f"{day:02}"
        month = f"{month:02}"
        
        # Return formatted date
        return f"{year}-{month}-{day}"
    except (ValueError, IndexError):
        return False

def load(date):
    # Decide which method to use based on format
    if '/' in date:
        return meth_one(date)
    elif ',' in date:
        return meth_two(date)
    else:
        return False

while True:
    ddate = input("Date: ").strip()
    result = load(ddate)
    
    if result:
        print(result)  # Print the valid formatted date
        break
