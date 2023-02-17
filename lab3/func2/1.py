movies = [
{
"name": "Usual Suspects", 
"imdb": 7.0,
"category": "Thriller"
},
{
"name": "Hitman",
"imdb": 6.3,
"category": "Action"
},
{
"name": "Dark Knight",
"imdb": 9.0,
"category": "Adventure"
},
{
"name": "The Help",
"imdb": 8.0,
"category": "Drama"
},
{
"name": "The Choice",
"imdb": 6.2,
"category": "Romance"
},
{
"name": "Colonia",
"imdb": 7.4,
"category": "Romance"
},
{
"name": "Love",
"imdb": 6.0,
"category": "Romance"
},
{
"name": "Bride Wars",
"imdb": 5.4,
"category": "Romance"
},
{
"name": "AlphaJet",
"imdb": 3.2,
"category": "War"
},
{
"name": "Ringing Crime",
"imdb": 4.0,
"category": "Crime"
},
{
"name": "Joking muck",
"imdb": 7.2,
"category": "Comedy"
},
{
"name": "What is the name",
"imdb": 9.2,
"category": "Suspense"
},
{
"name": "Detective",
"imdb": 7.0,
"category": "Suspense"
},
{
"name": "Exam",
"imdb": 4.2,
"category": "Thriller"
},
{
"name": "We Two",
"imdb": 7.2,
"category": "Romance"
}
]

#Write a function that takes a single movie and returns True if its IMDB score is above 5.5

def single_score(n):
    for i in movies:
        if ( i["name"]==n and i["imdb"]>5.5):
            return True
    return False

s=input()
print(single_score(s))

def sublist_score(movies):
    l=[]
    for i in movies:
        if ( i["imdb"] > 5.5 ):
            l.append(i["name"])
    return l

print(sublist_score(movies))

def category(n):
    l=[]
    for i in movies:
        if i['category']==n:
            l.append(i["name"])
    return l


s=str(input())
print(category(s))

def average(n):
    l=[]
    for i in n:
        score=i['imdb']
        l.append(score)
    av= sum(l)/len(l)
    return av

print(average(movies))

def cat_average(n):
    l=[]
    for i in movies:
        if i['category']==n:
            l.append(i["imdb"])
    
    av= sum(l)/len(l)
    return av

s=str(input())
print(cat_average(s)) 