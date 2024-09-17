# list of backpacks
# https://helldivers.fandom.com/wiki/Stratagem_Codes_(Helldivers_2) 

# Mission Stratagems
mission_stratagems = ['Reinforce', 'SOS Beacon', 'Resupply', 'Hellbomb',
                      'SSSD Delivery', 'Seismic Probe', 'Upload Data', 
                      'Eagle Rearm', 'SEAF Artillery', 'Super Earth Flag']
# Supplies
backpacks = ['Jump Pack', 'Supply Pack', 'Guard Dog Rover', 
             'Ballistic Shield Backpack', 'Shield Generator Backpack',
             'Guard Dog']

support_weapons = ['Machine Gun', 'Anti-Material Rifle', 'Flamethrower', 
                   'Stalwart', 'Expendable Anti-Tank', 'GR-8 Recoilless Rifle',
                   'Flamethrower', 'Autocannon', 'Heavy Machine Gun', 
                   'Railgun', 'Spear Launcher', 'Grenade Launcher', 
                   'Laser Cannon', 'Arc Thrower', 'Quasar Cannon',
                   'Airbust Rocket Launcher']

# other
exosuits = ['Patriot Exosuit', 'Emancipator Exosuit']

# Defensive Stratagems
defensive = ['HMG Emplacement', 'Shield Generator Relay', 'Tesla Tower', 
             'Anti-Personnel Minefield', 'Incendiary Mines', 
             'Machine Gun Sentry', 'Gatling Sentry', 'Mortar Sentry', 
             'Autocannon Sentry', 'Rocket Sentry', 'EMS Mortar Sentry']


# put all items in a list
list_of_items = backpacks + support_weapons + exosuits + defensive

# print list of items
#for i in list_of_items:
#    print(i, end = '\n')



# randomly choose 4 items from the list
import random
random_items = random.sample(list_of_items, 4)
print('\nRandom Loadout Selector:')
for i in random_items:
    print(i, end = '\n')
