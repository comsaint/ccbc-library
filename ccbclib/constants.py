"""
Define constants here
"""
# In days
RENEW_DURATION = 14
BORROW_DURATION = 14

# book status
ONSHELF = 'OS'
BORROWED = 'BR'
RENEWED = 'RN'
OVERDUE = 'OD'
RESERVED = 'RS'
LOST = 'LS'
BOOK_STATUS_CHOICE=(
                    (ONSHELF,'On-shelf'),
                    (BORROWED,'Borrowed'),
                    (RENEWED,'Renewed'),
                    (OVERDUE,'Overdue'),
                    (RESERVED,'Reserved'),
                    (LOST,'Lost'),
                    )

# borrower status
IDLE = 'I'
BORROWING = 'B'
OVERDUING = 'D'
BORROWER_STATUS_CHOICE=(
                        (IDLE,'Idle'),
                        (BORROWING,'Borrowing'),
                        (OVERDUING,'Overduing'),
                        )

