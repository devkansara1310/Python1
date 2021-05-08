#auto story generator 

import random
when = ["A few years ago", "Yesterday", "Last Night", "A long time ago","On 23th Feb"]
who = ["Maxwell","Elle","Hannah","Jhon"]
residance=["India","England","USA"]
went= ["cinema", "university", "hotel", "mall", "food court"]
happened = ["made a lot friends","Eats a burger","found car","wrote book","solved sum"]

print(random.choice(when) + ',' + random.choice(who)+' that lived in '+ random.choice(residance)+",went to the "+random.choice(went)+" and " + random.choice(happened))
