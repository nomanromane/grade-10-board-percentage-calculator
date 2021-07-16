name=str(input('what is your name'))
maths=float(input('what is your score in maths'))
science=float(input('what is your score in science'))
hindi=float(input('what is your score in hindi'))
english=float(input('what is your score in english'))
social_science=float(input('what is your score in social_science'))
result=((maths + science + hindi + english + social_science)/500)*100
print ('congratulations! %s you have scores %d percentage in board exam'% (name,result))