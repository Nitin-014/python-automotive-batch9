# Function to calculate compound interest for senior citizens
def calculate_ci(principal, age, time):
    try:
        # Check for valid inputs
        if principal <= 0 or time <= 0:
            raise ValueError("Principal and time must be greater than zero")

        # Check senior citizen condition
        if age < 60:
            raise Exception("Compound interest is applicable only for senior citizens")

        rate = 8  # 8% per annum

        # CI formula as given
        ci = principal + (principal * rate * time) / 100

        return ci

    except ValueError as ve:
        return f"Input Error: {ve}"

    except Exception as e:
        return f"Eligibility Error: {e}"


# ---- Main Program ----
try:
    p = float(input("Enter principal amount: "))
    age = int(input("Enter age: "))
    t = int(input("Enter time (in years): "))

    result = calculate_ci(p, age, t)
    print("Calculated Amount:", result)

except Exception as e:
    print("Unexpected Error:", e)
