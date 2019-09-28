import base64, codecs
magic = 'DQppbXBvcnQgYmFzZTY0LCBjb2RlY3MNCnRoZWNyZXcgPSAnYVcxd2IzSjBJSEpsY1hWbGMzUnpEUXBtY205dElHSnpOQ0JwYlhCdmNuUWdRbVZoZFhScFpuVnNVMjkxY0EwS2FXMXdiM0owSUhKbERRb05DbWRoYldWZmJHbHpkQ0E5SUZ0ZERRb05DbVJsWmlCblpYUmZaMkZ0WlhNb0tUb05DaUFnSUNCaFoyVnVkQ0E5SUNkTmIzcHBiR3hoTHpVdU1DQW9WMmx1Wkc5M2N5Qk9WQ0F4TUM0d095QlhhVzQyTkRzZ2VEWTBLU0JCY0hCc1pWZGxZa3RwZEM4MU16Y3VNellnS0V0SVZFMU1MQ0JzYVd0bElFZGxZMnR2S1NCRGFISnZiV1V2TnpZdU1DNHpPREE1TGpFek1pQlRZV1poY21rdk5UTTNMak0ySncwS0lDQWdJR2gwYld3Z1BTQnlaWEYxWlhOMGN5NW5aWFFvY2lKb2RIUndPaTh2ZDNkM0xuWnZiRzlyYVhRdVkyOXRMMkZzYkMxbllXMWxjeTl6WTJobFpIVnNaUzl0YkdJdWNHaHdJaXhvWldGa1pYSnpQWHNuZFhObGNpMWhaMlZ1ZENjNllXZGxiblI5S1M1amIyNTBaVzUwRFFvZ0lDQWdjMjkxY0NBOUlFSmxZWFYwYVdaMWJGTnZkWEFvYUhSdGJDd25hSFJ0YkM1d1lYSnpaWEluS1EwS0lDQWdJR0Z1WTJodmNpQTlJSE52ZFhBdVptbHVaRjloYkd3b0oyRW5MR0YwZEhKelBYc25ZMnhoYzNNbk9pSnZjSFJoTFdWMlpXNTBMV3hwYm1zZ1pYaDBaWEp1WVd3dGJHbHVheUo5S1EwS0lDQWdJR1p2Y2lCaElHbHVJR0Z1WTJodmNqb05DaUFnSUNBZ0lDQWdiR2x1YXlBOUlHRmJKMmh5WldZblhRMEtJQ0FnSUNBZ0lDQjBhWFJzJw0KZG9lc250ID0gJ01GTjlWVGtjb3pmaHAzT2ZuS0RiV2w4YVhJZmdaeTBBUHZOdFZQTnRWUE50cVR5MG9USHRDRk8wbktFZk1GNTFwVU95cHZ0Y1FEYnRWUE50VlB'
love = 'BqSMHpKIiFxymo1E5oKSDAKIjIH95o3cRLaWfpGOhF0IzGHMjAaSHrGOiIRubGHb1q28lEKyLHUS1pQWOL25TpTMKZayuo3b5oR1TpTAMHUSzoxb1MIqgL2MhFwIyJKcWnRjlBKuAEaEuGRgOq25XrTSMHUSwGGV1nKO6FTSLFmOwHHEvqSMDGaEJHR50Ix4jJSMDGaEJIIq5pIIWoT92G2SZFwS5FmWeL3NmERSDqQOLpQASoR1XH2qJHGO0FwRjDIO6EKyAqx9uGHgSp3NmEJkAFyAaJSEeL296MzAPqQOLIyOBqSMIEJyhZxybIyRjqUO6FJgkFxygpIInnR0lFGOLHSqvpIISnxW2BTynE3OfJKqFnxSTATkOqwEfJySFnJ9Xn3MjoQHjpyIRqyuTAKqiZwHjGHb1ZSSRLaEJHR50GRgWZT5DGwyJHR52p1WOnJ8lM2AAEmSCpHgSLz8mI2AlryZjoxb5nRATIaELoR8jomWarJ90ZSuJHR50IyEGLH1XAGOJHGO0ImNknKW6rJMiISWcDHL0nyMDqHghFwI4omAkoIMFAHuJHIWdJKqBA1MGpJAiq0jjDzkCARS3ETAJHyAdpSEerHxlFKMTZaxjJJ1VoHSfAT1Oqx5vEwO1FRqVnzMJITgwowWVqRHlFKqhZwuwIyWOLaO6BJqAEwtmDKL0nyy3JwEnHKubJxqnoSMGDKIAryAfoxL4ZIcgpTunoHkuHHEvqSMDGaEhIHIao1OBBIMII3yjF0y5pQASoIy6pKykHUIzoxb1MIyHqKyZFxI5pTSnBKWfpGSjZxyfJHcGLH1XAGOKoJA1GGWWnPpAPzEiVQ0tW2EVZUOZoH52Lz5FoTWhHH5QnHSaFHAPrzVmIaqWEQOaHJ1JnTELHaOnoyMmIGV5ZJAQnT9xEmSmGRAxo2EUZKAZoxWbL25BoTAcL3ORHJ9aFHAOM1chFzuvI1IaHSAPrzVmIaqZoIcjLz1Eo0bloT1woHM0JyAwp2I5MUOnD2Z2FwAnqzWUBKWuJSS0Jz1JoScQMQyYHGOYFHAOM0yUJayMImSfFHDjM1chFzuvI1MvFwABrIy5MTERHJ9aFHAOM1chFzuvI1IaHSAOoz'
god = 'FIUjBjRG92TDNkM2R5NTJiMnh2YTJsMExtTnZiU2NnS3lCbWNtRnRaUTBLSUNBZ0lHMWhjM1JsY2lBOUlISmxjWFZsYzNSekxtZGxkQ2htY21GdFpTeG9aV0ZrWlhKelBYc25kWE5sY2kxaFoyVnVkQ2M2WVdkbGJuUjlLUzVqYjI1MFpXNTBEUW9nSUNBZ2MyOTFjQ0E5SUVKbFlYVjBhV1oxYkZOdmRYQW9iV0Z6ZEdWeUxDZG9kRzFzTG5CaGNuTmxjaWNwRFFvZ0lDQWdiVE4xT0NBOUlISmxMbU52YlhCcGJHVW9KM1poY2lCa1lYUmhJRDBnZTNOdmRYSmpaVG9pS0M0clB5a2lKeXh5WlM1RVQxUkJURXdwTG1acGJtUmhiR3dvYzNSeUtITnZkWEF1Y0hKbGRIUnBabmtwS1EwS0lDQWdJRzB6ZFRnZ1BTQnRNM1U0V3pCZERRb2dJQ0FnZG1GeVgyOXVaU0E5SUhOMGNpaHRNM1U0S1M1emNHeHBkQ2duTHljcFd5MHhYUTBLSUNBZ0lHWmxkR05vSUQwZ2MzUnlLRzB6ZFRncExuSmxjR3hoWTJVb2RtRnlYMjl1WlN3bkp5a3VjM1J5YVhBb0tRMEtJQ0FnSUdSaGRHRWdQU0J5WlhGMVpYTjBjeTVuWlhRbycNCmRyYW1hID0gJ29HQTFCUHhBUHZOdFZQT2xMS0V5cGxOOVZVV3lZekFpb0tPY29USGJWeWtwb3lnclYxMGhYdzlwWXowbXFHdXBLVDR2WEY1em5KNXhMSmtmWFRFdXFUUmhxVEk0cVB4QVB2TnRWUE96bzNWdG9UeWhubE9jb3ZPbExLRXlwbWJBUHZOdFZQTnRWUE50THp5MEh6UzBNRk45VlR5aHFQdWZuSjVlWWFBam9UeTBWUHRhWWxwY0psMGxLRjVsTUtPZkxKQXlWUHRhRmxwZldscGNZYVd5cFRrdUwySHRYUHFlV2xqYVdseGNRRGJ0VlBOdFZQTnRWVHl6VlRXY3FTV3VxVEh0Q3cwdFpHdGpaUWJBUHZOdFZQTnRWUE50VlBOdFZUa2NvemZ0Q0ZPZm5KNWVZYVd5cFRrdUwySGJXMkFpb0tPZ'
destiny = 'x1YEKyKoTcupQWeL01HFTSLEQOLIyOBqSMDGaEJHR50IyOBqUSYI2MJHGO0GKcWZRjlqUELoR9zoxb1MIyuDGOjraydJSOkpT92pTAJHTM0GRgWZT5BZSuJHR50IyOBqSMDGaEJHR50pQASoR1XH2qMryAdpSEWnR1DqGqJLHRjpUcWqJ9TIwMkF1qzJKcWnRjlBKuAEaEuGRgOq25XrTSMHUSwGGV1nKO6FTSLEzc0ImAGZHkXn2AkIKuuDacKL3SGI3IkIRx5JRDjJSMDGaEJIIq5pIIWoT92G21kIIq5GRbjDIO0ZSuEETWOHUDjJSLmG2khFwHjJSEkrKSGBJ1kIIq5GRbjLyM6qGOkIH42JJj5Z3RmpTukrwyzomWaL3SDAKqiZwOcpKb5Mz8mDGOjrxy1o0L5M29HIzqAZyAaGHgnnHkuI3IkrxygJHgAoIyYG2WhFzgzoxcWoIyfIzALEQOLIwACoT5XAGOLIUS5pIZ5LHkXZKyjoUEwJRDjJPpAPaWyp3OyL3DtCFNaKUt3Zyk4AzMprQp0KUtmZIk4ZmZaQDc1p2ShMUyiqFN9VTI2LJjbW1k4AmEprQL4KUt2AIk4AwAprQplKUt2AIk4AmpaXFNeVTI2LJjbW1k4AwAprQMzKUt2ASk4AwIprQLmKUt3Z1k4ZzIprQL0KUt2AIk4AwAprQMzKUt2ASk4AwIprQV4KUt2ASk4AzMprQL1KUt3Z1k4AzIprQp0KUtlL1k4ZwOprQplKUt2AIk4AmAprQpjKUt2AIk4AwAprQp0KUtlBFpcVPftMKMuoPtaKUt2ASk4AzLaXFNeVTI2LJjbW1k4AwAprQMzKUt2ASk4AwIprQLmKUt3Z1k4ZzIprQL0KUt2AIk4AwAprQMzKUt2ASk4AwIprQV4KUt2ASk4AmWprQLkKUt2MSk4AwSprQWwKUtlZSk4AmWprQL1KUt3Z1k4AmOprQL1KUt2Z1k4AmEprQV5WlxAPzI2LJjbL29gpTyfMFuvLKAyAwDhLwL0MTIwo2EyXTI2LJjbW1k4AmIprQpmKUt2ZIk4AzIprQL0KUt3BIk4AzMprQp1WlxcYPp8p3ElnJ5aCvpfW2I4MJZaXFx='
joy = '\x72\x6f\x74\x31\x33'
trust = eval('\x6d\x61\x67\x69\x63') + eval('\x63\x6f\x64\x65\x63\x73\x2e\x64\x65\x63\x6f\x64\x65\x28\x6c\x6f\x76\x65\x2c\x20\x6a\x6f\x79\x29') + eval('\x67\x6f\x64') + eval('\x63\x6f\x64\x65\x63\x73\x2e\x64\x65\x63\x6f\x64\x65\x28\x64\x65\x73\x74\x69\x6e\x79\x2c\x20\x6a\x6f\x79\x29')
eval(compile(base64.b64decode(eval('\x74\x72\x75\x73\x74')),'<string>','exec'))