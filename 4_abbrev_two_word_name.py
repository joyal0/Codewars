#Abbreviate a Two Word Name
"""
Write a function to convert a name into initials. This kata strictly takes two words with one space in between them.

The output should be two capital letters with a dot separating them.

It should look like this:

Sam Harris => S.H

patrick feeney => P.F

STRINGSFUNDAMENTALS"""
#Solution
def abbrev_name(name):
    t=0
    abbrev = name[0].upper() + '.'
    for i in name:
        if i==' ':
            t=1
        elif t==1:
            res = abbrev + i.upper()
            t=0
            break
    return res
#OUTPUTS
"""
Time: 721ms Passed: 205Failed: 0
Test Results:
Fixed Tests
Basic Test Cases
 (5 of 5 Assertions)
Completed in 0.21ms
Random Tests
Testing for abbrev_name(YflnZfXsOfep UnvIOrp)
Testing for abbrev_name(lRcPjGhwLJKuqgnf ZFobRHFMHPL)
Testing for abbrev_name(KVJps pzGOBqIeYa)
Testing for abbrev_name(szKtLJgwNLZEz LtmRIIRNyH)
Testing for abbrev_name(RQJzliBOyoxDNdxRnK NmSGtIZhaf)
Testing for abbrev_name(hiBxiHVU hqdKTGj)
Testing for abbrev_name(ByMx ZxvFwFYVP)
Testing for abbrev_name(MRtjqXaKnnOKmAPDxw auMCxwCXBUNhldD)
Testing for abbrev_name(OTTncC MXJZjqHL)
Testing for abbrev_name(nT f)
Testing for abbrev_name(KrWfONUqKsuOjOrqQKl BfdDgfK)
Testing for abbrev_name(c zzrbnNIHnhLQ)
Testing for abbrev_name(SFTXAlWNwRzAXcen MnRIv)
Testing for abbrev_name(WCY tQzvUmobjcrfiK)
Testing for abbrev_name(HZJGDrbDtCrHXWcrpW IZAsmJRzvGvhENRNNc)
Testing for abbrev_name(rMKPPs EOpMkxcxL)
Testing for abbrev_name(rvpqxOrnLtSNOCrnL YJQyISfazvEtNV)
Testing for abbrev_name(dfuECDogKgJNuQoHmJiC nbmVIWutzIuWCLSNBFl)
Testing for abbrev_name(PMjhBlhPRrQXRSN UCIYmAcLJFSMHsTl)
Testing for abbrev_name(qamHeeZu HtzeGLRGNkhlTKGF)
Testing for abbrev_name(XYqAokNxWblhlNYihw yoWGCTrmwq)
Testing for abbrev_name(Stb IdipMLxyTmCheBBePwWQ)
Testing for abbrev_name(GGJoBt WyYvQIApdFOFhYVpO)
Testing for abbrev_name(ICtkH U)
Testing for abbrev_name(JilTWJexazvZZicLYGiM B)
Testing for abbrev_name(TcD v)
Testing for abbrev_name(tafhIptY guqReqCGeHshm)
Testing for abbrev_name(JHpBGfyDbhPOftmZpWg WzJ)
Testing for abbrev_name(IzQcAeglSREM QfPAOWNYpSoFju)
Testing for abbrev_name(lpYbMEWAuNEsdfTascNT FaSfaZxDRmuMSo)
Testing for abbrev_name(ljc ry)
Testing for abbrev_name(ms bHJsjfviKbdY)
Testing for abbrev_name(QLCdgnZEiFaEdkjK CiWoZDGzWCTptobYLQet)
Testing for abbrev_name(BcdHaRvvtnAmcBnh yJ)
Testing for abbrev_name(OIxHvbeWOKgQhhMFB SlznraIe)
Testing for abbrev_name(CvYzcdGiIVSQQB iykvsxkorJZQQMAPjiH)
Testing for abbrev_name(ZLuVcUkdhRe PKJNmjm)
Testing for abbrev_name(s NvPmEj)
Testing for abbrev_name(naaerLAG AAqWCWsGJJkXOEN)
Testing for abbrev_name(rBvPnHr VKstuoRMiuOtxfsCgShi)
Testing for abbrev_name(VmRRTJFEPUUeDmoaVxoL MNizUEF)
Testing for abbrev_name(hiN czIp)
Testing for abbrev_name(IYTFgM mcTaaeOIwXeyLbci)
Testing for abbrev_name(xvSjkvVEjtjW GlS)
Testing for abbrev_name(XzNepstcBS GI)
Testing for abbrev_name(aSvGdaGHVIOLEOe qUJvuXGxReasM)
Testing for abbrev_name(KyASRZPHqqvOEcdVtB vP)
Testing for abbrev_name(ZEtTdlDzaMnaM avVXoUGgAVdu)
Testing for abbrev_name(cXNOuEv XnkKD)
Testing for abbrev_name(PRfnosiLVkTsNBKy EiReFc)
Testing for abbrev_name(v SfuQDGTPnKfyFl)
Testing for abbrev_name(uwxYBgswOUKsMAUeFRC JTdWQvtUc)
Testing for abbrev_name(WHT l)
Testing for abbrev_name(lEPIhM cOXuiGjqEmfAy)
Testing for abbrev_name(SIZxxmvyfbLEnePiJUi lzAgtpDLUmutUWS)
Testing for abbrev_name(udUbMxzwADT ZRmeKbEUU)
Testing for abbrev_name(WynsS MsWralttcA)
Testing for abbrev_name(ocmIsWgbvntlq HmKJnyyvqDZX)
Testing for abbrev_name(tBpci kSzQjSx)
Testing for abbrev_name(iUFgZzvVap f)
Testing for abbrev_name(wrnKicMstcm LEttgrJEzrGNXiHZnxtX)
Testing for abbrev_name(CcqiYzEuWj FLjuCw)
Testing for abbrev_name(dF EimsHWsIEpOSfLBU)
Testing for abbrev_name(gBaKCAlBVECvgn icGerZyQx)
Testing for abbrev_name(yiTMJfSPpPFFKfdW rCFYfsAFos)
Testing for abbrev_name(xi tsREECReymODxPC)
Testing for abbrev_name(UwVe mnH)
Testing for abbrev_name(pisbOp TLxZK)
Testing for abbrev_name(GkbTMMftyXivIXyka hBdpkigCcSx)
Testing for abbrev_name(AABhJW ZDgTrMmSXlXl)
Testing for abbrev_name(KBQPLgXoL fBOyIgvBcuW)
Testing for abbrev_name(AMSD OiJJYRofKhgDJuG)
Testing for abbrev_name(PfHJUrMBZJPoNslGiZus PRc)
Testing for abbrev_name(hkZGGBgKyICIbHADqJ sq)
Testing for abbrev_name(zGofQsidPD MXoT)
Testing for abbrev_name(aZzkzuJWQLj uoz)
Testing for abbrev_name(WWpTiXtqyYBdX zNRZloYTHMZtcEjmmy)
Testing for abbrev_name(qXVoyNE PPlZYlj)
Testing for abbrev_name(H qYHFNKNz)
Testing for abbrev_name(qvdeXLpjYxyIClM r)
Testing for abbrev_name(sUkRq c)
Testing for abbrev_name(WlnyoivJ bcrhuORbCRCRGzGV)
Testing for abbrev_name(bzzOCkUd uxhfGZsSgPCvSjUU)
Testing for abbrev_name(Ua c)
Testing for abbrev_name(XKW FUkuIHNXlTyJAVwmKXX)
Testing for abbrev_name(SlroBFryepBIdfIKi rwwaPUjfjWORuxjNgwmK)
Testing for abbrev_name(ebH AhlUe)
Testing for abbrev_name(zmJsUK OMzMbzyBrPmz)
Testing for abbrev_name(Jdkb IMMopHondfWuVbw)
Testing for abbrev_name(gcQPKcxmXluSOxt SnsEULtSfuAWpc)
Testing for abbrev_name(KINuqgDeJONY aq)
Testing for abbrev_name(svPNjBcpMfsCgkVBYh kPLqgwhKTyrHUzeJ)
Testing for abbrev_name(JLA jUtOV)
Testing for abbrev_name(XqRBAvslSm WeAZTBrdzOycjRZoCFFn)
Testing for abbrev_name(zZoPLlRfzxYHhGNWfPO hEYRACGbbBhxWbriy)
Testing for abbrev_name(JHSDWLPRTpbGSbe lPHzMWsmbWTMNrsp)
Testing for abbrev_name(lLFIUOAwsVzQcdkJm BQXxiek)
Testing for abbrev_name(XxjRkrlY bUeJKCizEmDvv)
Testing for abbrev_name(FB glIvHicHniCbsXKzm)
Testing for abbrev_name(nnqTwJheKK PVhke)
Testing for abbrev_name(WZIzubQeTwNGVAGg eBvnSQXNOzdsmvoZdeB)
Testing for abbrev_name(QdmsSregsEowWsxRMY aAmIXPJkQwDIodUCgx)
Testing for abbrev_name(MuzndvG QzFOiy)
Testing for abbrev_name(sevGNUKZNT ZdLpsryPuHMTmIrm)
Testing for abbrev_name(LExyCFuFDW bGhMmslHvtVRGwBg)
Testing for abbrev_name(fGXK eMuLStStTXCxsksjRiW)
Testing for abbrev_name(nb HhxRX)
Testing for abbrev_name(eZPMtpyO VIIIDMMZMgSNIZhr)
Testing for abbrev_name(bpQCquIyPWaVrDQJdEy zvLSkOUIErr)
Testing for abbrev_name(RqxDjGd ixKieXlfjzDhjcpx)
Testing for abbrev_name(UayJq lTTgBj)
Testing for abbrev_name(aqOYhCIrdPVpYvUMlR tx)
Testing for abbrev_name(RPh FP)
Testing for abbrev_name(hIj KVYjmvYEdEiaYc)
Testing for abbrev_name(HoB d)
Testing for abbrev_name(T slKgBqfcrcXKlNMnWUDK)
Testing for abbrev_name(chaIsRZNmNWLrNnE TKfhPsgrjUxKXY)
Testing for abbrev_name(BxUKJn BeKLbvfDxCkHMf)
Testing for abbrev_name(UElALjPQTC t)
Testing for abbrev_name(EeXyDcqmsFJKPcvmTILp ygZxsvQMp)
Testing for abbrev_name(fDTNjEkQZcD tXavQsGRlIJBdV)
Testing for abbrev_name(tXgjhOqNbeqplYej aksNKgJKBVnps)
Testing for abbrev_name(UCpLUDADYVtYFlbRhQKi SzC)
Testing for abbrev_name(TYoGdZhUihCAl vSJ)
Testing for abbrev_name(SOqZzTGUqgnuVkMQmEY bPqoUdPthyCc)
Testing for abbrev_name(fUDGAnwzuVWNWw ZynPGJALCeMQPjBKXCcB)
Testing for abbrev_name(jU XRutYvl)
Testing for abbrev_name(CqFMNYnnvDKFkAEu fnPBVFAdtISLSFvBosK)
Testing for abbrev_name(fhJel QlNVJPdBpBFwVGveF)
Testing for abbrev_name(uFko LByt)
Testing for abbrev_name(veswUDCMPeLyMOMGwuv tVmCR)
Testing for abbrev_name(mLHnsWBqcB ePnoxWQnFkkFXnKJTo)
Testing for abbrev_name(h fjuEnSBpbcOJUwptvyd)
Testing for abbrev_name(LOyk uzJm)
Testing for abbrev_name(OMeO QwXXQlqJLVb)
Testing for abbrev_name(tfmhPxxdIdlNkbN mvQagyMWBv)
Testing for abbrev_name(PQdOovEVMYDrAmlPHngs UBzloWDbTMIcDChCa)
Testing for abbrev_name(DJOCOky sAHKET)
Testing for abbrev_name(nxmLRsjToLm VYjJ)
Testing for abbrev_name(YBfAESnbfNaFnFCpvCFJ wXUktIJo)
Testing for abbrev_name(PAmcdtLfvT gEdx)
Testing for abbrev_name(evRzkQIiKHK bWfkYKrjPgCDXunHcCTO)
Testing for abbrev_name(lrC FjSPIsUKrNXTksyumzz)
Testing for abbrev_name(ag scGtfhzvJUZTimEl)
Testing for abbrev_name(PZGNNVJKxZ xIjTH)
Testing for abbrev_name(LROIXBKXAprmXSCo BNhavFGFfNlglIsVRXSi)
Testing for abbrev_name(wkfpPly oHOMsSmKqHWFsYqkp)
Testing for abbrev_name(cSGTgjvLAXhQf HLMGMBSFgfPL)
Testing for abbrev_name(MwBU JgacIqfARAPqboveSJ)
Testing for abbrev_name(ZygxHuxbkskNbsnnIiyJ pxvsIFQeRUHBvA)
Testing for abbrev_name(rQG a)
Testing for abbrev_name(KChVGZnqVrXxWpZYmAUK JbzQNyhOpdjwWdb)
Testing for abbrev_name(RmTmbHvEyHx cToxHvKKCWoAfROr)
Testing for abbrev_name(alEnSLtqCqfwBIDYMBOT C)
Testing for abbrev_name(flanCniz YoQxcdGfuYjoWKlN)
Testing for abbrev_name(ojJAqdOmUN Oo)
Testing for abbrev_name(rZI m)
Testing for abbrev_name(vApAsEcbhRKgyzj GSEtnYRtSJZuJ)
Testing for abbrev_name(OuOYsuhJlWEF nCguFpOYmTSEbJkmZO)
Testing for abbrev_name(bhETYRFpOUvfg DyJzeCYQLBBsajsmkAd)
Testing for abbrev_name(WvKnwCuwMoZcSeLD kDHKCJgKYQcvZb)
Testing for abbrev_name(LULZX KqRh)
Testing for abbrev_name(oIjZx jKrnpHUQ)
Testing for abbrev_name(aFfRylCSlvdqMDkYwUOp yBWknvQxtKpPzRIgg)
Testing for abbrev_name(FIsBr oLCDdPPXgrT)
Testing for abbrev_name(gmNtXvmbdqMBeqWTkzhD ZyQfaDDaFLGWcDODhzp)
Testing for abbrev_name(WTuUpISBrBlQ puEvfioHw)
Testing for abbrev_name(ZkJOUYKBOr DQSFgk)
Testing for abbrev_name(pwUrthnUbwVOfCCliF LQeWpwYRn)
Testing for abbrev_name(DBkGaGc xOxjEmezYgJgqETZy)
Testing for abbrev_name(vuwvsgcyFStl RAhZbNYhejbtL)
Testing for abbrev_name(NmqirLhYKEGeDmDrHvXG xOIUcgiTJGSbll)
Testing for abbrev_name(NSrgRMtbmaoQIhAkKsP RXbifhIPaW)
Testing for abbrev_name(iYnbszFcJKDidMDRvTb HyUywwCvByIZjjFDGYg)
Testing for abbrev_name(FjTXAxxMrEPX lDWXGvycnwrvupxFm)
Testing for abbrev_name(PFYzTZuKzLexxVekjUbX WOyr)
Testing for abbrev_name(gQRkfl SiqurP)
Testing for abbrev_name(yi dcMiBXizEgGEYPmM)
Testing for abbrev_name(bmZwyIylyY QXbrwPuhTgV)
Testing for abbrev_name(qHhgvQdtGVTMeOZ YJyKhXK)
Testing for abbrev_name(HEFyoe UD)
Testing for abbrev_name(VALyMSvLYQgHH pnxTBbMpHqxuaUJseivs)
Testing for abbrev_name(vyJwjSUdyyMrNfbUF GkxQgWW)
Testing for abbrev_name(MAANBgkdvFnuyR PVoWGSxX)
Testing for abbrev_name(xsOVAtxznWhkrejfRN jgzDRwg)
Testing for abbrev_name(hDzXZJVyEOilXBJOSOb QPm)
Testing for abbrev_name(SoMMLdHEABUHiepRuOrj FoRBqqoHWzCplfjpagsP)
Testing for abbrev_name(eZzFQALHnOcEf efZoPVUFZjnbYH)
Testing for abbrev_name(VziFaq fhCLQZBK)
Testing for abbrev_name(fKab bwEC)
Testing for abbrev_name(lcgiQKLzF jZiWZIB)
Testing for abbrev_name(FMGCwrg QmcObNX)
Testing for abbrev_name(VVGULQauBgxunI UnYYzWkHRVolSK)
Testing for abbrev_name(bRNzwwFAPSvJDuv rBmsV)
Testing for abbrev_name(Uhmdko OMVkG)
Testing for abbrev_name(IqtVvopjindszjfvv zguZH)
Testing for abbrev_name(B EznhQoD)
Testing for abbrev_name(fsvxxMyMJHhBg a)
Testing for abbrev_name(tuEBaivyMJL bcmkMQVvHNzqDcDnU)
Testing for abbrev_name(fdsWKJDGIrRnvyPqqxV NFh)
Completed in 24.38ms
You have passed all of the tests! :)"""
#alternate solutions
def abbrevName(name):
    return '.'.join(w[0] for w in name.split()).upper()
#alternate solutions
def abbrevName(name):
    first, last = name.upper().split(' ')
    return first[0] + '.' + last[0]
#alternate solutions
def abbrevName(name):
    names = name.split()
    return f"{names[0][0]}.{names[1][0]}".upper()
#alternate solutions
def abbrevName(name):
    return name.split(' ')[0][0].upper()+'.'+name.split(' ')[1][0].upper()
#alternate solutions
def abbrevName(name):
    first_initial = name[0]
    for letter in range(len(name)):
        if name[letter]  == ' ':
            last_initial = name[letter + 1]
          
    return (first_initial.upper() + "." + last_initial.upper())
#alternate solutions
def abbrevName(name):
    x = name
    y = name.split()
    return y[0][0].upper() + "." + y[1][0].upper()
#alternate solutions
def abbrevName(name):
    return '.'.join(x[0].upper() for x in name.split())