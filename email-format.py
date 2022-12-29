def full_email(people):
    result = []
    for name, email in people:
        result.append(f"{name} <{email}>")
    return result


print(full_email([('Maneesh', 'maneesh.negi@binmile.com'), ('Satya', 'satya@binmile.com'), ('Nitiesh', 'nitiesh@binmile.com')]))
