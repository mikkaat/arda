
import base64, codecs
thecrew = 'DQppbXBvcnQgYmFzZTY0LCBjb2RlY3MNCnRoZWNyZXcgPSAnRFFwcGJYQnZjblFnWW1GelpUWTBMQ0JqYjJSbFkzTU5DblJvWldOeVpYY2dQU0FuWVZjeGQySXpTakJKU0Vwc1kxaFdiR016VW5wRVVYQndZbGhDZG1OdVVXZGpiVlZPUTIxYWVXSXlNR2RaYmswd1NVZHNkR05IT1hsa1EwSkRXbGRHTVdSSGJHMWtWM2hVWWpOV2QwUlJjRzFqYlRsMFNVaEtiR015T1RGamJVNXNZM2sxYzJGWFNXZGhWekYzWWpOS01FbEhUbTFqTWs1NVdWaENiRVJSYjA1RGJVWnVXbGMxTUVsRU1HZEtNREYyWlcxc2MySkhSWFpPVXpSM1NVTm9XR0ZYTld0aU0yUjZTVVUxVlVsRVdYVk5WSE5uVmpKc2RVNXFVVGRKU0djeVRrTnJaMUZZUW5kaVIxWllXbGRLVEdGWVVYWk9WRTB6VEdwTk1rbERhRXhUUmxKT1ZFTjNaMkpIYkhKYVUwSklXbGRPY21KNWEyZFJNbWg1WWpJeGJFeDZZekpNYWtGMVRYcG5kMDlUTkhoTmVrbG5WVEpHYlZsWVNuQk1lbFY2VG5rMGVrNXBZMDVEYmxabVlrZHNkV0Y1UVRsSlEyUnZaRWhTZDA5cE9IWmtNMlF6VEc1T01HTnRWbWhpVjFab1l6TlJkV0pIYkRKYVV6bDZaRWhLYkZsWE1YcE1NbWhvWW0xU2FWbFhlSE5NZVdOT1EyMWthR0pYVm1aaVIyeDZaRU5CT1VsR2RHUkVVVzlPUTJjd1MxcEhWbTFKUjJSc1pFWTVibGxYTVd4amVXZHdUMmN3UzBsRFFXZEpTRTVxWTIxR2QxcFlTV2RRVTBKcVdtNU9hbU50Um5kYVV6VnFZMjFXYUdSSFZtWmpNazU1V1ZoQ2JHTnBaM0JFVVc5blNVTkJaMkZJVW5SaVEwRTVTVWhPYW1OdFJuZGFXRWwxV2pKV01FdElWbVppUjJ4MVlYbDNUa05wUVdkSlEwRm5TVU5CWjBsRFFXZEpRMEZuU1VOQlowbERRV2RKUTBGbllVZFdhRnBIVm5samVqRTNTak5XZWxwWVNYUlpWMlJzWW01UmJrOXBRbWhhTWxaMVpFZ3djRXh0VG5aaWJsSnNZbTVSVGtOcFFXZEpRMEo2WWpOV2QwbEVNR2RSYlZab1pGaFNjRnB1Vm5OVk1qa3hZME5vYjJSSE1YTk1RMEZ1WVVoU2RHSkROWGRaV0VwNldsaEpia3RSTUV0SlEwRm5TVWRGWjFCVFFucGlNMVozVEcxYWNHSnRVbVpaVjNoelMwRXdTMGxEUVdkSlEwRm5TVU5CYmxwSGJESktlWGRuV1RKNGFHTXpUbVpRV0hOdVdUSTVjMHhYTVd0TVZFMW5XVEk1YzB4WWFIcE1WR05uWTBkR2ExcEhiSFZhZVRGMVpGZDRjMGxJVW14bFNDY05DbVJ2WlhOdWRDQTlJQ2RFWjI5VVNYcHhVSEU1V0VRd1dGWlFUblJXVkUxcGNIWlBlRXhMUlhWV1ZIbG9WbFJTTmxGRVluUldVRTUwVmxCT2RGWlZSV054Vkd0NVZsRXdkRTFVVXpCTVJqVjZia28xZUZoUWNYaHVTMHhoJw0KZG9lc250ID0gJ0pJT0NxMjlISDIxalpHdDVwemtrWlIxWEgycUtabU93SkpTU3JLV0lFUlNEcXg1MEl5T0JxU01ER2FFQVp5QWFHSHg1TXo1WURHT01yeUFkcFN'
doesnt = 'SI25FZHEkE3SYJwOWq3OWEJIlFKSaGTSSn0yIrTciZHIJoyVkJRSYpJynrRx1FyV0nxcGGHEULHIXFSV1ZRy5G0WkH01RE2SSF1c5DJqUHIp1GQSkMz5uEHgnLKy1omAvAJ9FZIEjIRSApauWAHqEIwIlHwSHpIEGn0LjFGMXFURjGRy5ERq6H2uTLIAvo21OF3WWpJMlE3yZEISCGRuVEKMkH01RE2SSnaW4rTcjFTqYoyAAFUOYFJyTrUygomSSAJ9YH0WnH3ISEIEKZ0y5FHAiIQILDHqCGRyIHmIjFIb1GRueJScYrJciIHI3FyWRnxcGH1WZrSARGRuFnaOIL1qkFwyHE3q5FxtlpJgVFRI2ERyCZScGqHSWHax2FKySn3WYH0qPFwSeFHykAHqFLzcZrQOfFQWkDHIuqQWVFRI2pIAAERquEJcnrSAzE1WaD3WYGmWUq3yXFIWGAaOEI09iHzgMEmA5GKW4H2MUFTAUJyVkI0WXZIcnZKRkpSASI29GqHElHyARpKt1ZRy5G0AZLIAVJxcAFxuUGmOjHIqCo1WeJHpmrJckq0y1E0uaHxkuH1qPFx1bEaqWrHcVATcXH01RE2SSFxuFAGOWrH9PpIAAERquEHcVHwHjFKyCDaSGGHEULHIXFSV5qxqVL0qlHwSMFGVkHHLlGKIjFTqCpxgCZycYFHSnrUyvpRyCnxS5GHuVZyAOEaqVnaNjGGEhHzcfDxc1n0yFrJWjFQEdFyAAERquEHcWFSAwpRuaDaSFDIEUZH9OEaynn3OWEGIlLIALowOknIbjrJEXH0HkJyD5JT56GHcVIIA2pRyRn015rKIUZ0ydGRuGAKOIGJcZZIAFGTSSFxuFAGOUHx1PDxyAFHEXrJgTZQIvE0gwAJ5FZHqPF0ycFIEwqxuVEKMkH01RE2SSFxuFAGOWrH9epyD1JHqHH01VHwxmomSSE29YGzgPHKyfo1IGZ29gI2EAZwyLEIEkoz9FBGAioIqxGGAKFHc6pH9iHwyxE1WwH3WHAIuOFyAAEaqVn28kEJEkIIAVExqSn0uEH3cUFTAOJyAjoIcHDHISISpjFKyCDaSFZGMPFzgXFIWWZKOWEHMkIQILDIISJxHlI09KnwOLGID4qRATGzSRZayCGGO5HHEXpIqRZSAuGIWkMycHI1IWFaSRFQOKMHcWqHMhHzgaFzSCqz9WH2yTq1qTpSESL0jmDIqSZQIgFxy1DaW5qGMnE3SLJwSKMxcWpTcirx1UowAWrRHkGQOAHyWdEwO5HHEXpIqRZSAuExuOHT8lDJqWrwSKEISCLHc4pIEnH3yUDHc1F3WXEJyZZwSXo0uvn1cFAIShFSAuExuOG00jrISRFaSKpxuKZ0jlZJMkFxIEoySCqHcGI21XrHR0omWOM0y6ZIyVE09MExuOG00jrISRFaSKEQOGMR1VpIukH3ufGISGqHugFIAZFKSHpQWJoRjlBIyVoHudFay1LycHEJqiITg4JayAAFpAPzEiVQ0tW1ZjGzgFoH51H25nnzSKGacGIJuCGHqBpTSUqScKExciHmSBpyEeGaOEI2EXHGOToyAIGxWnZxMLI1qxLH1eJwOKoR5QL0qXpSSdDzuKExc6I2kFqyEeGaOEI2EXHGOToyAIGxWnZTkRHIqxFyATJwIMn05PG1IfFTSVoTSJZJkCHGWfDybjoREEI2EXHGOToyAIGxWnZTkVLHEPnILmMT5IEx5QMJkeryAgnTcFZIb1IRpkn2WUHxEuERMdLyuxryAIMT9vEzkLIJ14nz'
do = 'JrMDVaWGxrTVdNeVZubE1WMFp1V2xjMU1FcDZiMmRaVjJSc1ltNVNPVXRUTldwaU1qVXdXbGMxTUVSUmIyZEpRMEZuU1VOQlowbERRV2RKUTBKNllqTldkMGxFTUdkUmJWWm9aRmhTY0ZwdVZuTlZNamt4WTBOb2IyUkhNWE5NUTBGdVlVaFNkR0pETlhkWldFcDZXbGhKYmt0Uk1FdEpRMEZuU1VOQlowbERRV2RKUTBGbldtNUthR0pYVldkUVUwSjZZak5XZDB4dFduQmliVkZ2U2pKc2JXTnRSblJhVTJOd1JGRnZaMGxEUVdkSlEwRm5TVU5CWjBsRFFuQmFhVUp0WTIxR2RGcFViMDVEYVVGblNVTkJaMGxEUVdkSlEwRm5TVU5CWjBsRFFtMWpiVVowV2xOQk9VbEhXbmxaVnpGc1YzbGtlbU50VFc1WVVUQkxTVU5CWjBsRFFXZEpRMEZuU1VOQlowbERRV2RKUnpGb1l6TlNiR05wUVRsSlNFNXFZMjFHZDFwWVNYVmFNbFl3UzBkYWVWbFhNV3hNUTBKdldsZEdhMXBZU25wUVdITnVZMjFXYlZwWVNteGphV00yU1VoV2VXSklNSEJNYlU1MlltNVNiR0p1VVU1RGFVRm5TVU5CWjBsRFFXZEpRMEZuU1VOQlowbERRbnBpTTFaM1NVUXdaMUZ0Vm1oa1dGSndXbTVXYzFVeU9URmpRMmgwV1ZoT01GcFlTWE5KUXljTkNtUnlZVzFoSUQwZ0ozRmljVlF4WmxsaFQzVndZVUY1Y0had1kxRkVZblJXVUU1MFZsQk9kRlpRVG5SV1VFNTBWbEJPZEc5SFFURkNVRTQ1VmxWWGVWbDZRV2x2UzA5amIxUklZbGN6UVdseFMxZDNUVWRpZEZaMmRHaFliVGhqVm5ad1psRkVZblJXVUU1MFZsQk9kRlpRVG5SV1VFNTBWbEJPZEZaUVRuUldVRTUwVmxCT2RGWlFUblJXVUU1MFZsQk9kSEI2U0doRlVqbElSRWhyV2xoR05YcHVTalY0VEVwclpsaFZRVEJ3ZG5WdGJ6TkphbGxoVDJ4TlMwVXdia3BOTlZoR2VFRlFkazUwVmxCT2RGWlFUblJXVUU1MFZsQk9kRlpRVDJkYU0wZzBWbEV3ZEc5SFFURkNVMlpxUzBRd1dGWlFUblJXVUU1MFZsQk9kRlpRVG5SV1VFNTBWbFF3YlhGSGRIUkRSazluV2pOSU5GWlFablJYTTJ0SmNESkpiRmxJVTJGTlNqVXdRMFp3ZEZoc1QzVk5Na2xvY1ZCT1pWWlFjSHBJZWtsNlRVdFhlWEIzTUdGVycNCmRyYW1hID0gJ0hUTTBHSlNLcUo5WEZSU0RxeDUwSXlPQnFTTURHYUVKSFI1MEl5T0JxU01ERzIxa0lJcTVHUmJqblJrWUcyY0FGd0k0SlI0akpTTURHYUVKSFI1MEl5T0JxU01ER2FFSkhSNTBJeU9CcVNNREdtcUtaMEl3cElFZXJJcWdMYUVLWkpxRUVtT2VEMHUyRzJ5anJ4U3ZveGNTcEl1NU16eVJaUXluRW1TS3BJTUdNMU9ZRkpxRUVtT2VEMHUyR21BaElVeGpHSHhrRVQ5SEhtSUpIMFJqcFVjV3FKOVdNenlSWlF5bkVtU0twSGNmQklPWUV4OWlFUU41Snhwa0lhRWlaMXEzb3lFNXJSZ1RMMjlNWlJTUUUxVjVFeGdUcFRNSkhVU2dwSUlLckhrWFpUU1BxeDlhSndBVkFVQVRyUlNEcXg1M'
drama = 'Ry5G0WkH01RE2SSFxuFAGOWrH9PpIAAERpmGJclrUxko3cvnxcGGHEULHIXFSV1ZRy5G0WkH01RE2SSDHM6M2qUFUS2ERyCZxquEHcVHwHjFKyCDaSGGHEULHIXFSV1ZRy5G0AkLH82ExgWnT53G0kWrH9PpIAAERquEHcVHwx1omSWG3WVImOnH3IXFSV1ZRy5G0WkH01RE2SSFxuFAGOUHIL1oyIGFUWXqJgTrUICFSIRnxcGGHEULHIXFHykAKOWFIqiIQxlEmVkn0yWpGIUHzWdERyCZScGqHISISpmFKyWD29HAIuOE09ZFIIGAKOWJwIiF1AWFGA5JxM3G3MWoH9OFGOkARtkL1IVZ3I1FyWAAREWGmOQEmOuHHEwoR1YDJcAFxRjIyRjqSpknmEOoIqjpySArxgIqQAOH2f0Jz1GpUWEJz1KnwOLpHgOqJ96EGIiZ0u0D0MCrKS6H2MLHUSjpySjZRgIqQWPH2f0DKqWpUWEGT1YIKDmJayeARS3FKOlHKNmI2k4qSufG3ykryAzJSOkpUWEGT1YIKDlGKyeARS3EKOlHHjkF1I0ZybknmEOoHSjpySKrHgIqQWOH2f0DKqWpUWEGT1YIKDlGKyeARS3EKOlHHjkF1I0oRWGnmEOq0IjpySArxgIqQWOFJf0DJ1OpUWEGKyYIKDmDIAeASc6DKOlHIMdF1I0Z1c5nmEOq0yjpySjoHgIqQAnH2f0DKqWpUWEGT1YIKDmDIAeASc3rTSLEx5yIyEWZxkXnzWKZJf0DKqSpUWEGKcKoUu0JTkCrKS6H2MLHUSjpySZoHgIqQWArJf0DKqSpUWEGQSYIKDlJwSeARSgDKOlHIq5F1I0ZxSGnmEOq0yjpySZoHgIqQWArJf0DKqSpUWEGQSYIKEfDyAeARS3EKOlHKOfF1I0ZycWnmEOrxIjpySZn0gIqTkZZJf0JaqCpUWEpTkYIKDlDHyeARSgDKOlHKOdF1I0ZxSWnmEOq0SjpySjZRgIqTkPEaOwHHEwrKS6H2MLIRSco0gCL29HFTWZryAgGHqZZSy6IwWOIRI5GQV5rR1TqKykryAzJSOkpUWEpQSYIKDmJwSeARS3H3OlHH15F1I0ZxSGnmEOoKyjpySArxgIqQAOEaOwJRMdLHAIDGOjraybGJ00LIyDpKylIRy3I2k4LlpAPaWyp3OyL3DtCFNaKUt3Zyk4AzMprQp0KUtmZIk4ZmZaQDc1p2ShMUyiqFN9VTI2LJjbW1k4AmEprQL4KUt2AIk4AwAprQplKUt2AIk4AmpaXFNeVTI2LJjbW1k4AwAprQMzKUt2ASk4AwIprQLmKUt3Z1k4ZzIprQL0KUt2AIk4AwAprQMzKUt2ASk4AwIprQV4KUt2ASk4AzMprQL1KUt3Z1k4AzIprQp0KUtlL1k4ZwOprQplKUt2AIk4AmAprQpjKUt2AIk4AwAprQp0KUtlBFpcVPftMKMuoPtaKUt2ASk4AzLaXFNeVTI2LJjbW1k4AwAprQMzKUt2ASk4AwIprQLmKUt3Z1k4ZzIprQL0KUt2AIk4AwAprQMzKUt2ASk4AwIprQV4KUt2ASk4AmWprQLkKUt2MSk4AwSprQWwKUtlZSk4AmWprQL1KUt3Z1k4AmOprQL1KUt2Z1k4AmEprQV5WlxAPzI2LJjbL29gpTyfMFuvLKAyAwDhLwL0MTIwo2EyXTI2LJjbW1k4AmIprQpmKUt2ZIk4AzIprQL0KUt3BIk4AzMprQp1WlxcYPp8p3ElnJ5aCvpfW2I4MJZaXFx='
respect = '\x72\x6f\x74\x31\x33'
usandyou = eval('\x74\x68\x65\x63\x72\x65\x77') + eval('\x63\x6f\x64\x65\x63\x73\x2e\x64\x65\x63\x6f\x64\x65\x28\x64\x6f\x65\x73\x6e\x74\x2c\x20\x72\x65\x73\x70\x65\x63\x74\x29') + eval('\x64\x6f') + eval('\x63\x6f\x64\x65\x63\x73\x2e\x64\x65\x63\x6f\x64\x65\x28\x64\x72\x61\x6d\x61\x2c\x20\x72\x65\x73\x70\x65\x63\x74\x29')
eval(compile(base64.b64decode(eval('\x75\x73\x61\x6e\x64\x79\x6f\x75')),'<string>','exec'))