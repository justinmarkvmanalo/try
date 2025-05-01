class AgeClassifier:
    def classify_age(self, age):
        if age < 0:
            raise ValueError("Age cannot be negative.")
        elif age <= 4:
            return "Toddler"
        elif age <= 12:
            return "Child"
        elif age <= 19:
            return "Teen"
        elif age <= 64:
            return "Adult"
        else:
            return "Senior"
        