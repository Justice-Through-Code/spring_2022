print('Question 1')

borough = {
    'name': 'Queens',
    'airports': [
        {
            'name': 'JFK',
            'description': 'John F. Kennedy International Airport is an international airport in Queens, New York, USA. It is the primary international airport serving New York City.'
        },
        {
            'name': 'LGA',
            'description': 'LaGuardia Airport is an airport in Queens, New York. The airport is the third busiest airport serving New York City, and the twentieth busiest in the United States. LaGuardia Airport covers 680 acres.'
        }
    ],
    'beaches': [
        {
            'name': 'Rockaway Beach',
            'description': 'From surfers to swimmers to the Ramones, everyone wants to \"hitch a ride to Rockaway Beach.\" Rockaway Beach is a year-round resource for residents all along the Rockaway peninsula, and it comes alive each summer with millions of visitors. Beach goers can enjoy the sand and water, the variety of concessions, and the city\'s only legal surfing beaches. Rockaway Beach is also home to a variety of playgrounds and other outdoor activities.'
        }
    ]
}
# TODO: 1.1 Print the borough's name

# TODO: 1.2 Print the names of the borough's airports

# TODO: 1.3 Write an if/else statement to see if a 'parks' key exists in the borough dictionary...
# If it exists, print 'This borough has beautiful parks!'
# Else print 'Sorry! This borough does not have parks.'

print()

print('Question 2')
# This list contains dictionaries of boroughs that make up New York City
# Take a moment to look through this list and see how things are nested, what key value pairs exist
nyc = [
    {
        'name': 'Bronx',
        'beaches': [
            {
                'name': 'Orchard Beach',
                'description': 'Orchard Beach, Bronx\'s sole public beach, was proclaimed \"The Riviera of New York\" when it was created in the 1930s. The 115-acre, 1.1-mile-long beach contains a hexagonal-block promenade, a central pavilion, snack bars, food and souvenir carts, two playgrounds, two picnic areas, a large parking lot, and 26 courts for basketball, volleyball, and handball. Changing areas and showers are available.'
            },
        ],
        'zoos': [
            {
                'name': 'Bronx Zoo',
                'description': 'The Bronx Zoo is a zoo located within Bronx Park in the Bronx, New York. It is one of the largest zoos in the United States by area, and is the largest metropolitan zoo in the United States by area, comprising 265 acres of park lands and naturalistic habitats separated by the Bronx River.'
            },
        ]
    },
    {
        'name': 'Brooklyn',
        'beaches': [
            {
                'name': 'Brighton Beach',
                'description': 'Also known as "Little Odessa" due its tight-knit Russian and Eastern European communities, Brooklyn\'s Brighton Beach is a lively neighborhood with many high-rise residential buildings. Traditional ethnic restaurants and food markets line Brighton Beach Avenue. The beach and boardwalk here are more laid-back than nearby Coney Island, catering largely to locals. Splashy nightclubs attract partiers in the evenings.'
            },
            {
                'name': 'Coney Island',
                'description': 'Coney Island is a residential Brooklyn neighborhood that morphs into a relaxation and entertainment destination each summer. Locals and tourists crowd its beach, the Wonder Wheel and Luna Park, an amusement park featuring the famed Cyclone roller coaster. Street performers, the Circus Sideshow and the Mermaid Parade in June lend an eccentric vibe. Nathan\'s Famous is known for its July 4th hot-dog eating contest.'
            },
            {
                'name': 'Manhattan Beach',
                'description': 'Manhattan Beach is a laid-back South Bay community popular with families and outdoor enthusiasts. The Strand bike path winds along the oceanfront between modern mansions and wide stretches of sand lined with volleyball courts. Low-key Manhattan Beach Pier features a quaint aquarium and views of surfers. There are several parks, and a small downtown area with boutiques, brunch cafes, pubs & creative, upscale eateries.'
            }
        ],
    },
    {
        'name': 'Manhattan',
        'food': [
            {
                'name': 'Cheeky Sandwiches',
                'description': 'A hip sandwich shop offering a select menu of po\' boys & other Big Easy bites in a tiny storefront.'
            },
            {
                'name': 'Katz\'s Delicatessen',
                'description': 'No-frills deli with theatrically cranky service serving mile-high sandwiches since 1888.'
            },
            {
                'name': 'Veselka',
                'description': 'Borscht & pierogi are menu highlights at this cheap, no-frills Ukrainian eatery open 24 hours a day.'
            }
        ],
        'parks': [
            {
                'name': 'Central Park',
                'description': 'Central Park is an urban park in New York City located between the Upper West and Upper East Sides of Manhattan. It is the fifth-largest park in the city by area, covering 843 acres.'
            },
            {
                'name': 'Riverside Park',
                'description': 'Riverside Park is a scenic waterfront public park in the Upper West Side, Morningside Heights, and Hamilton Heights neighborhoods of the borough of Manhattan in New York City.'
            },
            {
                'name': 'The High Line',
                'description': 'The High Line is a 1.45-mile-long elevated linear park, greenway and rail trail created on a former New York Central Railroad spur on the west side of Manhattan in New York City. The High Line\'s design is a collaboration between James Corner Field Operations, Diller Scofidio + Renfro, and Piet Oudolf.'
            },
            {
                'name': 'Washington Square Park',
                'description': 'Washington Square Park is a 9.75-acre public park in the Greenwich Village neighborhood of Lower Manhattan, New York City. One of the best known of New York City\'s public parks, it is an icon as well as a meeting place and center for cultural activity.'
            }
        ]
    },
    {
        'name': 'Queens',
        'airports': [
            {
                'name': 'JFK',
                'description': 'John F. Kennedy International Airport is an international airport in Queens, New York, USA. It is the primary international airport serving New York City.'
            },
            {
                'name': 'LGA',
                'description': 'LaGuardia Airport is an airport in Queens, New York. The airport is the third busiest airport serving New York City, and the twentieth busiest in the United States. LaGuardia Airport covers 680 acres.'
            }
        ],
        'beaches': [
            {
                'name': 'Rockaway Beach',
                'description': 'From surfers to swimmers to the Ramones, everyone wants to \"hitch a ride to Rockaway Beach.\" Rockaway Beach is a year-round resource for residents all along the Rockaway peninsula, and it comes alive each summer with millions of visitors. Beach goers can enjoy the sand and water, the variety of concessions, and the city\'s only legal surfing beaches. Rockaway Beach is also home to a variety of playgrounds and other outdoor activities.'
            }
        ]
    },
    {
        'name': 'Staten Island',
        'beaches': [
            {
                'name': 'Cedar Grove Beach',
                'description': 'The city\'s newest beach is a converted oceanfront bungalow colony. This charming beach is smaller and somewhat more tranquil than its neighbors, Midland Beach and South Beach, and is popular with the area\'s families.'
            },
            {
                'name': 'Midland Beach',
                'description': 'Midland Beach shares the Franklin D. Roosevelt Boardwalk with neighboring South Beach, and tends to be the somewhat less crowded of the two beaches. The beach\'s attractions include a playground and courts for tennis and shuffleball, as well as a sea turtle fountain for children.'
            },
            {
                'name': 'South Beach',
                'description': 'Beachgoers can sunbathe while taking in a lovely view of the Verazzano Bridge, bike through a scenic trail, jog along the boardwalk, kayak, play tennis, or fish off of the Ocean Breeze Fishing Pier, one of the city\'s most popular. A park on the beach designed especially for seniors contains chess tables, benches, and bocce courts. The beach\'s Fountain of Dolphins is a popular stop on any tour of the boardwalk.'
            },
            {
                'name': 'Wolfes Pond Beach',
                'description': 'Love the ocean but think NYC\'s beaches are just too chaotic? Wolfe\'s Pond Beach is the city\'s best-kept secret, a small, calm, and secluded beach that\'s a perfect retreat for those looking to get away from summer\'s crowds.'
            }
        ],
        'food': [
            {
                'name': 'Lees Tavern',
                'description': 'Family-run neighborhood pub with photos on the wall serving a range of pizza & brews.'
            },
            {
                'name': 'Lees Tavern',
                'description': 'Staten Island-born chain dispensing Italian ices & ice cream in 100-plus flavors since 1928.'
            },
            {
                'name': 'Lees Tavern',
                'description': 'A local Italian bakery serves bread, pastries & coffees, with an adjacent cucina for hot meals.'
            }
        ]
    },
]

# Create a for loop and inside...
# TODO: 2.1 Print the name of every borough in the list.
# TODO: 2.2 If a borough has beaches, print the name of every beach in the borough
# TODO: 2.3 Let's add a '\t' (tab) to the print statement in 2.2
# TODO: 2.4 Do steps 2.2 through 2.3 again but for 'parks' instead of 'beaches'

# All of Question 2 solutions go here!

print()

print('Question 3')
# We will create an command line application that searches for places in NYC

# Acceptable inputs are 'airports', beaches', food', 'parks' or 'zoos'
# places_input = input('Search places in NYC: ') # Uncomment this line
# print(f'Searching for {places_input}...') # Uncomment this line

# Create a for loop and inside...
# TODO: 3.1 Print the name of every borough in the list.
# TODO: 3.2 If a borough has places that matches the 'places_input', then print the names of those places
# TODO: 3.3 Let's add a '\t' (tab) to the print statements in 3.2

# All of Question 3 solutions go here!
