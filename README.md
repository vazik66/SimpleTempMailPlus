# SimpleTempMailPlus

With SimpleTempMailPlus you can create temporary mailboxes (max 2 hours) with custom names, and read all messages in them.

## Usage

```
from SimpleTempMailPlus import Tempmail

# Random mailbox
mailbox = Tempmail(Tempmail.generate_name(), Tempmail.get_random_domain())
mailbox.create()

# You can use custom mailbox name
mailbox = Tempmail(my_mailbox_name, Tempmail.get_random_domain())
mailbox.create()

# Also you can choose one of domains
domains = Tempmail.get_domains() # List of str

mailbox = Tempmail(my_mailbox_name, one_of_domains)
mailbox.create()
```

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.
