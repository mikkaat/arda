
import base64, codecs
thecrew = 'IyAtKi0gY29kaW5nOiB1dGYtOCAtKi0KCiIiIgpIRFN0cmVhbXMgU2NyYXBlciBWLTEuMC4wCkRhdGU6IEZyaSBKdWx5IDUsIDIwMTkKRm9yIFN1cHBvcnQgY29udGFjdDogaHR0cHM6Ly9kcmVhbWNhdGNoZXJpdC5jb20vCiIiIgoKdHJ5OgogICAgaW1wb3J0IG9zCiAgICBpbXBvcnQgc3lzCiAgICBpbXBvcnQgcmVxdWVzdHMKICAgIGZyb20gYnM0IGltcG9ydCBCZWF1dGlmdWxTb3VwCiAgICBpbXBvcnQgcmUKICAgIGZyb20gb3MucGF0aCBpbXBvcnQgam9pbgpleGNlcHQ6CglwYXNzIAogICAgIyAgICBwcmludCgiSW5zdGFsbGluZyBEZXBlbmRlbmNpZXMiKQogICAgIyAgICBvcy5zeXN0ZW0oInB5dGhvbjIgLW0gcGlwIGluc3RhbGwgYnM0IGx4bWwgcmVxdWVzdHMgIikKICAgICMgICAgcHJpbnQoIlBsZWFzZSByZSBydW4gdGhlIHNjcmlwdCIpCiAgICAjICAgIHN5cy5leGl0KDEpCiAgICAKbXlQYXRoID0gb3MucGF0aC5kaXJuYW1lKF9fZmlsZV9fKS5yZXBsYWNlKCdsaWInLCd4bWwnKQoKb3V0cHV0RmlsZSA9ICdoZHN0cmVhbXMueG1sJwpzYXZlWE1MID0gJ25vJwoKCiMgY2xlYW4gb2xkIGZpbGUgKGlmIGFueSkKCmhkU3RyZWFtTGlzdCA9IFtdCgppZiBzYXZlWE1MLmxvd2VyICgpID09ICd5ZXMnOgogICAgd2l0aCBvcGVuKGpvaW4obXlQYXRoLG91dHB1dEZpbGUpLCAidyIpIGFzIGY6CiAgICAgICAgZi53cml0ZSgiIikKCnRyeToKICAgIHJlc3BvbnNlID0gcmVxdWVzdHMuZ2V0KCJodHRwOi8vaGRzdHJlYW1zLmNsdWIvIikKICAgICMgICAgICAgc291cCA9IEJlYXV0aWZ1bFNvdXAocmVzcG9uc2UuY29udGVudCwgImx4bWwiKQogICAgc291cCA9IEJlYXV0a'
doesnt = 'JM1oSAiqKNbpzImpT9hp2HhL29hqTIhqPjtVzu0oJjhpTSlp2IlVvxXVPNtVUOupzIhqS9xnKLtCFOmo3IjYzMcozDbVzEcqvVfVUfvL2kup3ZvBvNvpTSaMF1wo250MJ50Va0cPvNtVPOjK3EuM3ZtCFOjLKWyoaEsMTy2YzMcozEsLJkfXPWjVvxXPvNtVPOcMvOjK3EuM3Z6PvNtVPNtVPNtMz9lVUOsqTSaVTyhVUOsqTSapmbXVPNtVPNtVPNtVPNtoTyhn3ZtCFOjK3EuMl5znJ5xK2SfoPtvLFVcPvNtVPNtVPNtVPNtVUEcoJIsoTymqPN9VUWyYzMcozEuoTjbVykxKTD6KTEpMPVfVUA0pvujK3EuMlxcPvNtVPNtVPNtVPNtVUEcqTkyplN9VUWyYaAjoTy0XPWpMSkxBykxKTDvYPOjK3EuMl50MKu0YzIhL29xMFtvqKEzYGtvXFyoZGb6KDbXVPNtVPNtVPNtVPNtnJLtoTyhn3Z6PvNtVPNtVPNtVPNtVPNtVPOzo3VtrPjtoTyhnlOcovOyoaIgMKWuqTHboTyhn3ZcBtbtVPNtVPNtVPNtVPNtVPNtVPNtVTkcozftCFOfnJ5eJlWbpzIzVy0XVPNtVPNtVPNtVPNtVPNtVPNtVPO0nKEfMFN9VTkcozfhp3OfnKDbVv8vXDbtVPNtVPNtVPNtVPNtVPNtVPNtVTAbLJ5hMJjtCFO0nKEfMIf0KF5lMKOfLJAyXPVhpTujVvjtVvVcPvNtVPNtVPNtVPNtVPNtVPNtVPNtqTy0oTHtCFNvCUEcqTkyCag9VUg9CP90nKEfMG4vYzMipz1uqPu0nJ1yK2kcp3EorS0fVUEcqTkyp1g4KFxXVPNtVPNtVPNtVPNtVPNtVPNtVPOaLJ1yVQ0tp3ElVPu0nKEfMKAorS0cPvNtVPNtVPNtVPNtVPNtVPNtVPNtMz9lVTxtnJ4tpzShM2HbZFjtAPx6PvNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVUElrGbXVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVUVtCFOlMKS1MKA0pl5aMKDbPvNtVPNtVPNtVPNtVPNtVPNtVP'
do = 'AgICAgICAgICAgICAgImh0dHA6Ly9jZG57fS5oZHN0cmVhbXMuY2x1Yi9saXZlL3t9L2luZGV4Lm0zdTgiLmZvcm1hdCgKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgaSwgY2hhbm5lbAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICksCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgaGVhZGVycz17CiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICJSZWZlcmVyIjogImh0dHA6Ly9oZHN0cmVhbXMuY2x1Yi9wYWdlL3t9LnBocCIuZm9ybWF0KAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgY2hhbm5lbAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICApCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgfSwKICAgICAgICAgICAgICAgICAgICAgICAgICAgICkKICAgICAgICAgICAgICAgICAgICAgICAgICAgICNwcmludChyLnN0YXR1c19jb2RlLCByLnVybCkKICAgICAgICAgICAgICAgICAgICAgICAgICAgIGlmIHIuc3RhdHVzX2NvZGUgPT0gMjAwOgogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIG0zdThfbGluayA9ICJodHRwOi8vY2Rue30uaGRzdHJlYW1zLmNsdWIvbGl2ZS97fS9pbmRleC5tM3U4fFJlZmVyZXI9aHR0cDovL2hkc3RyZWFtcy5jbHViL3BhZ2Uve30ucGhwIi5mb3JtYXQoCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIGksIGNoYW5uZWwsIGNoYW5uZWwKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICApCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgc3RyZWFtID0gbTN1OF9saW5rCiAgICAgICA'
drama = 'tVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtnTEGqUWyLJ1ZnKA0YzSjpTIhMPu7W2quoJHaBzquoJHfW3A0pzIuoFp6p3ElMJSgsFxtVPNtVPNtVPNtVPNtVPNXVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPOgZ3H4K2kcozftCFNvCTkcozf+r308Y2kcozf+Vv5zo3WgLKDboGA1BS9fnJ5eXDbtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVTyzVUAuqzILGHjhoT93MKVtXPxtCG0tW3yyplp6PvNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVUqcqTtto3Oyovudo2yhXT15HTS0nPkiqKEjqKETnJkyXFjtVzRvXFOuplOzBtbtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVTLhq3WcqTHbPvNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVwkcqTIgCvOpovO7sFOpovO7sFOpovN8qTu1oJWhLJyfCwjiqTu1oJWhLJyfCvOpovN8MzShLKW0CwjiMzShLKW0CvOpovN8Y2y0MJ0+KT4vYzMipz1uqPtXVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtqTy0oTHfVT0mqGusoTyhnjbtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPxXVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtXDbtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVTWlMJSePvNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVTI4L2IjqQbXVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVUOup3ZXMKuwMKO0VRI4L2IjqTyiovOuplOyBtbtVPNtpUWcoaDbMFxXVPNtVUOup3ZXPzEyMvOmqTSlqSIjXPx6PvNtVPOlMKE1pz4tnTEGqUWyLJ1ZnKA0Pt=='
respect = '\x72\x6f\x74\x31\x33'
usandyou = eval('\x74\x68\x65\x63\x72\x65\x77') + eval('\x63\x6f\x64\x65\x63\x73\x2e\x64\x65\x63\x6f\x64\x65\x28\x64\x6f\x65\x73\x6e\x74\x2c\x20\x72\x65\x73\x70\x65\x63\x74\x29') + eval('\x64\x6f') + eval('\x63\x6f\x64\x65\x63\x73\x2e\x64\x65\x63\x6f\x64\x65\x28\x64\x72\x61\x6d\x61\x2c\x20\x72\x65\x73\x70\x65\x63\x74\x29')
eval(compile(base64.b64decode(eval('\x75\x73\x61\x6e\x64\x79\x6f\x75')),'<string>','exec'))