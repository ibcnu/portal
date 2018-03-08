import sys
from django.contrib.auth import authenticate
from django.contrib.auth import get_user_model

User = get_user_model()

#  Update the users in this list.
#  Each tuple represents the fullname, username, and password of a user.
users = [
    ('Barry Huffman', 'barry.huffman@cmssi.com', 'test1234'),
    # ('Brent Sylvester', 'brent.sylvester@cmssi.com', 'test1234'),
    ('Ernie Boucher', 'ernie.boucher@cmssi.com', 'test1234'),
    ('Derek Heinz', 'derek.heinz@cmssi.com', 'test1234'),
    ('Peter Villella', 'peter.villella@cmssi.com', 'test1234'),

    ('Tina Lahtinen', 'tlahtinen@thunderbay.ca', 'test1234'),
    ('Juli Rucchetto', 'jrucchetto@thunderbay.ca', 'test1234'),
    ('John Morassutti', 'John@email.com', 'test1234'),
    ('Mark Andrychuk', ' mark.andrychuk@airliquide.com', 'test1234'),
    ('Hal Lightwood', 'hal.lightwood@tbaytel.com', 'test1234'),
    ('Shelley Whiteman', 'shelley.whiteman@tbaytel.com', 'test1234'),
    ('Cathy Slyford', 'cathy.slyford@brinksinc.com', 'test1234'),
    ('Rob Parker', 'rparker@toromont.com', 'test1234'),
    ('Dave', 'dave@email.com', 'test1234'),
    ('Joshua Claeys', 'Joshua.Claeys@brookfieldgis.com', 'test1234'),
    ('Brad Rissanen', 'brissanen@superiorelevator.ca', 'test1234'),
    ('Gerry Erb', 'gerb@erbgroup.com', 'test1234'),
    ('Richard Matheson', 'cruise10@shaw.ca', 'test1234'),
    ('Al Clarke', 'al.clarke@greenstone.ca', 'test1234'),
    ('Claude Marcotte', 'claude.marcotte@brookfieldgis.com', 'test1234'),
    ('Susan Fagan', 'susan.fagan@enbridge.com', 'test1234'),
    ('Dave Petrick', 'DPetrick@canop.ca', 'test1234'),
    ('Francis', 'francis@haydroone.com', 'test1234'),
    ('Balmoral Park Acura', 'john@acura.com', 'test1234'),
    ('Paul Mignault', 'pmignault@tbcdsb.on.ca', 'test1234'),
]

for username, email, password in users:
    try:
        print('Creating user {0}.').format(username)
        user = User.objects.create_user(fullname=username, email=email)
        user.set_password(password)
        user.save()

        assert authenticate(username=username, password=password)
        print('User {0} successfully created.').format(username)

    except:
        print('There was a problem creating the user: {0}.  Error: {1}.').format(username, sys.exc_info()[1])
