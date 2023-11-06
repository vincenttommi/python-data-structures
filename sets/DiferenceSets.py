""""


The difference() method returns a set that contains the difference between two sets. The returned set contains items that exist only in the first set, and not in both sets.


"""

clubs  =set(["Manchester-United","Arsenal","Chelsea","Manchester-City",])

clubsb = set(["Everton","Manchester-United","Liverpool","Totehnam"])


allcubs =  clubs - clubsb
print(allcubs)