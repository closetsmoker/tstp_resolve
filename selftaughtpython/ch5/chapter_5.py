# 1: Create a list of your favorite musicians 
musicians = ["Dave Grohl", "Counterparts", "Daft Punk"]
print(musicians) 

# 2: Create a list of tuples, with each tuple containing the longitude and latitude of somewhere you've lived or visited.
coordinates = ("Waukesha: 43.0117° N, 88.2315° W", "Milwaukee: 43.0389° N, 87.9065° W", "Singapore: 1.3521° N, 103.8198° E", "Shanghai: 31.2304° N, 121.4737° E")
print(coordinates)

# 3: Create a dictionary that contains different attributes about you: height, favorite color, favorite author, etc. 
ian = {"eyes":"brown",
       "hair":"dirty blonde",
       "height":"6'1\"",
       "age":"30",
       "hands":"very cracked"}
print(ian)

# 4: Write a program that lets the user ask your height, favorite color, or favorite author and return the result from challenge 3

question = input("Ask me about my eyes hair or height: ")

if question in ian: 
    answer = ian[question]
    print(answer)
else: 
    print("Fat boy")

# 5: Create a dictionary mapping your favorite musicians to a list of your favorite songs by them. 

# list of FF songs
ff_songs = ["One by One", "My Hero", "Best of You", "All My Life", "The Pretender"]

# list of Daft Punk songs 
dp_songs = ["Lose Yourself to Dance", "One More Time", "Doin' It Right", "Harder Better Faster Stronger"]

# list of counterparts songs: 
cp_songs = ["Outlier", "Stillborn", "Burn"]

mapping_dict = {"Foo Fighters":ff_songs,
                "Daft Punk":dp_songs,
                "Counterparts":cp_songs}
print(mapping_dict)