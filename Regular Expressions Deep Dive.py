# Task #1

import re

text = "Emails: user1@domain.com, user2@exclude.com, user3@domain.com, user4@exclude.com, user5@exclude.com, user6@domain.com"

emails = re.findall(r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b", text)
exclude_email = re.sub(r"\b[A-Za-z0-9._%+-]+@[exclude]+\.[A-Z|a-z]{2,}\b", "", text)

print("\nAll emails in the original list:", emails)
print("New", exclude_email)
