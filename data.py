from faker import Faker
from faker.providers import DynamicProvider
import json
import csv

medical_professions_provider = DynamicProvider(
    provider_name="medical_profession",
    elements=["10-15", "15-18" ,"18-23", "23-30", "30-40", "40-50", "50-60", "60-80"]
)
gender_provider = DynamicProvider(
    provider_name="gender",
    elements=['male','female','lesbian','gay','bi','asexual']
)
ethnicity_provider = DynamicProvider(
    provider_name='ethnicity',
    elements=['white','abazins','black','african american',
              'indigenous people','americans','hispanic and latino',
              'asian','europeans','caucasian','american indian','mutiracial',
              'mexicans','german americans','puerto ricans','italian',
              'english','irish','scottish','indian','filipino',
              'indian americans','people of caucasus',
              'chinese','russian','japaneses','bengalis','slavs','kurukh']
)
hobbies_provider = DynamicProvider(
    provider_name='hobbies',
    elements=[ "Hiking"
 ,"Backpacking"
 ,"Camping"
 ,'Hunting'
 ,'Fishing'
 ,'Archery'
 ,'Canoeing'
 ,'Kayaking'
 ,'Running'
 ,'Geocaching'
 ,'Growing Vegetables'
 ,'Composting'
 ,'Metal Detecting'
 ,'Bird Watching'
 ,'Beekeeping'
 ,'Cool Hobbies'
 ,'LARPing'
 ,'Parkour'
 ,'Astronomy'
 ,'Meteorology'
 ,'Kite Flying'
 ,'Sand Castle Making'
 ,'Hobby Horsing'
 ,'Antiquing'
 ,'Coin Collecting'
 ,'Stamp Collecting'
 ,'Vintage Clothing Collecting'
 ,'Classic Car Collecting'
 ,'Antique Book and Manuscript Collecting'
 ,'Art Collecting'
 ,'Shell and Sea Glass Collecting'
 ,'Leaf Collecting and Pressing'
 ,'Record Collecting'
 ,'Postcard Collecting'
 ,'Shoe Collecting'
 ,'Toy Collecting'
 ,'Memorabilia Collecting (e.g. Star Wars products)'
 ,'Sports Memorabilia Collecting'
 ,'Rock Tumbling'
 ,'Cooking'
 ,'Baking'
 ,'Interesting Hobbies'
 ,'Gingerbread House Making'
 ,'Home Brewing'
 ,'Wine Making'
 ,'Mixology'
 ,'Bread Making'
 ,'Cheese Making'
 ,'Sewing'
 ,'Painting'
 ,'Drawing'
 ,'Origami'
 ,'Photography'
 ,'Scrapbooking'
 ,'Calligraphy'
 ,'Quilting'
 ,'Crocheting'
 ,'Knitting'
 ,'Embroidery'
 ,'Carpet and Tapestry Weaving'
 ,'Designing and Making Clothes'
 ,'Jewelry Making'
 ,'Pottery'
 ,'Metal Working'
 ,'Wood Carving'
 ,'Welding'
 ,'Leather Tooling'
 ,'Cobbling'
 ,'Model Railroads'
 ,'Furniture Building'
 ,'Home Improvement'
 ,'Model Building'
 ,'LEGO'
 ,'Trivia'
 ,'Video Games'
 ,'Board Games'
 ,'Card Games'
 ,'Chess'
 ,'Puzzles'
 ,'Juggling'
 ,'Table Tennis'
 ,'Billiards'
 ,'Genealogy'
 ,'Language Learning'
 ,'Journaling'
 ,'Creative Writing'
 ,'Book Club'
 ,'Home Science Experiments'
 ,'Wikipedia Editing'
 ,'Volunteering for a Historical Society'
 ,'Playing an Instrument'
 ,'Podcast Hosting'
 ,'Amateur Radio'
 ,'Thrifting'
 ,'Makeup'
 ,'Dancing'
 ,'Hula Hooping'
 ,'Aquarium Keeping'
 ,'Computer Programming'
 ,'Working on Cars'
 ,'Travel'
 ,'Cosplaying'
 ,'Survivalist Prepping'
 ,'Scuba Diving'
 ,'Mountain Biking'
 ,'Coffee Roasting'
 ,'Adult Coloring']
)
fake = Faker()

# then add new provider to faker instance
fake.add_provider(medical_professions_provider)
fake.add_provider(gender_provider)
fake.add_provider(ethnicity_provider)
fake.add_provider(hobbies_provider)
'''
Features that needs to be generated
age(define this based on age group)
gender(male,female,bi,homo)
interests(yet to decide list)
occupation(yet to decide list)
likes(yet to decide list)
hates(yet to decide list)
hobbies(yet to decide list)
ethnicity(american,latin like this)

'''
names=[]
age=[]
gender=[]
occupation=[]
ethnicity=[]
hobby1=[]
hobby2=[]
hobby3=[]
hobby4=[]
hobby5=[]
def genereateData():
    for i in range(0,10000):
        giveName()
        age.append(fake.medical_profession())
        gender.append(fake.gender())
        job=fake.job().split(',')[0]
        print(job)
        occupation.append(job)
        ethnicity.append(fake.ethnicity())
        hobby1.append(fake.hobbies())
        hobby2.append(fake.hobbies())
        hobby3.append(fake.hobbies())
        hobby4.append(fake.hobbies())
        hobby5.append(fake.hobbies())
    final_data=[]
    for i in range(0,10000):
        data={'name':names[i],'age-group':age[i],'gender':gender[i],'occupation':occupation[i],'ethnicity':ethnicity[i],
              'hobby1':hobby1[i],'hobby2':hobby2[i],'hobby3':hobby3[i],'hobby4':hobby4[i],'hobby5':hobby5[i]}
        final_data.append(data)
    jsonString = json.dumps(final_data)
    jsonFile = open("test_data.json", "w")
    jsonFile.write(jsonString)
    jsonFile.close()
    with open("test_data.csv", "w", newline="") as f:  # python 2: open("output.csv","wb")
        title = "name,age-group,gender,occupation,ethnicity,hobby1,hobby2,hobby3,hobby4,hobby5".split(",")  # quick hack
        cw = csv.DictWriter(f, title, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
        cw.writeheader()
        cw.writerows(final_data)



def giveName():
    name = fake.name()
    if name not in names:
        names.append(name)
    else:
        giveName()




genereateData()





