"""
Define constants here
"""
# In days
BORROW_DURATION = 14
RENEW_DURATION = 14

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

# book area
BOOK_AREA = (
        ('信仰個人成長','信仰個人成長'),
        ('靈修','靈修'),
        ('宣教','宣教'),
        ('護教','護教'),
        ('見證','見證'),
        ('佈道','佈道'),
        ('家庭、兩性關係','家庭、兩性關係'),
        ('情緒','情緒'),
        ('祈禱','祈禱'),
        ('敬拜','敬拜'),
        ('兒童(宗教)','兒童(宗教)'),
        ('兒童(其他)','兒童(其他)'),
        ('少年','少年'),
        ('UNKNOWN','UNKNOWN'),
        )
# book language
BOOK_LANG = (
             ('C','Chinese'),
             ('E','English'),
             )

#code_colour
CODE_COLOUR = (
               ('Blue','Blue'),
               ('Red','Red'),
               ('Black','Black'),
               ('Green','Green'),
               ('White','White'),
               ('Orange','Orange'),
               ('Yellow','Yellow'),
               ('Pink','Pink'),
               ('Gray','Gray'),
               ('Black lines','Black lines'),
               )