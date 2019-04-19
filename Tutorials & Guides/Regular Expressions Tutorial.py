import re
import urllib.request

'''
#r tells the print fuction what what's ahead is differnet from normal strings
#\s means space
#* means 0 or more, and 1* means one or more


#This removes spaces between words
print(''.join(re.split(r'\s1*', 'here ar e   some  words')))


#This seperates a string into a list of words and spaces
print(re.split(r'(\s1*)', 'here ar e   some words'))


#This splits the string where there are one or more s characters
#This way, all s characters are isolated
print(re.split(r'(s1*)', 'here are some words'))


#This splits the string wherever there are letters a though f (Lowercase)
print(re.split(r'[a-f]', 'hasklhfjekrnvjkfbuewba'))


#This removes all numbers (digits) from the string
print(''.join(re.split(r'[0-9]','one 2 three 4 five 6 seven 8 nine 10')))


#This removes any a or b or y or z or 0-9 characters (list)
print(re.split(r'[a-by-z0-9]', '7 blue avacados, your 1 zest'))


#This also removes a-f, but it now ignores case -- re.I
#These re.I and re.M are called flags
print(re.split(r'[a-f]', 'haCklhFjEkanvjkfbuEwba', flags=re.I))


#This is equivalent to the one above, but w/o flags
print(re.split(r'[a-fA-F]', 'haCklhFjEkanvjkfbuEwba'))


#This removes any places where a-f(case insentitive) happens twice in a row
print(re.split(r'[a-f][a-f]', 'afyyyAABueihfutfarkntn', flags=re.I))


#This removes any 4-digit numbers
print(re.split(r'[0-9][0-9][0-9][0-9]','5471 BBF Rd.'))


#This will look for (find all) addresses
print(re.findall(r'\d{1,5}\s\w+\s\w+\.','ungure324 main st..ihtuirbfe'))
#\d is equivalent to [0-9], but \D searches for non-digits
#{a,b} specifies an inclusive range. Here, we have 1-5 digits
#{n} specifies exactly n-many
#\s means a single space
#\w means alphanumeric characters
#+ means 1 or more of
#\. means exactly a period (. means something ese beisdes the '.' character)


#This gets the title of webpages
sites = "google yahoo cnn youtube wikipedia code".split() #List of site names
pat=re.compile(r'<title>+.*</title>+',flags=re.I|re.M)
for s in sites:
    #print("Searching "+s+" Right Now.")
    try:
        u= urllib.request.urlopen("http://"+s+".com")
    except (NameError):
        u=urllib.request.urlopen("http://"+s+".org")
    except:
        u=urllib.request.urlopen("http://"+s+".gov")
    text = u.read()
    title = re.findall(pat,str(text))
    print(str(title[0])[7:-8])

#This finds urls of form: www.?????.??? where ?'s are alphanumeric
print(re.findall(r'www\.\w+\.\w{1,3}',"ewifnweofiwww.cantnot2weetthis.co-einfuwebfjwwww.youtube.comnfeuibferbfwww.google.comfnerouifneruifnwww.reddit.comeioneuiwfbe"))

#This finds my name: william boyles
print(re.findall(r'william\s*boyles',"hellotheremy nameis williamboyles.That'sright myname is William Boyles.did oyu finds all of them?there are three williamboylesesaournd here.",flags=re.I))
'''
