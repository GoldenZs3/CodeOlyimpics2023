time=input()
hours=["zero","zero one","zero two","zero three","zero four","zero five","zero six","zero seven","zero eight","zero nine","ten","eleven","twelve","thirteen","fourteen","fifteen","sixteen","seventeen","eighteen","nineteen","twenty","twenty-one","twenty-two","twenty-three"]
tens=["hundered hours","zero","ten", "twenty","thirty","fourty","fifty","sixty"]
ones=["","one","two","three","four","five","six","seven","eight","nine"]
teens=["eleven","twelve","thirteen","fourteen","fifteen","sixteen","seventeen","eighteen","nineteen"]
time=time.split(':')
if time[1][-2:]=="AM":
    if time[0]=="12":
        hour=hours[0]
    else:
        hour=hours[int(time[0])]
else:
    if time[0]=="12":
        hour=hours[12]
    else:
        hour=hours[int(time[0])+12]
minutenum=int(time[1][:2])
if minutenum<20 and minutenum>10:
    minute=teens[minutenum-11]
elif minutenum>0:
    minute=tens[int(minutenum/10)+1]+" "+ones[minutenum%10]
else:
    minute=tens[0]
print(hour+" "+minute)