from app import app, ski_schema, user_schema
from models import db, Ski, User
import json

# ??
with app.app_context():

    # List of 14 skis with data nested in objects
    skis_data = [
        {
            "brand": "Head",
            "name": "Kore 105",
            "dimensions": {
                "waist": 105,
                "tip": 135,
                "tail": 125
            },
            "lengths": [
                171,
                180,
                189
            ],
            "year": "2018",
            "weight": 1860,
            "image": [
                "https://mikes-ski-finder.netlify.app/images/kore/kore-top.webp",
                "https://mikes-ski-finder.netlify.app/images/kore/kore-zoom.jpeg"
            ],
            "content": "As the ultimate lightweight freeride ski, the KORE 105 has versatility for all-mountain adventures. The KORE construction reduces weight without sacrificing performance, thanks to a combination of Graphene, Karuba wood and multi layers of carbon. The sandwich sidewall construction adds responsiveness on hardpack snow, and tip and tail rocker provides flotation for deep days.",
            "stoke_profile": {
                "playfulness": 0.1,
                "performance": 0.6,
                "rocker": 0.3
            },
        },
        {
            "brand": "Atomic",
            "name": "Bent Chetler 120",
            "dimensions": {
                "waist": 120,
                "tip": 144,
                "tail": 135
            },
            "lengths": [
                176,
                184,
                192
            ],
            "year": "2022",
            "weight": 1800,
            "image": [
                "https://mikes-ski-finder.netlify.app/images/chetler/chetler-top.webp",
                "https://mikes-ski-finder.netlify.app/images/chetler/chetler-base.webp",
                "https://mikes-ski-finder.netlify.app/images/chetler/chetler-zoom.jpeg"
            ],
            "content": "The Atomic Bent Chetler 120 is Chris Benchetler’s signature ski and the big brother of the Bent ski family. This pillow-bashing, powder-slashing machine features topsheet and base art by the man himself. With construction and shaping designed and refined by Chris Benchetler since 2008, the latest iteration redefines what’s possible in big mountain terrain. Dura Cap Sidewall construction combined with revolutionary HRZN Tech offers more surface area in the tip and tail for better tracking through chop and crud with less tip deflection. The Light Woodcore shaves weight while the Carbon Backbone adds strength and stiffness. The Powder Rocker profile offers the perfect amount of tip and tail turn-up, and camber under foot delivers epic performance through deep turns, side hits, and nose butters.",
            "stoke_profile": {
                "playfulness": 0.4,
                "performance": 0.2,
                "rocker": 0.4
            },
        },
        {
            "brand": "ON3P",
            "name": "Woodsman 110",
            "dimensions": {
                "waist": 110,
                "tip": 139,
                "tail": 128
            },
            "lengths": [
                167,
                172,
                177,
                182,
                187,
                192
            ],
            "year": "2022",
            "weight": 2240,
            "image": [
                "https://mikes-ski-finder.netlify.app/images/woodsman/woodsman-top.webp",
                "https://mikes-ski-finder.netlify.app/images/woodsman/woodsman-base.webp",
                "https://mikes-ski-finder.netlify.app/images/woodsman/woodsman-zoom.jpeg"
            ],
            "content": "The Woodsman 110 represents our take on an everyday platform for west coast skiers who need float and stability in their everyday ski.  Versatility is the name of the game these days - so an everyday platform that can double duty on deep days is what we find ourselves reaching for most of the time.  The Woodsman 110 blends equal parts muscle, float, and quickness for aggressive skiers needing a supportive everyday ride for their all mountain pursuits.",
            "stoke_profile": {
                "playfulness": 0.2,
                "performance": 0.6,
                "rocker": 0.2
            },
        },
        {
            "brand": "Blizzard",
            "name": "Zero G 95",
            "dimensions": {
                "waist": 95,
                "tip": 127,
                "tail": 111
            },
            "lengths": [
                157,
                164,
                171,
                178,
                185
            ],
            "year": "2023",
            "weight": 1260,
            "image": [
                "https://mikes-ski-finder.netlify.app/images/zerog/zerog-top.webp",
                "https://mikes-ski-finder.netlify.app/images/zerog/zerog-zoom.jpeg"
            ],
            "content": "The Zero G 95 was the ski of choice for ski mountaineers Hilaree Nelson and Jim Morrison to conquer their epic, first descent on the world’s highest, biggest line—the Lhotse Couloir on 27,940-foot Lhotse peak in Nepal’s Himalayas. The Zero G 95 gave them the performance they needed to get down safely—not to mention the high-altitude pow turns they scored! An ultra-lightweight paulownia wood core paired with updated iteration of Blizzard’s proven Carbon Drive technology in version 3.0 provides for efficiency on the skin track and a more consistent, stable feel on the descent. Your backcountry adventure may be closer to home, but you can still reap the benefits of Austrian engineering that delivers the best downhill performance for the weight.",
            "stoke_profile": {
                "playfulness": 0,
                "performance": 0.9,
                "rocker": 0.1
            },
        },
        {
            "brand": "Sego",
            "name": "Comp 110",
            "dimensions": {
                "waist": 110,
                "tip": 140,
                "tail": 131
            },
            "lengths": [
                175,
                181,
                187,
                192
            ],
            "year": "2021",
            "weight": 2230,
            "image": [
                "https://mikes-ski-finder.netlify.app/images/sego/sego-top.webp",
                "https://mikes-ski-finder.netlify.app/images/sego/sego-base.webp",
                "https://mikes-ski-finder.netlify.app/images/sego/sego-zoom.jpeg"
            ],
            "content": "The 2022 Sego Cleaver Comp is a bit of a monster. Designed for Freeride World Tour Champion Isaac Freeland to compete on, these 110mm beasts are for charging mixed conditions on steep faces. A 7cm wide strip of titanal runs the length of the ski, providing a very stout backbone, and there is less rocker than the Big Horn series making these super stable. But Isaac is most famous for the tricks he thows and proper twin tip tail makes that possible on these and makes them stand out from the competition.",
            "stoke_profile": {
                "playfulness": 0.2,
                "performance": 0.6,
                "rocker": 0.2
            },
        },
        {
            "brand": "Line",
            "name": "Blend 100",
            "dimensions": {
                "waist": 133,
                "tip": 100,
                "tail": 122
            },
            "lengths": [
                171,
                178,
                185
            ],
            "year": "2023",
            "weight": 1940,
            "image": [
                "https://mikes-ski-finder.netlify.app/images/blend/blend-top.webp",
                "https://mikes-ski-finder.netlify.app/images/blend/blend-base.webp",
                "https://mikes-ski-finder.netlify.app/images/blend/blend-zoom.webp"
            ],
            "content": "Introducing the 2022/2023 LINE Blend. If you couldn't tell by the intro, the LINE Blend continues to be a go-to ski for our freestyle team. Will Wesson, Mitchell Brower, Sami Ortlieb, Peter Koukov, Andy Parry, the list goes on! One thing these guys have in common is the creativity that can be found in their skiing. From 50-50 combinations to unique butters and nose blocks, to locking in wheelies, the Blend opens up new lanes of creativity on the mountain. Thanks to the ample 100mm waist width and incredibly playful feel you're guaranteed to have a good time on the Blend, whether you're skiing the best park in the world or lapping a 100-foot rope tow. Get ready to start bending your Blends and making the whole mountain your playground.",
            "stoke_profile": {
                "playfulness": 0.8,
                "performance": 0,
                "rocker": 0.2
            },
        },
        {
            "brand": "Black Crows",
            "name": "Corvus Freebird 107",
            "dimensions": {
                "waist": 107,
                "tip": 140,
                "tail": 119
            },
            "lengths": [
                176,
                183.4,
                188.2
            ],
            "year": "2023",
            "weight": 1825,
            "image": [
                "https://mikes-ski-finder.netlify.app/images/corvus/corvus-top.webp",
                "https://mikes-ski-finder.netlify.app/images/corvus/corvus-base.webp",
                "https://mikes-ski-finder.netlify.app/images/corvus/corvus-zoom.jpeg"
            ],
            "content": "The choice of the true touring skiers, the Corvus Freebird benefits from a slight rocker rise in the tip, a dynamic tail and long sidecut. The result is an aggressive and very precise on the entry and exit of the curve for a very energetic skiing. It is also equipped with a titanium plate under the foot to adapt to the new hybrid bindings. Life is always in the pink.",
            "stoke_profile": {
                "playfulness": 0.1,
                "performance": 0.8,
                "rocker": 0.1
            },
        },
        {
            "brand": "ON3P",
            "name": "Jeffrey 110",
            "dimensions": {
                "waist": 110,
                "tip": 137,
                "tail": 131
            },
            "lengths": [
                166,
                171,
                176,
                181,
                186,
                191
            ],
            "year": "2022",
            "weight": 2100,
            "image": [
                "https://mikes-ski-finder.netlify.app/images/jeffrey/jeffrey-top.webp",
                "https://mikes-ski-finder.netlify.app/images/jeffrey/jeffrey-base.webp",
                "https://mikes-ski-finder.netlify.app/images/jeffrey/jeffrey-zoom.jpeg"
            ],
            "content": "Long the workhorse of our lineup, the Jeffrey 110 is the do-it-all choice for west coast skiers looking for a playful yet powerful daily driver. For 2022, we've increased the waist width to provide better float on soft days and increased the turning radius to create a slightly more aggressive platform.  As agile as it is versatile, it is at-home in the park, powder, crud, hardpack, and anywhere between. We say it’s an all mountain ski, and we mean it - it’s the only ski you’ll ever need.",
            "stoke_profile": {
                "playfulness": 0.4,
                "performance": 0.3,
                "rocker": 0.3
            },
        },
        {
            "brand": "Armada",
            "name": "ARV JJ 116",
            "dimensions": {
                "waist": 116,
                "tip": 139,
                "tail": 135
            },
            "lengths": [
                165,
                175,
                185,
                192
            ],
            "year": "2022",
            "weight": 2250,
            "image": [
                "https://mikes-ski-finder.netlify.app/images/jj/jj-top.webp",
                "https://mikes-ski-finder.netlify.app/images/jj/jj-base.webp",
                "https://mikes-ski-finder.netlify.app/images/jj/jj-zoom.jpeg"
            ],
            "content": "The iconic Armada ARV 116 JJ continues to carve its name into ski lore, coming correct with a Poplar-Ash wood core for maximum energy return and pop when sending it down pillow lines and ripping tree shots. The JJ's balanced flex profile is ideal for surfing powder while maintaining enough stiffness through the tip and tail to excel in tight conditions and no-fall zones. Smear Tech 3D base beveling in the tips and tails allow limitless directions of slashes, presses and butters as you put your signature on the mountain.",
            "stoke_profile": {
                "playfulness": 0.4,
                "performance": 0.2,
                "rocker": 0.4
            },
        },
        {
            "brand": "Armada",
            "name": "Magic J 126",
            "dimensions": {
                "waist": 126,
                "tip": 143,
                "tail": 140
            },
            "lengths": [
                180,
                190
            ],
            "year": "2023",
            "weight": 2000,
            "image": [
                "https://mikes-ski-finder.netlify.app/images/magicj/magicj-top.webp",
                "https://mikes-ski-finder.netlify.app/images/magicj/magicj-base.webp",
                "https://mikes-ski-finder.netlify.app/images/magicj/magicj-zoom.webp"
            ],
            "content": "The Magic J is reborn. Tanner’s ultimate powder ski gets the ultralight treatment thanks to a Caruba Core and edgeless tips and tails that shave serious heft for a nimbler ride and more playful feel. The flex pattern and 124mm waist deliver maximum float and pop, encouraging you to butter, slash and send in every conceivable way, just like Tanner. The iconic Scarface graphic is a throwback to the T-Hall Signature Model from 2006/07, a vintage nod and another element of this modern classic brought back to life.",
            "stoke_profile": {
                "playfulness": 0.4,
                "performance": 0,
                "rocker": 0.6
            },
        },
        {
            "brand": "Faction",
            "name": "Prodigy 4.0 116",
            "dimensions": {
                "waist": 116,
                "tip": 140,
                "tail": 132
            },
            "lengths": [
                179,
                185,
                191
            ],
            "year": "2022",
            "weight": 2200,
            "image": [
                "https://mikes-ski-finder.netlify.app/images/prodigy/prodigy-top.webp",
                "https://mikes-ski-finder.netlify.app/images/prodigy/prodigy-base.webp",
                "https://mikes-ski-finder.netlify.app/images/prodigy/prodigy-zoom.webp"
            ],
            "content": "The Prodigy 4.0 shares all the characteristics of its narrower, ever-popular sibling, but is wider, providing optimal float on the optimal day. Incredibly playful by nature, the Prodigy 4.0 effortlessly butters and smears; stomps big airs; and nimbly dances through pow-laden forests. Complementing its prowess in the deep stuff, the ski reliably holds its edge and is highly adept in tight-turning scenarios, for the days spent impatiently waiting for the next storm to arrive.",
            "stoke_profile": {
                "playfulness": 0.4,
                "performance": 0.3,
                "rocker": 0.3
            },
        },
        {
            "brand": "Atomic",
            "name": "Redster G9 68",
            "dimensions": {
                "waist": 68,
                "tip": 110,
                "tail": 96.5
            },
            "lengths": [
                167,
                172,
                177,
                182
            ],
            "year": "2022",
            "weight": 3229,
            "image": [
                "https://mikes-ski-finder.netlify.app/images/redster/redster-top.webp",
                "https://mikes-ski-finder.netlify.app/images/redster/redster-base.webp",
                "https://mikes-ski-finder.netlify.app/images/redster/redster-zoom.jpeg"
            ],
            "content": "The Atomic Redster G9 Revoshock S is packed with World Cup DNA. Its racing heritage shines through with every big, sweeping turn. With Atomic’s Revoshock S technology, the Redster G9 Revoshock S turns icy morning groomers into a stable ride that will fire out of every turn. It features Ultrawall sidewall construction, merging the power of full sidewalls and Dura Cap durability. The dual-layer TI Powered laminate maintains torsional rigidity while working together with the Redster G9 Revoshock S’ Power Woodcore to create insane edge hold through the turns. While you might not be racing on the World Cup this year, you can still experience World Cup performance every time you click into this ski.",
            "stoke_profile": {
                "playfulness": 0,
                "performance": 10,
                "rocker": 0
            },
        },
        {
            "brand": "Volkl",
            "name": "Revolt 121",
            "dimensions": {
                "waist": 121,
                "tip": 143,
                "tail": 135
            },
            "lengths": [
                177,
                184,
                191
            ],
            "year": "2023",
            "weight": 2320,
            "image": [
                "https://mikes-ski-finder.netlify.app/images/revolt/revolt-top.webp",
                "https://mikes-ski-finder.netlify.app/images/revolt/revolt-base.webp",
                "https://mikes-ski-finder.netlify.app/images/revolt/revolt-zoom.jpeg"
            ],
            "content": "The Revolt 121 is the result of a close cooperation between Lead Engineer Lucas Romain, Product & Team Manager Jean-Claude Pedrolini and the riders Markus Eder, Paddy Graham, Fabio Studer, Colter Hinchliffe, Tanner Rainville, Sam Smoothy and Tom Ritsch. The tip & tail rocker ski comes with a slight camber under the binding for that little bit of extra pressure und steering when approching the kicker. \"Incredibly versatile\" - that's one of the most often heard comments from people riding the Revolt 121. This is made possible due to the 3 radius construction and a specially shaped tip that works great for nose butters and drift turns in soft snow. The tough box construction with Multilayer Woodcore makes the ski strong enough to go where dedicated freeskiers dare to go.",
            "stoke_profile": {
                "playfulness": 0.3,
                "performance": 0.4,
                "rocker": 0.3
            },
        },
        {
            "brand": "Armada",
            "name": "Whitewalker 116",
            "dimensions": {
                "waist": 116,
                "tip": 139,
                "tail": 135
            },
            "lengths": [
                185,
                192
            ],
            "year": "2024",
            "weight": 1800,
            "image": [
                "https://mikes-ski-finder.netlify.app/images/whitewalker/whitewalker-top.webp",
                "https://mikes-ski-finder.netlify.app/images/whitewalker/whitewalker-base.webp",
                "https://mikes-ski-finder.netlify.app/images/whitewalker/whitewalker-zoom.jpeg"
            ],
            "content": "We set out to build Sammy a powder twin tip that is stable enough to charge exposed lines and take big hits with maximum confidence yet light enough for foot-powered backcountry access. A strategically enhanced Caruba Core allows these concepts to merge while the rockered Pin Tip and Tail guarantee quick turn initiation, reduce drag and further lower the swingweight. Lightweight and stable, but offering plenty of release when needed, the Whitewalker perfectly compliments Sammy's laid-back, surf-inspired style that's peppered with sudden bursts of all-out aggression.",
            "stoke_profile": {
                "playfulness": 0.1,
                "performance": 0.5,
                "rocker": 0.4
            },
        }
    ]

    # Clear whatever is in the skis table
    Ski.query.delete()
    
    # Create an empty list to append the serialized ski data into
    skis_serialized = []
    # Loop through each attribute of each ski in the initial list of skis
    # If the value of the attribute is not a string, use the json.dumps() method to serialize it
    # Assign the serialized values to new ski object and append that object to the newly created list
    for ski in skis_data:
        new_ski = dict()
        for attr in ski:
            if type(ski[attr]) != str:
                new_ski[attr] = json.dumps(ski[attr])           
            else:
                new_ski[attr] = ski[attr]
                
        skis_serialized.append(new_ski)
    
    # Use the load method from Marshmallow to generate instances of the 'Ski' class
    ski_objs = [ski_schema.load(ski) for ski in skis_serialized]
    
    # Add the newly created instances to the db
    db.session.add_all(ski_objs)
    db.session.commit()
    
    # Repeat the above process for user data
    users_data = [
        {
            "username": "sproot",
            "stoke_profile": {
                "playfulness": 0.3,
                "performance": 0.4,
                "rocker": 0.3
            }
        }
    ]
    
    User.query.delete()
    
    users_serialized = []
    for user in users_data:
        new_user = dict()
        for attr in user:
            if type(user[attr]) != str:
                new_user[attr] = json.dumps(user[attr])
            else:
                new_user[attr] = user[attr]
                
        users_serialized.append(new_user)
    
    user_objs = [user_schema.load(user) for user in users_serialized]
    
    db.session.add_all(user_objs)
    db.session.commit()