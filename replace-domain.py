# replace old domain with new domain name in all the emails

def email_replace(email, old_domain, new_domain):
    if '@' + old_domain in email:
        index = email.index("@" + old_domain)
        new_email = email[:index] + "@" + new_domain
        return new_email
    return email

email = "maneesh.negi@bmt2.com"
new_email = email_replace(email, 'bmt.com', 'binmile.com')
print(new_email)


# example
txt = "A kong text for an example"
new_txt = txt[:2] + "l" + txt[3:]
print(new_txt)