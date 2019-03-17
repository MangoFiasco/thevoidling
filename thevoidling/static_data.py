from thevoidling.models.roles import *
from thevoidling.models.ranks import *
from thevoidling.models.tiers import *


from thevoidling import db

db.session.query(Roles).delete()
db.session.query(Ranks).delete()
db.session.query(Tiers).delete()

data = Roles(
    role="MIDDLE"
)
db.session.add(data)
data = Roles(
    role="TOP"
)
db.session.add(data)
data = Roles(
    role="JUNGLE"
)
db.session.add(data)
data = Roles(
    role="CARRY"
)
db.session.add(data)
data = Roles(
    role="SUPPORT"
)
db.session.add(data)
#############################################
data = Ranks(
    name="I"
)
db.session.add(data)
data = Ranks(
    name="II"
)
db.session.add(data)
data = Ranks(
    name="III"
)
db.session.add(data)
data = Ranks(
    name="IV"
)
db.session.add(data)
############################################

data = Tiers(
    name="IRON"
)
db.session.add(data)
data = Tiers(
    name="BRONZE"
)
db.session.add(data)
data = Tiers(
    name="SILVER"
)
db.session.add(data)
data = Tiers(
    name="GOLD"
)
db.session.add(data)
data = Tiers(
    name="PLATINUM"
)
db.session.add(data)
data = Tiers(
    name="DIAMOND"
)
db.session.add(data)
data = Tiers(
    name="MASTER"
)
db.session.add(data)
data = Tiers(
    name="GRANDMASTER"
)
db.session.add(data)
data = Tiers(
    name="CHALLENGER"
)
db.session.add(data)

db.session.commit()