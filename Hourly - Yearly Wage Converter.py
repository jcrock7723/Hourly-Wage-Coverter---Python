#Hourly wage converter

#Input
#Get hourly wage
hourly_wage = float(input('What do you make an hour? '))

#Get desired hourly wage
des_wage = float(input('What would you like to make an hour? '))

#Processing
cweekly_wage = (hourly_wage*40)
dweekly_wage = (des_wage*40)

cYearly = (cweekly_wage*52)
dYearly = (dweekly_wage*52)

hour_diff = (des_wage - hourly_wage)
weekly_diff = (dweekly_wage - cweekly_wage)
yearly_diff = (dYearly - cYearly)

perc_wage = ((cYearly/dYearly)*100)

#Output
print('You make approximately $', format(cYearly, '.2f'), ' per year.', sep="")
print('You would like to make $', format(dYearly, '.2f'), ' per year.', sep="")
print('That is a difference of $', format(yearly_diff, '.2f'), ' per year, or $', \
      format(hour_diff, ',.2f'), ' per hour.', sep="")
print('In other words you made about ', int(perc_wage), '% percent of what you wanted to make.', sep="")
