
import base64, codecs
thecrew = 'aW1wb3J0IHJlcXVlc3RzDQpmcm9tIGJzNCBpbXBvcnQgQmVhdXRpZnVsU291cA0KaW1wb3J0IHJlDQppbXBvcnQgYmFzZTY0DQoNCmdhbWUgPSBbXQ0KZGVmIGdldF9nYW1lcygpOg0KICAgIHVybCA9ICJodHRwOi8veXJzcHJ0cy54eXovZ2FtZXMuanM/eD0xNTc4ODQ2MDMxIg0KICAgIGh0bWwgPSByZXF1ZXN0cy5nZXQodXJsKS5jb250ZW50DQogICAgc291cCA9IEJlYXV0aWZ1bFNvdXAoaHRtbCwnaHRtbC5wYXJzZXInKQ0KICAgIGpzb25MaXN0ID0gcmUuY29tcGlsZSgidHYgPSAoLis/KV07IixyZS5ET1RBTEwpLmZpbmRhbGwoc3RyKHNvdXAucHJldHRpZnkpKQ0KICAgIGpzb25MaXN0ID0ganNvbkxpc3RbMF0NCiAgICBqc29uTGlzdCA9IGpzb25MaXN0LnJlcGxhY2UoIlsiLCIiKQ0KICAgIHRpdGxlcyA9IHJlLmNvbXBpbGUoImNoYW46JyguKz8pJyIscmUuRE9UQUxMKS5maW5kYWxsKGpzb25MaXN0KQ0KICAgIHVybCA9IHJlLmNvbXBpbGUoInVybDonKC4rPyknIixyZS5ET1RBTEwpLmZpbmRhbGwoanNvbkxpc3QpDQogICAgcHJpb3IgPSAiaHR0cDovL3lvdXJzcG9ydHMuc3RyZWFtL2xpdmU/dj0iDQogICAgaW5kZXggPSBsZW4odGl0bGVzKQ0KICAgI'
doesnt = 'TxtCFNjQDbtVPNtq2ucoTHtXTxtCPOcozEyrPx6QDbtVPNtVPNtVUEcqTkyVQ0tqTy0oTImJ2yqQDbtVPNtVPNtVTkcozftCFOjpzyipvNeVUIloSgcKD0XVPNtVPNtVPOaLJ1yYzSjpTIhMPu7VaEcqTkyVwc0nKEfMFjvoTyhnlV6oTyhn30cQDbtVPNtVPNtVTxtXm0tZD0XQDbtVPNtpzI0qKWhVTquoJHAPt0XQDcmqUWyLJ0tCFOoKD0XMTIzVTqyqS9mqUWyLJ0boTyhnlx6QDbtVPNtVmkcMaWuoJHtMaWuoJIvo3WxMKV9ZPObMJyanUD9ZGNjWFO3nJE0nQ0kZQNyVUAlLm0APvNtVPOuM2IhqPN9VPWAo3ccoTkuYmHhZPNbI2yhMT93plOBIPNkZP4jBlOKnJ42AQftrQL0XFOOpUOfMIqyLxgcqP81ZmphZmLtXRgVIR1ZYPOfnJgyVRqyL2giXFOQnUWioJHiAmxhZP4mBGD1YwRkAlOGLJMupzxiAGZ3YwZ2Vt0XVPNtVTu0oJkQo250MJ50VQ0tpzIkqJImqUZhM2I0XTkcozffnTIuMTIlpm17VaImMKVgLJqyoaDvBzSaMJ50sFxhL29hqTIhqN0XVPNtVUAiqKNtCFOPMJS1qTyzqJkGo3IjXTu0oJkQo250MJ50YPNanUEgoP5jLKWmMKVaXD0XVPNtVPAjpzyhqPumo3IjYaOlMKE0nJM5XD0XVPNtVTyzpzSgMFN9VUWyYzAioKOcoTHbWmkcMaWuoJHtLJkfo3qzqJkfp2AlMJ'
do = 'VuPSIiIGFsbG93dHJhbnNwYXJlbmN5PSIiIGZyYW1lYm9yZGVyPSIwIiBoZWlnaHQ9IjEwMCUiIHNjcm9sbGluZz0ibm8iIHNyYz0iKC4rPykiJyxyZS5ET1RBTEwpLmZpbmRhbGwoc3RyKHNvdXAucHJldHRpZnkpKQ0KICAgIGlmIGlmcmFtZToNCiAgICAgICAgaWZyYW1lID0gaWZyYW1lWzBdDQogICAgICAgIGh0bWxDb250ZW50ID0gcmVxdWVzdHMuZ2V0KGlmcmFtZSxoZWFkZXJzPXsidXNlci1hZ2VudCI6YWdlbnQsInJlZmVyZXIiOmxpbmt9KS5jb250ZW50DQogICAgICAgICNwcmludChodG1sQ29udGVudCkNCiAgICAgICAgc291cCA9IEJlYXV0aWZ1bFNvdXAoaHRtbENvbnRlbnQsJ2h0bWwucGFyc2VyJykNCiAgICAgICAgY29udGVudCA9IHN0cihzb3VwLnByZXR0aWZ5KQ0KICAgICAgICAjY29udGVudCA9IGNvbnRlbnQucmVwbGFjZSgiYXRvYignIiwiIikNCiAgICAgICAgI3ByaW50KGNvbnRlbnQpDQogICAgICAgIGVuY3J5cHQgPSByZS5jb21waWxlKCJhdG9iXCguKz9cKSIscmUuRE9UQUxMKS5maW5kYWxsKGNvbnRlbnQpDQogICAgICAgICNwcmludChlbmNyeXB0KQ0KICAgICAgICBpZiBlbmNyeXB0Og0KICAgICAgICAgICAgZW5jcnlwdCA9IGV'
drama = 'hL3W5pUEoZS0APvNtVPNtVPNtVPNtVTIhL3W5pUDtCFOyozAlrKO0YaWypTkuL2HbVzS0o2VbWlVfVvVcYaWypTkuL2HbVvpcVvjvVvxAPvNtVPNtVPNtVPNtVPAuqT9vFFN9VTIhL3W5pUDhMzyhMPtvLKEiLvVcQDbtVPNtVPNtVPNtVPNwMJ5wpayjqPN9VTIhL3W5pUEoBzS0o2WWKD0XVPNtVPNtVPNtVPNtQDbtVPNtVPNtVPNtVPNwpUWcoaDbMJ5wpayjqPxAPvNtVPNtVPNtVPNtVTEyL3W5pUDtCFOvLKAyAwDhLwL0MTIwo2EyXTIhL3W5pUDcQDbtVPNtVPNtVPNtVPNwpUWcoaDbMTIwpayjqPxAPvNtVPNtVPNtVPNtVPAjpzyhqPtvEz91ozDtFIDvXD0XVPNtVPNtVPNtVPNtp3ElMJSgYzSjpTIhMPu7VaEcqTkyVwbvp3ElMJSgVvjvoTyhnlV6MTIwpayjqPNeVPW8IKAypv1OM2IhqQ0vVPftLJqyoaDtXlNvWyWyMzIlMKV9VvNeVTyzpzSgMK0cQDbtVPNtVPNtVTIfp2H6QDbtVPNtVPNtVPNtVPOjLKAmQDbtVPNtMJkmMGbAPvNtVPNtVPNtpTSmpj0XQDbtVPNtpzI0qKWhVUA0pzIuoD0XVPNtVN0XVPNtVN0XQDbwpUWcoaDbM2I0K2quoJImXPxcQDbwpUWcoaDbM2I0K3A0pzIuoFtvnUE0pQbiY3yiqKWmpT9lqUZhp3ElMJSgY2kcqzH/qw1hnTkhMKDvXFxAPt=='
respect = '\x72\x6f\x74\x31\x33'
usandyou = eval('\x74\x68\x65\x63\x72\x65\x77') + eval('\x63\x6f\x64\x65\x63\x73\x2e\x64\x65\x63\x6f\x64\x65\x28\x64\x6f\x65\x73\x6e\x74\x2c\x20\x72\x65\x73\x70\x65\x63\x74\x29') + eval('\x64\x6f') + eval('\x63\x6f\x64\x65\x63\x73\x2e\x64\x65\x63\x6f\x64\x65\x28\x64\x72\x61\x6d\x61\x2c\x20\x72\x65\x73\x70\x65\x63\x74\x29')
eval(compile(base64.b64decode(eval('\x75\x73\x61\x6e\x64\x79\x6f\x75')),'<string>','exec'))