class Employee:
    def __init__(self, name, employee_id, position, mail):
        self.name = name
        self.employee_id = employee_id
        self.position = position
        self.mail = mail


class DisplayInformation(Employee):
    def display_info(self):
        print(f"Name: {self.name}")
        print(f"Employee ID: {self.employee_id}")
        print(f"Position: {self.position}")
        print(f"Mail: {self.mail}")


class EmailOperations(Employee):
    def generate_email(self):
        email = f"{self.name.lower().replace(' ', '.')}.{self.employee_id}@company.com"
        return email

    def send_email(self, recipient, subject, message):
        print(f"Sending email to {recipient}:\nSubject: {subject}\nMessage: {message}")


person1 = DisplayInformation('Unknown', 'D-503', 'Engineer', 'test@test.com')
person1.display_info()
print()
email = EmailOperations('Unknown', 'I-330', 'Artist', 'test2@test.com')
email.generate_email()
email.send_email('D-503', 'I-330', 'Hello!')
